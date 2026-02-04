---
name: archive-sweep
description: Auto-archive emails above 80% confidence threshold
argument-hint: "[confidence-threshold]"
---

# Email Archive Sweep

Scan the Outlook inbox and archive emails that meet the confidence threshold.

## Configuration

- **Default threshold**: 80%
- **Override**: Pass a number as argument (e.g., `/admin:inbox:archive-sweep 90`)

## Archive Criteria

Emails are scored on likelihood of being safe to archive:

### High Confidence (90%+)
- **One-time passcodes**: 2FA codes, verification emails, login alerts, security codes
  - Subject patterns: "verification code", "security code", "one-time", "OTP", "sign-in", "2FA"
- **Past meeting notifications**: Calendar invites/updates for meetings that already occurred
  - Check meeting date against current date
- **Automated system notifications**: Build alerts, deployment notices, system status

### Medium-High Confidence (80-89%)
- **Stale newsletters**: Newsletters, digests, or marketing emails >1 day old
  - Subject patterns: "newsletter", "digest", "weekly", "daily", "update from"
  - Sender patterns: "noreply@", "newsletter@", "updates@"
- **Read + old emails**: Already read and >3 days old
- **CC'd notifications**: You're in CC (not To), already read

### Lower Confidence (<80%)
- Emails from direct reports or leadership
- Unread emails from humans
- Emails with questions or action items
- Recent emails (<1 day old) from unknown senders

## Instructions

### 1. Get Browser Context

```
mcp__claude-in-chrome__tabs_context_mcp
```

### 2. Navigate to Outlook Inbox

If not already there: `https://outlook.office.com/mail/inbox`

### 3. Read Inbox List

Use `mcp__claude-in-chrome__read_page` to get the email list. Extract for each email:
- Sender name and email
- Subject line
- Timestamp/date
- Read/unread status
- To/CC status

### 4. Score Each Email

For each email, calculate archive confidence:
1. Check against high-confidence patterns
2. Check against medium-high patterns
3. Apply penalties for important signals

### 5. Archive High-Confidence Emails

For emails meeting the threshold:
1. Select the email
2. Use the Archive action (or move to Archive folder)
3. Track what was archived

### 6. Report Results

```
## Archive Sweep Complete

**Threshold**: [X]%
**Archived**: [count] emails

### Archived Items
| Subject | Sender | Confidence | Reason |
|---------|--------|------------|--------|
| [subject] | [sender] | [X]% | [reason] |

### Skipped (below threshold)
- [count] emails left in inbox

### Borderline (70-79%)
- [subject] from [sender] - [reason for uncertainty]
```

### 7. Offer Manual Review

Ask if user wants to:
- Review any archived items
- Lower threshold and re-run
- Archive specific borderline items

## Outlook Web Selectors

Common actions in Outlook Web:
- Archive button in toolbar
- Right-click → Archive
- Keyboard shortcut: `e` (if enabled)

Use `mcp__claude-in-chrome__find` to locate the archive action.
