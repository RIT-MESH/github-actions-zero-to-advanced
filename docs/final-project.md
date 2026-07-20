# Final project

Build a complete CI/CD pipeline for `examples/python-app`. No cloud resources, no real secrets.

## Pipeline stages

1. **Lint** — basic Python syntax check (`python -m py_compile`).
2. **Test matrix** — run pytest on Python 3.10, 3.11, 3.12.
3. **Docker build** — build the image (no push).
4. **Package** — upload the app as an artifact.
5. **Release** — on a `v*` tag, create a GitHub release with the artifact.
6. **Deploy (simulated)** — to a `production` environment requiring approval.

## Rules

- Use `needs:` to order the stages.
- Use minimal `permissions:` per job.
- Reuse Lesson 15's reusable workflow for the build/package stage.
- Include a security scan stage.
- No `pull_request_target` with untrusted code.
- Never print secrets.

## Rubric

| Criterion | Pass when |
|-----------|----------|
| Triggers | Runs on push to main; release on tag `v*` |
| Ordering | Stages run in the correct dependency order |
| Permissions | Each job uses least privilege |
| Reuse | Build stage uses the reusable workflow |
| Security scan | Gitleaks stage present |
| Release | Tag creates a release with an attached file |
| Deployment | Production job uses an environment |
| Safety | No secrets printed; no cloud resources |

## Reference solution

```yaml
name: "Final Project Pipeline"
on:
  push:
    branches: [main]
    tags: ["v*"]
  workflow_dispatch:
permissions:
  contents: read
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m py_compile examples/python-app/app.py

  test:
    needs: lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: |
          python -m pip install --upgrade pip
          pip install -r examples/python-app/requirements.txt
      - run: |
          cd examples/python-app
          python -m pytest -q

  build-package:
    needs: test
    uses: ./.github/workflows/12-reusable-build.yml
    with:
      app-name: final-project-app

  security-scan:
    needs: build-package
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  docker:
    needs: build-package
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v6
        with:
          context: examples/python-app
          push: false
          load: true
          tags: final-app:ci

  release:
    needs: [docker, security-scan]
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: reusable-build
      - uses: softprops/action-gh-release@v2
        with:
          tag_name: ${{ github.ref_name }}
          name: Release ${{ github.ref_name }}
          files: app.txt

  deploy-production:
    needs: release
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "Deploying to PRODUCTION (simulated)"
```

Save this as `.github/workflows/final-project.yml` to complete the project. Note: the `production` environment must be created in repo **Settings → Environments** with a required reviewer for the approval gate to take effect.
