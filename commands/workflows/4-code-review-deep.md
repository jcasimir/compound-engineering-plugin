---
name: workflows:4-code-review:deep
description: Two-round collaborative code review where reviewers learn from each other before finalizing
argument-hint: "[PR number, GitHub URL, branch name, or latest]"
---

# Deep Review Command

<command_purpose>A rare, thorough two-round review process where reviewers first analyze independently, then read each other's reports and produce enriched final reports informed by their colleagues' perspectives.</command_purpose>

## When to Use This

This is **not** your everyday review. Use it for:
- Major architectural changes
- Security-critical features
- Complex refactors touching many systems
- Pre-launch reviews of significant features
- When you want reviewers to build on each other's insights

This will take significantly longer than a standard review. That's the point.

## The Process

```
ROUND 1: Independent Analysis
Each reviewer examines the code alone, produces initial report
                    │
                    ▼
TRIAGE: Abby recommends Round 2 participants
Based on engagement and findings from Round 1
                    │
                    ▼
ROUND 2: Cross-Pollination
Selected reviewers read ALL Round 1 reports
Then rewrite their own report with new perspective
                    │
                    ▼
SYNTHESIS: Abby consolidates enriched reports
Produces final prioritized summary
```

---

## Phase 1: Setup

<review_target> #$ARGUMENTS </review_target>

### Step 1: Determine Review Target

- [ ] Identify the PR, branch, or commit range to review
- [ ] Fetch PR metadata: `gh pr view --json title,body,files,commits`
- [ ] Ensure we're on the correct branch for analysis
- [ ] Note the scope — this helps Abby select Round 2 participants

### Step 2: Discover Available Reviewers

