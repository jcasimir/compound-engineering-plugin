# Leadership Ops Plugin

This plugin provides workflows for leadership and administrative work.

## Commands

### Admin Workflows (`/admin:*`)

#### Email
- `/admin:inbox` - Full inbox management (runs all sub-commands)
- `/admin:inbox:archive-sweep` - Auto-archive emails at 80% confidence threshold
- `/admin:inbox:needs-response` - Create Jira tickets for emails needing response

#### Calendar
- `/admin:calendar-sync [mode]` - Sync Outlook calendar to Google Calendar
  - `fast` - Next 3 days (default, every couple hours)
  - `mid` - Next 14 days (nightly)
  - `full` - Next 90 days (couple times per week)

### Meeting Workflows (`/meeting:*`)
- `/meeting:prep [meeting-name]` - Prepare for a meeting with context gathering

### 1:1 Workflows (`/1on1:*`)
- `/1on1:prep [person-name]` - Prepare for a 1:1 with history and context

## Data Storage

1:1 notes are stored in `docs/1on1s/[person-name].md` files in the current project.

## Environment Variables

Required for Jira integration:
- `JIRA_EMAIL` - Atlassian account email
- `JIRA_API_TOKEN` - Atlassian API token

Required for Google Calendar API (calendar-sync):
- `GCAL_CLIENT_ID` - Google OAuth Client ID
- `GCAL_CLIENT_SECRET` - Google OAuth Client Secret
- `GCAL_REFRESH_TOKEN` - Google OAuth Refresh Token (obtained via OAuth flow)

## Browser Automation

All workflows use browser automation via `mcp__claude-in-chrome__*` tools:
- **Email**: Outlook Web (outlook.office.com)
- **Calendar**: Outlook Web + Google Calendar (calendar.google.com)

Ensure the Claude in Chrome extension is installed and active.

## Jira Integration

The `needs-response` workflow creates Tasks in the JC project at digital-greatminds.atlassian.net. Each email is tracked with a unique key stored in the ticket description. Follow-up scans auto-resolve tickets when emails leave the inbox.

## Calendar Sync

Hybrid approach for Outlook → Google Calendar sync:
- **Read**: Browser automation for Outlook (mcp__claude-in-chrome__*)
- **Write**: Google Calendar API via curl (fast, reliable)
- Events include Outlook ID in GCal description for deduplication
- Response status syncs both directions (confirmed status wins over tentative)
