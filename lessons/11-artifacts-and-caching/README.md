# Lesson 11 — Artifacts and caching

## What are artifacts and caches?

- **Artifact:** a file (or folder) saved from a workflow run so you can download it later, or pass it to another job.
- **Cache:** saved dependencies reused to make future runs faster.

## Why do they exist?

- Artifacts: so a build result survives after the runner is destroyed, and so jobs can share files.
- Caches: so you do not download the same dependencies on every single run.

## Real-world analogy

- Artifact: the finished cake you take home from the bakery.
- Cache: a stocked pantry. Next time you bake, the flour is already there — no trip to the store.

## Uploading an artifact

```yaml
steps:
  - run: echo "build output" > build.txt
  - uses: actions/upload-artifact@v4
    with:
      name: my-build
      path: build.txt
```

## Downloading in another job

```yaml
steps:
  - uses: actions/download-artifact@v4
    with:
      name: my-build
  - run: cat build.txt
```

## Caching dependencies

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: ~/.cache/pip
      key: pip-${{ runner.os }}-${{ hashFiles('**/requirements.txt') }}
```

- `key:` identifies the cache. If `requirements.txt` changes, a new key is produced and a new cache is stored.

## See it in this repo

[`../../.github/workflows/08-artifacts-cache.yml`](../../.github/workflows/08-artifacts-cache.yml) uploads a file as an artifact and caches Python packages.

## Exercise

Add a step that uploads `README.md` as an artifact named `readme-snapshot`.

> Solution: [`solutions/11-artifacts-cache.md`](../../solutions/11-artifacts-cache.md)

## Common mistakes

- Artifacts are deleted after a default retention period — do not use them as permanent storage.
- A cache key that never changes means the cache never updates; one that always changes means the cache is never reused.
- Never put secrets into artifacts or caches.

## Knowledge check

1. What is an artifact?
2. What is a cache for?
3. What happens to a cache when its key changes?

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