param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"

function Invoke-Ripgrep {
    param([string[]]$Arguments)

    $output = & rg @Arguments 2>&1
    $code = $LASTEXITCODE

    if ($code -gt 1) {
        Write-Error "ripgrep failed with exit code $code`n$output"
    }

    return $output
}

if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
    Write-Error "ripgrep (rg) is required for this release check."
}

$rootPath = (Resolve-Path $Root).Path
Write-Host "Scanning public release tree: $rootPath"

$baseArgs = @(
    "-n",
    "-i",
    "--hidden",
    "--glob", "!/.git/*",
    "--glob", "!tools/check_public_release_redactions.ps1",
    "--glob", "!tools/copy_sanitized_project.ps1",
    # Benchmark verifier intentionally contains private-path and secret keyword
    # regexes as test patterns; it does not contain actual private values.
    "--glob", "!benchmarks/podmr-model-first-resonance-2026-05/scripts/verify_public_package.py"
)

$pathPatterns = @(
    "[A-Za-z]:[\\/][^\\/]+[\\/]Documents[\\/]MATLAB",
    "\\\\wsl",
    "/mnt/[A-Za-z]/[^/]+/Documents",
    "/home/[^/]+",
    "nv_bridge[\\/]queue",
    "[\\/]Users[\\/][^<\\/]+",
    "\.openclaw[\\/]workspace"
)

$keywordPattern = "(token|webhook|chat[-_]?id|password|secret|api[-_]?key|credential|authorization|bearer|cookie|slack|telegram|whatsapp)"
$keywordArgs = $baseArgs + @(
    "--glob", "!.gitignore",
    "--glob", "!README.md",
    "--glob", "!PUBLIC_RELEASE_MANIFEST.md",
    "--glob", "!SOURCE_PROVENANCE.md",
    "--glob", "!cases/README.md",
    "--glob", "!cases/*/project/README.md",
    "--glob", "!matlab/README.md",
    # Reviewed execution-source copies contain API/client code and schema terms such as
    # token/secret/webhook as identifiers. The path scan above still applies.
    "--glob", "!python/openclaw_nv_execution_source/**",
    "--glob", "!matlab/claw_execution_source/**",
    "--glob", "!openclaw_skills/**"
)

$hasHits = $false

Write-Host ""
Write-Host "== Local path and live-queue regex scan =="
foreach ($pattern in $pathPatterns) {
    $hits = Invoke-Ripgrep ($baseArgs + @("--", $pattern, $rootPath))
    if ($hits) {
        $hasHits = $true
        Write-Host ""
        Write-Host "[HIT] $pattern"
        $hits | ForEach-Object { Write-Host $_ }
    }
}

if (-not $hasHits) {
    Write-Host "[OK] No local path or live-queue regex hits."
}

Write-Host ""
Write-Host "== Sensitive keyword scan outside allowlisted release docs =="
$keywordHits = Invoke-Ripgrep ($keywordArgs + @($keywordPattern, $rootPath))
if ($keywordHits) {
    $hasHits = $true
    $keywordHits | ForEach-Object { Write-Host $_ }
}
else {
    Write-Host "[OK] No sensitive keyword hits outside allowlisted release docs."
}

Write-Host ""
if ($hasHits) {
    Write-Host "[FAIL] Review the hits above before publishing."
    exit 1
}

Write-Host "[PASS] No redaction hits found by this check."
