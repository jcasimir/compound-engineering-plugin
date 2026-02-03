---
name: workflow:2-plan-review:deep
description: Two-round collaborative plan review where reviewers learn from each other before finalizing
argument-hint: "[plan file path or plan content]"
---

# Deep Plan Review Command

<command_purpose>A thorough two-round review process where plan reviewers first analyze independently, then read each other's reports and produce enriched final reviews informed by their colleagues' diverse perspectives.</command_purpose>

## When to Use This

This is **not** your everyday plan review. Use it for:
- Major strategic initiatives
- Plans with significant resource commitments
- Cross-functional projects affecting multiple teams
- Plans where diverse perspectives are crucial
- When you want product, design, and engineering viewpoints to cross-pollinate

This takes longer than a standard plan review. That's the point — you're getting eight distinct worldviews (product strategy + technical architecture) to build on each other.

## The Reviewers

Each brings a radically different lens:

### Product & Strategy

| Reviewer | Lens | Core Question |
|----------|------|---------------|
| **Jason Fried** | Scope & Sustainability | "What can we cut? Will this burn people out?" |
| **Charles Eames** | Systems & Constraints | "Is this the right problem? Are we embracing constraints?" |
| **Marty Cagan** | Discovery & Validation | "What's the evidence? Have we validated the risks?" |
| **Melissa Perri** | Outcomes & Strategy | "Is this outcome-driven or are we in the build trap?" |
| **Sandy Speicher** | Human-Centered & Equity | "Who's affected? Whose voices are missing?" |

### Technical Architecture

| Reviewer | Lens | Core Question |
|----------|------|---------------|
| **Steve Kinney** | Frontend Architecture | "Will this scale? Is this simple enough to maintain?" |
| **Avi** | Rails Architecture | "Does this follow Rails conventions? What's the ecosystem doing?" |
| **Greg Baugues** | AI Integration | "Is this the right use of AI? What are the real risks?" |

## The Process

```
ROUND 1: Independent Analysis
Each reviewer examines the plan alone from their unique perspective
                    │
                    ▼
TRIAGE: Erin recommends Round 2 participants
Based on engagement, findings, and cross-connections
                    │
                    ▼
ROUND 2: Cross-Pollination
Selected reviewers read ALL Round 1 reports
Then rewrite their own report with enriched perspective
                    │
                    ▼
SYNTHESIS: Erin consolidates enriched reports
Produces final prioritized summary with cross-cutting themes
```

---

## Phase 1: Setup

<plan_target> #$ARGUMENTS </plan_target>

### Step 1: Identify the Plan

- [ ] Read the plan document or content provided
- [ ] Identify key sections: goals, approach, timeline, resources, risks
- [ ] Note the scope — this helps Erin select Round 2 participants

### Step 2: Prepare Plan Context

Summarize the plan for reviewers:
- What is being proposed?
- What problem does it solve?
- What's the timeline and resource commitment?
- What are the stated assumptions?

---

## Phase 2: Round 1 — Independent Review

<round_1_instruction>
Launch all five plan reviewers in parallel. Each reviewer analyzes the plan independently from their unique perspective and produces their initial report.
</round_1_instruction>

### Execute Round 1

```
# Launch all plan reviewers in parallel

# Product & Strategy
Task 2-plan-review-jason-fried(Plan context) → round1_jason.md
Task 2-plan-review-charles-eames(Plan context) → round1_charles.md
Task 2-plan-review-marty-cagan(Plan context) → round1_marty.md
Task 2-plan-review-melissa-perri(Plan context) → round1_melissa.md
Task 2-plan-review-sandy-speicher(Plan context) → round1_sandy.md

# Technical Architecture
Task 2-plan-review-steve-frontend(Plan context) → round1_steve.md
Task 2-plan-review-avi-rails(Plan context) → round1_avi.md
Task 2-plan-review-greg-ai(Plan context) → round1_greg.md
```

### Collect Round 1 Reports

Store each reviewer's initial report. These will be:
1. Shown to Erin for triage
2. Shared with Round 2 participants

---

## Phase 3: Triage — Select Round 2 Participants

<triage_instruction>
Erin reviews all Round 1 reports and recommends which reviewers should participate in Round 2, based on their engagement, the significance of their findings, and potential cross-connections.
</triage_instruction>

### Erin's Triage Task

