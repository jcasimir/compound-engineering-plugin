# Leadership Ops Plugin

A Claude Code plugin for leadership and administrative workflows.

## Installation

```bash
/plugin install https://github.com/jcasimir/compound-engineering-plugin?plugin=leadership-ops
```

## Features

### Email Management
- **`/admin:inbox`** - Full inbox triage (archive + needs-response)
- **`/admin:inbox:archive-sweep`** - Auto-archive at 80% confidence
- **`/admin:inbox:needs-response`** - Create Jira tickets for emails needing response

### Calendar Sync
- **`/admin:calendar-sync [mode]`** - Sync Outlook → Google Calendar
  - `fast` - Next 3 days (every couple hours)
  - `mid` - Next 14 days (nightly)
  - `full` - Next 90 days (couple times per week)

### Meeting Prep
- **`/meeting:prep [meeting-name]`** - Gather context for upcoming meetings

### 1:1 Management
- **`/1on1:prep [person-name]`** - Prepare for 1:1s with historical context
- Tracks notes per person in `docs/1on1s/`

## Requirements

- Claude Code CLI
- Claude in Chrome extension (for browser automation)
- Jira API token (for email→Jira integration)
- Google Calendar API credentials (for calendar sync)

## Environment Variables

```bash
# Jira integration (for /admin:inbox:needs-response)
export JIRA_EMAIL="your.email@company.com"
export JIRA_API_TOKEN="your-api-token"

# Google Calendar API (for /admin:calendar-sync)
export GCAL_CLIENT_ID="your-client-id.apps.googleusercontent.com"
export GCAL_CLIENT_SECRET="your-client-secret"
export GCAL_REFRESH_TOKEN="your-refresh-token"
```

## Google Calendar API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (e.g., "Calendar-Sync")
3. Enable the Google Calendar API
4. Create OAuth 2.0 credentials (Desktop app type)
5. Add scope: `https://www.googleapis.com/auth/calendar`
6. Download the credentials JSON
7. Run the OAuth flow to get a refresh token (one-time setup)

## Archive Criteria

Emails auto-archived at 80%+ confidence:
- One-time passcodes / 2FA codes
- Past meeting notifications
- Newsletters >1 day old
- Read emails >3 days old

## Calendar Sync Details

- **Direction**: Outlook → Google Calendar (one-way)
- **Approach**: Hybrid (browser reads Outlook, API writes to GCal)
- **Deduplication**: Outlook event ID embedded in GCal description
- **Response status**: Bi-directional sync (confirmed wins over tentative)
- **Data synced**: Title, time, duration, location, attendees (in description)

## Data Storage

1:1 notes stored locally in your project:
```
docs/1on1s/
  jane-smith.md
  bob-jones.md
```
