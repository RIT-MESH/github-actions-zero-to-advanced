# Lesson 17 — Securing workflows

## What is workflow security?

Practices that prevent a workflow from being abused to leak secrets, run malicious code, or take unwanted actions.

## Why does it exist?

Workflows run with tokens and secrets. A poorly designed workflow can be tricked by a malicious pull request into leaking those.

## Real-world analogy

A building with many doors. Locks and keycards keep only authorized people in. Security is about reducing the number of unlocked doors.

## Core rules (all followed in this repo)

1. **Minimal permissions.** Always set `permissions:` to the least needed. Avoid the default broad token.
2. **No `pull_request_target` with untrusted code.** That event runs with secrets in the base branch context; a forked PR can exploit it.
3. **Pin actions to a version or SHA.** Avoid `@main`/`@master` which can change unexpectedly.
4. **No secrets in logs.** Never `echo` a secret. Print metadata only.
5. **No secrets in artifacts or caches.**
6. **Dependabot enabled** to keep actions and dependencies current.
7. **Secret scanning** (Gitleaks) runs on every push.
8. **Treat masking as incomplete.** Rotate anything that may have leaked.

## Example: minimal permissions

```yaml
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "read-only token"
```

## Example: safe handling of a secret

```yaml
env:
  TOKEN: ${{ secrets.FAKE_TOKEN }}
steps:
  - run: echo "Token present: ${{ env.TOKEN != '' }}"
```

We check *whether* it is set, never *what* it is.

## See it in this repo

- Every workflow sets `permissions:`.
- [`../../.github/workflows/15-security-scan.yml`](../../.github/workflows/15-security-scan.yml) runs Gitleaks.
- [`../../.github/dependabot.yml`](../../.github/dependabot.yml) keeps dependencies updated.
- [`../../SECURITY.md`](../../SECURITY.md) documents the policy.

## Exercise

List three risks of using `pull_request_target` to run a fork's code with secrets.

> Solution: [`solutions/17-security.md`](../../solutions/17-security.md)

## Common mistakes

- Relying on default permissions (too broad).
- Using `pull_request_target` then checking out and running the PR code.
- Pinning actions to a moving tag like `@v1` only — prefer `@v4` or a SHA for critical workflows.

## Knowledge check

1. Why set `permissions:` explicitly?
2. Why is `pull_request_target` risky?
3. Name one thing masking does NOT protect against.

## Exact steps to watch a workflow run on GitHub

1. Open the repository page on GitHub.
2. Select the **Actions** tab near the top.
3. In the left sidebar, select the workflow name (e.g. "01 - Hello World").
4. If the workflow has a **Run workflow** button, click it, choose the **main** branch, then click the green **Run workflow** button.
5. Click the newest run that appears.
6. Click the job name to expand it.
7. Click each step to expand its log and read the output.

## Troubleshooting

If a run fails, see [`docs/troubleshooting.md`](../../docs/troubleshooting.md) for a decision tree and common fixes. The most common cause of "file not found" is a missing `actions/checkout@v4` step.