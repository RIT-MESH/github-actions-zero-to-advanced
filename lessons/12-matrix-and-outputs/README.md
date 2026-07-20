# Lesson 12 — Matrix builds and job outputs

## What is a matrix?

A **matrix** runs the same job multiple times with different settings, automatically.

## Why does it exist?

So you can test against several Python versions, several operating systems, etc. in one definition.

## Real-world analogy

A kitchen testing a recipe on three different ovens at once, to be sure it works everywhere.

## Matrix example

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -c "print('Python ' + __import__('sys').version)"
```

This runs three jobs, one per Python version.

## Job outputs

A job can produce a value that later jobs read:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.set.outputs.version }}
    steps:
      - id: set
        run: echo "version=1.2.3" >> "$GITHUB_OUTPUT"
  use:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Version is ${{ needs.build.outputs.version }}"
```

- `$GITHUB_OUTPUT` is a special file GitHub reads to collect step outputs.
- `outputs:` at the job level exposes them to other jobs.
- `${{ needs.build.outputs.version }}` reads another job's output.

## See it in this repo

[`../../.github/workflows/09-matrix-outputs.yml`](../../.github/workflows/09-matrix-outputs.yml) runs a matrix and shares an output between jobs.

## Exercise

Add a fourth Python version (3.13) to the matrix in your own copy and watch four jobs run.

> Solution: [`solutions/12-matrix-outputs.md`](../../solutions/12-matrix-outputs.md)

## Common mistakes

- Reading `outputs` from a job that has not finished — always `needs:` it first.
- Forgetting the `>>` append to `$GITHUB_OUTPUT` (a single `=` overwrites).
- Matrix values that include incompatible versions for your app.

## Knowledge check

1. What does a matrix do?
2. How do you expose a step's value to other jobs?
3. How do you read another job's output?

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