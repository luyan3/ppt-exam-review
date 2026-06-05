#!/usr/bin/env python3
"""
PPT Exam Review — HTML Converter
==================================
Converts the structured Markdown review output into a beautiful,
self-contained HTML page with sidebar TOC, collapsible sections,
KaTeX-rendered formulas, color-coded priority markers, and print layout.

Usage:
  python to_html.py assp4_complete_review.md -o review.html
  python to_html.py assp4_complete_review.md                   # stdout
  python to_html.py assp4_complete_review.md --open             # browser

Dependencies:
  pip install markdown
"""

import argparse
import re
import sys
import webbrowser
from pathlib import Path


# ── HTML Template ──────────────────────────────────────────────────────────

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{
    delimiters: [
      {{left: '\\[', right: '\\]', display: true}},
      {{left: '\\(', right: '\\)', display: false}},
    ],
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    throwOnError: false
  }});"></script>
<style>
  /* ── Reset & Base ── */
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC",
                 "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 15px; line-height: 1.7; color: #1a1a2e;
    background: #f4f6f9;
  }}

  /* ── Layout: sidebar + main ── */
  .layout {{
    display: flex; min-height: 100vh;
  }}

  /* ── Sidebar ── */
  .sidebar {{
    position: fixed; top: 0; left: 0; bottom: 0;
    width: 240px; background: #1a1a2e; color: #cdd6f4;
    overflow-y: auto; z-index: 100;
    display: flex; flex-direction: column;
    box-shadow: 2px 0 8px rgba(0,0,0,0.15);
  }}
  .sidebar-header {{
    padding: 20px 18px 14px; border-bottom: 1px solid #2a2a4e;
    flex-shrink: 0;
  }}
  .sidebar-header h2 {{
    font-size: 14px; font-weight: 700; color: #f0f4ff;
    letter-spacing: 1px; text-transform: uppercase;
  }}
  .sidebar-header .badge {{
    font-size: 11px; color: #8892b0; margin-top: 4px;
  }}
  .sidebar-nav {{
    flex: 1; padding: 8px 0; overflow-y: auto;
  }}
  .sidebar-nav a {{
    display: flex; align-items: center; gap: 8px;
    padding: 8px 18px; color: #8892b0; text-decoration: none;
    font-size: 13px; transition: all 0.15s; border-left: 3px solid transparent;
  }}
  .sidebar-nav a:hover {{ color: #f0f4ff; background: #2a2a4e; }}
  .sidebar-nav a.active {{
    color: #fff; background: #2a2a4e; border-left-color: #58a6ff;
    font-weight: 600;
  }}
  .sidebar-nav a .icon {{ font-size: 14px; width: 20px; text-align: center; }}
  .sidebar-nav a .num {{
    display: inline-flex; align-items: center; justify-content: center;
    width: 20px; height: 20px; border-radius: 50%;
    background: #2a2a4e; font-size: 11px; flex-shrink: 0;
  }}
  .sidebar-nav a.active .num {{ background: #58a6ff; color: #1a1a2e; }}

  /* Sidebar control buttons */
  .sidebar-footer {{
    padding: 10px 14px; border-top: 1px solid #2a2a4e; flex-shrink: 0;
    display: flex; gap: 6px; flex-wrap: wrap;
  }}
  .sidebar-footer button {{
    flex: 1; padding: 5px 0; border: 1px solid #3a3a5e; border-radius: 6px;
    background: transparent; color: #8892b0; cursor: pointer;
    font-size: 11px; transition: all 0.15s; min-width: 60px;
  }}
  .sidebar-footer button:hover {{ background: #2a2a4e; color: #f0f4ff; }}

  /* Hamburger (mobile) */
  .hamburger {{
    display: none; position: fixed; top: 12px; left: 12px; z-index: 200;
    width: 36px; height: 36px; border: none; border-radius: 8px;
    background: #1a1a2e; color: #fff; font-size: 20px; cursor: pointer;
    align-items: center; justify-content: center;
  }}

  /* ── Main Content ── */
  .main {{
    flex: 1; margin-left: 240px; padding: 24px 32px; max-width: 960px;
  }}

  /* ── Header ── */
  .review-header {{
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: #fff; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px;
  }}
  .review-header h1 {{ font-size: 22px; margin-bottom: 4px; letter-spacing: 1px; }}
  .review-header .subtitle {{ font-size: 13px; opacity: 0.7; }}
  .review-header .header-badge {{
    display: inline-block; background: rgba(255,255,255,0.12);
    padding: 2px 10px; border-radius: 20px; font-size: 12px; margin-top: 6px;
  }}

  /* ── Module Sections ── */
  .module {{
    background: #fff; border-radius: 10px; margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06); overflow: hidden;
  }}
  .module-header {{
    padding: 13px 22px; cursor: pointer; user-select: none;
    display: flex; align-items: center; justify-content: space-between;
    transition: background 0.15s;
  }}
  .module-header:hover {{ background: #f8f9fc; }}
  .module-header .icon {{ font-size: 17px; margin-right: 8px; }}
  .module-header .title {{ font-weight: 600; font-size: 15px; color: #1a1a2e; }}
  .module-header .arrow {{
    transition: transform 0.2s; font-size: 12px; color: #999;
  }}
  .module.collapsed .module-header .arrow {{ transform: rotate(-90deg); }}
  .module.collapsed .module-content {{ display: none; }}
  .module-content {{ padding: 0 22px 18px; }}

  /* ── P0 / P1 / P2 Cards ── */
  .p0-tag, .p1-tag, .p2-tag {{
    display: inline-block; font-size: 11px; font-weight: 700;
    padding: 1px 8px; border-radius: 10px; margin-right: 5px;
    vertical-align: middle;
  }}
  .p0-tag {{ background: #dc3545; color: #fff; }}
  .p1-tag {{ background: #fd7e14; color: #fff; }}
  .p2-tag {{ background: #6c757d; color: #fff; }}

  .module-content h3, .module-content h4 {{
    margin-top: 16px; margin-bottom: 6px;
  }}

  /* ── KaTeX formula blocks ── */
  .module-content .katex-display {{
    margin: 6px 0; padding: 4px 0; overflow-x: auto;
  }}
  .module-content .katex {{ font-size: 1.05em; }}
  .katex-block {{
    background: #f0f4ff; padding: 8px 14px; border-radius: 6px;
    margin: 8px 0; overflow-x: auto; border: 1px solid #dde6f5;
  }}

  /* ── Tables ── */
  .module-content table {{
    width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 14px;
  }}
  .module-content th {{
    background: #eef2f7; padding: 7px 11px; text-align: left;
    font-weight: 600; border: 1px solid #dde2e8;
  }}
  .module-content td {{
    padding: 7px 11px; border: 1px solid #dde2e8;
  }}
  .module-content tr:nth-child(even) {{ background: #fafbfc; }}

  /* ── Code blocks (TSV, shells) ── */
  .module-content pre {{
    background: #1e1e2e; color: #cdd6f4; padding: 12px 16px;
    border-radius: 8px; overflow-x: auto; font-size: 13px;
    line-height: 1.5; margin: 8px 0;
  }}
  .module-content code {{
    font-family: "JetBrains Mono", "Fira Code", "Consolas", monospace;
    font-size: 13px;
  }}
  .module-content :not(pre) > code {{
    background: #eef2f7; padding: 1px 5px; border-radius: 3px; color: #cf222e;
  }}

  /* ── Blockquote ── */
  .module-content blockquote {{
    border-left: 3px solid #8b949e; padding: 5px 13px; margin: 6px 0;
    color: #57606a; background: #f6f8fa; border-radius: 0 4px 4px 0;
  }}

  /* ── Lists ── */
  .module-content ul, .module-content ol {{
    padding-left: 22px; margin: 6px 0;
  }}
  .module-content li {{ margin-bottom: 3px; }}

  /* ── Horizontal rules ── */
  .module-content hr {{
    border: none; border-top: 1px solid #e4e7ed; margin: 16px 0;
  }}

  /* ── Print styles ── */
  @media print {{
    .sidebar {{ display: none !important; }}
    .main {{ margin-left: 0 !important; padding: 0 !important; }}
    .hamburger {{ display: none !important; }}
    body {{ background: #fff; font-size: 11px; }}
    .module {{ break-inside: avoid; box-shadow: none; border: 1px solid #ddd; }}
    .no-print {{ display: none !important; }}
  }}

  /* ── Mobile ── */
  @media (max-width: 768px) {{
    .hamburger {{ display: flex; }}
    .sidebar {{
      transform: translateX(-100%); transition: transform 0.25s;
    }}
    .sidebar.open {{ transform: translateX(0); }}
    .main {{ margin-left: 0; padding: 12px 10px; }}
    .review-header {{ padding: 18px 16px; }}
    .review-header h1 {{ font-size: 18px; }}
    .module-content {{ padding: 0 14px 14px; }}
    .module-header {{ padding: 10px 14px; }}
  }}
</style>
</head>
<body>

<!-- Hamburger toggle (mobile) -->
<button class="hamburger no-print" id="hamburger" aria-label="Toggle sidebar">&#9776;</button>

<div class="layout">

  <!-- ── Sidebar ── -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h2>复习导航</h2>
      <div class="badge">{stats}</div>
    </div>
    <nav class="sidebar-nav" id="toc">
{toc_items}
    </nav>
    <div class="sidebar-footer no-print">
      <button onclick="expandAll()">展开全部</button>
      <button onclick="collapseAll()">折叠全部</button>
    </div>
  </aside>

  <!-- ── Main ── -->
  <div class="main">

    <header class="review-header">
      <h1>{title}</h1>
      <div class="subtitle">{subtitle}</div>
      <div class="header-badge">{stats}</div>
    </header>

    <main>
{body}
    </main>

  </div>
</div>

<script>
(function() {{
  // ── Collapsible modules ──
  document.querySelectorAll('.module-header').forEach(header => {{
    header.addEventListener('click', function() {{
      const module = this.parentElement;
      module.classList.toggle('collapsed');
    }});
  }});

  // Collapse all modules except the first by default
  document.querySelectorAll('.module').forEach((m, i) => {{
    if (i > 0) m.classList.add('collapsed');
  }});

  // ── Sidebar hamburger (mobile) ──
  const sidebar = document.getElementById('sidebar');
  const hamburger = document.getElementById('hamburger');
  if (hamburger) {{
    hamburger.addEventListener('click', function() {{
      sidebar.classList.toggle('open');
    }});
    // Tap outside closes sidebar
    document.addEventListener('click', function(e) {{
      if (window.innerWidth <= 768 &&
          !sidebar.contains(e.target) &&
          !hamburger.contains(e.target)) {{
        sidebar.classList.remove('open');
      }}
    }});
  }}

  // ── TOC: click → expand + scroll ──
  document.querySelectorAll('#toc a').forEach(link => {{
    link.addEventListener('click', function(e) {{
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const module = document.getElementById(targetId);
      if (!module) return;

      // Expand it
      module.classList.remove('collapsed');

      // Close sidebar on mobile
      if (window.innerWidth <= 768) sidebar.classList.remove('open');

      // Scroll header into view with offset for sidebar
      const header = module.querySelector('.module-header');
      if (header) {{
        const offset = 20;
        const top = header.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({{ top, behavior: 'smooth' }});
      }}
    }});
  }});

  // ── IntersectionObserver: highlight active module in sidebar ──
  const moduleEls = document.querySelectorAll('.module');
  const tocLinks = document.querySelectorAll('#toc a');
  if (moduleEls.length && tocLinks.length) {{
    const observer = new IntersectionObserver(entries => {{
      // Find the first module currently intersecting
      let activeId = null;
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          if (!activeId) activeId = entry.target.id;
        }}
      }});
      // If none are intersecting, pick the last one above viewport
      if (!activeId) {{
        let closest = null;
        let closestDist = Infinity;
        entries.forEach(entry => {{
          const rect = entry.target.getBoundingClientRect();
          const dist = Math.abs(rect.top);
          if (rect.top < 200 && dist < closestDist) {{
            closestDist = dist;
            closest = entry.target.id;
          }}
        }});
        activeId = closest;
      }}
      // Update active class
      tocLinks.forEach(link => {{
        link.classList.toggle('active', link.getAttribute('href') === '#' + activeId);
      }});
    }}, {{
      threshold: 0,
      rootMargin: '-80px 0px -60% 0px',
    }});
    moduleEls.forEach(m => observer.observe(m));
  }}

  // ── Expand / collapse all ──
  window.expandAll = function() {{
    document.querySelectorAll('.module').forEach(m => m.classList.remove('collapsed'));
  }};
  window.collapseAll = function() {{
    document.querySelectorAll('.module').forEach(m => m.classList.add('collapsed'));
  }};
}})();
</script>

</body>
</html>"""


# ── Markdown → HTML processing ─────────────────────────────────────────────

def _protect_formulas(md_text: str) -> tuple[str, list[str]]:
    """Replace LaTeX formulas with safe placeholders before markdown processing.

    Returns (text_with_placeholders, list_of_formula_html).
    """
    placeholders = []
    formula_map = {}

    def _replace_display(m):
        html = '<div class="katex-block">\\[' + m.group(1) + '\\]</div>'
        idx = len(placeholders)
        placeholders.append(html)
        return f'@@KATEX_DISPLAY_{idx}@@'

    def _replace_inline(m):
        html = '<span class="katex-inline">\\(' + m.group(1) + '\\)</span>'
        idx = len(placeholders)
        placeholders.append(html)
        return f'@@KATEX_INLINE_{idx}@@'

    # Process display math first ($$...$$), then inline ($...$)
    text = re.sub(r'\$\$(.+?)\$\$', _replace_display, md_text)
    text = re.sub(r'\$(.+?)\$', _replace_inline, text)

    return text, placeholders


def _restore_formulas(html: str, placeholders: list[str]) -> str:
    """Restore formula placeholders after markdown processing."""
    for idx, formula_html in enumerate(placeholders):
        html = html.replace(f'@@KATEX_DISPLAY_{idx}@@', formula_html)
        html = html.replace(f'@@KATEX_INLINE_{idx}@@', formula_html)
    return html


def preprocess_for_html(md_text: str) -> tuple[str, list[str]]:
    """Apply P0/P1 badges and protect formulas from markdown processing.

    Returns (processed_markdown, formula_placeholders).
    """
    lines = md_text.split("\n")
    output = []
    in_code_block = False

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block
            output.append(line)
            continue
        if in_code_block:
            output.append(line)
            continue

        # P0/P1 tag badges in headings
        if '\U0001f534 P0' in line or '\U0001f534P0' in line:
            line = re.sub(r'\U0001f534\s*P0', '', line)
            if line.startswith('#'):
                line = re.sub(r'^(#{1,5}\s+)', r'\1<span class="p0-tag">P0</span> ', line)
        if '\U0001f7e1 P1' in line or '\U0001f7e1P1' in line:
            line = re.sub(r'\U0001f7e1\s*P1', '', line)
            if line.startswith('#'):
                line = re.sub(r'^(#{1,5}\s+)', r'\1<span class="p1-tag">P1</span> ', line)

        output.append(line)

    return "\n".join(output), []


def convert_to_html(md_text: str, title: str = "复习材料",
                     subtitle: str = "", stats: str = "") -> str:
    """Full pipeline: protect formulas -> preprocess -> markdown -> restore formulas -> wrap."""
    # Step 1: Protect formulas from markdown processing
    md_text, formula_placeholders = _protect_formulas(md_text)

    # Step 2: Apply P0/P1 badges
    md_text, _ = preprocess_for_html(md_text)

    # Step 3: Convert markdown to HTML
    import markdown as md_lib
    extensions = [
        "markdown.extensions.extra",
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
    ]
    body_html = md_lib.markdown(md_text, extensions=extensions)

    # Step 4: Restore formula placeholders
    body_html = _restore_formulas(body_html, formula_placeholders)

    # Step 5: Extract modules and wrap
    modules = extract_module_structure(md_text)
    toc_items = build_toc(modules)
    wrapped_body = wrap_modules_in_html(body_html, modules)

    return HTML_TEMPLATE.format(
        title=title,
        subtitle=subtitle,
        stats=stats,
        toc_items=toc_items,
        body=wrapped_body,
    )


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
    """Build sidebar TOC links from module list."""
    icons = {1: "🎯", 2: "🗺", 3: "📝", 4: "📐", 5: "🔄",
             6: "📄", 7: "🃏", 8: "✍️"}
    items = []
    for mod in modules:
        icon = icons.get(mod["num"], "📌")
        title = mod["title"] if mod["title"] else f"模块 {mod['num']}"
        items.append(
            f'      <a href="#module-{mod["num"]}">'
            f'<span class="num">{mod["num"]}</span>'
            f'<span class="icon">{icon}</span>{title}</a>'
        )
    return "\n".join(items)



def wrap_modules_in_html(body_html: str, modules: list[dict]) -> str:
    """Wrap module content in <section class="module"> blocks."""
    module_boundary = re.compile(
        r'(<h[1-3][^>]*>\s*模块\s*\d+\s*[：:]\s*[^<]*</h[1-3]>)',
        re.IGNORECASE
    )
    parts = module_boundary.split(body_html)

    if len(parts) <= 2:
        return body_html

    icons = {1: "🎯", 2: "🗺", 3: "📝", 4: "📐", 5: "🔄",
             6: "📄", 7: "🃏", 8: "✍️"}
    result = []

    if parts[0].strip():
        result.append(parts[0])

    i = 1
    while i < len(parts):
        header_html = parts[i]
        content_html = parts[i + 1] if i + 1 < len(parts) else ""

        num_match = re.search(r'模块\s*(\d+)', header_html)
        mod_num = int(num_match.group(1)) if num_match else 0
        icon = icons.get(mod_num, "📌")

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

    return "\n".join(result)


# ── Stats extractor ────────────────────────────────────────────────────────

def extract_stats(md_text: str) -> tuple[str, str, str]:
    """Extract title, subtitle, stats from the markdown frontmatter."""
    lines = md_text.split("\n")
    title = "复习材料"
    subtitle = ""
    stats = ""

    for line in lines[:6]:
        if line.startswith("# ") and "模块" not in line:
            title = line.lstrip("# ").strip()
        if line.startswith("> 来源："):
            subtitle = line.lstrip("> ").strip()

    p0_count = len(re.findall(r'🔴\s*P0', md_text))
    p1_count = len(re.findall(r'🟡\s*P1', md_text))

    stats_parts = []
    if p0_count:
        stats_parts.append(f"P0 考点: {p0_count}")
    if p1_count:
        stats_parts.append(f"P1 概念: {p1_count}")
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
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdout.write(html)


if __name__ == "__main__":
    main()
