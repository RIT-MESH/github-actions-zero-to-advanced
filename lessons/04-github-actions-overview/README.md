# Lesson 04 — GitHub Actions overview

## What is GitHub Actions?

**GitHub Actions** is the automation system built into GitHub. You write a **workflow** file in your repository; GitHub runs it for you whenever something happens.

## Why does it exist?

So you do not need to set up your own automation servers. You describe the work in a file; GitHub provides computers (runners) to do it. You get automation without infrastructure.

## Real-world analogy

Imagine a restaurant. The **menu** (your workflow file) describes what dishes exist and when they are served (events). The **kitchen** (the runner) actually cooks them when an order (event) arrives. You write the menu; GitHub runs the kitchen.

## The five core ideas

1. **Workflow** — the YAML file that describes the automation. Lives in `.github/workflows/`.
2. **Event** — what starts the workflow (a push, a pull request, a schedule, a manual click...).
3. **Job** — a group of steps that runs on one runner.
4. **Step** — one action or command inside a job.
5. **Runner** — the computer (GitHub-provided or your own) that runs the jobs.

## How a run flows

```text
[Event happens] --> [Workflow starts] --> [Job(s) run on runner(s)] --> [Steps execute] --> [Result]
```

- An event (e.g. you push code) triggers a workflow.
- The workflow has one or more jobs.
- Each job runs on a runner.
- Each job has steps that run in order.
- When all steps succeed, the job succeeds.

## Where workflows live

```text
your-repo/
└── .github/
    └── workflows/
        └── my-workflow.yml
```

Any `.yml`/`.yaml` file under `.github/workflows/` becomes a workflow. The file name is your choice.

## The smallest real workflow

```yaml
name: Hello World
on: push
jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello from GitHub Actions!"
```

- `name:` is the workflow's display name.
- `on: push` means "run when someone pushes code".
- `jobs:` starts the jobs.
- `say-hello:` is the job's id (you choose it).
- `runs-on: ubuntu-latest` means "run on a GitHub-provided Linux computer".
- `steps:` lists the steps.
- `- run: echo "..."` runs a shell command.

This exact file lives in this repo at [`../../.github/workflows/01-hello-world.yml`](../../.github/workflows/01-hello-world.yml). You can watch it run on the **Actions** tab.

## What you will see

On the **Actions** tab of this repository you will see a green check when the workflow succeeds. Click a run to see each step's output.

## Exercise

Without looking, write the five core ideas of GitHub Actions from memory. Then check this lesson. Which one did you forget?

## Common mistakes

- Putting the workflow file **outside** `.github/workflows/`. It will not run.
- Naming the folder `workflow` (singular). It must be `workflows`.
- Forgetting `on:` — the workflow never starts.

## Knowledge check

1. Which folder must workflows live in?
2. What does `runs-on:` decide?
3. Name the five core ideas.

> Answers in [`quizzes/README.md`](../quizzes/README.md).
