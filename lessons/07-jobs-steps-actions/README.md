# Lesson 07 — Jobs, steps, and actions

## What are jobs, steps, and actions?

- **Job:** a group of steps that runs on one runner.
- **Step:** one task inside a job. Either a shell command (`run:`) or a reusable **action** (`uses:`).
- **Action:** packaged, reusable automation you can call with `uses:`.

## Why do they exist?

To let you organize work into logical chunks (jobs) and reuse community work (actions) instead of writing everything yourself.

## Real-world analogy

A job is a **shift** at a bakery. Each step is a single task (mix dough, bake bread). An action is a pre-made machine you plug in (a dough mixer) instead of mixing by hand.

## A job with several steps

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run a command
        run: echo "Ready"
```

Line by line:

- `uses: actions/checkout@v4` — an **action** that copies your repository files onto the runner. Without it, the runner is empty.
- `with:` passes inputs to an action. Here, `python-version: "3.12"`.
- `run: echo "Ready"` — a plain shell command step.

## Multiple jobs that depend on each other

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "building"
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "testing"
```

- `needs: build` means the `test` job waits for `build` to finish first.
- Without `needs`, jobs run in **parallel** at the same time.

## See it in this repo

[`../../.github/workflows/03-multiple-steps.yml`](../../.github/workflows/03-multiple-steps.yml) (steps) and the validation workflow (jobs with `needs:`).

## Exercise

Make a workflow with two jobs: `setup` and `verify`, where `verify` runs only after `setup` succeeds.

> Solution: [`solutions/07-jobs-steps-actions.md`](../../solutions/07-jobs-steps-actions.md)

## Common mistakes

- Forgetting `actions/checkout` — the runner has none of your files, so tests fail with "file not found".
- Using `needs:` with the wrong job id (typos).
- Expecting steps in different jobs to share files — they do not by default (see the **artifacts** lesson).

## Knowledge check

1. What keyword runs a reusable action?
2. What keyword runs a shell command?
3. What does `needs:` do?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
