---
name: prep
description: Prepare for a 1:1 meeting with history and context
argument-hint: "[person-name]"
---

# 1:1 Preparation

You are helping prepare for a 1:1 meeting with a direct report.

## Instructions

1. **Identify the person**:
   - Use the provided name argument
   - If not provided, ask who the 1:1 is with

2. **Load their history** from `docs/1on1s/`:
   - Look for `docs/1on1s/[person-name].md` (try variations: lowercase, hyphenated, first-name-only)
   - If no file exists, note this and offer to create one

3. **Extract from history**:
   - Last meeting date and key outcomes
   - Pending action items (both yours and theirs)
   - Recurring topics or concerns
   - Development goals and recent progress
   - Any noted wins or challenges

4. **Generate prep document**:

   ```markdown
   ## 1:1 Prep: [Person Name]
   **Date**: [today's date]
   **Last 1:1**: [date from history]

   ### Pending Action Items
   **Yours (manager)**:
   - [ ] [item from previous notes]

   **Theirs**:
   - [ ] [item from previous notes]

   ### Topics to Revisit
   - [topic from recent history that needs follow-up]

   ### Development Goals
   - [goal]: [recent progress or notes]

   ### Suggested Check-ins
   - How are you feeling about [recent project/topic]?
   - Any blockers I can help with?
   - [personalized question based on history]

   ### Recent Wins to Acknowledge
   - [if any noted in history]

   ### Notes Space
   [leave blank for during-meeting notes]
   ```

5. **If no history exists**, offer to create initial file:
   - Ask about their role, tenure, current projects
   - Ask about development goals
   - Create starter template in `docs/1on1s/[person-name].md`

## After the Meeting

Remind the user they can use `/1on1:notes [person-name]` to document outcomes (when implemented).

## File Format

1:1 history files follow this structure:
```markdown
# 1:1 Notes: [Person Name]

## Info
- **Role**: [their role]
- **Started**: [when they joined/started reporting to you]
- **Development Goals**: [current goals]

## [YYYY-MM-DD]
### Topics Discussed
- [topic]

### Action Items
- [ ] [Manager]: [action]
- [ ] [Person]: [action]

### Notes
[freeform notes]

---
(previous entries below)
```
