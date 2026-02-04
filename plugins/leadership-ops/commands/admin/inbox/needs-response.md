---
name: needs-response
description: Identify emails needing response and create Jira tickets for tracking
---

# Needs Response Scanner

Scan the Outlook inbox for emails requiring a response and create Jira tickets for tracking.

## Jira Configuration

- **Instance**: digital-greatminds.atlassian.net
- **Project**: JC (Jeff Casimir)
- **Issue Type**: Task (ID: 10358)
- **Auth**: Uses `JIRA_EMAIL` and `JIRA_API_TOKEN` environment variables

## Email Key Format

Each email gets a unique key for Jira tracking:
```
email:{sender-email}:{ISO-timestamp}
```

Example: `email:jane.smith@greatminds.org:2024-01-15T10:30:00Z`

This key is stored in the Jira ticket description and used to:
1. Check if a ticket already exists
2. Match tickets to emails on follow-up scans

## Needs-Response Criteria

### Sender-Based (high priority)
- Direct reports
- Your leadership chain
- Key stakeholders
- Known important contacts

### Content-Based
- Contains a direct question to you
- Explicitly requests action or decision
- Mentions deadlines or time-sensitivity
- Flagged/starred by sender as important

### Exclusions (not needs-response)
- Newsletters and automated notifications
- CC'd emails (unless explicitly asking for input)
- FYI/informational emails
- Already responded to (check for your reply in thread)

## Instructions

### 1. Get Browser Context

```
mcp__claude-in-chrome__tabs_context_mcp
```

### 2. Navigate to Outlook Inbox

If not already there: `https://outlook.office.com/mail/inbox`

### 3. Read Inbox List

Use `mcp__claude-in-chrome__read_page` to get the email list. Extract:
- Sender name and email address
- Subject line
- Timestamp (for email key)
- Preview text if visible
- Read/unread status

### 4. Identify Needs-Response Emails

For each email, evaluate:
1. Is the sender someone who warrants a response?
2. Does the subject/preview suggest action needed?
3. Is this a reply thread where you haven't responded?

### 5. Check Existing Jira Tickets

For each needs-response email, search Jira for existing ticket:

```bash
# Search for existing ticket by email key
curl -s --user "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
  "https://digital-greatminds.atlassian.net/rest/api/3/search" \
  -G --data-urlencode "jql=project = JC AND description ~ \"EMAIL-KEY: email:{sender}:{timestamp}\""
```

### 6. Create Jira Tickets for New Items

For needs-response emails without existing tickets:

```bash
curl -s --user "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
  -X POST \
  -H "Content-Type: application/json" \
  "https://digital-greatminds.atlassian.net/rest/api/3/issue" \
  -d '{
    "fields": {
      "project": {"key": "JC"},
      "summary": "[Email] {subject}",
      "description": {
        "type": "doc",
        "version": 1,
        "content": [
          {
            "type": "paragraph",
            "content": [
              {"type": "text", "text": "Email from: {sender}"},
              {"type": "hardBreak"},
              {"type": "text", "text": "Date: {date}"},
              {"type": "hardBreak"},
              {"type": "hardBreak"},
              {"type": "text", "text": "[EMAIL-KEY: email:{sender}:{timestamp}]"}
            ]
          }
        ]
      },
      "issuetype": {"id": "10358"}
    }
  }'
```

### 7. Check for Resolved Items

Search for open email tickets and verify if the email is still in inbox:

```bash
# Find open email tickets
curl -s --user "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
  "https://digital-greatminds.atlassian.net/rest/api/3/search" \
  -G --data-urlencode "jql=project = JC AND summary ~ '[Email]' AND status != Done"
```

For each open ticket:
1. Extract the EMAIL-KEY from description
2. Check if matching email still exists in inbox
3. If email is gone (archived/deleted/responded), transition ticket to Done

### 8. Report Results

```
## Needs Response Scan Complete

### New Tickets Created ([count])
| Email | Sender | Jira |
|-------|--------|------|
| [subject] | [sender] | [JC-XXX](link) |

### Existing Tickets (already tracked)
- [subject] → [JC-XXX]

### Resolved (email no longer in inbox)
- [JC-XXX]: [subject] → Marked Done

### Summary
- [X] emails need response
- [Y] new tickets created
- [Z] tickets marked done
```

## Follow-Up Workflow

Run this command periodically to:
1. Catch new needs-response emails
2. Auto-resolve tickets when emails are handled
3. Surface emails that have been waiting too long

Consider running daily as part of `/admin:daily` routine.
