# GitHub Action Repository

This is the source repository where GitHub actions (push, pull request, merge) are monitored.

## Purpose
This repository serves as the **event source** for the webhook monitoring system. Any actions performed here will trigger webhooks that are captured and displayed in the `webhook-repo` system.

## Setup Instructions

### 1. Create this Repository on GitHub
```bash
# Initialize the repository locally
git init
git add .
git commit -m "Initial commit"

# Create a new repository on GitHub, then:
git remote add origin <your-action-repo-url>
git push -u origin main
```

### 2. Configure Webhook
1. Go to **Settings** → **Webhooks** → **Add webhook**
2. **Payload URL**: `https://your-webhook-server.com/webhook`
   - For local testing: Use ngrok URL (e.g., `https://abc123.ngrok.io/webhook`)
   - For production: Use your deployed webhook server URL
3. **Content type**: `application/json`
4. **Secret**: Leave empty (or add for security)
5. **Which events?**: Select:
   - ✅ Push events
   - ✅ Pull requests
6. ✅ Active
7. Click **Add webhook**

### 3. Test the System

#### Test Push Events
```bash
# Make a change
echo "Test push event" >> README.md
git add .
git commit -m "Test: trigger push webhook"
git push origin main
```

#### Test Pull Request Events
```bash
# Create a new branch
git checkout -b feature/test-pr
echo "Test PR" >> test.txt
git add .
git commit -m "Test: create PR"
git push origin feature/test-pr

# Then create a pull request on GitHub from feature/test-pr to main
```

#### Test Merge Events
```bash
# Merge the pull request on GitHub
# This will trigger a merge webhook event
```

## What Gets Tracked?
- **Push**: When you push commits to any branch
- **Pull Request**: When you open a new pull request
- **Merge**: When you merge a pull request (closes it)

## Branches
- `main` - Main branch
- `staging` - Staging branch (create if needed)
- `development` - Development branch (create if needed)
- Feature branches: `feature/*`

## Testing Scenarios

### Scenario 1: Simple Push
```bash
git checkout main
echo "Feature A" >> features.txt
git add .
git commit -m "Add Feature A"
git push
```

### Scenario 2: Branch Push
```bash
git checkout -b staging
echo "Staging changes" >> staging.txt
git add .
git commit -m "Staging update"
git push origin staging
```

### Scenario 3: Pull Request Flow
```bash
# Create feature branch
git checkout -b feature/new-feature
echo "New feature code" >> feature.js
git add .
git commit -m "Implement new feature"
git push origin feature/new-feature

# Go to GitHub and create PR: feature/new-feature → main
# Webhook triggers with PULL_REQUEST action

# Merge the PR on GitHub
# Webhook triggers with MERGE action
```

## Verification
After performing actions:
1. Check the webhook deliveries in GitHub: **Settings** → **Webhooks** → Click on your webhook → **Recent Deliveries**
2. View events in the monitoring UI at `http://localhost:5000` or your deployed URL
3. Events should appear within 15 seconds due to the auto-refresh

## Troubleshooting

### Webhook Not Triggering?
1. Check webhook configuration in GitHub settings
2. Verify the payload URL is correct and accessible
3. Look at "Recent Deliveries" to see if GitHub is sending requests
4. Check if your webhook server is running

### Events Not Showing in UI?
1. Check MongoDB connection in webhook-repo
2. Verify Flask app is running
3. Check browser console for errors
4. Manually test the `/events` API endpoint

## Repository Structure
```
action-repo/
├── README.md          # This file
├── .gitignore        # Git ignore rules
└── src/              # Sample source code (optional)
```
