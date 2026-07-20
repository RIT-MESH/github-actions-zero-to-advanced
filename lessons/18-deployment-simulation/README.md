# Lesson 18 — Deployment simulation (no real cloud)

## What is deployment?

**Deployment** is delivering your built application to where it will be used (a server, a service, etc.).

## Why does this lesson use a *simulation*?

Because real cloud deployments need real credentials and may cost money — both against this tutorial's safety rules. We simulate the steps so you learn the *shape* of a deployment pipeline without risk.

## Real-world analogy

A flight simulator. You practice landing the plane without ever leaving the ground.

## A simulated deployment pipeline

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "building (simulated)" > artifact.txt
      - uses: actions/upload-artifact@v4
        with:
          name: build
          path: artifact.txt
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/download-artifact@v4
        with: { name: build }
      - run: echo "Deploying to STAGING (simulated)"
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "Deploying to PRODUCTION (simulated)"
```

- `build` makes an artifact.
- `deploy-staging` runs in the `staging` environment (can require approval).
- `deploy-production` runs in `production` (can require additional approval).

**No real cloud resources are created.** Every step just echoes a message.

## Adding approval gates

On GitHub: **Settings → Environments → New environment** → name it `production` → add **Required reviewers**. Now the `production` job waits for a human to approve before running.

## See it in this repo

[`../../.github/workflows/16-deployment-sim.yml`](../../.github/workflows/16-deployment-sim.yml) runs the full simulated pipeline.

## Exercise

Add a `deploy-dev` job before `deploy-staging` that runs without an environment.

> Solution: [`solutions/18-deployment-simulation.md`](../../solutions/18-deployment-simulation.md)

## Common mistakes

- Forgetting `needs:` — staging and production deploy at the same time.
- Treating the simulation as real — it does nothing to any actual cloud.
- Not setting up environment approvals in GitHub settings.

## Knowledge check

1. Why do we simulate deployment here?
2. What does `environment: production` enable?
3. What makes a job wait for an earlier job?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
