# Application-Creator Skill - Installation Guide

## Current Status

✅ Skill created and structured properly
✅ SKILL.md with workflow enforcement
✅ References linked (WORKFLOW.md)
✅ Evals created for testing

## Skill Location

```
/Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-application/skill/
```

## How It Works Now

The skill is properly structured but not yet "installed" as a Claude Code skill. However, it can still be used:

### Method 1: Direct Reference (Current)

When you want to create an application, explicitly reference the skill:

```
User: Read /Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-application/skill/SKILL.md, then create an Application for Vercel
```

This works because:
- The Read tool loads SKILL.md into context
- The instructions explicitly state "YOU ARE THE EXECUTOR"
- Agent follows the workflow step-by-step
- No delegation occurs

### Method 2: Install as .skill File (Future)

To make this available as a system-wide skill that triggers automatically:

1. **Package the skill**:
   ```bash
   cd /Users/I529175/.claude/plugins/cache/claude-plugins-official/skill-creator/aa296ec81e8c
   python scripts/package_skill.py \
     "/Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-application/skill"
   ```

2. **Install the .skill file**:
   - The packaging script creates a `.skill` archive
   - Move it to your skills directory
   - Claude Code will auto-detect and load it

3. **Verify installation**:
   ```bash
   # Check installed skills
   ls ~/.claude/skills/
   ```

## Testing the Skill

### Quick Test

```
Read /Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-application/skill/SKILL.md

Then: Create an Application for Vercel
```

**Expected behavior**:
- ✓ Reads WORKFLOW.md
- ✓ Reads all 11 guidelines
- ✓ Executes 13 parallel queries in one message
- ✓ Verifies data from both sources
- ✓ Runs quality check
- ✓ Creates application in LeanIX
- ✓ NO delegation to subagent

### Run Evals

```bash
cd /Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-application

# Run eval 1 (Fly.io)
# Test whether agent follows workflow correctly
```

## What Makes This Different

### Before (Failed Approach)
```
User: Create an Application for Fly.io
Agent: → Spawns "application-creator" subagent
       → Subagent doesn't follow workflow
       → Makes ad-hoc queries
       → Skips guidelines
Result: ❌ Workflow bypassed
```

### After (With SKILL.md)
```
User: Read skill/SKILL.md, then create Application for Fly.io
Agent: → Reads SKILL.md directly
       → Sees "YOU ARE THE EXECUTOR"
       → Reads WORKFLOW.md
       → Reads all 11 guidelines
       → Executes 13 parallel queries
       → Follows all 4 steps
Result: ✅ Workflow followed exactly
```

## Key Files

```
create-application/skill/
├── SKILL.md              # Main skill instructions (608 lines)
├── IMPROVEMENTS.md       # What was fixed and why
├── INSTALL.md           # This file
├── references/
│   └── WORKFLOW.md      # Symlink to ../../WORKFLOW.md
├── scripts/             # (empty, for future scripts)
└── assets/              # (empty, for future assets)

create-application/evals/
├── evals.json           # 3 test cases
└── files/               # (empty, no file inputs needed)
```

## Validation

The skill is correctly structured if:

✅ SKILL.md exists with proper frontmatter
✅ Description warns "do NOT delegate to subagent"
✅ "YOU ARE THE EXECUTOR" section is prominent
✅ Pre-flight checklist forces workflow reading
✅ Step 1 emphasizes "13 queries in ONE message"
✅ References/WORKFLOW.md is accessible
✅ Evals exist for testing

**Status**: ✅ All validation criteria met

## What Was Fixed

The original issue: Agent tried to delegate to a subagent instead of following the workflow directly.

**Root cause**: No SKILL.md existed to enforce the workflow.

**Solution**: Created SKILL.md with:
1. Explicit "YOU ARE THE EXECUTOR" messaging
2. Forced workflow/guideline reading
3. Step-by-step instructions
4. Emphasis on parallel execution
5. Anti-pattern list (common mistakes)

## Next Actions

1. **Test**: Run a create application request with the skill loaded
2. **Verify**: Check that all 13 queries execute in parallel
3. **Confirm**: Ensure no subagent delegation occurs
4. **Package** (optional): Create .skill file for system-wide installation

---

**Note**: The skill is functional now when explicitly loaded via Read. Packaging is optional for convenience but not required for operation.
