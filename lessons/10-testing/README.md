# Lesson 10 — Automated testing

## What is automated testing?

**Automated testing** means running small checks (tests) against your code automatically, so you find problems before anyone else sees them.

## Why does it exist?

Because code changes constantly. Manually checking every feature after every change is impossible. A test file says "this should happen"; the computer checks it instantly.

## Real-world analogy

A factory inspecting each product on the conveyor belt. If one fails, the belt stops before a bad product ships.

## The two sample apps in this repo

- Python: [`examples/python-app`](../../examples/python-app) — a function that adds two numbers, plus tests.
- Node: [`examples/node-app`](../../examples/node-app) — the same idea in JavaScript.

## Running tests locally

```powershell
# Windows PowerShell (Python)
cd examples\python-app
python -m pip install -r requirements.txt
python -m pytest
```

```bash
# macOS / Linux (Python)
cd examples/python-app
python3 -m pip install -r requirements.txt
python3 -m pytest
```

Expected output (last line):

```text
====== 2 passed in 0.05s ======
```

```powershell
# Windows PowerShell (Node)
cd examples\node-app
npm install
npm test
```

```bash
# macOS / Linux (Node)
cd examples/node-app
npm install
npm test
```

## Running tests in GitHub Actions

This is the heart of CI. See [`../../.github/workflows/06-test-python.yml`](../../.github/workflows/06-test-python.yml) and [`../../.github/workflows/07-test-node.yml`](../../.github/workflows/07-test-node.yml). They check out the code, install dependencies, and run the tests on every push and pull request.

## Exercise

Add a new test to `examples/python-app/tests/test_app.py` that checks `add(0, 0) == 0`. Push and watch the CI test it.

> Solution: [`solutions/10-testing.md`](../../solutions/10-testing.md)

## Common mistakes

- Forgetting `actions/checkout` — there is no code to test.
- Not installing dependencies — tests fail with "module not found".
- Committing `node_modules/` or `__pycache__/` (they are gitignored for you).

## Knowledge check

1. What does automated testing do for you?
2. Why install dependencies before running tests?
3. Which workflow file tests the Python app?

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