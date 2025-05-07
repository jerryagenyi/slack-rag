# Implementation Plan for SkillUp Life Slackbot

## 1. Technology Stack

- **Automation Engine:** N8N (Workflow Automation Engine)
- **Database & Vector Store:** Supabase with pgvector extension
- **Embedding Model:** OpenAI text-embedding-ada-002
- **LLM for Summarization:** OpenAI gpt-4o-mini
- **Version Control:** GitHub

## 2. Implementation Steps

### 2.1 Set up Supabase

1. Create a Supabase project
2. Enable the pgvector extension in the database
3. Create the following tables:
   - `daily_updates` (for storing raw and summarized updates)
   - `documents` (for storing document chunks and their embeddings)
4. Obtain Supabase credentials (URL, API key) for use in N8N

### 2.2 Set up N8N

1. Install and configure N8N
2. Install necessary N8N nodes:
   - Supabase
   - OpenAI
   - Slack
   - Function/Set nodes
   - Cron trigger

### 2.3 Create the Workflow

1. Configure a "Slack" trigger node to listen for new messages in the #daily-updates channel
2. Add a "Filter" node to only process messages from specific users
3. Use a "Function" node or "Set" nodes to extract relevant information from Slack messages
4. Add an OpenAI node with gpt-4o-mini and the summarization prompt
5. Configure a Supabase node to:
   - Insert raw updates into the daily_updates table
   - Insert summarized updates into the daily_updates table
6. Add an OpenAI node to generate embeddings using text-embedding-ada-002
7. Configure another Supabase node to store embeddings in the documents table
8. Add a Slack node to post the summary to a designated channel

### 2.4 Version Control Setup

1. Create a GitHub repository for the project
2. Store N8N workflow JSON files in this repository
3. Use VSCode to manage these files


## 3. Database Schema

### 3.1 daily_updates Table
- `id` (SERIAL PRIMARY KEY)
- `slack_user_id` (TEXT)
- `update_text` (TEXT)
- `timestamp` (TIMESTAMP)
- `summary` (TEXT)
- `created_at` (TIMESTAMP)

### 3.2 documents Table
- `id` (SERIAL PRIMARY KEY)
- `content` (TEXT)
- `metadata` (JSONB)
- `embedding` (vector(1536))
- `daily_update_id` (INTEGER, FOREIGN KEY)
- `created_at` (TIMESTAMP)

## 4. Additional Resources

- **N8N Workflow Template:** See `n8n-workflow-template.json` for a sample workflow configuration
- **Project Structure:** See `project-structure.md` for the recommended folder structure

## 5. Implementation Notes

### 5.1 Supabase Setup
When setting up the pgvector extension in Supabase, use the following SQL:

```sql
-- Enable the pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

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

### 5.2 N8N Workflow Configuration
- Replace all placeholder values in the workflow template
- Adjust the trigger settings based on your needs
- Implement error handling for API calls
- Consider using a Cron trigger for daily summaries