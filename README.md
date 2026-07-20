# GitHub Actions Zero to Advanced

> A beginner-friendly, hands-on GitHub Actions tutorial covering CI/CD, workflows, runners, testing, Docker, security, reusable workflows, releases, deployments, and advanced automation.

GitHub Actions Zero to Advanced is a beginner-friendly, hands-on learning repository covering workflow fundamentals, YAML, events, runners, automated testing, caching, artifacts, Docker, reusable workflows, security, releases, deployment approvals, and complete CI/CD pipeline design.

---

## Who is this for?

You have **zero** technical background. You have never used GitHub, Git, YAML, or CI/CD. By the end you will design, read, and debug production-grade GitHub Actions pipelines.

This tutorial assumes you do **not** know:

- GitHub or Git
- YAML
- CI/CD
- Linux commands
- environment variables
- secrets
- runners
- Docker
- cloud deployment
- software testing

Every concept is explained from scratch, in simple English, with analogies, small runnable examples, exercises, solutions, common mistakes, and knowledge checks.

## What you will learn

1. What automation means
2. What CI/CD means
3. What GitHub Actions is
4. How workflows are structured
5. How YAML works
6. How events trigger workflows
7. How jobs, steps, actions, runners, and commands work
8. How to test applications automatically
9. How to use artifacts, caches, matrices, outputs, and environments
10. How to manage secrets safely
11. How to build Docker images
12. How to create releases
13. How to reuse workflow logic
14. How to secure workflows
15. How to debug failures
16. How to build a realistic CI/CD pipeline

## Repository structure

```text
.
├── .github/
│   ├── workflows/              # Runnable example workflows (01–16)
│   ├── ISSUE_TEMPLATE/         # Bug report & feature request templates
│   ├── dependabot.yml          # Dependency update automation
│   └── pull_request_template.md
├── lessons/                    # Progressive lessons (01–20)
├── exercises/                  # Hands-on exercises
├── solutions/                  # Reference solutions
├── quizzes/                    # Knowledge checks with answers
├── examples/                   # Sample apps (Python + Node) and Docker
│   ├── python-app/
│   └── node-app/
├── docs/                       # Final project, interview guide, troubleshooting, diagrams
├── scripts/                    # Validation helper scripts
├── Makefile                    # `make validate` and friends
├── validate.ps1                # PowerShell validation entry point
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
└── README.md
```

## How to use this tutorial

1. Read the lessons in order, starting with `lessons/01-introduction/README.md`.
2. Each lesson ends with an exercise and a knowledge check.
3. Try the exercise yourself, then compare with the solution in `solutions/`.
4. Each workflow file in `.github/workflows/` is runnable. Push it (or run it on a branch) and watch it on the **Actions** tab.
5. Finish with the final project in `docs/final-project.md`.

See [`docs/getting-started.md`](docs/getting-started.md) for the full local setup guide.

## Quick start

```powershell
# Windows PowerShell
git clone https://github.com/RIT-MESH/github-actions-zero-to-advanced.git
cd github-actions-zero-to-advanced
.\validate.ps1
```

```bash
# macOS / Linux
git clone https://github.com/RIT-MESH/github-actions-zero-to-advanced.git
cd github-actions-zero-to-advanced
make validate
```

## Validation

This repository validates itself. The [`validation`](.github/workflows/90-validation.yml) workflow runs on every push and pull request and checks YAML, JSON, Markdown, Python tests, Node tests, secret scanning, and workflow syntax. See [`docs/validation-report.md`](docs/validation-report.md) for results.

## Safety

- No credentials, tokens, or private keys are committed.
- No cloud (AWS/Azure/GCP) account is required.
- No paid services are required.
- Cloud deployment examples are **simulated** and create no real resources.
- Workflows use minimal permissions.

See [`SECURITY.md`](SECURITY.md) for details.

## License

[MIT](LICENSE)

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). By participating you agree to [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
