# Team Member Management

This document outlines how team members are managed in the SkillUp Life Slackbot system.

## Team Member Storage

### Initial Configuration

For the MVP phase, team members are initially configured in two places:

1. **Environment Variables**: The `.env` file contains a comma-separated list of Slack User IDs for team members whose updates should be monitored:
   ```
   TEAM_MEMBER_IDS=U12345678,U87654321
   ```

2. **N8N Workflow**: The "Filter - Product Team Members" node in the N8N workflow contains the same list of Slack User IDs.

### Future Implementation

In future phases, team members will be managed through a more flexible system:

1. **Database Storage**: Team members will be stored in a Supabase table with the following schema:
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

2. **Admin Interface**: A simple admin interface will be created to:
   - Add new team members
   - Deactivate team members who are no longer with the project
   - Update team member information
   - Assign team members to specific teams or roles

3. **Dynamic Filtering**: The N8N workflow will be updated to query the database for active team members rather than using a hardcoded list.

## Team Member Identification

The system identifies team members in Slack messages using their Slack User IDs. When a message is posted in the monitored channel, the system:

1. Extracts the Slack User ID of the message author
2. Checks if this ID is in the list of team members
3. If it is, processes the message as a team member update
4. If not, ignores the message

## Onboarding New Team Members

When a new volunteer joins the SkillUp Life development team:

1. **Slack Onboarding**:
   - The volunteer is added to the Slack workspace
   - Their Slack User ID is obtained

2. **System Configuration**:
   - In the MVP phase, their Slack User ID is added to the environment variables and N8N workflow
   - In future phases, they are added to the team_members database table

3. **Documentation**:
   - The new team member is provided with the daily update format guide
   - They are informed about the AI-powered summarization system

## Privacy Considerations

- Team members are informed that their daily updates will be processed by an AI system
- Only professional updates posted in the designated channel are processed
- Personal information is not stored beyond what is necessary for the system to function
