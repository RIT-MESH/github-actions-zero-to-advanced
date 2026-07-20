# Lesson 21 — Service containers

## What is a service container?

A **service container** is a Docker container GitHub Actions starts next to your job to provide a dependency such as a database (PostgreSQL, MySQL, Redis) without you installing it manually.

## Why do they exist?

So tests that need a real database can run in CI without a cloud database or any external service. The container lives only for the duration of the job.

## Real-world analogy

A pop-up tool bench wheeled next to your worktable while you build. When you finish, the bench is rolled away.

## The smallest example

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - name: Check the database is reachable
        run: |
          pg_isready -h localhost -p 5432 -U postgres
```

Line by line:

- `services:` starts the service containers for this job.
- `image: postgres:16` pulls the official Postgres 16 image.
- `env:` sets the password used to initialize the database.
- `ports:` maps the container's port 5432 to the runner.
- `options:` adds a health check so the job waits until Postgres is ready.
- `pg_isready` confirms the database is reachable from the step.

## Important notes

- Service containers run **on the runner**, not in any cloud. They create **no external resources** and cost nothing.
- On `ubuntu-latest` (Linux) they run directly. On Windows/macOS runners you must use the `container:` feature instead.
- The container is destroyed when the job ends — do not store data you need later.

## See it in this repo

[`../../.github/workflows/17-service-containers.yml`](../../.github/workflows/17-service-containers.yml) starts a Postgres service container and checks it is ready.

## Exercise

Change the service to `redis:7` and verify it answers with a `PING`.

> Solution: [`solutions/21-service-containers.md`](../../solutions/21-service-containers.md)

## Common mistakes

- Forgetting the health check — steps run before the database is ready and fail.
- Wrong host: use `localhost` (and port mapping) on Linux runners.
- Expecting the data to persist after the job — it does not.

## Knowledge check

1. What is a service container?
2. Why add a health check?
3. Does a service container create cloud resources?

> Answers: 1) A Docker container that provides a dependency (e.g. a database) for the job. 2) So steps wait until the service is ready. 3) No — it runs on the runner only.

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