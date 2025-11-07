# Push to GitHub - Authentication Required

## Option 1: Use GitHub CLI (Easiest)

```bash
cd /home/keith/tilli-prompts
gh auth login
git push -u origin main
```

## Option 2: Use Personal Access Token (HTTPS)

1. Create a Personal Access Token:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (full control)
   - Copy the token

2. Push using token:
```bash
cd /home/keith/tilli-prompts
git remote set-url origin https://github.com/keithesanks-prog/tilli-prompts.git
git push -u origin main
# When prompted:
# Username: keithesanks-prog
# Password: <paste your token>
```

## Option 3: Set up SSH Keys

```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: https://github.com/settings/keys
# Then push:
cd /home/keith/tilli-prompts
git push -u origin main
```

## After Pushing Successfully

Once the code is pushed to GitHub, run these commands to add as submodules:

```bash
# In prompt-eval-tool
cd /home/keith/prompt-eval-tool
pip uninstall tilli-prompts -y  # Remove old editable install
git submodule add https://github.com/keithesanks-prog/tilli-prompts.git tilli-prompts
pip install -e tilli-prompts
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"

# In SEAL
cd /home/keith/seal
git submodule add https://github.com/keithesanks-prog/tilli-prompts.git tilli-prompts
pip install -e tilli-prompts
git add .gitmodules tilli-prompts
git commit -m "Add tilli-prompts as Git submodule"
```

