# Interview guide

Short Q&A set to test understanding after completing the tutorial.

**Q1. What is the difference between CI and CD?**
CI automatically builds/tests on every change; CD automatically prepares or ships the tested result.

**Q2. Name the five core concepts of GitHub Actions.**
Workflow, event, job, step, runner.

**Q3. Why set `permissions:` explicitly?**
To grant the token only the privileges needed, reducing blast radius if a workflow is abused.

**Q4. Why is `pull_request_target` dangerous with untrusted code?**
It runs in the base branch context with secrets/token access, so a forked PR can run malicious code with elevated privileges.

**Q5. How do you pass a value from one job to another?**
Set `outputs:` on the job using `$GITHUB_OUTPUT`, then read `${{ needs.<job>.outputs.<name> }}`.

**Q6. What is a matrix for?**
Running the same job across multiple configurations (OS, language version) automatically.

**Q7. What is the difference between an artifact and a cache?**
Artifacts are saved run outputs for download/sharing; caches speed up future runs by reusing dependencies.

**Q8. How do you trigger a workflow manually?**
Add `workflow_dispatch` to `on:` and use the Run workflow button on the Actions tab.

**Q9. Why never `echo` a secret?**
It can leak even though GitHub masks exact matches (split, encoded, or URL forms may bypass masking).

**Q10. How do you make a deployment wait for human approval?**
Use `environment:` with required reviewers configured in repo settings.
