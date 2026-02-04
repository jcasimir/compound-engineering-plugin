---
name: 1on1-tracker
description: Track 1:1 meeting history and notes per person. Use when the user wants to record, review, or manage 1:1 meeting notes for their direct reports.
---

# 1:1 Tracker Skill

This skill manages 1:1 meeting notes stored in `docs/1on1s/` in the current project.

## Storage Location

All 1:1 notes are stored in `docs/1on1s/[person-name].md` where `[person-name]` is lowercase with hyphens (e.g., `jane-smith.md`).

## File Format

Each person has a single markdown file with this structure:

```markdown
# 1:1 Notes: [Person Name]

## Info
- **Role**: [their role/title]
- **Started**: [when they joined or started reporting to you]
- **Development Goals**:
  - [goal 1]
  - [goal 2]

## [YYYY-MM-DD]
### Topics Discussed
- [topic 1]
- [topic 2]

### Decisions Made
- [decision]

### Action Items
- [ ] [Manager]: [action item for you]
- [ ] [Person]: [action item for them]

### Notes
[freeform notes, observations, concerns, wins]

---

## [Previous Date]
[previous entry...]
```

## Operations

### Creating a New Person File

When tracking a new direct report:
1. Create `docs/1on1s/` directory if it doesn't exist
2. Create `[person-name].md` with the template above
3. Fill in the Info section with what's known
4. Ask user for any missing information

### Adding a Meeting Entry

When documenting a 1:1:
1. Read the existing file
2. Add new entry at the top (below Info section)
3. Include date, topics, decisions, action items, notes
4. Preserve all previous entries

### Reading History

When preparing for a 1:1:
1. Read the person's file
2. Extract pending action items (unchecked boxes)
3. Identify recurring topics
4. Note development goal progress
5. Find recent wins or concerns

### Updating Action Items

When an action item is completed:
1. Find the item in the file
2. Change `[ ]` to `[x]`
3. Optionally add completion note

## Name Matching

When looking for a person's file, try these variations:
- Exact match: `jane-smith.md`
- First name only: `jane.md`
- Case variations: `Jane-Smith.md`, `JANE-SMITH.md`
- With/without hyphens: `janesmith.md`, `jane_smith.md`

## Privacy Notes

- These files contain sensitive personnel information
- Never share content outside the local project
- Summarize rather than quote when discussing with others
- Action items should be specific but not include sensitive details
