# Solution 17 — Security

Three risks of `pull_request_target` running a fork's code with secrets:

1. The fork author can change the workflow code that runs in the privileged base-branch context, gaining access to the `GITHUB_TOKEN` and repository secrets.
2. A malicious checkout/run of the PR code executes arbitrary code on the runner with secret access enabled.
3. Token scope and write permissions granted to the base branch apply, so the attacker can modify the repo or push results back.

Avoid it: never run untrusted PR code under `pull_request_target`; use `pull_request` instead.