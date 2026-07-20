# Security Policy

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

Email: `security@example.invalid` (placeholder — replace with your real contact for forks).

Or use GitHub's **Report a vulnerability** feature on the **Security** tab of this repository.

## What this repository protects

- **No secrets in code.** No API keys, tokens, passwords, or private keys are stored in this repository.
- **Minimal permissions.** Every workflow sets `permissions:` to the least privileges needed.
- **No cloud resources.** Deployment examples are simulated and create nothing real.
- **No unsafe `pull_request_target`.** Workflows do not use `pull_request_target` to run untrusted code with secrets.
- **Secret scanning.** A Gitleaks scan runs on every push and pull request.
- **Dependency updates.** Dependabot keeps GitHub Actions and npm/Python dependencies current.

## Important: secret masking is not a complete boundary

GitHub Actions automatically hides (masks) the value of a registered secret in logs. This is helpful but **not** a complete security boundary:

- A secret can leak through indirect output (e.g. split across lines, base64, or used in a URL).
- A workflow can be tricked into printing a secret via `pull_request_target` if it runs untrusted code.
- Masking only applies to *exact* matches of the registered secret string.

**Rules:**

1. Never `echo` a secret on purpose.
2. Never store secrets in artifacts or caches.
3. Never pass secrets to workflows you do not control.
4. Treat any secret that *may* have leaked as **compromised** and rotate it.

## Secret hygiene for learners

For this tutorial you will use **fake** secret values like `EXAMPLE_SECRET_VALUE` so nothing real is ever exposed.

See [`lessons/13-environments-and-secrets/README.md`](lessons/13-environments-and-secrets/README.md) for safe, guided practice.
