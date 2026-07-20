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

> Answers in [`quizzes/README.md`](../quizzes/README.md).
