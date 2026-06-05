# PPT Processing Reference

Edge cases, advanced techniques, and quality assurance for exam review PPT parsing.

---

## 1. Input Type Handling Matrix

| Input Type | Recommended Tool | Quality | Notes |
|-----------|----------------|---------|-------|
| .pptx with text | `extract_ppt.py` | ⭐⭐⭐⭐⭐ | Best — preserves hierarchy, notes, tables |
| .pdf (text-based) | `extract_ppt.py` (pdfplumber) | ⭐⭐⭐⭐ | Good — loses some hierarchy, best-effort tables |
| .pdf (scanned) | `extract_ppt.py --ocr` | ⭐⭐⭐ | Requires pytesseract + tesseract-ocr, verify accuracy |
| .png/.jpg slide | `extract_ppt.py --ocr` | ⭐⭐ | Single image, no context between slides |
| User pasted text | Direct analysis | ⭐⭐⭐⭐⭐ | Best quality, but user must provide complete content |
| YouTube lecture | — | ❌ | Not supported; ask user to find PPT or notes |

> **Critical note for Claude**: If extraction returns empty or nearly empty content (all slides say "[No extractable text content]"), immediately inform the user that the file appears image-only and suggest the OCR path. Do not proceed with analysis on empty data.

---

## 2. Character Handling Guidelines

### Chinese + English Mixed Content
- Keep technical English terms in original (CPU, GDP, DNA, etc.)
- Translate non-technical English annotations if they appear in slides
- Preserve Chinese terminology exactly (专业术语不翻译)

### Formulas
- Math: Use LaTeX `$...$` for inline, `$$...$$` for display
- Chemical: Use standard notation (H₂O, CO₂ — can use subscript if Unicode)
- If formula is an image → mark as `[公式图片 — 无法提取文本，请核对]`
- Long derivations: Break into step-by-step, each step numbered

### Special Characters
- Arrows: Use → (→) or ⇒ (⇒)
- Approx: Use ≈
- Degree: Use °C, ° (not \textdegree)
- Bullets: Use - or * (not • or ◦)

---

## 3. Long PPT Handling (>40 slides)

### Chunking Strategy
Do NOT try to analyze a 60+ slide PPT in one pass. Instead:

1. **First pass**: Extract content → analyze structure (chapter map + page count)
2. **Present overview**: "This PPT has 60 slides across 5 chapters. Which chapter should I start with?"
3. **Per-chapter deep analysis**: Take user's chosen chapter, do Pass 2-5 on that subset
4. **Progress tracking**: "Chapter 2/5 done. Continue to Chapter 3?"
5. **Final assembly**: When all chapters processed, offer to generate cross-chapter materials (comparison tables, merged formula sheet, comprehensive one-pager)

### Memory Optimization
- Keep only P0 items in active memory between chapters
- Store P1/P2 as summarized references, not full notes
- After completing a chapter, write its output to a file if user wants to preserve

---

## 4. Priority Detection Signals

Detect these patterns to assign P0/P1/P2:

### P0 Triggers (Core Exam Point)
| Signal | Example | Weight |
|--------|---------|--------|
| Explicit exam marking | "考点","必考","考试重点" | 🔴 Highest |
| Repeated across slides | Same concept on 3+ slides | 🔴 High |
| Speaker notes emphasis | Notes: "这个一定会考" | 🔴 High |
| Visual emphasis | Red text, surrounded by ⚠️/❗/⭐ | 🔴 High |
| Summary slides | "本章重点" / "Key Points" section | 🔴 High |
| Bold + larger font | Title-level emphasis on a specific term | 🟡 Medium |
| Definition formulas | Any `=` equation with named variables | 🟡 Medium |

### P1 Triggers (Important)
- Definitions introduced with "是","指","称为","defined as"
- Classification lists (types, categories, classifications)
- Step-by-step processes (number of stages ≥ 3)
- Comparison tables with ≥ 2 rows
- Graphs with labeled axes (describe the relationship)

### P2 Triggers (Supplementary)
- Examples preceded by "例如","比如","e.g."
- Historical background
- Anecdotes or case studies
- Statistics without conceptual framing
- "拓展阅读" sections

---

## 5. Table Interpretation

Tables in PPTs are often dense exam material. When extracting:

### Single-dimension tables
```
| 方法 | 优点 | 缺点 |
| A    | X1   | Y1   |
| B    | X2   | Y2   |
```
→ Extract as comparison table | Keep column headers | Ideal for Comparison Table output

### Multi-dimension/merged cells
```
|        | 条件A | 条件B |
| 方法1  | 适用  | 不适用 |
| 方法2  | 不适用 | 适用  |
```
→ Preserve matrix structure | Explicitly note merged cells | Mark as [复杂表格] if ambiguous

### Long text in cells
If a table cell contains >20 words → it's likely a list, not a table cell.
Extract it as: `- **Header**: Item 1, Item 2, Item 3...`

---

## 6. Image and Diagram Handling

When the PPT contains images/diagrams (no extractable text):

1. **Read the slide context** — surrounding text, title, and notes usually describe the image
2. **Describe what can be inferred**: "P30 contains a diagram labeled [title from nearby text]"
3. **Do NOT hallucinate diagram content** — say "该页为示意图，具体内容需人工查看"
4. **For flowcharts**: If text boxes in the image are separate elements, extract them in order
5. **For graphs**: Extract the axis labels and title; note the trend direction if mentioned in notes

---

## 7. Multi-Source Merge — Advanced

When merging ≥2 files, follow this algorithm:

```
Step 1: Parse each source independently
  Source A → [知识点列表A]
  Source B → [知识点列表B]

Step 2: Match by concept name similarity
  - Exact name match → 同一知识点
  - Partial match (Jaccard similarity >0.6) → 建议人工确认
  - Fuzzy match on Chinese characters (>=70% overlap) → 建议人工确认

Step 3: For matched items, compare:
  - Definition consistency → if same, keep the more complete version
  - Priority level → take the higher priority (P0 beats P1)
  - Content conflict → flag for user

Step 4: Resolution Rules
  - 内容一致 → 合并，保留最完整表述
  - 内容冲突 → 高亮标注："【冲突】来源A说X，来源B说Y"
  - 独家内容 → 标记为 [仅来源B提及]
```

---

## 8. Quality Assurance

### Self-Check Prompts
After completing any analysis, run through:
1. Does every P0/P1 item have a **source page**?
2. Are all **formulas** correctly formatted in LaTeX?
3. Are **contradictory statements** flagged?
4. Does the **one-pager** truly fit on one page (~500 words)?
5. Are **speaker notes** incorporated?
6. Is there any **hallucinated content** that wasn't in the PPT?
7. For **tables** — are they Markdown tables or plain text lists? (Should be tables)

### Red Flags
- PPT has <5 content slides → ask if this is the complete material
- Entirely image-based → suggest OCR
- User says "随便" or "你看着办" → default to Exam Intel + Core Notes
- Content is all bullet lists with no paragraphs → still valid, extract faithfully
