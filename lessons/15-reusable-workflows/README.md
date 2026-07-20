# Lesson 15 — Reusable workflows

## What is a reusable workflow?

A **reusable workflow** is one workflow that can be called by other workflows using `workflow_call`. You write the logic once and reuse it everywhere.

## Why does it exist?

To avoid copy-pasting the same jobs into many workflow files. Change it once; every caller benefits.

## Real-world analogy

A shared recipe book. Many kitchens cook the same dish using the same recipe, instead of each writing it down separately.

## Defining a reusable workflow

```yaml
name: Reusable Build
on:
  workflow_call:
    inputs:
      app-name:
        required: true
        type: string
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building ${{ inputs.app-name }}"
```

- `workflow_call` makes this workflow callable by others.
- `inputs:` declares values callers must (or may) provide.

## Calling it

```yaml
jobs:
  use-it:
    uses: ./.github/workflows/reusable-build.yml
    with:
      app-name: my-app
```

- `uses:` points at the reusable file path.
- `with:` passes the declared inputs.

> Note: a job that calls another workflow with `uses:` cannot also have `steps:`. They are separate concepts.

## See it in this repo

[`../../.github/workflows/12-reusable-build.yml`](../../.github/workflows/12-reusable-build.yml) is the reusable workflow. [`../../.github/workflows/13-call-reusable.yml`](../../.github/workflows/13-call-reusable.yml) calls it.

## Exercise

Make the reusable workflow take a second input `language` and print it.

> Solution: [`solutions/15-reusable-workflows.md`](../../solutions/15-reusable-workflows.md)

## Common mistakes

- Mixing `steps:` and `uses:` in the same job — not allowed for caller jobs.
- Forgetting `workflow_call` in `on:` — the workflow cannot be called.
- Wrong path in `uses:` (must start with `./` for same-repo workflows).

## Knowledge check

1. Which event makes a workflow reusable?
2. What keyword passes inputs to a called workflow?
3. Can a caller job have its own `steps:`?

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