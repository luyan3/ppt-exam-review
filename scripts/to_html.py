#!/usr/bin/env python3
"""
PPT Exam Review — HTML Converter
==================================
Converts the structured Markdown review output into a beautiful,
self-contained HTML page with collapsible sections, color-coded
priority markers, formula rendering, and print layout.

Usage:
  python to_html.py assp4_complete_review.md -o review.html
  python to_html.py assp4_complete_review.md                   # outputs to stdout
  python to_html.py assp4_complete_review.md --open             # open in browser

Dependencies:
  pip install markdown
"""

import argparse
import re
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path


# ── HTML Template ──────────────────────────────────────────────────────────

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  /* ── Reset & Base ── */
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC",
                 "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 15px; line-height: 1.7; color: #1a1a2e;
    background: #f4f6f9; max-width: 1000px; margin: 0 auto; padding: 20px;
  }}

  /* ── Header ── */
  .review-header {{
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: #fff; border-radius: 12px; padding: 32px 40px; margin-bottom: 24px;
    position: relative; overflow: hidden;
  }}
  .review-header h1 {{ font-size: 24px; margin-bottom: 6px; letter-spacing: 1px; }}
  .review-header .subtitle {{ font-size: 14px; opacity: 0.8; }}
  .review-header .badge {{
    display: inline-block; background: rgba(255,255,255,0.15);
    padding: 3px 10px; border-radius: 20px; font-size: 12px; margin-top: 8px;
  }}

  /* ── TOC ── */
  .toc {{
    background: #fff; border-radius: 10px; padding: 20px 24px;
    margin-bottom: 24px; box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  }}
  .toc h2 {{ font-size: 16px; margin-bottom: 12px; color: #0f3460; }}
  .toc ul {{ list-style: none; padding: 0; columns: 2; column-gap: 24px; }}
  .toc li {{ margin-bottom: 4px; }}
  .toc a {{
    color: #0f3460; text-decoration: none; font-size: 14px;
    padding: 2px 6px; border-radius: 4px; display: inline-block;
  }}
  .toc a:hover {{ background: #e8edf5; }}

  /* ── Module Sections ── */
  .module {{
    background: #fff; border-radius: 10px; margin-bottom: 16px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06); overflow: hidden;
  }}
  .module-header {{
    padding: 14px 24px; cursor: pointer; user-select: none;
    display: flex; align-items: center; justify-content: space-between;
    transition: background 0.15s;
  }}
  .module-header:hover {{ background: #f8f9fc; }}
  .module-header .icon {{ font-size: 18px; margin-right: 10px; }}
  .module-header .title {{ font-weight: 600; font-size: 16px; color: #1a1a2e; }}
  .module-header .arrow {{ transition: transform 0.2s; font-size: 14px; color: #999; }}
  .module.collapsed .module-header .arrow {{ transform: rotate(-90deg); }}
  .module-content {{ padding: 0 24px 20px; }}

  /* ── P0 / P1 / P2 Cards ── */
  .p0-block {{
    border-left: 4px solid #dc3545; background: #fff5f5;
    padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0;
  }}
  .p1-block {{
    border-left: 4px solid #fd7e14; background: #fffbf0;
    padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0;
  }}
  .p2-block {{
    border-left: 4px solid #6c757d; background: #f8f9fa;
    padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0;
  }}
  .p0-tag {{
    display: inline-block; background: #dc3545; color: #fff;
    font-size: 11px; font-weight: 700; padding: 1px 8px;
    border-radius: 10px; margin-right: 6px; vertical-align: middle;
  }}
  .p1-tag {{
    display: inline-block; background: #fd7e14; color: #fff;
    font-size: 11px; font-weight: 700; padding: 1px 8px;
    border-radius: 10px; margin-right: 6px; vertical-align: middle;
  }}
  .p2-tag {{
    display: inline-block; background: #6c757d; color: #fff;
    font-size: 11px; font-weight: 700; padding: 1px 8px;
    border-radius: 10px; margin-right: 6px; vertical-align: middle;
  }}

  /* ── Formula blocks ── */
  .formula {{
    font-family: "Times New Roman", "STIX", serif; font-size: 16px;
    background: #f0f4ff; padding: 8px 14px; border-radius: 6px;
    margin: 8px 0; overflow-x: auto; border: 1px solid #dde6f5;
  }}
  .inline-formula {{
    font-family: "Times New Roman", "STIX", serif;
    padding: 0 2px; white-space: nowrap;
  }}

  /* ── Tables ── */
  .module-content table {{
    width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 14px;
  }}
  .module-content th {{
    background: #eef2f7; padding: 8px 12px; text-align: left;
    font-weight: 600; border: 1px solid #dde2e8;
  }}
  .module-content td {{
    padding: 8px 12px; border: 1px solid #dde2e8;
  }}
  .module-content tr:nth-child(even) {{ background: #fafbfc; }}

  /* ── Code blocks (TSV / shells) ── */
  .module-content pre {{
    background: #1e1e2e; color: #cdd6f4; padding: 14px 18px;
    border-radius: 8px; overflow-x: auto; font-size: 13px;
    line-height: 1.5; margin: 10px 0;
  }}
  .module-content code {{
    font-family: "JetBrains Mono", "Fira Code", "Consolas", monospace;
    font-size: 13px;
  }}
  .module-content :not(pre) > code {{
    background: #eef2f7; padding: 1px 5px; border-radius: 3px;
    color: #cf222e;
  }}

  /* ── Blockquote (speaker notes, source citations) ── */
  .module-content blockquote {{
    border-left: 3px solid #8b949e; padding: 6px 14px; margin: 8px 0;
    color: #57606a; background: #f6f8fa; border-radius: 0 4px 4px 0;
  }}

  /* ── Horizontal rules ── */
  .module-content hr {{
    border: none; border-top: 1px solid #e4e7ed; margin: 20px 0;
  }}

  /* ── Print styles ── */
  @media print {{
    body {{ background: #fff; padding: 0; font-size: 12px; }}
    .toc {{ break-after: page; }}
    .module {{ break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }}
    .module-header {{ break-after: avoid; }}
    .p0-block, .p1-block {{ break-inside: avoid; }}
    .no-print {{ display: none !important; }}
  }}

  /* ── Responsive ── */
  @media (max-width: 600px) {{
    body {{ padding: 10px; }}
    .review-header {{ padding: 20px; }}
    .toc ul {{ columns: 1; }}
    .module-content {{ padding: 0 14px 14px; }}
    .module-header {{ padding: 10px 14px; }}
  }}
</style>
</head>
<body>

<div class="review-header">
  <h1>{title}</h1>
  <div class="subtitle">{subtitle}</div>
  <div class="badge">{stats}</div>
</div>

<nav class="toc no-print">
  <h2>📑 目录</h2>
  <ul>
{toc_items}
  </ul>
</nav>

<main>
{body}
</main>

<script>
(function() {{
  // Collapsible modules
  document.querySelectorAll('.module-header').forEach(header => {{
    header.addEventListener('click', function() {{
      const module = this.parentElement;
      const content = module.querySelector('.module-content');
      const isCollapsed = module.classList.toggle('collapsed');
      content.style.display = isCollapsed ? 'none' : '';
    }});
  }});

  // Expand all / collapse all buttons
  const nav = document.querySelector('.toc ul');
  if (nav) {{
    const controls = document.createElement('div');
    controls.style.cssText = 'margin-top:8px; display:flex; gap:8px;';
    controls.innerHTML = `
      <button class="no-print" onclick="expandAll()"
        style="padding:4px 14px;border:1px solid #dde2e8;border-radius:6px;
               background:#fff;cursor:pointer;font-size:13px;">展开全部</button>
      <button class="no-print" onclick="collapseAll()"
        style="padding:4px 14px;border:1px solid #dde2e8;border-radius:6px;
               background:#fff;cursor:pointer;font-size:13px;">折叠全部</button>`;
    nav.parentElement.appendChild(controls);
  }}

  window.expandAll = function() {{
    document.querySelectorAll('.module').forEach(m => {{
      m.classList.remove('collapsed');
      const c = m.querySelector('.module-content');
      if (c) c.style.display = '';
    }});
  }};
  window.collapseAll = function() {{
    document.querySelectorAll('.module').forEach(m => {{
      m.classList.add('collapsed');
      const c = m.querySelector('.module-content');
      if (c) c.style.display = 'none';
    }});
  }};

  // Collapse all modules by default except first
  document.querySelectorAll('.module').forEach((m, i) => {{
    if (i > 0) {{
      m.classList.add('collapsed');
      const c = m.querySelector('.module-content');
      if (c) c.style.display = 'none';
    }}
  }});
}})();
</script>

</body>
</html>"""


# ── Markdown → HTML processing ─────────────────────────────────────────────

def preprocess_for_html(md_text: str) -> str:
    """Enhance markdown with P0/P1/P2 markers and formula wrappers.

    Transformations:
    - P0/P1/P2 tags in text → HTML span badges
    - Collapsible section headers → HTML module structure
    - Code blocks → preserved
    """
    lines = md_text.split("\n")
    output = []
    in_code_block = False
    in_table = False

    for line in lines:
        # Track code blocks
        if line.startswith("```"):
            in_code_block = not in_code_block
            output.append(line)
            continue

        if in_code_block:
            output.append(line)
            continue

        # P0/P1/P2 tag injection - both headings and bold text
        if '🔴 P0' in line or '🔴P0' in line:
            line = re.sub(r'🔴\s*P0', '', line)
            # If line is a heading, prepend badge
            if line.startswith('#'):
                line = re.sub(r'^(#{1,5}\s+)', r'\1<span class="p0-tag">P0</span> ', line)
            elif '**' in line and line.strip().startswith('###'):
                # bold headings like "### [Name] **P0**"
                pass  # let the HTML handle it
        if '🟡 P1' in line or '🟡P1' in line:
            line = re.sub(r'🟡\s*P1', '', line)
            if line.startswith('#'):
                line = re.sub(r'^(#{1,5}\s+)', r'\1<span class="p1-tag">P1</span> ', line)

        # Wrap formulas $...$ with inline formula span
        line = re.sub(r'\$(.+?)\$', r'<span class="inline-formula">\(\1\)</span>', line)

        output.append(line)

    return "\n".join(output)


def extract_module_structure(md_text: str) -> list[dict]:
    """Split the markdown into modules based on '# 模块 N' headers."""
    modules = []
    current = None
    current_lines = []

    for line in md_text.split("\n"):
        m = re.match(r'^#+?\s+模块\s*(\d+)\s*[：:]\s*(.*)', line)
        if m:
            if current is not None:
                modules.append({"num": current["num"], "title": current["title"],
                               "content": "\n".join(current_lines)})
            current = {"num": int(m.group(1)), "title": m.group(2).strip()}
            current_lines = []
        elif re.match(r'^#+?\s+模块\s*(\d+)', line):
            if current is not None:
                modules.append({"num": current["num"], "title": current["title"],
                               "content": "\n".join(current_lines)})
            current = {"num": int(re.match(r'^#+?\s+模块\s*(\d+)', line).group(1)),
                       "title": ""}
            current_lines = []
        else:
            if current is not None:
                current_lines.append(line)

    if current is not None:
        modules.append({"num": current["num"], "title": current["title"],
                       "content": "\n".join(current_lines)})

    return modules


def build_toc(modules: list[dict]) -> str:
    """Build TOC HTML from module list."""
    icons = {
        1: "🎯", 2: "🗺", 3: "📝", 4: "📐", 5: "🔄",
        6: "📄", 7: "🃏", 8: "✍️",
    }
    items = []
    for mod in modules:
        icon = icons.get(mod["num"], "📌")
        title = mod["title"] if mod["title"] else f"模块 {mod['num']}"
        items.append(
            f'    <li><a href="#module-{mod["num"]}">{icon} {title}</a></li>'
        )
    return "\n".join(items)


def convert_to_html(md_text: str, title: str = "复习材料",
                     subtitle: str = "", stats: str = "") -> str:
    """Full pipeline: preprocess → extract modules → convert → wrap."""
    md_text = preprocess_for_html(md_text)

    # Use Python markdown library for the body conversion
    import markdown as md_lib
    extensions = [
        "markdown.extensions.extra",
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
    ]
    body_html = md_lib.markdown(md_text, extensions=extensions)

    # Extract modules from the ORIGINAL markdown for TOC/structure
    modules = extract_module_structure(md_text)
    toc_items = build_toc(modules)

    # Wrap each module in collapsible section
    # We need to map HTML sections to modules
    wrapped_body = wrap_modules_in_html(body_html, modules)

    return HTML_TEMPLATE.format(
        title=title,
        subtitle=subtitle,
        stats=stats,
        toc_items=toc_items,
        body=wrapped_body,
    )


def wrap_modules_in_html(body_html: str, modules: list[dict]) -> str:
    """Wrap module content in <section class="module"> blocks.

    Uses the module headers as separation markers.
    """
    # Split the HTML at module header boundaries
    # Module headers in the HTML look like: <h2>模块 1...</h2> or <h1>...
    module_boundary = re.compile(
        r'(<h[1-3][^>]*>\s*模块\s*\d+\s*[：:]\s*[^<]*</h[1-3]>)',
        re.IGNORECASE
    )

    parts = module_boundary.split(body_html)

    if len(parts) <= 2:
        # No modules detected, return as-is
        return body_html

    icons = {1: "🎯", 2: "🗺", 3: "📝", 4: "📐", 5: "🔄",
             6: "📄", 7: "🃏", 8: "✍️"}
    result = []
    mod_idx = 0

    # parts[0] is content before first module header
    if parts[0].strip():
        result.append(parts[0])

    i = 1
    while i < len(parts):
        header_html = parts[i]
        content_html = parts[i + 1] if i + 1 < len(parts) else ""

        # Extract module number for icon
        num_match = re.search(r'模块\s*(\d+)', header_html)
        mod_num = int(num_match.group(1)) if num_match else 0
        icon = icons.get(mod_num, "📌")

        # Get the module title from our structure
        mod_title = ""
        for m in modules:
            if m["num"] == mod_num:
                mod_title = m["title"]
                break

        # Clean up the header: remove excess tags, add icon
        clean_header = re.sub(
            r'<h[1-3][^>]*>(.*?)</h[1-3]>',
            rf'<span class="icon">{icon}</span><span class="title">\1</span>',
            header_html
        )

        result.append(
            f'<section class="module" id="module-{mod_num}">\n'
            f'  <div class="module-header">\n'
            f'    {clean_header}\n'
            f'    <span class="arrow">▼</span>\n'
            f'  </div>\n'
            f'  <div class="module-content">\n'
            f'    {content_html}\n'
            f'  </div>\n'
            f'</section>'
        )

        i += 2
        mod_idx += 1

    return "\n".join(result)


# ── Stats extractor ────────────────────────────────────────────────────────

def extract_stats(md_text: str) -> tuple[str, str, str]:
    """Extract title, subtitle, stats from the markdown frontmatter."""
    lines = md_text.split("\n")
    title = "高等固体物理·第四章 维度"
    subtitle = ""
    stats = ""

    for line in lines[:6]:
        if line.startswith("# ") and not "模块" in line:
            title = line.lstrip("# ").strip()
        if line.startswith("> 来源："):
            subtitle = line.lstrip("> ").strip()

    # Count P0/P1 items
    p0_count = len(re.findall(r'🔴\s*P0', md_text))
    p1_count = len(re.findall(r'🟡\s*P1', md_text))
    formula_count = len(re.findall(r'\$[^$]+\$', md_text))

    stats_parts = []
    if p0_count:
        stats_parts.append(f"P0 考点: {p0_count}")
    if p1_count:
        stats_parts.append(f"P1 概念: {p1_count}")
    if formula_count:
        stats_parts.append(f"公式: {formula_count}")
    if stats_parts:
        stats = " | ".join(stats_parts)

    return title, subtitle, stats


# ── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Convert exam review Markdown to beautiful HTML page.",
    )
    parser.add_argument("input", help="Path to the .md review file")
    parser.add_argument("-o", "--output", help="Output HTML file path (default: stdout)")
    parser.add_argument("--open", action="store_true",
                       help="Open the generated HTML in browser")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found", file=sys.stderr)
        sys.exit(1)

    raw = input_path.read_text(encoding="utf-8")
    title, subtitle, stats = extract_stats(raw)
    html = convert_to_html(raw, title=title, subtitle=subtitle, stats=stats)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(html, encoding="utf-8")
        print(f"HTML written to: {out_path.resolve()}", file=sys.stderr)
        if args.open:
            webbrowser.open(str(out_path.resolve()))
    else:
        # stdout might be GBK on Windows, encode to utf-8 and write bytes
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdout.write(html)


if __name__ == "__main__":
    main()
