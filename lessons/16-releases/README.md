# Lesson 16 — Creating releases

## What is a release?

A **release** is a labeled, downloadable version of your project at a point in time (e.g. `v1.0.0`).

## Why does it exist?

So users can find a known, stable version instead of the latest untested commit.

## Real-world analogy

A publisher printing "First Edition, 2026". Readers buy that specific edition, not loose pages.

## Creating a release in a workflow

```yaml
permissions:
  contents: write   # needed to create a release
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: softprops/action-gh-release@v2
        with:
          tag_name: v1.0.0
          name: Release v1.0.0
          body: "Automated release"
```

- `contents: write` is required to create tags/releases.
- `softprops/action-gh-release@v2` is a popular, maintained action.

## Attaching artifacts to a release

Build first, upload an artifact, then attach its files:

```yaml
- uses: actions/download-artifact@v4
  with:
    name: my-build
    path: dist
- uses: softprops/action-gh-release@v2
  with:
    files: dist/*
```

## See it in this repo

[`../../.github/workflows/14-release.yml`](../../.github/workflows/14-release.yml) creates a release when a tag starting with `v` is pushed.

## Triggering it manually

```powershell
# Windows PowerShell
git tag v0.1.0
git push origin v0.1.0
```

```bash
# macOS / Linux
git tag v0.1.0
git push origin v0.1.0
```

## Exercise

Create a workflow that builds a text file and attaches it to a release named `v0.2.0`.

> Solution: [`solutions/16-releases.md`](../../solutions/16-releases.md)

## Common mistakes

- Missing `permissions: contents: write` — release creation is denied.
- Tagging on the wrong branch.
- Forgetting to push the tag (`git push origin <tag>`).

## Knowledge check

1. What permission is needed to create a release?
2. What action does this repo use to create releases?
3. How do you trigger a tag-based workflow?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
