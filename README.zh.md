# 📚 PPT Exam Review — Claude Code Skill

> **把期末复习 PPT 变成你的私人备考引擎。**
>
> Parse university exam review slides → structured notes, formula sheets, Anki cards, practice questions — all inside Claude Code.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

---

## ✨ 功能一览

| 模块 | 说明 | 适用场景 |
|------|------|---------|
| 🎯 **考试情报卡** | 章节权重、题型分布、PPT 明确标记 | 快速了解考试范围 |
| 🗺 **章节导航图** | 树形目录 + 页码映射 + P0/P1/P2 计数 | 制定复习路线 |
| 📝 **核心知识点精编** | 定义、通俗理解、考试形态、易错警示 | 核心背诵材料 |
| 📐 **公式/定理速查表** | 公式 + 适用条件 + 常见变形 | 考前速刷 |
| 🔄 **对比辨析表** | 易混淆概念并排对比 | 攻克选择题陷阱 |
| 📄 **一页纸终极总结** | 整门课缩为一页 A4 | 考前 1 小时救命 |
| 🃏 **Anki 卡片导出** | TSV 格式，直接导入 Anki | 碎片时间刷卡 |
| ✍️ **练习题生成** | 选择 + 简答 + 计算，含解析和评分要点 | 自测查漏 |

---

## 🚀 快速开始

### 前置条件

- [Claude Code](https://claude.ai/code) 已安装
- Python 3.8+

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/ppt-exam-review.git
cd ppt-exam-review

# 2. 安装 Python 依赖
pip install -r scripts/requirements.txt

# 3. 安装 Claude Code Skill
# macOS / Linux
ln -sf "$(pwd)/skill/SKILL.md" ~/.claude/skills/ppt-exam-review/SKILL.md

# Windows (PowerShell Admin)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\ppt-exam-review\SKILL.md" -Target "$pwd\skill\SKILL.md"

# 4. (可选) 复制参考文件以便 skill 内引用
cp PPT-PROCESSING.md OUTPUT-FORMATS.md ~/.claude/skills/ppt-exam-review/
```

### 使用示例

在 Claude Code 中：

**最简单的用法：**
```
> 帮我复习这份宏观经济学 PPT
> （拖入文件或给出路径）
```

**指定输出格式：**
```
> 复习这份 PPT，只要一页纸总结 + Anki 卡片
```

**多份 PPT 整合：**
```
> 我有老师课件和学长笔记两份 PPT，帮我合并整理重点
```

**深入某个章节：**
```
> 第 3 章讲得太简略了，展开详细一点
```

---

## 🧠 核心工作机制

### 五遍分析法

```
Pass 1 — 结构映射：识别章节架构，输出目录树
Pass 2 — 优先级分类：标记 P0/P1/P2
Pass 3 — 知识提取：定义、公式、考试形态
Pass 4 — 关联网络：连接相关知识点
Pass 5 — 输出合成：按选定格式生成复习材料
```

### 优先级判定

| 级别 | 含义 | 检测信号 |
|------|------|---------|
| 🔴 **P0** | 核心考点 | 标红/加粗/重复出现/含"必考""重点"等关键词/备注强调 |
| 🟡 **P1** | 重要概念 | 定义、定理、分类表、流程图、公式 |
| ⚪ **P2** | 背景了解 | 举例、背景介绍、拓展阅读 |

### 多源合并

当提供多份资料时自动进入合并模式：
- 交叉标记高频重点
- 高亮内容冲突
- 保留独家补充内容

---

## 📂 项目结构

```
ppt-exam-review/
├── README.md              # 👈 本文件
├── LICENSE                # MIT
├── PPT-PROCESSING.md      # 边缘情况处理参考
├── OUTPUT-FORMATS.md      # 输出模板大全
├── skill/
│   └── SKILL.md           # Claude Code Skill 本体
├── scripts/
│   ├── extract_ppt.py     # PPT/PDF 提取脚本
│   └── requirements.txt   # Python 依赖
└── examples/
    └── sample_output.md   # 输出示例
```

---

## 🛠 技术细节

### 支持的输入格式

| 格式 | 支持 | 说明 |
|------|------|------|
| `.pptx` | ✅ 原生 | 保留层级、表格、备注栏 |
| `.pdf` (文本) | ✅ pdfplumber | 最佳效果文本 PDF |
| `.pdf` (扫描) | ✅ OCR | 需安装 tesseract, 准确率 85-95% |
| `.png/.jpg` | ✅ OCR | 单张幻灯片识别 |
| 纯文本 | ✅ 直接 | 用户粘贴内容直接分析 |

### 依赖说明

```
# 核心依赖
python-pptx>=1.0.0     # PPTX 解析
pdfplumber>=0.10.0     # PDF 解析

# OCR 依赖（可选）
pytesseract>=0.3.10    # OCR 引擎
Pillow>=10.0.0         # 图片处理
pdf2image>=1.16.0      # PDF 转图片
```

---

## 🔄 交互流程

```
用户: "帮我复习这份PPT"
  │
  ▼
运行 extract_ppt.py 提取内容
  │
  ▼
Pass 1: 结构分析 → 输出章节概览
  │
  ├─ "这份PPT共5章42页，我发现了15个P0重点点"
  ├─ "你想看哪个模块？1.考试情报 2.章节导航 3.核心笔记..."
  │
  ▼
用户选择模块 → 输出对应内容
  │
  ▼
"需要深入哪个章节？/生成Anki卡片？/对比易混概念？"
```

---

## 🤝 贡献指南

欢迎 PR！无论是新增输出格式、改进 OCR 准确率、还是增加学科定制模板，都可以。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing`)
3. 提交改动 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing`)
5. 提交 Pull Request

### 开发方向

- [ ] 更多学科定制模板（医学、法学、计算机…）
- [ ] 自动检测图片中的公式并渲染为 LaTeX
- [ ] 支持 Markdown 输入（Obsidian 笔记）
- [ ] 生成思维导图（MMD 格式）
- [ ] 语音复习模式（将要点转为口语化录音稿）
- [ ] Web 界面（非 Claude Code 用户的独立版本）

---

## 📜 许可

MIT License — 可以自由使用、修改、商用。

---

## ⭐ Star History

如果你觉得有用，请点个 ⭐ — 让更多被期末考折磨的同学看到它！

---

<p align="center">Made with ❤️ for every student facing finals week</p>
