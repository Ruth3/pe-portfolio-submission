#!/bin/bash

# 1. cd into project folder
cd ~/pe-portfolio-submission || { echo "Project folder not found"; exit 1; }

# 2. Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# 3. Enter virtual environment and install dependencies
source .venv/bin/activate
pip install -r requirements.txt

# 4. Restart myportfolio service
systemctl restart myportfolio

echo "Redeploy complete. myportfolio service restarted."
