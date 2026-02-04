---
name: inbox
description: Email inbox management orchestrator - runs triage, archive-sweep, and needs-response
---

# Email Inbox Orchestrator

You are an executive assistant managing an Outlook Web inbox.

## Instructions

This is the top-level inbox command that orchestrates sub-commands.

### 1. Get Browser Context

```
mcp__claude-in-chrome__tabs_context_mcp
```

### 2. Navigate to Outlook

If not already on Outlook, navigate to `https://outlook.office.com/mail/inbox`

Wait for the inbox to fully load.

### 3. Run Sub-Workflows

Execute these in sequence:

#### A. Archive Sweep
Identify and archive emails meeting the 80% confidence threshold:
- One-time passcodes / 2FA verification codes
- Meeting notifications for past events
- Newsletters more than 1 day old

For each candidate, evaluate confidence and archive if ≥80%.

#### B. Needs Response Scan
Identify emails requiring a response based on:
- Sender (direct reports, leadership, key stakeholders)
- Content (direct questions, action requests)

For each needs-response email:
1. Check if Jira ticket already exists (search by email key)
2. If not, create a Task in project JC
3. Include email key in description for tracking

#### C. Summary Report

Present a summary:

```
## Inbox Triage Complete

### Archived ([count] emails)
- [subject] - [reason]

### Needs Response ([count] emails)
- [sender]: [subject] → [Jira ticket link or "ticket created"]

### Remaining Inbox
- [count] emails for manual review
```

### 4. Ask for Further Actions

Ask if the user wants to:
- Review any archived items
- Open specific emails
- Run individual sub-commands with different parameters

## Sub-Commands

For granular control, use:
- `/admin:inbox:archive-sweep` - Only run archive sweep
- `/admin:inbox:needs-response` - Only run needs-response scan
