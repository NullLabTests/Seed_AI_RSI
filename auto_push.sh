#!/bin/bash
# Navigate to the project directory
cd /home/vagrant/projects

# Add all changes to staging
git add .

# Commit changes with a message
git commit -m "Auto commit $(date)"

# Push to the remote repository
git push origin main

