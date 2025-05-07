# AI-Powered Slackbot (slack-rag)

A general-purpose AI-powered Slackbot that monitors channels for updates, summarizes them using LLMs, and stores them in a vector database for future reference and retrieval.

**Current Implementation:** This project is currently being customized for [SkillUp Life](https://www.skilledup.life) to create a Slack integration that monitors daily team updates, summarizes them using AI, and makes the knowledge searchable through vector embeddings.

## Overview

This project uses N8N as an automation engine to monitor a Slack channel for daily updates, process them using OpenAI's GPT models, and store both the raw updates and their summaries in a Supabase database with vector search capabilities.

## Features

- Monitor the #daily-updates Slack channel for new messages
- Identify updates from specific team members
- Extract and parse update information
- Generate concise summaries using OpenAI's gpt-4o-mini
- Store updates and summaries in Supabase
- Create and store vector embeddings for future search capabilities

## Technology Stack

- **Automation Engine:** N8N (Workflow Automation Engine)
- **Database & Vector Store:** Supabase with pgvector extension
- **Embedding Model:** OpenAI text-embedding-ada-002
- **LLM for Summarization:** OpenAI gpt-4o-mini
- **Version Control:** GitHub

## Project Structure

```
slack-rag/
├── .github/workflows/        # GitHub Actions workflows
├── n8n/workflows/            # N8N workflow JSON files
├── docs/                     # Documentation
├── config/                   # Configuration files
├── scripts/                  # Utility scripts
├── README.md                 # This file
└── LICENSE                   # License information
```

For more details on the project structure, see [project-structure.md](docs/project-structure.md).

## Getting Started

### Prerequisites

- N8N instance (cloud or self-hosted)
- Supabase account
- OpenAI API key
- Slack workspace with admin privileges

### Setup Instructions

1. **Set up Supabase:**
   - Create a new Supabase project
   - Enable the pgvector extension
   - Create the required tables using the SQL in [plan.md](docs/plan.md)

2. **Set up N8N:**
   - Install and configure N8N
   - Install the necessary nodes (Supabase, OpenAI, Slack)
   - Import the workflow template from [daily_update_summarizer_v1.json](n8n/workflows/daily_update_summarizer_v1.json)
   - Configure credentials for Slack, OpenAI, and Supabase

3. **Configure Slack:**
   - Create a Slack app with the necessary permissions
   - Install the app to your workspace
   - Obtain the required tokens and IDs

4. **Start the Workflow:**
   - Activate the workflow in N8N
   - Test with sample messages in your Slack channel

## Documentation

- [Product Requirements Document](docs/prd.md)
- [Implementation Plan](docs/plan.md)
- [Implementation Checklist](docs/implementation-checklist.md)
- [Project Structure](docs/project-structure.md)
- [Technical Specifications](docs/technical-specifications.md)
- [N8N Workflow Template](n8n/workflows/daily_update_summarizer_v1.json)
- [Reference Workflow](references/Supabase_RAG_AI_Agent.json)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Initially developed for [SkillUp Life](https://www.skilledup.life) to streamline team communication
- Designed to be adaptable for any organization using Slack
- Inspired by RAG (Retrieval-Augmented Generation) patterns for knowledge management
- Built with open-source tools and frameworks
