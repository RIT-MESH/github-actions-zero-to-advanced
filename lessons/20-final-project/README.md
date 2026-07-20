# Lesson 20 — Final project

## Goal

Combine everything into one realistic CI/CD pipeline.

## Scenario

A small application (`examples/python-app`) must be:

1. Linted.
2. Tested on a matrix of Python versions.
3. Built into a Docker image (no push).
4. Packaged as an artifact.
5. Released on a tag.
6. Deployed to a simulated `production` environment requiring approval.

## Your tasks

1. Read [`docs/final-project.md`](../../docs/final-project.md) for the full spec and rubric.
2. Write a single workflow `.github/workflows/final-project.yml` that performs all stages with proper `needs:` and minimal `permissions:`.
3. Use the reusable workflow from Lesson 15 for the build stage.
4. Add a security scan stage.
5. Confirm the `production` environment has a required approval (in repo settings).

## What "done" means

- The workflow runs green on `main`.
- A tag push creates a release.
- The `production` job waits for approval.
- No secrets are exposed; no cloud resources created.

> Reference solution lives in [`docs/final-project.md`](../../docs/final-project.md) under "Reference solution".

## Knowledge check

1. List the six stages of the final project.
2. Why does deployment need approval?
3. Why reuse the build workflow?

> Answers in [`quizzes/README.md`](../quizzes/README.md).

Congratulations — you have gone from zero to advanced. 🎉
