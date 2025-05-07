# Project Structure

```
slack-rag/
├── .github/
│   └── workflows/
│       └── n8n-workflow-backup.yml  # Optional: Automation for backing up N8N workflows
├── n8n/
│   └── workflows/
│       └── daily_update_summarizer_v1.json  # Your N8N workflow JSON files
│       └── ... (other workflow JSONs as you build more features)
├── docs/
│   ├── prd.md                      # Product Requirements Document
│   ├── plan.md                     # Implementation Plan
│   ├── technical-specifications.md # Detailed technical specifications
│   └── ... (other documentation)
├── config/
│   └── .env.example                # Example environment variables (API keys, etc.)
│   └── .env.development            # Development environment variables (if applicable)
├── scripts/
│   └── backup_n8n_workflows.py     # Optional: Script to automate N8N workflow backup
├── README.md                       # Project overview and setup instructions
└── LICENSE                         # Project license
```

## Explanation of the Folders and Files

* **`slack-rag/` (Root Directory):** The main folder containing all project files.

* **`.github/workflows/`:**
  * **`n8n-workflow-backup.yml` (Optional):** GitHub Action to automatically back up N8N workflow JSON files.

* **`n8n/workflows/`:**
  * **`daily_update_summarizer_v1.json`:** Exported JSON files of N8N workflows, versioned as needed.

* **`docs/`:**
  * **`prd.md`:** Product Requirements Document outlining project goals, scope, and features.
  * **`plan.md`:** Implementation plan with detailed steps.
  * **`technical-specifications.md`:** Detailed technical design decisions, API integrations, database schema, etc.

* **`config/`:**
  * **`.env.example`:** Template file showing required environment variables.
  * **`.env.development`:** Development environment variables (not committed to Git).

* **`scripts/`:**
  * **`backup_n8n_workflows.py`:** Optional script to export workflows from N8N instance.

* **`README.md`:** Main documentation with project overview and setup instructions.

* **`LICENSE`:** Project license information.

## Development Workflow

1. **N8N:** Core automation logic resides within N8N. Work primarily in the N8N UI.
2. **VSCode:** Use for managing documentation, configuration, and scripts.
3. **GitHub:** Version control for all project files.

This structure provides organization, clarity, scalability, and follows best practices for software development projects.
