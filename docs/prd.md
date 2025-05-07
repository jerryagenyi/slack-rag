# Product Requirements Document (PRD) - SkillUp Life Slackbot

## 1. Introduction

### 1.1 Purpose
The SkillUp Life Slackbot assists new volunteers with onboarding information, streamlines team updates, and automates routine tasks.

### 1.2 Goals
- Provide quick answers to common onboarding questions
- Automate the collection and summarization of daily team updates
- Integrate with existing tools (Slack, Google Sheets, GitHub)
- Lay a foundation for future expansion (e.g., document knowledge base)

### 1.3 Target Audience
- New volunteers
- Team leads
- Administrators

## 2. Scope

### 2.1 In-Scope (MVP - Phase 1)
- Monitoring the #daily-updates Slack channel
- Identifying updates from specific product team members (initially by manual user ID)
- Extracting key information from daily updates based on a defined format
- Summarizing these updates (using gpt-4o-mini)
- Posting the summary to a designated Slack channel
- Storing raw and summarized daily updates in a Supabase database
- Using Supabase with pgvector to store embeddings of daily updates

### 2.2 Out-of-Scope (for MVP)
- Remembering arbitrary information or creating schedules based on user requests
- Direct messaging capabilities beyond initial greetings/notifications
- Calendar bot integration
- Team membership verification
- Integration with GitHub projects
- Google Sheets CRUD operations beyond basic appending
- Handling "no update" scenarios gracefully
- Telegram integration
- Local Ollama integration

## 3. Functional Requirements

### 3.1 Monitor Daily Updates
The bot will continuously monitor the #daily-updates channel for new messages.

### 3.2 Identify Team Updates
The bot will identify messages posted by members of the product teams (initially based on a predefined list of Slack User IDs).

### 3.3 Extract Update Information
The bot will parse the content of the daily update messages to extract relevant details (initially based on the expected format).

### 3.4 Summarize Updates
The bot will use the gpt-4o-mini model with the provided prompt to generate a concise summary of the extracted updates.

### 3.5 Post Summary
The bot will post the generated summary to a designated Slack channel at a specific time (e.g., end of the workday).

### 3.6 Store Updates
The bot will store the raw and summarized daily updates in the daily_updates table in Supabase.

### 3.7 Store Embeddings
The bot will generate embeddings for the daily updates using OpenAI's text-embedding-ada-002 and store them in the documents table in Supabase, leveraging the pgvector extension.

## 4. Non-Functional Requirements

### 4.1 Reliability
The bot should consistently perform its core functions without errors.

### 4.2 Efficiency
The bot should process and summarize updates in a reasonable timeframe.

### 4.3 Usability
The bot's notifications and summaries should be clear and easy to understand.

### 4.4 Maintainability
The N8N workflows should be well-organized and easy to modify.

### 4.5 Cost-Effectiveness
The solution should aim to minimize usage of paid AI API tokens and cloud resources within the free tiers as much as possible.

## 5. Technical Specifications

### 5.1 Automation Engine
N8N (Workflow Automation Engine)

### 5.2 Database and Vector Store
Supabase (free tier) with the pgvector extension

### 5.3 LLM for Summarization
OpenAI gpt-4o-mini

### 5.4 Embedding Model
OpenAI text-embedding-ada-002

### 5.5 Slack Integration
Slack API

### 5.6 Hosting
N8N Cloud (free tier initially) and Supabase Cloud (free tier)

## 6. Phases

### Phase 1: Daily Update Monitoring, Summarization, and Vector Storage (MVP)
- Set up Supabase with pgvector
- Set up N8N and connect to Slack
- Create a workflow to listen for updates from specific users
- Implement basic parsing of update messages
- Integrate with the gpt-4o-mini model for summarization
- Post the summary to a Slack channel
- Store raw and summarized updates in the daily_updates table
- Generate embeddings for the updates and store them in the documents table using pgvector

### Phase 2 (Future)
Implement other functionalities (Google Sheets integration, GitHub integration, more advanced Q&A, etc.) in separate, modular workflows

## 7. Modules

### 7.1 Core Modules
- Slack Input (Trigger)
- User Identification (Filter/Lookup)
- Data Extraction (Function/Set)
- LLM Interaction (OpenAI Node)
- Supabase Vector Store (for embedding storage)
- Supabase Database (for storing raw and summarized updates)
- Slack Output (Post Message Node)

## 8. Version Control

GitHub will be used for version control of N8N workflow JSON exports, managed through VSCode.

## 9. Next Steps

For detailed implementation steps and progress tracking, refer to the [Implementation Checklist](implementation-checklist.md). This checklist breaks down all the tasks required to implement this project, including:

1. Setting up Supabase with pgvector
2. Configuring Slack integration
3. Setting up OpenAI API access
4. Installing and configuring N8N
5. Implementing the workflow
6. Testing and deployment