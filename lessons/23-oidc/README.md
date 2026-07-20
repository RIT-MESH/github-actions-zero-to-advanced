# Lesson 23 — OIDC and keyless cloud auth

## What is OIDC?

**OIDC** (OpenID Connect) lets a GitHub Actions workflow prove its identity to a cloud provider **without** a long-lived secret. The cloud trusts a short-lived token issued by GitHub for that specific run.

## Why does it exist?

Long-lived cloud credentials (access keys, service-account JSON) are dangerous: they can be stolen and reused. OIDC replaces them with a token that lives only for that run and is scoped to your repository.

## Real-world analogy

A hotel keycard that works only for your room and only during your stay. When you check out, it stops working. Compare that to carrying a master key everywhere.

## Why this lesson is simulation-only

Setting up real OIDC requires an AWS/Azure/GCP account and trust configuration — which this tutorial forbids (no cloud accounts, no paid services). So we show the *shape* of an OIDC workflow and how it would be configured, without connecting to a real cloud.

## The two required pieces

1. On the cloud side: configure a trust relationship (OIDC provider + role/policy) that trusts your repo.
2. On the workflow side: request a token and exchange it for cloud credentials.

## The workflow shape (simulated)

```yaml
permissions:
  id-token: write   # required to request an OIDC token
  contents: read
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Request OIDC token (simulated, no real cloud)
        run: |
          echo "In production this step exchanges the GitHub OIDC token for"
          echo "short-lived cloud credentials. Here we only print that the"
          echo "workflow has id-token: write permission set."
```

- `id-token: write` is the permission that lets the job request an OIDC token.
- No `secrets.*` is used for cloud auth — that is the whole point.

## How a real cloud exchange looks (reference, not run here)

```yaml
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789012:role/github-actions
    aws-region: us-east-1
```

This action reads the OIDC token automatically and assumes the role. No `AWS_ACCESS_KEY_ID` secret is needed. (Requires the AWS account trust setup first.)

## Security notes

- OIDC removes long-lived secrets, but the **permissions** and **trust policy** still matter.
- Restrict the cloud role to your repository and branch, not `*`.
- Never grant `id-token: write` to workflows that do not need it.

## Exercise

In one sentence, explain why OIDC is safer than a long-lived cloud access key.

> Solution: [`solutions/23-oidc.md`](../../solutions/23-oidc.md)

## Common mistakes

- Forgetting `permissions: id-token: write` — the token request is denied.
- Configuring the cloud trust policy as `*` — any repo could assume your role.
- Treating OIDC as "no security needed" — least-privilege still applies.

## Knowledge check

1. What does OIDC replace?
2. Which permission lets a job request an OIDC token?
3. Why is OIDC safer than a long-lived key?

> Answers: 1) Long-lived cloud credentials/access keys. 2) `id-token: write`. 3) The token is short-lived and scoped to your repo/run, so a stolen token cannot be reused.