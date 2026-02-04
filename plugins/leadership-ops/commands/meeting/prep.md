---
name: prep
description: Prepare for a meeting with context gathering
argument-hint: "[meeting-name or attendee]"
---

# Meeting Preparation

You are helping prepare for an upcoming meeting.

## Instructions

1. **Identify the meeting**:
   - If the user provided a meeting name or attendee, use that
   - Otherwise, use browser automation to check the calendar and list upcoming meetings

2. **Gather context** from multiple sources:

   ### From the codebase (if relevant)
   - Search for any documents mentioning the meeting topic or attendees
   - Check `docs/` folder for related notes
   - Look for recent commits or work related to the topic

   ### From 1:1 history (if meeting with a direct report)
   - Check `docs/1on1s/[person].md` for recent notes and pending items

   ### From calendar (via browser)
   - Meeting time, duration, and attendees
   - Meeting description or agenda if available
   - Previous meetings with the same group

3. **Generate a prep document**:

   ```markdown
   ## Meeting Prep: [Meeting Name]
   **Date**: [date/time]
   **Attendees**: [list]
   **Duration**: [time]

   ### Context
   [Relevant background information gathered]

   ### Suggested Agenda
   1. [topic based on context]
   2. [topic]
   3. [topic]

   ### Questions to Consider
   - [question based on gathered context]

   ### Open Items from Previous Meetings
   - [if any found]

   ### Notes Space
   [leave blank for during-meeting notes]
   ```

4. **Present to user** and ask if they want to:
   - Add/modify agenda items
   - Save the prep document
   - Pull additional context

## For 1:1 Meetings

If this is a 1:1 meeting with a direct report, include:
- Recent 1:1 notes and outcomes
- Pending action items (theirs and yours)
- Development goals and progress
- Any concerns or kudos noted previously
