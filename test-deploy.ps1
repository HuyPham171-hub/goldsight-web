# Pre-deployment validation script

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "   Pre-Deploy Validation         " -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Checking Python version..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Python not found" -ForegroundColor Red
}
Write-Host ""

Write-Host "Checking required files..." -ForegroundColor Yellow
$requiredFiles = @(
    "requirements.txt",
    "rxconfig.py",
    "render.yaml",
    "runtime.txt",
    ".python-version",
    "README.md",
    "goldsight\goldsight.py"
)

$allFilesExist = $true
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "  OK: $file" -ForegroundColor Green
    } else {
        Write-Host "  MISSING: $file" -ForegroundColor Red
        $allFilesExist = $false
    }
}
Write-Host ""

Write-Host "Checking for duplicate requirements.txt..." -ForegroundColor Yellow
if (Test-Path "goldsight\requirements.txt") {
    Write-Host "  WARNING: Duplicate requirements.txt found" -ForegroundColor Red
} else {
    Write-Host "  OK: No duplicates" -ForegroundColor Green
}
Write-Host ""

Write-Host "Checking Reflex version..." -ForegroundColor Yellow
$reflexLine = Select-String -Path "requirements.txt" -Pattern "reflex=="
Write-Host "  $reflexLine" -ForegroundColor Green
Write-Host ""

Write-Host "Checking data cache..." -ForegroundColor Yellow
$cacheDir = "goldsight\data\cache"
if (Test-Path $cacheDir) {
    $jsonFiles = @(Get-ChildItem -Path $cacheDir -Filter "*.json")
    Write-Host "  OK: $($jsonFiles.Count) cache files" -ForegroundColor Green
} else {
    Write-Host "  WARNING: No cache directory" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Next: reflex run → git push → deploy" -ForegroundColor White
Write-Host "==================================" -ForegroundColor Cyan
