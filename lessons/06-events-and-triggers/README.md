# Lesson 06 — Events and triggers

## What is an event?

An **event** is something that starts a workflow. A push, a pull request, a schedule, a manual click — all are events.

## Why do events exist?

So automation only runs when it should. You do not want tests running constantly; you want them to run *when code changes* or *when someone asks*.

## Real-world analogy

A doorbell. It only rings when someone presses it. The press is the event; the chime is the workflow.

## Common events

| Event | Starts when... |
|-------|-----------------|
| `push` | Code is pushed to the repo. |
| `pull_request` | A pull request is opened or updated. |
| `workflow_dispatch` | A human clicks "Run workflow" manually. |
| `schedule` | A fixed time (cron) arrives. |
| `workflow_call` | Another workflow calls this one (reusable). |

## The smallest event example

```yaml
on: push
```

Run on every push.

## Multiple events

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

- `push` only on the `main` branch.
- `pull_request` only targeting `main`.
- `workflow_dispatch` adds a manual **Run workflow** button.

## See it in this repo

[`../../.github/workflows/02-events.yml`](../../.github/workflows/02-events.yml) shows several triggers, including `workflow_dispatch` so you can start it by hand.

## Run it manually

1. Open the **Actions** tab.
2. Select the **02 — Events** workflow on the left.
3. Click **Run workflow** → choose the branch → click the green button.
4. Watch the new run appear and turn green.

## Cron schedule

```yaml
on:
  schedule:
    - cron: "0 3 * * 1"   # every Monday at 03:00 UTC
```

Cron format: `minute hour day-of-month month day-of-week`. Five fields. The example above means minute 0, hour 3, every Monday (day 1).

> Keep cron rare. GitHub disables scheduled workflows on repos with no activity for 60 days.

## Exercise

Write a workflow that runs on `push` to a branch called `dev` and also manually.

> Solution: [`solutions/06-events.md`](../../solutions/06-events.md)

## Common mistakes

- Using `on: Push` (capital P). Events are lowercase.
- Cron shorter than 5 minutes — GitHub ignores it and it wastes resources.
- Forgetting `workflow_dispatch` and then wondering where the manual button is.

## Knowledge check

1. Which event gives you a manual "Run workflow" button?
2. What does `on: push` do?
3. How many fields does a cron expression have?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
