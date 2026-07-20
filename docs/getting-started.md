# Getting started (local setup)

This guide installs the tools you need and runs validation locally. No cloud account or paid service is required.

## Required tools

| Tool | Why | Get it |
|------|-----|-------|
| Git | Version control | <https://git-scm.com/downloads> |
| A code editor (VS Code recommended) | Edit files | <https://code.visualstudio.com/> |
| Python 3.10+ | Python sample app + validation scripts | <https://www.python.org/downloads/> |
| Node.js 20+ | Node sample app + markdown script | <https://nodejs.org/> |

Optional:

| Tool | Why | Get it |
|------|-----|-------|
| Docker | Build/run the Docker example | <https://docs.docker.com/get-docker/> |
| GitHub CLI | Create repos and runs from the terminal | <https://cli.github.com/> |

## Clone

```powershell
# Windows PowerShell
git clone https://github.com/RIT-MESH/github-actions-zero-to-advanced.git
cd github-actions-zero-to-advanced
```

```bash
# macOS / Linux
git clone https://github.com/RIT-MESH/github-actions-zero-to-advanced.git
cd github-actions-zero-to-advanced
```

## Install Python dependencies

```powershell
# Windows PowerShell
python -m pip install -r examples\python-app\requirements.txt
```

```bash
# macOS / Linux
python3 -m pip install -r examples/python-app/requirements.txt
```

## Run the sample apps

```powershell
# Windows PowerShell (Python)
cd examples\python-app
python app.py
python -m pytest
cd ..\..
```

```bash
# macOS / Linux (Python)
cd examples/python-app
python3 app.py
python3 -m pytest
cd ../..
```

```powershell
# Windows PowerShell (Node)
cd examples\node-app
npm install
node app.js
npm test
cd ..\..
```

```bash
# macOS / Linux (Node)
cd examples/node-app
npm install
node app.js
npm test
cd ../..
```

## Validate locally

```powershell
# Windows PowerShell
.\validate.ps1
```

```bash
# macOS / Linux
make validate
```

Both run the same checks: YAML/JSON validity, basic Markdown checks, Python tests, Node tests, and workflow structure.

## If something fails

See [`troubleshooting.md`](troubleshooting.md).
