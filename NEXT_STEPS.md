# Git Submodule Setup - Next Steps

## ✅ Completed

1. ✅ Git repository initialized in `/home/keith/tilli-prompts`
2. ✅ Initial commit created with all code
3. ✅ Branch renamed to `main`
4. ✅ `.gitignore` configured
5. ✅ Setup instructions created

## 📋 Next Steps (You Need to Do)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `tilli-prompts`
3. Description: "Shared prompt templates and Pydantic schemas for SEAL and Prompt-Eval-Tool"
4. Choose Public or Private
5. **DO NOT** check "Initialize with README" (we already have one)
6. Click "Create repository"
7. Copy the repository URL (e.g., `https://github.com/yourusername/tilli-prompts.git`)

### Step 2: Push to GitHub

```bash
cd /home/keith/tilli-prompts
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

Replace `<YOUR_GITHUB_REPO_URL>` with your actual GitHub repository URL.

### Step 3: Add as Submodule in Prompt-Eval-Tool

```bash
cd /home/keith/prompt-eval-tool
# Remove the old editable install (optional - it will be replaced)
pip uninstall tilli-prompts -y

# Add as submodule
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts

# Install from submodule
pip install -e tilli-prompts

# Commit the submodule reference
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"
```

### Step 4: Add as Submodule in SEAL

```bash
cd /home/keith/seal
# Add as submodule
git submodule add <YOUR_GITHUB_REPO_URL> tilli-prompts

# Install from submodule
pip install -e tilli-prompts

# Commit the submodule reference
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"
```

## 🔄 After Setup

### Updating the Shared Package

When you make changes to prompts/schemas:

```bash
cd /home/keith/tilli-prompts
git add .
git commit -m "Description of changes"
git push
```

### Updating in Repos

To pull the latest changes in each repo:

```bash
cd /home/keith/prompt-eval-tool  # or /home/keith/seal
git submodule update --remote tilli-prompts
pip install -e tilli-prompts  # Reinstall if needed
```

### Cloning Repos with Submodules

When someone clones a repo:

```bash
git clone <repo-url>
cd <repo-name>
git submodule update --init --recursive
pip install -e tilli-prompts
```

## 📝 Current Status

- ✅ Git repo ready: `/home/keith/tilli-prompts`
- ✅ Commits created: 3 commits
- ⏳ **Waiting for**: GitHub repository URL to complete setup

Once you create the GitHub repo and push, we can add it as a submodule to both repos!

