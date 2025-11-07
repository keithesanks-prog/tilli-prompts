# Git Submodule Setup Instructions

## Step 1: Create GitHub Repository

1. Go to GitHub and create a new repository named `tilli-prompts`
2. **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Copy the repository URL (e.g., `https://github.com/yourusername/tilli-prompts.git`)

## Step 2: Push to GitHub

```bash
cd /home/keith/tilli-prompts
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```

## Step 3: Add as Submodule in Prompt-Eval-Tool

```bash
cd /home/keith/prompt-eval-tool
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts
pip install -e tilli-prompts
```

## Step 4: Add as Submodule in SEAL

```bash
cd /home/keith/seal
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts
pip install -e tilli-prompts
```

## Step 5: Update .gitignore (Optional)

Add to `.gitignore` in each repo if you want to ignore the submodule directory:
```
# Don't ignore - we want the submodule tracked
# tilli-prompts/
```

## Step 6: Commit Submodule References

```bash
# In prompt-eval-tool
cd /home/keith/prompt-eval-tool
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"

# In SEAL
cd /home/keith/seal
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"
```

## Updating the Submodule

When the shared package is updated:

```bash
# In tilli-prompts
cd /home/keith/tilli-prompts
git add .
git commit -m "Update prompts/schemas"
git push

# In each repo that uses it
cd /home/keith/prompt-eval-tool  # or /home/keith/seal
git submodule update --remote tilli-prompts
```

## Cloning Repos with Submodules

When someone clones a repo that uses the submodule:

```bash
git clone <repo-url>
cd <repo-name>
git submodule update --init --recursive
pip install -e tilli-prompts
```

## Current Status

✅ Git repository initialized in `/home/keith/tilli-prompts`
⏳ Waiting for GitHub repository URL to complete setup

