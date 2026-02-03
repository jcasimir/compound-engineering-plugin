---
name: lfg
description: Full autonomous engineering workflow
argument-hint: "[feature description]"
---

Run these slash commands in order. Do not do anything else.

1. `/ralph-wiggum:ralph-loop "finish all slash commands" --completion-promise "DONE"`
2. `/workflows:1-plan $ARGUMENTS`
3. `/workflows:1-plan:deep`
4. `/workflows:3-code`
5. `/workflows:4-code-review`
6. `/compound-engineering:resolve_todo_parallel`
7. `/compound-engineering:test-browser`
8. `/compound-engineering:feature-video`
9. Output `<promise>DONE</promise>` when video is in PR

Start with step 1 now.
