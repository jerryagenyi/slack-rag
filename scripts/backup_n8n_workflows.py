#!/usr/bin/env python3
"""
Script to backup N8N workflows to the repository.
This script fetches all workflows from an N8N instance and saves them as JSON files.
"""

import os
import json
import requests
from datetime import datetime

# Get environment variables
N8N_URL = os.environ.get('N8N_URL')
N8N_API_KEY = os.environ.get('N8N_API_KEY')

# Check if environment variables are set
if not N8N_URL or not N8N_API_KEY:
    print("Error: N8N_URL and N8N_API_KEY environment variables must be set.")
    exit(1)

# Ensure the URL ends with a slash
if not N8N_URL.endswith('/'):
    N8N_URL += '/'

# API endpoint for workflows
WORKFLOWS_ENDPOINT = f"{N8N_URL}api/v1/workflows"

# Headers for authentication
HEADERS = {
    "X-N8N-API-KEY": N8N_API_KEY,
    "Content-Type": "application/json"
}

def get_workflows():
    """Fetch all workflows from the N8N instance."""
    try:
        response = requests.get(WORKFLOWS_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workflows: {e}")
        return None

def save_workflow(workflow):
    """Save a workflow to a JSON file."""
    workflow_id = workflow.get('id')
    workflow_name = workflow.get('name', 'unknown')
    
    # Create a safe filename
    safe_name = ''.join(c if c.isalnum() or c in ['-', '_'] else '_' for c in workflow_name)
    filename = f"n8n/workflows/{safe_name}_v1.json"
    
    # Save the workflow to a file
    with open(filename, 'w') as f:
        json.dump(workflow, f, indent=2)
    
    print(f"Saved workflow '{workflow_name}' to {filename}")

def main():
    """Main function to backup all workflows."""
    print(f"Backing up N8N workflows from {N8N_URL}")
    
    # Get all workflows
    workflows = get_workflows()
    
    if not workflows:
        print("No workflows found or error occurred.")
        return
    
    print(f"Found {len(workflows)} workflows.")
    
    # Save each workflow
    for workflow in workflows:
        save_workflow(workflow)
    
    print("Backup completed successfully.")

if __name__ == "__main__":
    main()
