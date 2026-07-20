# Lesson 08 — Environment variables and contexts

## What is an environment variable?

An **environment variable** is a named value available to programs while they run. It is like a labeled box holding a value your scripts can read.

## Why do they exist?

So you can keep values (like a path or a name) in one place and reuse them, and so the system can pass information (like the runner's operating system) to your scripts automatically.

## Real-world analogy

A nametag. Everyone in the room can read your name without you repeating it each time. The nametag is the variable; the name is the value.

## Defining your own variable

```yaml
env:
  GREETING: "Hello from a variable"
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "$GREETING"
```

- `env:` at the top applies to the whole workflow.
- `$GREETING` reads the variable on Linux/macOS runners.

On Windows runners you would use `$env:GREETING`, but the GitHub-hosted `ubuntu-latest` (Linux) is what we use for most examples, so `$VAR` works.

## Step-level variables

```yaml
steps:
  - env:
      STEP_VAR: "only here"
    run: echo "$STEP_VAR"
```

## Built-in contexts

A **context** is a collection of values GitHub Actions fills in for you. You read them with `${{ ... }}`.

```yaml
steps:
  - run: echo "Branch is ${{ github.ref_name }}"
  - run: echo "Actor is ${{ github.actor }}"
```

- `${{ github.ref_name }}` — the branch or tag name.
- `${{ github.actor }}` — the user who triggered the run.
- `${{ runner.os }}` — the runner's operating system.

## See it in this repo

[`../../.github/workflows/04-environment-variables.yml`](../../.github/workflows/04-environment-variables.yml) prints several built-in and custom variables.

## Exercise

Add a workflow variable `FAVORITE` with your favorite word, and a step that prints it.

> Solution: [`solutions/08-environment-variables.md`](../../solutions/08-environment-variables.md)

## Common mistakes

- Using `$GREETING` on a Windows runner (use `$env:GREETING`). We avoid this by using Linux runners in examples.
- Forgetting the `${{ }}` syntax when reading a context value.
- Putting a real secret into `env:` in plain text — use **secrets** (Lesson 13) instead.

## Knowledge check

1. What is an environment variable?
2. What syntax reads a context value?
3. Give one example of a built-in context value.

> Answers in [`quizzes/README.md`](../quizzes/README.md).
