# Database Schema

This document outlines the database schema for the SkillUp Life Slackbot project.

## Tables

### daily_updates

Stores raw daily updates from Slack and their summaries.

```sql
CREATE TABLE IF NOT EXISTS daily_updates (
  id SERIAL PRIMARY KEY,
  slack_user_id TEXT NOT NULL,
  update_text TEXT NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  summary TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### documents

Stores vector embeddings for semantic search capabilities.

```sql
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

### team_members

Stores information about team members whose updates should be monitored.

```sql
CREATE TABLE IF NOT EXISTS team_members (
  id SERIAL PRIMARY KEY,
  slack_user_id TEXT NOT NULL UNIQUE,
  display_name TEXT,
  email TEXT,
  role TEXT,
  team TEXT,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Setup SQL

The following SQL script can be used to set up the database schema:

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

-- Create the team_members table
CREATE TABLE IF NOT EXISTS team_members (
  id SERIAL PRIMARY KEY,
  slack_user_id TEXT NOT NULL UNIQUE,
  display_name TEXT,
  email TEXT,
  role TEXT,
  team TEXT,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Functions

### match_updates

Function to perform similarity search on daily updates.

```sql
CREATE OR REPLACE FUNCTION match_updates (
  query_embedding vector(1536),
  match_threshold float,
  match_count int
)
RETURNS TABLE (
  id bigint,
  slack_user_id text,
  update_text text,
  summary text,
  similarity float
)
LANGUAGE SQL STABLE
AS $$
  SELECT
    daily_updates.id,
    daily_updates.slack_user_id,
    daily_updates.update_text,
    daily_updates.summary,
    1 - (documents.embedding <=> query_embedding) AS similarity
  FROM documents
  JOIN daily_updates ON documents.daily_update_id = daily_updates.id
  WHERE 1 - (documents.embedding <=> query_embedding) > match_threshold
  ORDER BY documents.embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Indexes

The following indexes are created to optimize query performance:

1. Primary key indexes on all tables
2. Vector similarity index on the `documents` table using IVFFLAT algorithm
3. Unique index on `team_members.slack_user_id`
4. Foreign key index on `documents.daily_update_id`
