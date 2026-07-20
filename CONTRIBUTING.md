# Contributing

First: thank you for wanting to help. 🎉

This repository is a teaching resource. Contributions that improve clarity, fix errors, or add safe, beginner-friendly examples are welcome.

## Ways to contribute

- Fix a typo or unclear sentence.
- Add a beginner-friendly example that needs **no cloud account** and **no secrets**.
- Improve a diagram (see `docs/diagrams.md`).
- Add a quiz question with an explained answer.

## Before you start

1. Read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
2. Open an issue describing your change so we can discuss it first.

## Making a change

```powershell
# Windows PowerShell
git checkout -b docs/your-fix
# ...make changes...
.\validate.ps1
git add -A
git commit -m "docs: clarify YAML indentation"
git push -u origin docs/your-fix
```

```bash
# macOS / Linux
git checkout -b docs/your-fix
make validate
git add -A
git commit -m "docs: clarify YAML indentation"
git push -u origin docs/your-fix
```

Then open a Pull Request using the [PR template](.github/pull_request_template.md).

## Rules

- **No secrets, tokens, or credentials.**
- **No cloud resources** (AWS/Azure/GCP) are created by any example.
- All enabled workflows must be functional.
- Keep language simple and beginner-friendly.
- Run `make validate` (or `.\validate.ps1` on Windows) before pushing.

## Validation checklist

Your PR passes if:

- YAML lints clean.
- Markdown lints clean.
- JSON is valid.
- Python and Node sample tests pass.
- Gitleaks finds no secrets.
- No new workflow triggers excessively (e.g. on a cron shorter than 5 minutes).

Thank you! 💚
