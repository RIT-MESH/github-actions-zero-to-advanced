# Lesson 14 — Building Docker images

## What is Docker?

**Docker** packages your application and its dependencies into one portable image that runs the same everywhere.

## Why does it exist?

So "works on my machine" stops being a problem. The image includes everything needed to run the app.

## Real-world analogy

A sealed lunchbox. It contains a complete meal. Open it on any table and the meal is identical.

## A simple Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

- `FROM` starts from a ready-made Python image.
- `WORKDIR` sets the working folder inside the container.
- `COPY` copies a file in.
- `CMD` says what to run when the container starts.

## Building in GitHub Actions

See [`../../.github/workflows/11-docker-build.yml`](../../.github/workflows/11-docker-build.yml). It builds the image (and optionally loads it) using `docker/build-push-action`. It does **not** push to any registry, so no credentials are needed.

## Local run (optional, needs Docker installed)

```powershell
# Windows PowerShell
cd examples\python-app
docker build -t python-app-demo .
docker run --rm python-app-demo
```

```bash
# macOS / Linux
cd examples/python-app
docker build -t python-app-demo .
docker run --rm python-app-demo
```

Expected output:

```text
Sum of 2 and 3 is 5
```

## Exercise

Change the Dockerfile so the app prints a greeting before the sum. Rebuild and run.

> Solution: [`solutions/14-docker.md`](../../solutions/14-docker.md)

## Common mistakes

- Building on every push without a cache — slow. Use build cache actions.
- Forgetting `COPY` — the file is not in the image.
- Pushing to a real registry without secrets configured (this repo avoids pushing entirely).

## Knowledge check

1. What does Docker package?
2. Which instruction runs the app when the container starts?
3. Does this repo push images to a registry?

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