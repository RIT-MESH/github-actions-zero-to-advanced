# Lesson 19 — Debugging failures

## What is debugging?

**Debugging** is finding and fixing why a workflow failed.

## Why does it exist?

Because even well-written workflows break. You need a repeatable way to find the cause instead of guessing.

## Real-world analogy

Detective work. You gather clues (logs, variables, context) and follow them to the culprit.

## Step-by-step approach

1. **Open the failed run** on the Actions tab.
2. **Click the failing step** to expand its log.
3. **Read the last lines** — the actual error is usually near the bottom.
4. **Check inputs/variables** — print them safely to confirm values.
5. **Re-run with debug logging** if needed.

## Enabling debug logging

Set these repository secrets (values can be `true`):

- `ACTIONS_RUNNER_DEBUG=true`
- `ACTIONS_STEP_DEBUG=true`

Re-run the workflow. Much more detail appears in the logs.

## Printing context safely for debugging

```yaml
steps:
  - run: echo "ref=${{ github.ref_name }} os=${{ runner.os }}"
  - run: |
      echo "workspace=$GITHUB_WORKSPACE"
      ls -la
```

Never print secrets; print their length or `!= ''` status.

## Common causes and fixes

| Symptom | Likely cause | Fix |
|--------|--------------|-----|
| "file not found" | Forgot `actions/checkout` | Add it as the first step. |
| "permission denied" on release | Missing `contents: write` | Add it to `permissions:`. |
| Job skipped unexpectedly | `if:` condition is false | Check the condition value. |
| Matrix not running | Wrong key/indentation | Verify `strategy.matrix`. |
| Secret shows as empty | Name typo or wrong scope | Confirm secret name and environment. |

## See the troubleshooting guide

[`docs/troubleshooting.md`](../../docs/troubleshooting.md) has a full decision tree.

## Exercise

Find one previously failing run (yours or a sample) and write one sentence on its root cause.

> Solution: [`solutions/19-debugging.md`](../../solutions/19-debugging.md)

## Common mistakes

- Re-running without reading the log — you learn nothing.
- Printing secrets while debugging — rotate them after.
- Changing many things at once — you no longer know which fix worked.

## Knowledge check

1. Where do you find the actual error text?
2. How do you enable extra debug logging?
3. Why avoid printing secrets when debugging?

> Answers in [`quizzes/README.md`](../quizzes/README.md).