```
Task other-erin("Review these Round 1 plan reviews and recommend which reviewers should participate in Round 2.

**Your Role:** You're orchestrating a collaborative review process. Round 2 lets reviewers build on each other's insights.

**Consider:**
- Which reviewers found significant concerns or opportunities?
- Which reviewers' perspectives would benefit from seeing others' findings?
- Are there natural connections? (e.g., Jason's scope concerns + Melissa's outcome focus)
- Which reviewers had relatively light findings? (They may not need Round 2)
- Where would cross-pollination create the most value?

**Produce:**
1. Recommended Round 2 participants (with reasoning)
2. Reviewers who can skip Round 2 (with reasoning)
3. Specific cross-connections you'd like reviewers to explore

**Round 1 Reports:**
[Include all Round 1 reports here]
")
```

### Present Recommendations to User

```markdown
## Round 1 Complete — Round 2 Triage

Erin has reviewed all initial reports and recommends the following for Round 2:

### Recommended for Round 2:
- **Jason** — Scope concerns connect to Melissa's outcome clarity questions
- **Marty** — Validation gaps would benefit from Sandy's human-centered lens
- **Sandy** — Equity concerns touch multiple reviewers' findings
- [etc.]

### Can Skip Round 2:
- **Charles** — Constraint analysis was thorough; minimal cross-pollination value
- [etc.]

**Proceed with these Round 2 participants?**
1. Yes, proceed with Erin's recommendations
2. Modify the list (add/remove reviewers)
3. Include all reviewers in Round 2
4. Skip Round 2, go straight to synthesis
```

Wait for user confirmation before proceeding.

---

## Phase 4: Round 2 — Cross-Pollination

<round_2_instruction>
Each selected reviewer reads ALL Round 1 reports (not just their own), then rewrites their report with the benefit of their colleagues' diverse perspectives.
</round_2_instruction>

### Round 2 Prompt Template

For each Round 2 participant, provide:

```
You are [Name], and you've completed your initial review of this plan. Now you have access to what your fellow reviewers found — each bringing a completely different lens.

**Your Round 1 Report:**
[Their original report]

**Your Colleagues' Round 1 Reports:**

*Product & Strategy:*

**Jason Fried (Scope & Sustainability):**
[Jason's report]

**Charles Eames (Systems & Constraints):**
[Charles's report]

**Marty Cagan (Discovery & Validation):**
[Marty's report]

**Melissa Perri (Outcomes & Strategy):**
[Melissa's report]

**Sandy Speicher (Human-Centered & Equity):**
[Sandy's report]

*Technical Architecture:*

**Steve Kinney (Frontend Architecture):**
[Steve's report]

**Avi (Rails Architecture):**
[Avi's report]

**Greg Baugues (AI Integration):**
[Greg's report]

---

**Your Round 2 Task:**

Read through your colleagues' reports carefully. Notice how different their lenses are from yours. Then produce a **rewritten** version of your report (not an addendum) that:

1. **Incorporates new perspective** — What did you learn from others that changes or deepens your analysis? A product person might see something you missed. A designer might reframe a concern.

2. **References your colleagues** — Explicitly cite where you agree, disagree, or build on their findings. "Marty's point about validation gaps reinforces my concern about..." or "While Jason wants to cut scope, I'd argue..."

3. **Highlights connections** — Where do your findings connect to or reinforce others' findings? Where do they create productive tension?

4. **Notes cross-cutting themes** — What patterns do you see across multiple reviewers that deserve attention?

5. **Adjusts your recommendations** — With the full picture from product, design, systems, and business perspectives, would you change what you recommend?

Your Round 2 report replaces your Round 1 report. Write it as a complete, standalone report that reflects your enriched understanding and explicitly engages with your colleagues' perspectives.
```

### Execute Round 2

```
# Launch Round 2 participants in parallel (with all Round 1 context)
Task jason-round2(Round 2 prompt with all Round 1 reports) → round2_jason.md
Task marty-round2(Round 2 prompt with all Round 1 reports) → round2_marty.md
Task sandy-round2(Round 2 prompt with all Round 1 reports) → round2_sandy.md
[etc. for each Round 2 participant]
```

---

## Phase 5: Final Synthesis

<synthesis_instruction>
Erin receives all Round 2 reports (plus Round 1 reports from reviewers who skipped Round 2) and produces the final synthesis.
</synthesis_instruction>

### Erin's Final Synthesis

