# PowerShell validation entry point (Windows). Equivalent of `make validate`.
[CmdletBinding()]
param()
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repo
$fail = 0

function Step($name, $script) {
    Write-Host "==> $name"
    try {
        & $script
        Write-Host "OK: $name"
    } catch {
        Write-Host "FAILED: $name : $_"
        $script:fail++
    }
}

Step "YAML/JSON" { python scripts/validate_yaml_json.py }
Step "Markdown"  { node scripts/validate-markdown.js }
Step "Workflows" { python scripts/validate-workflows.py }
Step "Python tests" {
    Push-Location examples/python-app
    python -m pytest -q
    Pop-Location
}
Step "Node tests" {
    Push-Location examples/node-app
    if (Test-Path package-lock.json) { npm ci } else { npm install }
    npm test
    Pop-Location
}

if ($fail -gt 0) {
    Write-Host "$fail step(s) failed."
    exit 1
}
Write-Host "All validation steps passed."
