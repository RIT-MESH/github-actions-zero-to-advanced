# Lesson 05 — Workflow fundamentals

## What is a workflow?

A **workflow** is the YAML file that describes an automated process. It is the top-level container for everything GitHub Actions does.

## Why does it exist?

To give you one file that fully describes *what* runs, *when* it runs, *where* it runs, and *what steps* it performs. Everything is in version control, so automation is reviewable and repeatable.

## Anatomy of a workflow

```yaml
name: My Workflow        # 1) Display name
on: push                 # 2) Trigger(s)
permissions:
  contents: read         # 3) Minimal permissions
jobs:
  build:                 # 4) Job id
    runs-on: ubuntu-latest   # 5) Runner
    steps:               # 6) Steps
      - name: Say hi
        run: echo "hi"
```

### Line-by-line

1. `name:` — shown on the Actions tab. Optional but recommended.
2. `on:` — the event(s) that start this workflow.
3. `permissions:` — what the workflow's token is allowed to do. Keep it minimal.
4. `jobs:` — a map of job ids to job definitions.
5. `runs-on:` — the runner type. Common values: `ubuntu-latest` (Linux), `windows-latest` (Windows), `macos-latest` (macOS).
6. `steps:` — an ordered list. Each step is either an `action` (`uses:`) or a command (`run:`).

## The real example in this repo

See [`../../.github/workflows/03-multiple-steps.yml`](../../.github/workflows/03-multiple-steps.yml), which has several named steps running commands in order.

## Run it yourself

1. Make a **branch**: `git checkout -b try-workflow`.
2. Edit `.github/workflows/03-multiple-steps.yml` (any small change, even a comment).
3. Commit and push:

```powershell
# Windows PowerShell
git add .github\workflows\03-multiple-steps.yml
git commit -m "Try multiple steps"
git push -u origin try-workflow
```

```bash
# macOS / Linux
git add .github/workflows/03-multiple-steps.yml
git commit -m "Try multiple steps"
git push -u origin try-workflow
```

4. Open the **Actions** tab and watch the run.

Expected result: green check, with each step's logs visible.

## Exercise

Add a third step that prints your name. Push it and watch it run.

> Solution: [`solutions/05-workflow-fundamentals.md`](../../solutions/05-workflow-fundamentals.md)

## Common mistakes

- Indenting `steps:` wrong so they belong to the wrong job.
- Forgetting the `-` before a step.
- Using `runs-on: ubuntu` (incomplete). Use `ubuntu-latest`.

## Knowledge check

1. What key starts the list of jobs?
2. What does `runs-on:` choose?
3. Why set `permissions:` explicitly?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
