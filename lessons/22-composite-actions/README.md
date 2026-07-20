# Lesson 22 — Composite actions

## What is a composite action?

A **composite action** packages several steps into one reusable action, defined in an `action.yml` file, without any Docker container or separate runtime.

## Why do they exist?

So you can reuse a small group of steps across many workflows without copy-pasting, and without the overhead of a full reusable workflow.

## Real-world analogy

A pre-assembled toolkit: one box containing a screwdriver, a wrench, and a tape measure. You grab the box instead of three separate tools.

## How it differs from a reusable workflow

| Feature | Reusable workflow | Composite action |
|---------|-------------------|------------------|
| Lives in | `.github/workflows/` | any folder with `action.yml` |
| Trigger | `workflow_call` | `uses:` from a step |
| Can contain `jobs:` | yes | no (steps only) |
| Use case | larger pipelines | small reusable step groups |

## The composite action file

See [`examples/composite-action/action.yml`](../../examples/composite-action/action.yml):

```yaml
name: "Greet and report"
description: "Prints a greeting and reports the runner OS"
inputs:
  who:
    description: "Who to greet"
    required: true
    default: "learner"
runs:
  using: "composite"
  steps:
    - name: Greet
      shell: bash
      run: echo "Hello, ${{ inputs.who }}!"
    - name: Report OS
      shell: bash
      run: echo "Running on ${{ runner.os }}"
```

- `runs: using: composite` marks this as a composite action.
- `inputs:` declares values the caller can pass.
- `steps:` are ordinary steps, but each must set `shell:` (composite steps cannot assume a default shell).

## Calling it

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: ./examples/composite-action
    with:
      who: "GitHub Actions"
```

`uses: ./examples/composite-action` points at the folder containing `action.yml` in the same repo.

## See it in this repo

[`../../.github/workflows/18-composite-actions.yml`](../../.github/workflows/18-composite-actions.yml) calls the composite action.

## Exercise

Add a second input `mood` to the composite action and print it in a third step.

> Solution: [`solutions/22-composite-actions.md`](../../solutions/22-composite-actions.md)

## Common mistakes

- Forgetting `shell:` on composite steps — required, since no default shell is assumed.
- Forgetting `runs: using: composite` — the file is not treated as an action.
- Pointing `uses:` at the file instead of the folder (use the folder path).

## Knowledge check

1. Which file defines a composite action?
2. What must every composite step set?
3. Can a composite action contain `jobs:`?

> Answers: 1) `action.yml`. 2) `shell:`. 3) No — steps only.

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