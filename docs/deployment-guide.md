# Deployment Guide

This document provides detailed instructions for deploying the SkillUp Life Slackbot.

## Prerequisites

Before deployment, ensure you have:

- A Slack workspace with admin privileges
- An OpenAI API account with API key
- A Supabase account
- Access to an N8N instance (cloud or self-hosted)

## Step 1: Supabase Setup

### Create Supabase Project

1. Log in to [Supabase](https://app.supabase.io/)
2. Click "New Project"
3. Enter project details:
   - Name: `skilledup-slackbot`
   - Database Password: Create a strong password
   - Region: Choose a region close to your users
4. Click "Create new project"

### Enable pgvector Extension

1. Go to the SQL Editor in your Supabase project
2. Run the following SQL:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```
3. Click "Run" to execute the query

### Create Database Tables

1. In the SQL Editor, run the following SQL to create the necessary tables:
   ```sql
   -- Create the daily_updates table
   CREATE TABLE IF NOT EXISTS daily_updates (
     id SERIAL PRIMARY KEY,
     slack_user_id TEXT NOT NULL,
     update_text TEXT NOT NULL,
     timestamp TIMESTAMP NOT NULL,
     summary TEXT,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Create the documents table with vector support
   CREATE TABLE IF NOT EXISTS documents (
     id SERIAL PRIMARY KEY,
     content TEXT NOT NULL,
     metadata JSONB,
     embedding vector(1536),
     daily_update_id INTEGER REFERENCES daily_updates(id),
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Create an index for similarity search
   CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
   ```

2. Click "Run" to execute the query

### Get Supabase Credentials

1. Go to Project Settings > API
2. Note down the following:
   - Project URL
   - API Key (anon public)

## Step 2: Slack Setup

### Create Slack App

1. Go to [Slack API](https://api.slack.com/apps)
2. Click "Create New App" > "From scratch"
3. Enter app name (e.g., "SkillUp Life Bot") and select your workspace
4. Click "Create App"

### Configure App Permissions

1. In the left sidebar, click "OAuth & Permissions"
2. Scroll down to "Scopes" > "Bot Token Scopes"
3. Add the following scopes:
   - `channels:history`
   - `channels:read`
   - `chat:write`
   - `users:read`
4. Click "Save Changes"

### Install App to Workspace

1. Scroll up to "OAuth Tokens for Your Workspace"
2. Click "Install to Workspace"
3. Review the permissions and click "Allow"

### Get Slack Credentials

1. After installation, note down the "Bot User OAuth Token" (starts with `xoxb-`)
2. Go to "Basic Information" in the left sidebar
3. Scroll down to "App Credentials" and note down the "Signing Secret"

### Create App-Level Token

1. In the left sidebar, click "Basic Information"
2. Scroll down to "App-Level Tokens" and click "Generate Token"
3. Name the token (e.g., "SkillUp Life Bot Token")
4. Add the `connections:write` scope
5. Click "Generate"
6. Note down the generated token (starts with `xapp-`)

## Step 3: OpenAI Setup

1. Log in to [OpenAI](https://platform.openai.com/)
2. Go to API keys
3. Click "Create new secret key"
4. Name your key (e.g., "SkillUp Life Bot")
5. Note down the API key

## Step 4: N8N Setup

### Install N8N

#### Option 1: N8N Cloud

1. Sign up for [N8N Cloud](https://www.n8n.cloud/)
2. Create a new workspace
3. Create a new workflow

#### Option 2: Self-Hosted

1. Install N8N using npm:
   ```bash
   npm install n8n -g
   ```
2. Start N8N:
   ```bash
   n8n start
   ```

### Configure N8N

1. Open N8N in your browser
2. Go to Settings > Credentials
3. Add the following credentials:
   - Slack: Add your Bot User OAuth Token
   - OpenAI: Add your API key
   - Supabase: Add your Project URL and API Key

### Import Workflows

1. Download the workflow JSON files from the repository
2. In N8N, click the "+" button to create a new workflow
3. Click the three dots in the top right corner and select "Import from file"
4. Select the workflow JSON file
5. Repeat for each workflow

### Configure Workflows

1. Open each workflow and update the following:
   - Slack channels to monitor
   - Team member IDs
   - Scheduled triggers (if applicable)
   - Any other workflow-specific settings

### Activate Workflows

1. For each workflow, click the "Active" toggle in the top right corner
2. Confirm that you want to activate the workflow

## Step 5: Environment Configuration

Create a `.env` file in the project root with the following variables:

```
# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-token
SLACK_SIGNING_SECRET=your-signing-secret
SLACK_APP_TOKEN=xapp-your-token
SLACK_DAILY_UPDATES_CHANNEL=C12345678
SLACK_SUMMARY_CHANNEL=C87654321

# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key

# Supabase Configuration
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_API_KEY=your-api-key

# N8N Configuration
N8N_URL=https://your-n8n-instance.com
N8N_API_KEY=your-n8n-api-key

# Team Member Slack IDs (comma-separated)
TEAM_MEMBER_IDS=U12345678,U87654321
```

## Step 6: Testing

1. Post a test message in the #daily-updates channel
2. Verify that the message is captured by the Daily Update Collector workflow
3. Check the Supabase database to ensure the message is stored
4. Manually trigger the Daily Update Summarizer workflow
5. Verify that a summary is generated and posted to the designated channel
6. Check the Supabase database to ensure the summary is stored

## Step 7: Monitoring

1. Set up monitoring for your N8N instance
2. Configure alerts for workflow failures
3. Regularly check the N8N execution logs for any issues

## Troubleshooting

### Common Issues

1. **Workflow not triggering**:
   - Check that the workflow is activated
   - Verify that the Slack app has the necessary permissions
   - Check the N8N logs for any errors

2. **Database connection issues**:
   - Verify that the Supabase credentials are correct
   - Check that the tables are created correctly
   - Ensure the pgvector extension is enabled

3. **OpenAI API errors**:
   - Check that the API key is valid
   - Verify that you have sufficient credits
   - Check for rate limiting issues
