# Lesson 01 — Introduction to Automation

## What is automation?

**Automation** means letting a computer do a repeatable task for you, instead of doing it by hand every time.

Example: every time you finish a piece of work, you currently have to remember to run tests, then package the files, then send them somewhere. Automation turns those three manual steps into one button (or one event) that does all three automatically.

## Why does automation exist?

Because humans forget, get tired, and make mistakes — especially when repeating boring steps. A computer runs the same steps the same way every time.

## Real-world analogy

Think of a coffee machine with a "latte" button. You press it once; the machine grinds beans, heats water, extracts coffee, and froths milk automatically. You did not manually perform each step. That is automation.

## What is CI/CD?

- **CI (Continuous Integration):** automatically building and testing code every time a change is made, so problems are found early.
- **CD (Continuous Delivery / Deployment):** automatically preparing (or releasing) the tested code so it can be used.

Analogy: CI is the kitchen tasting each dish as it is cooked. CD is the conveyor belt that automatically delivers finished dishes to the customer.

## What is GitHub Actions?

**GitHub Actions** is GitHub's built-in automation service. You write small text files that describe jobs; GitHub runs them for you on computers it provides (called **runners**).

You do not need to install or manage any servers. You write the instructions; GitHub does the work.

## Key words (defined now so later lessons are clear)

| Term | Meaning |
|------|---------|
| Repository | A project folder stored on GitHub. |
| Workflow | An automated process described in a YAML file. |
| Event | Something that starts a workflow (e.g. a push, a pull request). |
| Runner | The computer that performs the workflow jobs. |
| Job | A group of steps executed on a runner. |
| Step | One individual task inside a job. |
| Action | Reusable automation packaged for GitHub Actions. |
| Artifact | A file saved from a workflow run. |
| Cache | Saved dependencies reused to make future runs faster. |
| Secret | Protected sensitive information used by workflows. |

You will meet each of these again, slowly, with examples.

## How to read this tutorial

Go in order. Each lesson builds on the previous one. Do not skip the exercises — typing and running things yourself is how you actually learn.

## Knowledge check

1. In one sentence, what is automation?
2. What does CI stand for, and what does it do?
3. What is a "runner"?