```
Task other-erin("Synthesize these enriched plan review reports into a final summary for the user.

**Context:** This plan went through a two-round collaborative review. In Round 2, reviewers read each other's reports and rewrote their own with cross-pollinated insights. They've explicitly referenced each other's perspectives.

**Round 2 Reports (enriched):**
[Round 2 reports from participants]

**Round 1 Reports (from reviewers who skipped Round 2):**
[Round 1 reports]

**Your Synthesis Task:**

1. **Cross-Cutting Themes** — What concerns or opportunities emerged across multiple reviewers? Especially note where reviewers from different disciplines converged.

2. **Productive Tensions** — Where did reviewers disagree? These tensions often reveal important trade-offs the team needs to navigate.

3. **Prioritized Findings** — Organize into:
   - 🛑 **Showstoppers** — Issues that should block proceeding
   - ⚠️ **Significant Concerns** — Must address before or during execution
   - 💡 **Opportunities** — Insights that could strengthen the plan
   - 💭 **Questions to Resolve** — Ambiguities the team should clarify
   - 📋 **Minor Notes** — Worth considering but not critical

4. **Reviewer Interactions** — Note where reviewers explicitly built on each other:
   - Who changed their view after reading colleagues?
   - What new insights emerged from the cross-pollination?
   - Where did different disciplines reinforce each other?

5. **Recommended Actions** — What should the team do with this feedback?

Produce a synthesis that honors each reviewer's unique perspective while creating a coherent narrative for the user.
")
```

---

## Phase 6: Deliverables

### Present Final Report

```markdown
## 🔬 Deep Plan Review Complete

**Plan:** [Plan name/title]
**Process:** Two-round collaborative review with cross-pollination

### Review Summary
- **Round 1 Participants:** 8 reviewers (Jason, Charles, Marty, Melissa, Sandy, Steve, Avi, Greg)
- **Round 2 Participants:** [X] reviewers (selected by Erin)
- **Perspectives Represented:** Business/Scope, Systems/Design, Product/Validation, Strategy/Outcomes, Human-Centered/Equity, Frontend Architecture, Rails Architecture, AI Integration

---

### Cross-Cutting Themes

Patterns that emerged across multiple reviewers:

1. **[Theme]** — Noted by [Reviewers]
   - [Description of shared concern or insight]

2. **[Theme]** — Noted by [Reviewers]
   - [Description]

---

### Productive Tensions

Where reviewers saw things differently (these are trade-offs to navigate):

1. **[Tension]**
   - Jason's view: [Position]
   - Melissa's view: [Counter-position]
   - Implication: [What the team needs to decide]

---

### Prioritized Findings

🛑 **Showstoppers**
[Issues that should block proceeding]

⚠️ **Significant Concerns**
[Must address before or during execution]

💡 **Opportunities**
[Insights that could strengthen the plan]

💭 **Questions to Resolve**
[Ambiguities the team should clarify]

📋 **Minor Notes**
[Worth considering but not critical]

---

### How Reviewers Built on Each Other

Notable interactions from the cross-pollination:
- [Reviewer] changed their assessment of [X] after reading [Other Reviewer]'s perspective
- [Multiple reviewers] converged on [concern] from different angles
- [Reviewer]'s [lens] reframed [Other Reviewer]'s concern as [new insight]

---

### Recommended Actions

**Before proceeding:**
1. [Action]
2. [Action]

**During execution:**
1. [Action]

**To strengthen the plan:**
1. [Action]

---

### Summary

[One paragraph synthesizing the overall assessment and key takeaways]
```

---

## Notes

**Why these eight reviewers?**

**Product & Strategy** — Different worldviews on what to build:
- **Jason** (37signals) — "Is this too much? Can we ship smaller?"
- **Charles** (Eames) — "Is this the right problem? Do constraints shape this?"
- **Marty** (SVPG) — "Have we validated this? What are the risks?"
- **Melissa** (Produx) — "Is this outcome-driven or feature-driven?"
- **Sandy** (IDEO) — "Who's affected? Is this human-centered?"

**Technical Architecture** — Different worldviews on how to build:
- **Steve** (Frontend Masters/Temporal) — "Will this scale? Is this maintainable?"
- **Avi** (Rails ecosystem) — "Does this follow conventions? What's the ecosystem doing?"
- **Greg** (AI practitioner) — "Is AI the right tool here? What actually works vs. hype?"

When product strategy and technical architecture perspectives cross-pollinate during planning, you catch issues before they're built — not after.

**Why Erin as orchestrator?**

Erin's role is process — how we work, not what we build. She's ideal for:
- Triaging which reviewers need Round 2
- Synthesizing diverse perspectives into coherent narrative
- Identifying where the collaborative process added value

**Why rewrite instead of addendum?**

Addendums create fragmented reports. A rewritten Round 2 report is a complete document that:
- Reflects the reviewer's full, enriched understanding
- Explicitly references colleagues' perspectives
- Is easier for humans to read and act on
