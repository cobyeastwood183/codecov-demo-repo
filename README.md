# Demo

This repository demonstrates integration with Codecov.

## Setup Instructions

1. **Fork the Repository**
    - Click the **"Fork"** button at the top right of this repository on GitHub.
    - This will create a copy of the repository under your own GitHub account.

2. **Clone your forked repository:**
```bash
git clone https://github.com/your-username/codecov-demo-repo.git
cd codecov-demo-repo
```

3. **Install Codecov GitHub App**
   - Go to https://github.com/apps/codecov/installations/new
   - Install the Codecov GitHub App for your organization or repository.
   - This allows PR checks to appear without needing a token for public repos.

4. **Add Codecov Token**
   - In Codecov, you will see configue next to the new repository, click on configure and scroll down to copy the upload token named `CODECOV_TOKEN`.
   - In your GitHub repository, go to Settings → Secrets and variables → Actions → New repository secret.
   - Name it `CODECOV_TOKEN` and paste in the token.

5. **Install Dependencies:**
   - Run `python3 -m venv venv`, `source venv/bin/activate`, `pip install -r requirements.txt` to install the necessary Python packages.

6. **First Commit & Enable Actions**
```bash
git add .
git commit -m "Initial Codecov demo setup"
git push origin main
```
 Alternatively, use the CodeEditor UI to commit and push changes.

Go to Actions in your repo in Github and click Enable workflows when prompted.

7. **Create a Feature Branch and Make a Small Change**
```bash
git checkout -b demo/feature-1
```
 Alternatively, use the CodeEditor UI to create a branch

Edit any file in src/ or tests/ (even adding a comment is fine).

8. **Run Tests Locally Before Pushing:**
This ensures you can see the generated files before CI runs.
   - Execute `PYTHONPATH=$(pwd) pytest --cov=src --cov-report=xml` to run tests and generate a coverage report. Add this `--junitxml=junit.xml -o junit_family=legacy` to the command to generate a JUnit report.

coverage.xml → coverage data (used by Codecov)
junit.xml → JUnit test report (viewable/downloadable in CI) 

9. **Commit and Push the Branch:**
```bash
git add .
git commit -m "Demo change to trigger CI"
git push -u origin demo/feature-1
```
Alternatively, use the CodeEditor UI to commit and push changes.

10. **Open a Pull Request**
   - From your fork, open a PR from demo/feature-1 → main. In the UI, you will normally see an notification after the push, else you can click the configure button on that feature branch and you will see the create PR.

Once the PR is created, you should see status updates directly on the PR page:
   - CI check (CI / test-and-coverage) — confirms whether your tests passed and uploads the JUnit report as an artifact.
   - Codecov checks (codecov/project and codecov/patch) — display the coverage status for your changes and overall project.

11. **What to do next**
- Wait for all checks to complete.
- Once you’re comfortable with the results, merge the PR into main.
- After merging, log in to Codecov and open your repository’s dashboard — you should see your coverage uploads listed there.
