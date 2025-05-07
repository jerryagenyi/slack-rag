# N8N Workflow Organization

This document outlines how N8N workflows are organized in the SkillUp Life Slackbot project.

## Folder Structure

The N8N workflows are organized in the following folder structure:

```
n8n/
├── workflows/
│   ├── daily_update_collector_v1.json       # Collects daily updates from Slack
│   ├── daily_update_summarizer_v1.json      # Summarizes collected updates
│   ├── daily_update_embedder_v1.json        # Creates embeddings for updates
│   ├── query_processor_v1.json              # Processes user queries (future)
│   └── ...
├── credentials/
│   ├── slack_credentials_template.json      # Template for Slack credentials
│   ├── openai_credentials_template.json     # Template for OpenAI credentials
│   └── supabase_credentials_template.json   # Template for Supabase credentials
└── examples/
    ├── sample_daily_update.json             # Sample daily update data
    ├── sample_summary.json                  # Sample summary data
    └── sample_query.json                    # Sample query data
```

## Workflow Naming Convention

Workflows are named using the following convention:

```
[function]_[version].json
```

Where:
- `[function]` describes the primary function of the workflow
- `[version]` indicates the version number (v1, v2, etc.)

## Workflow Organization Approach

For this project, we are using a **modular workflow approach** with multiple specialized workflows rather than a single monolithic workflow. This approach offers several advantages:

1. **Maintainability**: Smaller workflows are easier to understand and maintain
2. **Reliability**: Issues in one workflow don't affect others
3. **Scalability**: New features can be added as separate workflows
4. **Performance**: Each workflow can be optimized independently

## Workflow Types

The project uses the following specialized workflows:

### 1. Daily Update Collector

**File**: `daily_update_collector_v1.json`

**Purpose**: Monitors the Slack channel for new messages, filters for team member updates, and stores them in the database.

**Key Components**:
- Slack Trigger node
- Filter for team members
- Supabase node for storing raw updates

### 2. Daily Update Summarizer

**File**: `daily_update_summarizer_v1.json`

**Purpose**: Processes collected updates, generates summaries using OpenAI, and stores the summaries in the database.

**Key Components**:
- Scheduled trigger (e.g., daily at 5 PM)
- Supabase node for retrieving updates
- OpenAI node for summarization
- Supabase node for storing summaries
- Slack node for posting summaries

### 3. Daily Update Embedder

**File**: `daily_update_embedder_v1.json`

**Purpose**: Creates vector embeddings for updates and summaries, and stores them in the database for future retrieval.

**Key Components**:
- Scheduled trigger
- Supabase node for retrieving updates
- OpenAI node for generating embeddings
- Supabase node for storing embeddings

### 4. Query Processor (Future)

**File**: `query_processor_v1.json`

**Purpose**: Processes user queries, searches for relevant updates using vector similarity, and returns results.

**Key Components**:
- Slack Trigger for commands
- Function node for query processing
- Supabase node for vector search
- Slack node for responding with results

## Workflow Dependencies

The workflows are designed to work together in a pipeline:

1. **Daily Update Collector** runs continuously to collect updates
2. **Daily Update Summarizer** runs on a schedule to summarize collected updates
3. **Daily Update Embedder** runs after summarization to create embeddings
4. **Query Processor** runs on-demand when users submit queries

## Version Control

All workflow JSON files are stored in the GitHub repository. When changes are made to a workflow:

1. Export the updated workflow from N8N
2. Save it to the appropriate file in the `n8n/workflows/` directory
3. Commit the changes to the repository
4. If it's a major change, create a new version of the workflow
