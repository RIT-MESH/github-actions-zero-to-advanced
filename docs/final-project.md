# Final project (capstone)

Build a **portfolio-grade** CI/CD pipeline for `examples/python-app`. No cloud resources, no real secrets.

## Pipeline stages (portfolio-grade)

```text
Validate (YAML/JSON)
   |
Lint (syntax)
   |
Unit tests across Python 3.10/3.11/3.12   ->   Coverage report
   |
Secret/security scan (gitleaks, checksum verified)
   |
Build package + checksums
   |
Build and scan Docker image (Trivy, informational)
   |
Generate SBOM (SPDX)
   |
Simulated staging deployment (environment: staging)
   |
Manual approval (production environment required reviewers)
   |
Simulated production deployment (only on v* tag)
   |
Release on v* tag (artifact + checksums + SBOM)
```

## Rules

- Use `needs:` to order stages.
- Use minimal `permissions:` per job (e.g. `contents: write` only for the release job).
- Add `concurrency:` to cancel redundant runs.
- Add `timeout-minutes:` to every job.
- Verify the gitleaks download checksum.
- Staging deploys after a successful main-branch build.
- Production deploys **only** on a version tag (`v*`) and requires approval.
- Release happens **only** on a version tag.
- Never print secrets; never create real cloud resources.

## Rubric

| Criterion | Pass when |
|-----------|----------|
| Stages | All stages present and ordered correctly |
| Permissions | Least privilege per job |
| Concurrency | `concurrency:` set, `cancel-in-progress: true` |
| Timeouts | Every job has `timeout-minutes:` |
| Coverage | Coverage report generated and uploaded |
| Security scan | gitleaks with checksum verification |
| Docker scan | Image built and scanned (informational) |
| SBOM | SPDX SBOM generated and uploaded |
| Staging/production flow | Staging on main; production + release only on tag |
| Approval | Production job uses `environment: production` |
| Safety | No secrets printed; no cloud resources |

## Reference solution

The complete, runnable solution lives at [`../.github/workflows/final-project.yml`](../.github/workflows/final-project.yml). It implements every stage above with proper dependencies, per-job permissions, concurrency, and timeouts.

To watch it run: push a change to `.github/workflows/final-project.yml` or `examples/python-app/**`, then open the **Actions** tab → **Final Project - Capstone CI/CD**. For the release and production stages, push a tag:

```powershell
# Windows PowerShell
git tag v0.3.0
git push origin v0.3.0
```

```bash
# macOS / Linux
git tag v0.3.0
git push origin v0.3.0
```

> The `production` environment must be created in **Settings → Environments** with a required reviewer for the approval gate to take effect. Without that, the job runs but waits on no one.