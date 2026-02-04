---
name: admin:calendar-sync
description: Sync Outlook calendar events to Google Calendar (browser + API hybrid)
argument-hint: "[fast|mid|full]"
---

# Calendar Sync: Outlook → Google Calendar

Sync calendar events from Outlook Web to Google Calendar using a hybrid approach:
- **Read**: Browser automation for Outlook (best for reading complex UI)
- **Write**: Google Calendar API via curl (fast, reliable)

## Environment Variables Required

```bash
export GCAL_CLIENT_ID="..."      # Google OAuth Client ID
export GCAL_CLIENT_SECRET="..."  # Google OAuth Client Secret
export GCAL_REFRESH_TOKEN="..."  # Google OAuth Refresh Token
```

## Sync Modes

| Mode | Scope | Use Case |
|------|-------|----------|
| `fast` | Next 3 days | Every couple hours (default) |
| `mid` | Next 14 days | Nightly |
| `full` | Next 90 days | Couple times per week |

## Event Tracking

Each synced event includes an Outlook ID in the Google Calendar description:
```
[OUTLOOK-ID: {outlook-event-id}]

Attendees: Jane Smith, Bob Jones
Location: Zoom link or room
```

This enables:
- Deduplication (skip if already synced)
- Updates (find and modify existing)
- Response status sync

## Instructions

### 1. Get Browser Context

```
mcp__claude-in-chrome__tabs_context_mcp
```

### 2. Determine Sync Mode

Parse the argument:
- `fast` or no argument → 3 days
- `mid` → 14 days
- `full` → 90 days

Calculate the date range from today.

### 3. Read Outlook Calendar (Browser)

#### Navigate to Outlook Calendar

1. Navigate to `https://outlook.office.com/calendar/view/week`
2. Use `mcp__claude-in-chrome__read_page` to get the calendar structure

#### Extract Event Data

For each event in the date range, extract:
- **Event ID**: Look for data attributes or construct pseudo-ID
- **Title**: Event name/subject
- **Start time**: Date and time (ISO format)
- **End time**: Date and time (ISO format)
- **Location**: Room, Zoom link, or address
- **Attendees**: List of participants
- **Your response status**: Accepted, Tentative, Declined, None

For events without visible IDs, construct a pseudo-ID:
```
outlook:{title-hash}:{start-iso-timestamp}
```

#### Click into events if needed

If attendees or full details aren't visible in the list:
1. Click the event to open details panel
2. Extract additional information
3. Close/navigate back
4. Continue to next event

### 4. Get Google Calendar Access Token

```bash
ACCESS_TOKEN=$(curl -s -X POST 'https://oauth2.googleapis.com/token' \
  -d "client_id=${GCAL_CLIENT_ID}" \
  -d "client_secret=${GCAL_CLIENT_SECRET}" \
  -d "refresh_token=${GCAL_REFRESH_TOKEN}" \
  -d 'grant_type=refresh_token' | jq -r '.access_token')
```

### 5. Check Existing Events in Google Calendar (API)

Search for events with matching OUTLOOK-ID to avoid duplicates:

```bash
# Search for events in the date range
curl -s "https://www.googleapis.com/calendar/v3/calendars/primary/events" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -G \
  --data-urlencode "timeMin=${START_DATE}T00:00:00Z" \
  --data-urlencode "timeMax=${END_DATE}T23:59:59Z" \
  --data-urlencode "maxResults=250" \
  | jq '.items[] | {id, summary, description, start, end}'
```

Parse the results to find events with `[OUTLOOK-ID: ...]` in their description.

### 6. Create New Events (API)

For each Outlook event not already in Google Calendar:

```bash
curl -s -X POST "https://www.googleapis.com/calendar/v3/calendars/primary/events" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "{event_title}",
    "description": "[OUTLOOK-ID: {outlook_id}]\n\nAttendees: {attendee_list}\nLocation: {location}",
    "location": "{location}",
    "start": {
      "dateTime": "{start_iso}",
      "timeZone": "America/Denver"
    },
    "end": {
      "dateTime": "{end_iso}",
      "timeZone": "America/Denver"
    }
  }'
```

### 7. Update Existing Events (API)

If an event exists but needs updating (e.g., response status):

```bash
curl -s -X PATCH "https://www.googleapis.com/calendar/v3/calendars/primary/events/{gcal_event_id}" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "{updated_title}",
    "location": "{updated_location}"
  }'
```

### 8. Response Status: GCal → Outlook (Browser)

For events where:
- Outlook status is Tentative or None
- GCal status is Yes or No

Navigate back to Outlook and update the response:
1. Find the event in Outlook
2. Click to open
3. Update response (Accept or Decline)
4. Save

### 9. Report Results

```
## Calendar Sync Complete

**Mode**: {fast|mid|full}
**Range**: {start_date} to {end_date}
**Events processed**: {count}

### Created in Google Calendar ({count})
| Event | Date | Time |
|-------|------|------|
| {title} | {date} | {time} |

### Already Synced ({count})
- {count} events unchanged
- {count} events updated

### Response Status Synced to Outlook ({count})
| Event | Status |
|-------|--------|
| {title} | {Accepted/Declined} |

### Errors/Skipped ({count})
- {title}: {reason}
```

### 10. Offer Follow-up

Ask if user wants to:
- View any specific synced events
- Run a different sync mode
- Review events that had issues

## Tips for Outlook Web Navigation

### Finding Event IDs
- Look for `data-*` attributes on event elements
- Check the URL when viewing event details
- Use network requests to find API identifiers

### Agenda/List View
Try these approaches to get a list view:
1. Search for events in date range: Click search, enter date filter
2. Use "My Day" or "Agenda" panel on the right
3. Month view and click "Show as list" if available

### Handling Loading States
- Wait for spinners to complete
- Look for skeleton/placeholder elements
- Scroll to trigger lazy loading of events

## Google Calendar API Reference

### List Events
```bash
GET https://www.googleapis.com/calendar/v3/calendars/primary/events
  ?timeMin=2026-02-03T00:00:00Z
  &timeMax=2026-02-06T23:59:59Z
  &maxResults=250
```

### Create Event
```bash
POST https://www.googleapis.com/calendar/v3/calendars/primary/events
Content-Type: application/json
{summary, description, location, start, end}
```

### Update Event
```bash
PATCH https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}
Content-Type: application/json
{fields to update}
```

### Delete Event
```bash
DELETE https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}
```
