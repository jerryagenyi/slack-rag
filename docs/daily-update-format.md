# Daily Update Format Guide

This document outlines the recommended format for daily updates in the #daily-updates Slack channel. Following this format will help the AI bot better process and summarize updates.

## Basic Format

Daily updates should include the following sections:

```
**Today's Accomplishments**
- [List of tasks completed today]

**Challenges/Blockers**
- [Any challenges or blockers encountered]

**Tomorrow's Plan**
- [Tasks planned for tomorrow]

**Resources/Links**
- [Any relevant resources or links]
```

## Example

```
**Today's Accomplishments**
- Completed the user authentication flow for the volunteer registration page
- Fixed 3 bugs in the organization dashboard
- Reviewed and merged PR #42 for the notification system

**Challenges/Blockers**
- Having issues with the email service integration
- Need access to the test environment

**Tomorrow's Plan**
- Debug email service integration
- Start implementing the volunteer matching algorithm
- Update documentation for the registration process

**Resources/Links**
- PR: https://github.com/skilledup/platform/pull/42
- Documentation: https://docs.google.com/document/d/abc123
```

## Tips for Effective Updates

1. **Be Specific**: Include specific details about what you worked on
2. **Quantify When Possible**: Include numbers (e.g., "fixed 3 bugs")
3. **Include Links**: Add links to relevant PRs, documents, or resources
4. **Mention Blockers Early**: Highlight any blockers so the team can help
5. **Keep It Concise**: Aim for clarity and brevity

## How Updates Are Processed

Your daily updates are processed by an AI-powered bot that:

1. Extracts key information from your update
2. Generates a summary of the update
3. Stores both the original update and the summary in a database
4. Creates searchable embeddings for future reference

Following the recommended format helps the AI better understand and process your updates, making the summaries more accurate and useful for the team.
