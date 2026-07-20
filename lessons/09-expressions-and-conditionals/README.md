# Lesson 09 — Expressions and conditionals

## What is an expression?

An **expression** is a small formula evaluated by GitHub Actions, written inside `${{ ... }}`.

## Why do they exist?

So a workflow can make decisions: run this step only on a certain branch, only when a previous step failed, only on a certain operating system.

## Real-world analogy

Traffic lights. "If the light is red, stop; otherwise go." The condition decides the action.

## Common operators

| Operator | Meaning |
|----------|---------|
| `==` | equals |
| `!=` | not equals |
| `&&` | and |
| `\|\|` | or |
| `!` | not |

## `if` on a step

```yaml
steps:
  - name: Only on main
    if: github.ref_name == 'main'
    run: echo "This ran on main"
  - name: Always runs
    run: echo "I always run"
```

- The first step only runs when the branch is `main`.
- The second step always runs.

## `if` on a job

```yaml
jobs:
  deploy:
    if: github.ref_name == 'main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploying"
```

The whole `deploy` job is skipped unless on `main`.

## Special status functions

| Function | True when... |
|----------|--------------|
| `success()` | all previous steps in the job succeeded. |
| `failure()` | any previous step in the job failed. |
| `always()` | always (even on failure). |

```yaml
steps:
  - run: echo "trying"
  - if: always()
    run: echo "this runs no matter what"
```

## See it in this repo

[`../../.github/workflows/05-expressions-contexts.yml`](../../.github/workflows/05-expressions-contexts.yml) uses `if`, `github.ref_name`, and `runner.os`.

## Exercise

Make a step that only runs when the runner's OS is `Linux`. (Hint: `${{ runner.os == 'Linux' }}`.)

> Solution: [`solutions/09-expressions-conditionals.md`](../../solutions/09-expressions-conditionals.md)

## Common mistakes

- Using `=` instead of `==`. One `=` is assignment; YAML conditions need `==`.
- Forgetting quotes around strings: `github.ref_name == 'main'`.
- Putting `if:` in the wrong column so it attaches to the wrong step.

## Knowledge check

1. What wraps an expression?
2. What does `failure()` return?
3. Write a condition that is true only on the branch `dev`.

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