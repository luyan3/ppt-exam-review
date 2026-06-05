<#
.SYNOPSIS
    ppt-exam-review — Installer (Windows PowerShell)
.DESCRIPTION
    One-click installer for the ppt-exam-review Claude Code skill.
    Installs Python dependencies, clones the repo, and registers the skill.

    Usage:
        powershell -ExecutionPolicy Bypass -f install.ps1
        # or right-click → "Run with PowerShell"
#>

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/luyan3/ppt-exam-review"

Write-Host "╔══════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║    ppt-exam-review — Installer       ║" -ForegroundColor Blue
Write-Host "╚══════════════════════════════════════╝" -ForegroundColor Blue
Write-Host ""

# ── Check Python ──
Write-Host "==> Checking prerequisites..." -ForegroundColor Blue
$python = $null
foreach ($cmd in @("python3", "python")) {
    try {
        $v = & $cmd --version 2>&1
        if ($v -match "Python 3") {
            $python = $cmd
            break
        }
    } catch {}
}
if (-not $python) {
    Write-Host "  ✗ Python 3 not found!" -ForegroundColor Red
    Write-Host "    Download from: https://python.org"
    exit 1
}
Write-Host "  ✓ Python: $(& $python --version)" -ForegroundColor Green

# ── Claude Code check ──
try {
    $cc = & claude --version 2>&1
    Write-Host "  ✓ Claude Code: $cc" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ claude not in PATH — skill will be installed but won't activate until Claude Code is installed." -ForegroundColor Yellow
}

# ── Find repo directory ──
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (Test-Path "$ScriptDir\.git") {
    $CloneDir = $ScriptDir
    Write-Host "  ✓ Found local repository at $CloneDir" -ForegroundColor Green
} else {
    # Clone
    $CloneDir = "$env:USERPROFILE\.claude\ppt-exam-review"
    if (Test-Path "$CloneDir\.git") {
        Write-Host "==> Updating existing clone..." -ForegroundColor Blue
        git -C $CloneDir pull --ff-only
    } else {
        Write-Host "==> Cloning repository..." -ForegroundColor Blue
        git clone --depth=1 $RepoUrl $CloneDir
    }
}

# ── Install Python deps ──
Write-Host "==> Installing Python dependencies..." -ForegroundColor Blue
& $python -m pip install --quiet --upgrade python-pptx pdfplumber PyMuPDF markdown 2>&1 | Out-Null
Write-Host "  ✓ Dependencies installed" -ForegroundColor Green

# ── Install skill ──
Write-Host "==> Installing Claude Code skill..." -ForegroundColor Blue
$SkillDir = "$env:USERPROFILE\.claude\skills\ppt-exam-review"
New-Item -ItemType Directory -Force -Path "$SkillDir\scripts" | Out-Null

# On Windows we copy instead of symlink (symlinks need admin)
Copy-Item "$CloneDir\skill\SKILL.md" "$SkillDir\SKILL.md" -Force
if (Test-Path "$CloneDir\PPT-PROCESSING.md") { Copy-Item "$CloneDir\PPT-PROCESSING.md" "$SkillDir\" -Force }
if (Test-Path "$CloneDir\OUTPUT-FORMATS.md") { Copy-Item "$CloneDir\OUTPUT-FORMATS.md" "$SkillDir\" -Force }
Copy-Item "$CloneDir\scripts\extract_ppt.py" "$SkillDir\scripts\" -Force
Copy-Item "$CloneDir\scripts\to_html.py" "$SkillDir\scripts\" -Force
Copy-Item "$CloneDir\scripts\requirements.txt" "$SkillDir\scripts\" -Force

Write-Host "  ✓ Skill installed to $SkillDir" -ForegroundColor Green

# ── Test ──
Write-Host "==> Verifying..." -ForegroundColor Blue
try {
    & $python -c "from pptx import Presentation; from pdfplumber import open; print('  python-pptx + pdfplumber OK')" 2>&1 | Out-Null
    & $python -c "import markdown; import fitz; print('  markdown + PyMuPDF OK')" 2>&1 | Out-Null
    Write-Host "  ✓ All dependencies working" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Some dependencies incomplete (run: pip install markdown PyMuPDF)" -ForegroundColor Yellow
}

# ── Done ──
Write-Host ""
Write-Host "╔══════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  Installation complete!              ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "  Start Claude Code and try:"
Write-Host ""
Write-Host "    > 帮我复习这份 PPT"
Write-Host "    > (drag in a .pptx or .pdf file)"
Write-Host ""
Write-Host "  Or convert a review to HTML:"
Write-Host ""
Write-Host "    python $CloneDir\scripts\to_html.py review.md -o review.html --open"
Write-Host ""
Write-Host "  Repo: $RepoUrl"
Write-Host ""
