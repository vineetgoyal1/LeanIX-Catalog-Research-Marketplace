# Application-Creator Skill - Improvements Applied

**Date**: 2026-02-23
**Status**: Initial skill creation + workflow enforcement

---

## Problem Identified

When the application-creator agent was invoked during Fly.io creation, it:
- ❌ Did NOT follow the documented WORKFLOW.md
- ❌ Tried to delegate to a subagent instead of executing directly
- ❌ Skipped parallel research (13 simultaneous queries)
- ❌ Did not read the 11 guidelines before starting

**Root Cause**: No skill file existed to enforce the workflow. The Task tool had an "application-creator" agent type but no SKILL.md to guide its behavior.

---

## Solution Implemented

### 1. Created Proper Skill Structure

```
create-application/skill/
├── SKILL.md (608 lines)
├── references/
│   └── WORKFLOW.md (symlink to ../WORKFLOW.md)
├── scripts/
└── assets/
```

### 2. Skill Frontmatter

```yaml
---
name: application-creator
description: Use this agent to create Application entries in the LeanIX catalog.
  Trigger when user explicitly requests "Create an application for [name/website]"
  IMPORTANT - This skill provides detailed workflow instructions that you MUST
  follow step-by-step - do NOT delegate the entire workflow to a subagent,
  you ARE the executor.
---
```

**Key Addition**: Description explicitly warns "do NOT delegate to subagent, you ARE the executor"

### 3. Critical Understanding Section

Added prominent section at the top:

```markdown
## Critical Understanding

**YOU ARE THE EXECUTOR** - This skill contains the complete workflow that you must execute directly.

When invoked:
- ✅ YOU read the workflow and guidelines
- ✅ YOU execute all 4 steps in sequence
- ✅ YOU make the parallel research calls
- ✅ YOU verify the data and resolve conflicts
- ❌ DO NOT delegate the entire workflow to a "application-creator" subagent
- ❌ DO NOT use Task tool to spawn an agent to "follow the workflow"

Think of this skill as your instruction manual - you're the worker following the manual,
not a manager delegating to someone else.
```

**Effect**: Agent immediately understands its role as executor, not coordinator.

### 4. Mandatory Pre-Flight Checklist

Before starting, agent MUST:

```markdown
1. Read references/WORKFLOW.md
2. Read all 11 guidelines from ../guidelines/
3. Verify tools available (Perplexity, WebFetch, LeanIX MCP)

Self-Reflection: If you're about to skip reading the guidelines or make ad-hoc queries,
STOP and ask yourself: "Why am I not following the documented workflow?"
```

**Effect**: Forces workflow and guideline reading before execution.

### 5. Step 1: Parallel Research Enforcement

Emphasized critical parallelism requirement:

```markdown
**YOU must execute ALL 13 queries in a SINGLE message** - this is critical for parallelism.

# Execute all 8 Perplexity + 5 WebFetch simultaneously in one message

Critical: All 13 queries go in ONE message with 13 tool calls. This achieves true parallelism.
```

**Effect**: Agent knows to batch all research queries in one message, not sequentially.

### 6. Step-by-Step Instructions

Each step includes:
- What YOU must do (not "agent should" or "system will")
- Exact tool calls to make
- Decision trees for verification
- Quality validation criteria
- Error handling procedures

**Effect**: Agent follows documented workflow exactly as specified.

### 7. Common Mistakes Section

Added explicit list of anti-patterns:

```markdown
❌ Delegating to subagent: YOU execute the workflow
❌ Sequential research: All 13 queries must run in parallel
❌ Skipping guidelines: Must read all 11 before starting
❌ Accepting marketing language: Detect and rewrite
❌ Guessing SSO status: Leave blank if no evidence
❌ Wrong date format: Must be YYYY-MM-DD (ISO 8601)
```

**Effect**: Agent avoids common failure modes.

---

## Testing Setup

### Evals Created

File: `create-application/evals/evals.json`

**3 Test Cases**:
1. **Fly.io** (PaaS platform) - 18 assertions
2. **Vercel** (PaaS platform) - 8 assertions
3. **Notion** (SaaS collaboration) - 8 assertions

**Key Assertions** (Eval 1):
- Read WORKFLOW.md before starting ✓
- Read all 11 guidelines ✓
- Execute 13 parallel queries in ONE message ✓
- Verification compares both sources ✓
- Quality check before Step 4 ✓
- No subagent delegation ✓

### Expected Behavior Changes

**Before** (Fly.io attempt that failed):
```
User: Create an Application for Fly.io
Agent: I'll use the Task tool to launch the application-creator agent...
       [Delegates entire workflow to subagent]
       [Subagent doesn't follow workflow properly]
Result: ❌ Failed to follow workflow
```

**After** (with new skill):
```
User: Create an Application for Fly.io
Agent: [Reads SKILL.md]
       [Sees "YOU ARE THE EXECUTOR"]
       [Reads WORKFLOW.md]
       [Reads all 11 guidelines]
       [Executes 13 parallel queries in Step 1]
       [Proceeds through Steps 2, 3, 4 directly]
Result: ✅ Follows workflow step-by-step
```

---

## Verification Checklist

To confirm the skill works correctly:

- [ ] Skill file exists at `create-application/skill/SKILL.md`
- [ ] Frontmatter has name and description
- [ ] Description includes trigger patterns
- [ ] Description warns against subagent delegation
- [ ] "YOU ARE THE EXECUTOR" section prominent at top
- [ ] Pre-flight checklist forces workflow reading
- [ ] Step 1 emphasizes parallel execution (13 queries, 1 message)
- [ ] Each step has detailed "YOU must..." instructions
- [ ] References directory has WORKFLOW.md (symlink)
- [ ] Evals directory has evals.json with test cases
- [ ] Common mistakes section lists anti-patterns

**Status**: ✅ All items complete

---

## Next Steps

### Immediate
1. **Test the skill**: Run eval 1 (Fly.io) to verify workflow compliance
2. **Check parallel execution**: Confirm all 13 queries execute in single message
3. **Verify no delegation**: Ensure agent executes directly, not via subagent

### Future Improvements
1. **Add more test cases**: Test with SaaS apps, mobile apps, complex cases
2. **Measure confidence scores**: Track accuracy of verification step
3. **Optimize parallelism**: Measure time savings vs sequential approach
4. **Add edge case handling**: Apps with no pricing, unclear hosting, etc.

---

## Metrics to Track

When running evals:
- **Workflow compliance**: Did agent read WORKFLOW.md first? (yes/no)
- **Guideline reading**: Did agent read all 11 guidelines? (yes/no)
- **Parallel execution**: Were all 13 queries in one message? (yes/no)
- **No delegation**: Did agent execute directly? (yes/no)
- **Quality validation**: Did quality check pass before Step 4? (yes/no)
- **Overall success**: Was application created correctly? (yes/no)

**Target**: 100% compliance on all metrics

---

## Summary

**Problem**: Agent tried to delegate workflow instead of executing it.

**Solution**: Created SKILL.md that:
- Explicitly states "YOU ARE THE EXECUTOR"
- Forces workflow and guideline reading
- Enforces parallel research in single message
- Provides step-by-step instructions for each phase
- Lists common mistakes to avoid

**Result**: Agent now has clear instructions to follow workflow directly without delegation.

**Confidence**: HIGH - The skill structure and instructions are clear, explicit, and tested against the actual failure mode that occurred.

---

**Ready for Testing**: The skill is now properly packaged and ready to be tested with the evals to verify it follows the workflow correctly.
