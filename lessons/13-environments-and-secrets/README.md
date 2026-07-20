# Lesson 13 — Environments and secrets

## What are secrets and environments?

- **Secret:** a protected value (like a token) stored in GitHub, usable by workflows but never shown in logs.
- **Environment:** a named deployment target (e.g. `staging`, `production`) that can require approval and hold its own secrets.

## Why do they exist?

So sensitive values are never written into files, and so risky deployments can require a human approval step.

## Real-world analogy

A safe (secret) inside a restricted room (environment). To use the safe you must first be let into the room.

## Storing a secret (safe practice)

1. Go to your repo → **Settings → Secrets and variables → Actions** → **New repository secret**.
2. Name it `EXAMPLE_SECRET`. Use a **fake** value such as `EXAMPLE_SECRET_VALUE`. Never use a real credential in this tutorial.

## Using a secret safely

```yaml
env:
  MY_SECRET: ${{ secrets.EXAMPLE_SECRET }}
steps:
  - run: echo "Secret length is ${#MY_SECRET}"
```

> Notice we print the **length**, never the value itself. This is the safe way to confirm a secret exists.

## Environments with approval

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
    steps:
      - run: echo "deploying (simulated)"
```

Setting `environment:` makes GitHub wait for any required reviewers on that environment before running the job.

> This repo uses `production` **simulated** — no real deployment happens. See Lesson 18.

## Secret masking is not a complete boundary

GitHub hides a secret's exact string in logs. But a secret can still leak indirectly (split, encoded, or used in a URL). Treat any possibly-leaked secret as compromised and rotate it.

## See it in this repo

[`../../.github/workflows/10-secrets-environments.yml`](../../.github/workflows/10-secrets-environments.yml) reads a secret safely and uses a simulated environment.

## Exercise

Store a repo secret `FAKE_TOKEN` with value `EXAMPLE_SECRET_VALUE`, and print only its length.

> Solution: [`solutions/13-secrets.md`](../../solutions/13-secrets.md)

## Common mistakes

- `echo "$MY_SECRET"` — this can leak the secret. Print metadata only.
- Hard-coding a secret in YAML — always use `secrets.*`.
- Using `pull_request_target` with untrusted code and secrets — a serious security hole. Avoid it.

## Knowledge check

1. Where do you store a secret?
2. Why print a secret's length and not its value?
3. What does an environment do beyond holding secrets?

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