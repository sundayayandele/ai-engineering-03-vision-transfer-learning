# Educational lab — fork, branch and GitHub free-tier-eligible runners

1. Fork the public repository into your own account.
2. Create a branch named `learner/vision-lab-01` from `main`.
3. Review `.github/workflows/ci.yml` and `education.yml`; enable Actions in your fork.
4. In **Actions → education-smoke → Run workflow**, select your branch.
5. Inspect synthetic-data training, pytest results, artifact size and disk space.
6. Modify `vision_transfer/model.py` on your branch and open a pull request into **your fork's main**.
7. Run CI on the pull request. Record logs, commit SHA and observations in your portfolio.

**Free runners:** Standard GitHub-hosted runners are generally free for eligible public-repository workflows; review your account's billing and current GitHub policy. Runners are ephemeral and do not provide persistent hosting or guaranteed GPU access.

**Real transfer learning:** A genuine pretrained model requires obtaining authorized pretrained weights and a properly licensed dataset. The default synthetic smoke lab deliberately avoids external weight downloads and makes no accuracy claims.
