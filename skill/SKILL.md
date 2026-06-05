---
name: ppt-exam-review
description: >
  解析大学期末复习 PPT/PDF，提取核心知识，生成结构化复习材料。
  Detects content priority (P0/P1/P2), extracts definitions/formulas/tables,
  produces multi-format exam prep (notes, formula sheet, one-pager, Anki cards,
  practice questions). Use when user mentions "复习", "重点", "PPT", "课件",
  "期末", "exam review", uploads .pptx/.pdf, or asks to organize course
  materials for exam preparation.
---

# PPT Exam Review Engine

## Activation

1. User provides PPT/PDF or mentions a course to review
2. Run extraction: `python claude-files/ppt-exam-review/scripts/extract_ppt.py <filepath>`
3. If no file yet → ask for it; detect exam subject from description
4. If image-based → suggest `--ocr` flag + pytesseract install

## Multi-Pass Analysis Workflow

After ingesting the Markdown, perform these 5 passes:

### Pass 1 — Structure Mapping
Build the course tree: Chapter → Section → Subsection with slide ranges.
Note page counts per chapter to detect weight distribution.

### Pass 2 — Priority Classification
Label every content block as one of:
- **P0 Core Exam Point**: Red/bold text, repeated across slides, keywords ("考点","重点","必考","注意","⚠️"), speaker notes emphasis
- **P1 Important**: Definitions, theorems, key formulas, classification tables
- **P2 Supplementary**: Examples, background, case studies, anecdotes

### Pass 3 — Knowledge Extraction
For each P0/P1 item, extract:
- Exact definition/formula (preserve original wording)
- Exam-ready summary (1-sentence "layperson" version)
- Common question formats (MCQ, short answer, calculation, essay)
- Prerequisites (what you need to understand first)

### Pass 4 — Relationship Mapping
Connect related P0 items: causal, contrast, hierarchical, sequential.
Flag frequently co-examined concept pairs.

### Pass 5 — Output Synthesis
Generate user-requested format modules (see OUTPUT-FORMATS.md).
Ask before producing long outputs: "I found ~X P0 points across Y chapters.
Which output format(s) would you like? Options: [1-8]"

## Output Modules (User Selectable)

Ask: "What format(s) do you want?"
1. 📋 Exam Intel Card     — weights, question types, tips
2. 🗺  Chapter Map        — tree + slide mapping + P0/P1/P2 counts
3. 📝 Core Notes          — each P0/P1 expanded (definition, exam form, gotchas)
4. 📐 Formula Sheet       — all formulas with conditions, symbols, variants
5. 🔄 Comparison Table    — confuse-prone concept pairs side-by-side
6. 📄 One-Pager           — A4 cheat sheet (exam-final-hour material)
7. 🃏 Anki Cards          — TSV ready for Anki import (front|back|tags)
8. ✍️ Practice Questions  — generate from P0 points (MCQ + short answer)

Default when unspecified: #1 + #3 (quickest high-value).

## Interactive Refinement

After first output, offer:
- "Dive deeper into [chapter]" — expand that chapter's P1 notes
- "Simplify to only P0" — strip background, keep exam essentials only
- "Generate [Anki/Practice Qs]" — switch to another module
- "Compare with another PPT" — activate multi-source merge mode
- "Export as [format]" — if user wants plain text / JSON

## Multi-Source Merge Mode

When user has ≥2 files (e.g., lecture PPT + review session notes):
1. Extract each independently
2. Cross-reference: mark overlapping P0 items as [高频重点]
3. Flag content conflicts: "PPT A says X, PPT B says Y → verify with textbook"
4. Highlight unique items from each source
5. Generate merged outline with conflict notes

## Quality Checklist (Always Required)

- [ ] Every P0 item cites its source slide number ("来源：P15-P17")
- [ ] No fabricated content — mark uncertainties as [PPT未提及]
- [ ] Formulas use LaTeX ($...$ for inline, $$...$$ for display)
- [ ] Tables preserved as Markdown tables (not plain text)
- [ ] Speaker notes incorporated (they often contain exam hints)
- [ ] Active voice; no hedging ("might be", "possibly") on extracted facts
- [ ] For ambiguous slides, add footnote: [该页识别不清，建议人工核对]

## Constraints

- **Don't generate all 8 modules at once** — ask first, the output will exceed context
- **Keep each module focused** — one-pager is truly one page, not five
- **Chunk long PPTs** (>40 slides): output chapter-by-chapter, let user navigate
- **If extraction yields nothing** (image-only PPT): inform about OCR path
- **Never invent**: "PPT 中没有提到 [topic]" is better than guessing
