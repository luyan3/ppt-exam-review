#!/usr/bin/env bash
#
# ppt-exam-review — Installer (macOS / Linux / WSL)
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/luyan3/ppt-exam-review/main/install.sh | bash
#   # or
#   ./install.sh
#
set -euo pipefail

REPO_URL="https://github.com/luyan3/ppt-exam-review"
CLONE_DIR="$HOME/.claude/ppt-exam-review"
SKILL_DIR="$HOME/.claude/skills/ppt-exam-review"

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

info()  { echo -e "${BLUE}==>${NC} $1"; }
ok()    { echo -e "${GREEN}  ✓${NC} $1"; }
err()   { echo -e "${RED}  ✗${NC} $1"; exit 1; }

# ── Banner ──
echo ""
echo -e "${BLUE}╔══════════════════════════════════════╗${NC}"
echo -e "${BLUE}║    ppt-exam-review — Installer       ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════╝${NC}"
echo ""

# ── Check prerequisites ──
info "Checking prerequisites..."

PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON="$cmd"
        break
    fi
done
[ -z "$PYTHON" ] && err "Python 3 not found. Install from https://python.org"
ok "Python: $($PYTHON --version 2>&1)"

# Check Claude Code
if command -v claude &>/dev/null; then
    ok "Claude Code: $(claude --version 2>&1)"
else
    echo -e "  ${RED}⚠ claude not found in PATH — the skill will be installed but won't activate until Claude Code is installed.${NC}"
fi

# ── Clone or update ──
info "Downloading ppt-exam-review..."
if [ -d "$CLONE_DIR/.git" ]; then
    git -C "$CLONE_DIR" pull --ff-only 2>/dev/null && ok "Updated existing clone" || ok "Using existing clone"
else
    git clone --depth=1 "$REPO_URL" "$CLONE_DIR" 2>/dev/null && ok "Cloned repository" || err "Git clone failed"
fi

# ── Install Python deps ──
info "Installing Python dependencies..."
"$PYTHON" -m pip install --quiet --upgrade python-pptx pdfplumber PyMuPDF markdown 2>/dev/null
ok "Python dependencies installed"

# ── Install Claude Code skill ──
info "Installing Claude Code skill..."
mkdir -p "$SKILL_DIR/scripts"

ln -sf "$CLONE_DIR/skill/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$CLONE_DIR/PPT-PROCESSING.md" "$SKILL_DIR/" 2>/dev/null || true
cp "$CLONE_DIR/OUTPUT-FORMATS.md" "$SKILL_DIR/" 2>/dev/null || true
cp "$CLONE_DIR/scripts/extract_ppt.py" "$SKILL_DIR/scripts/" 2>/dev/null || true
cp "$CLONE_DIR/scripts/to_html.py" "$SKILL_DIR/scripts/" 2>/dev/null || true
cp "$CLONE_DIR/scripts/requirements.txt" "$SKILL_DIR/scripts/" 2>/dev/null || true

ok "Skill installed to $SKILL_DIR"

# ── Test ──
info "Verifying installation..."
"$PYTHON" -c "from pptx import Presentation; from pdfplumber import open; print('  python-pptx + pdfplumber OK')" 2>/dev/null && ok "Core dependencies work" || err "Dependency test failed"
"$PYTHON" -c "import markdown; import fitz; print('  markdown + PyMuPDF OK')" 2>/dev/null && ok "Extra dependencies work" || info "Optional dependencies incomplete (run: pip install markdown PyMuPDF)"

# ── Done ──
echo ""
echo -e "${GREEN}╔══════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Installation complete!              ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════╝${NC}"
echo ""
echo "  Start Claude Code and try:"
echo ""
echo "    > 帮我复习这份 PPT"
echo "    > (drag in a .pptx or .pdf file)"
echo ""
echo "  Or convert a completed review to HTML:"
echo ""
echo "    python $CLONE_DIR/scripts/to_html.py review.md -o review.html --open"
echo ""
echo "  Visit the repo for docs: $REPO_URL"
echo ""
