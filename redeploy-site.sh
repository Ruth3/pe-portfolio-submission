#!/bin/bash

# 1. Kill all existing tmux sessions
tmux kill-server 2>/dev/null

# 2. cd into project folder
cd ~/pe-portfolio-submission || { echo "Project folder not found"; exit 1; }

# 3. Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# 4. Enter virtual environment and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached tmux session running Flask
tmux new-session -d -s flask "cd ~/pe-portfolio-submission && source venv/bin/activate && flask run --host=0.0.0.0"

echo "Redeploy complete. Flask is running in tmux session 'flask'."
