# Git Submodule Setup - Quick Start

## ✅ Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `tilli-prompts`
3. Description: "Shared prompt templates and Pydantic schemas for SEAL and Prompt-Eval-Tool"
4. Choose Public or Private
5. **DO NOT** check "Initialize with README" (we already have one)
6. Click "Create repository"
7. Copy the repository URL (e.g., `https://github.com/yourusername/tilli-prompts.git`)

## ✅ Step 2: Push to GitHub

```bash
cd /home/keith/tilli-prompts
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

Replace `<YOUR_GITHUB_REPO_URL>` with your actual GitHub repository URL.

## ✅ Step 3: Add as Submodule in Prompt-Eval-Tool

```bash
cd /home/keith/prompt-eval-tool
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts
pip install -e tilli-prompts
```

## ✅ Step 4: Add as Submodule in SEAL

```bash
cd /home/keith/seal
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts
pip install -e tilli-prompts
```

## ✅ Step 5: Commit Submodule References

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

## Current Status

✅ Git repository initialized
✅ Initial commit created
✅ Branch renamed to `main`
⏳ **Waiting for GitHub repository URL** - Create repo and run Step 2

## After Setup

Once the submodule is set up, you can:

- **Update the shared package**: Make changes in `tilli-prompts`, commit, push
- **Update in repos**: Run `git submodule update --remote tilli-prompts` in each repo
- **Version control**: Each repo can pin to a specific commit of the shared package