List all review agents matching `4-code-review-*.md` in `agents/` directory. Exclude:
- `4-code-review-abby-synthesis` (she's the PM, not a reviewer)

The reviewers available for this deep review:

**Universal Reviewers:**
- Robo (`4-code-review-agent-native`) — Agent-native architecture
- Maya (`4-code-review-architecture`) — Systems and structure
- Alex (`4-code-review-code-simplicity`) — Simplicity and YAGNI
- Corey (`4-code-review-corey-test`) — Test quality
- Donna (`4-code-review-data-integrity`) — Data integrity
- Dana (`4-code-review-data-migration`) — Migration safety (if migrations present)
- Nathan (`4-code-review-deployment-verification`) — Deployment readiness (if risky changes)
- Erin (`other-erin`) — Process adherence
- Jim (`4-code-review-jim-git`) — Git history and storytelling
- Sandi (`4-code-review-pattern-recognition`) — Patterns and research
- Florence (`4-code-review-performance-oracle`) — Performance and scale
- Kevin (`4-code-review-security-sentinel`) — Security vulnerabilities

**Language-Specific (based on detected languages):**
- Julik (`4-code-review-julik-frontend-races`) — JavaScript/Stimulus races

---

## Phase 2: Round 1 — Independent Review

<round_1_instruction>
Launch all applicable reviewers in parallel. Each reviewer analyzes the code independently and produces their initial report.
</round_1_instruction>

### Execute Round 1

```
# Launch all reviewers in parallel
Task 4-code-review-agent-native(PR diff and context) → round1_robo.md
Task 4-code-review-architecture(PR diff and context) → round1_maya.md
Task 4-code-review-code-simplicity(PR diff and context) → round1_alex.md
Task 4-code-review-corey-test(PR diff and test files) → round1_corey.md
Task 4-code-review-data-integrity(PR diff and context) → round1_donna.md
Task other-erin(PR context and history) → round1_erin.md
Task 4-code-review-jim-git(commit history and PR metadata) → round1_jim.md
Task 4-code-review-pattern-recognition(PR diff and context) → round1_sandi.md
Task 4-code-review-performance-oracle(PR diff and context) → round1_florence.md
Task 4-code-review-security-sentinel(PR diff and context) → round1_kevin.md
[Plus language-specific reviewers as applicable]
```

### Collect Round 1 Reports

Store each reviewer's initial report. These will be:
1. Shown to Abby for triage
2. Shared with Round 2 participants

---

## Phase 3: Triage — Select Round 2 Participants

<triage_instruction>
Abby reviews all Round 1 reports and recommends which reviewers should participate in Round 2, based on their engagement and the significance of their findings.
</triage_instruction>

### Abby's Triage Criteria

```
Task 4-code-review-abby-synthesis("Review these Round 1 reports and recommend which reviewers should participate in Round 2.

Consider:
- Which reviewers found significant issues?
- Which reviewers' perspectives would benefit from seeing others' findings?
- Which reviewers had relatively empty reports? (They may not need Round 2)
- Are there clear connections between reviewers that would be enriched by cross-pollination?

Produce:
1. Recommended Round 2 participants (with reasoning)
2. Reviewers who can skip Round 2 (with reasoning)
3. Any specific cross-connections you'd like reviewers to explore

Round 1 Reports:
[Include all Round 1 reports here]
")
```

### Present Recommendations to User

```markdown
## Round 1 Complete — Round 2 Triage

Abby has reviewed all initial reports and recommends the following for Round 2:

### Recommended for Round 2:
- **Corey** — Found significant test gaps; would benefit from seeing Kevin's security concerns
- **Kevin** — Security findings connect to Maya's architecture concerns
- **Maya** — Architecture issues touch multiple reviewers' findings
- [etc.]

### Can Skip Round 2:
- **Jim** — Git history was clean; minimal findings to enrich
- [etc.]

**Proceed with these Round 2 participants?**
1. Yes, proceed with Abby's recommendations
2. Modify the list (add/remove reviewers)
3. Include all reviewers in Round 2
4. Skip Round 2, go straight to synthesis
```

Wait for user confirmation before proceeding.

---

## Phase 4: Round 2 — Cross-Pollination

<round_2_instruction>
Each selected reviewer reads ALL Round 1 reports (not just their own), then rewrites their report with the benefit of their colleagues' perspectives.
</round_2_instruction>

### Round 2 Prompt Template

For each Round 2 participant, provide:

```
You are [Name], and you've completed your initial review of this PR. Now you have access to what your fellow reviewers found.

**Your Round 1 Report:**
[Their original report]

**Your Colleagues' Round 1 Reports:**
[All other Round 1 reports]

---

**Your Round 2 Task:**

Read through your colleagues' reports carefully. Then produce a **rewritten** version of your report (not an addendum) that:

1. **Incorporates new perspective** — What did you learn from others that changes or deepens your analysis?

2. **Edits or reframes your findings** — Now that you've seen the bigger picture, would you change the priority or framing of any of your findings?

3. **Highlights connections** — Where do your findings connect to or reinforce others' findings? Call these out explicitly.

4. **Notes cross-cutting themes** — What patterns do you see across multiple reviewers that deserve attention?

5. **Adjusts your recommendations** — With the full picture, would you change what you recommend?

Your Round 2 report replaces your Round 1 report. Write it as a complete, standalone report that reflects your enriched understanding.
```

### Execute Round 2

```
# Launch Round 2 participants in parallel (with all Round 1 context)
Task corey-round2(Round 2 prompt with all Round 1 reports) → round2_corey.md
Task kevin-round2(Round 2 prompt with all Round 1 reports) → round2_kevin.md
Task maya-round2(Round 2 prompt with all Round 1 reports) → round2_maya.md
[etc. for each Round 2 participant]
```

---

## Phase 5: Final Synthesis

<synthesis_instruction>
Abby receives all Round 2 reports (plus Round 1 reports from reviewers who skipped Round 2) and produces the final synthesis.
</synthesis_instruction>

### Abby's Final Synthesis

```
Task 4-code-review-abby-synthesis("Synthesize these enriched review reports into a final summary.

**Round 2 Reports (enriched):**
[Round 2 reports from participants]

**Round 1 Reports (from reviewers who skipped Round 2):**
[Round 1 reports]

Note: Round 2 reviewers have already read each other's work and incorporated cross-cutting themes. Look for:
- Consensus that emerged across reviewers
- Themes that multiple reviewers highlighted
- Connections that reviewers explicitly called out
- Any remaining disagreements after cross-pollination

Produce your standard synthesis with:
- 🛑 Showstoppers
- ⚠️ Important
- 💭 Interesting to Think About
- 📋 Someday Maybe

Additionally, include a section on **Cross-Cutting Themes** that emerged from the collaborative review process.
")
```

---

## Phase 6: Deliverables

### Present Final Report

```markdown
## 🔬 Deep Review Complete

**Review Target:** PR #XXX — [Title]
**Process:** Two-round collaborative review

### Round Summary
- **Round 1 Participants:** [count] reviewers
- **Round 2 Participants:** [count] reviewers (selected by Abby)
- **Total Review Depth:** [Significant/Thorough/Exhaustive]

### Cross-Cutting Themes
[Themes that emerged across multiple reviewers after cross-pollination]

1. **[Theme]** — Noted by [Reviewer], [Reviewer], and [Reviewer]
   - [Description]

### Findings

🛑 **Showstoppers**
[List]

⚠️ **Important**
[List]

💭 **Interesting to Think About**
[List]

📋 **Someday Maybe**
[List]

### Reviewer Insights

Notable observations from the cross-pollination process:
- [Reviewer] changed their assessment of [X] after reading [Other Reviewer]'s findings
- [Multiple reviewers] converged on [concern] from different angles
- [Etc.]

### Next Steps
[Actionable recommendations]
```

### Create Todo Files

Use the file-todos skill to create todo files for findings, following the standard process from `/workflows:4-code-review`.

---

## Notes

**Why two rounds?**

Single-pass reviews are efficient but can miss connections. When Corey finds a test gap and Kevin finds a security issue, they might not realize those are related — until they read each other's reports. Round 2 lets reviewers build on collective intelligence.

**Why let Abby select Round 2 participants?**

Not every reviewer needs Round 2. If Jim found no issues with the git history, having him read everyone else's reports won't add much. Abby's triage ensures Round 2 effort goes where it matters.

**Why rewrite instead of addendum?**

Addendums create fragmented reports. A rewritten Round 2 report is a complete, standalone document that reflects the reviewer's full understanding — easier for humans to read and act on.
