# Application Creation Skill - Invocation Patterns

## Overview
This document defines the keywords, phrases, and patterns that should trigger the **create-application** skill. Use this as a reference for both AI agents (to recognize when to use this skill) and users (to know how to invoke it).

---

## Primary Invocation Pattern

### The Golden Pattern:
```
[ACTION_VERB] + "Application" + ["for" | ":" | "-"] + [APPLICATION_NAME_OR_URL]
```

**Examples:**
- "Create Application for Smartsheet"
- "Create Application for https://www.smartsheet.com"
- "Add Application: Salesforce"
- "New Application - Zoom"

---

## Valid Action Verbs

These verbs indicate **creation intent** and should trigger the skill:

| Action Verb | Example Usage | Trigger? |
|-------------|---------------|----------|
| **Create** | "Create Application for X" | ✅ YES |
| **Add** | "Add Application X" | ✅ YES |
| **Set up** | "Set up Application for X" | ✅ YES |
| **Make** | "Make an Application for X" | ✅ YES |
| **New** | "New Application: X" | ✅ YES |
| **Build** | "Build Application fact sheet for X" | ✅ YES |
| **Generate** | "Generate Application for X" | ✅ YES |

---

## Valid Invocation Patterns

### Pattern 1: Simple Creation
```
[ACTION] Application for [NAME/URL]
```

**Examples:**
- "Create Application for Smartsheet"
- "Add Application for Salesforce"
- "Set up Application for Zoom"
- "Make Application for Slack"

---

### Pattern 2: With "fact sheet"
```
[ACTION] [a/new] Application fact sheet for [NAME/URL]
```

**Examples:**
- "Create an Application fact sheet for Trello"
- "Create new Application fact sheet for Asana"
- "Add an Application fact sheet for Monday.com"

---

### Pattern 3: Colon/Dash Separator
```
[ACTION] Application: [NAME/URL]
[ACTION] Application - [NAME/URL]
```

**Examples:**
- "Create Application: Jira"
- "New Application: https://www.atlassian.com/software/jira"
- "Add Application - Confluence"

---

### Pattern 4: With URL Emphasis
```
[ACTION] Application for [URL]
```

**Examples:**
- "Create Application for https://www.smartsheet.com"
- "Add Application for https://www.salesforce.com/"
- "Set up Application for www.zoom.us"

---

### Pattern 5: Explicit LeanIX Context
```
[ACTION] [a/new] Application [fact sheet] in LeanIX for [NAME/URL]
```

**Examples:**
- "Create an Application in LeanIX for Smartsheet"
- "Add new Application fact sheet in LeanIX for Salesforce"

---

### Pattern 6: Conversational Style
```
Can you [ACTION] Application for [NAME/URL]
I need [a/to] [ACTION] Application for [NAME/URL]
Please [ACTION] Application for [NAME/URL]
```

**Examples:**
- "Can you create Application for Smartsheet?"
- "I need to add Application for Salesforce"
- "Please create an Application fact sheet for Zoom"
- "I need a new Application for Slack"

---

## Invalid Patterns (Should NOT Trigger)

### ❌ Update/Edit Commands
These indicate **modification**, not creation:

```
Update Application X
Edit Application Y
Modify Application Z
Change Application details for X
Fix Application information for Y
```

**Why not trigger**: User wants to modify existing Application, not create new one.

---

### ❌ Research/Query Commands
These indicate **information gathering**, not creation:

```
Research Application X
What is Application Y?
Find information about Application Z
Tell me about Application X
Search for Application Y
Show me Application Z
Look up Application X
Get details about Application Y
```

**Why not trigger**: User wants information, not to create a fact sheet.

---

### ❌ Other Entity Types
These are for **different fact sheet types**:

```
Create Provider for X
Add IT Component for Y
Set up Product Family for Z
Make Business Capability for X
```

**Why not trigger**: Different entity type requires different skill/workflow.

---

### ❌ Ambiguous or Unclear Intent
These lack clear **creation intent**:

```
Application for Smartsheet
Smartsheet Application
What about Application Salesforce?
Application Zoom
```

**Why not trigger**: No action verb, unclear if user wants creation or information.

---

## Edge Cases and Clarifications

### Edge Case 1: "Create Application" Without Target

**User says**: "Create Application"

**Agent should**: Ask for clarification
```
"Which Application would you like me to create? Please provide the application name or URL."
```

**Do NOT**: Trigger the skill without a target.

---

### Edge Case 2: Multiple Applications

**User says**: "Create Application for Smartsheet and Salesforce"

**Agent should**:
- Option A: Ask if they want both created
- Option B: Create them sequentially
- Option C: Explain that skill handles one at a time

**Do NOT**: Attempt to create both simultaneously unless workflow supports it.

---

### Edge Case 3: Incomplete URL

**User says**: "Create Application for smartsheet"

**Agent should**: Interpret as application name "Smartsheet", not URL
- The workflow will research and validate the correct URL
- User doesn't need to provide perfect URLs

---

### Edge Case 4: Application Already Exists

**User says**: "Create Application for Smartsheet" (but Smartsheet already exists)

**Agent should**:
- Check if Application exists in LeanIX first
- If exists: "Application for Smartsheet already exists. Would you like to update it instead?"
- If not exists: Proceed with creation

---

### Edge Case 5: Typos or Variations

**User says**: "Creat Application for Smartshet" (typos)

**Agent should**:
- Use fuzzy matching for action verbs
- Ask for confirmation: "Did you mean 'Create Application for Smartsheet'?"
- Proceed if intent is clear

---

## Recognition Logic for AI Agents

### Step 1: Extract Components

From user message, identify:
1. **Action verb**: create, add, set up, make, new, build, generate
2. **Entity type**: "Application" (case-insensitive)
3. **Target**: Application name or URL
4. **Exclusions**: update, edit, modify, research, find, search, show, what, tell

### Step 2: Pattern Matching

```python
# Pseudo-code for agent decision logic

def should_trigger_create_application_skill(user_message):
    message_lower = user_message.lower()

    # Required: Must mention "application"
    if "application" not in message_lower:
        return False

    # Required: Must have creation intent (action verb)
    creation_verbs = ["create", "add", "set up", "make", "new", "build", "generate"]
    has_creation_intent = any(verb in message_lower for verb in creation_verbs)

    if not has_creation_intent:
        return False

    # Exclusion: Must NOT have modification/research intent
    exclusion_verbs = ["update", "edit", "modify", "change", "fix",
                       "research", "find", "search", "show", "what", "tell", "look up"]
    has_exclusion = any(verb in message_lower for verb in exclusion_verbs)

    if has_exclusion:
        return False

    # Required: Must have a target (name or URL pattern)
    has_target = (
        "for " in message_lower or
        ": " in message_lower or
        " - " in message_lower or
        re.search(r'https?://', message_lower)
    )

    if not has_target:
        return False  # Ask for clarification

    # All criteria met
    return True
```

### Step 3: Extract Application Target

```python
def extract_application_target(user_message):
    # Pattern: "for [target]"
    match = re.search(r'for\s+(.+)', user_message, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Pattern: ": [target]" or " - [target]"
    match = re.search(r'[:\-]\s*(.+)', user_message)
    if match:
        return match.group(1).strip()

    # Pattern: URL directly
    match = re.search(r'https?://[\w\.\-/]+', user_message)
    if match:
        return match.group(0)

    return None  # No target found, ask user
```

---

## Examples Decision Matrix

| User Input | Action Verb | Entity | Target | Exclusion | Trigger? |
|------------|-------------|--------|--------|-----------|----------|
| "Create Application for Smartsheet" | create | application | Smartsheet | None | ✅ YES |
| "Create Application for https://www.smartsheet.com" | create | application | URL | None | ✅ YES |
| "Add Application Salesforce" | add | application | Salesforce | None | ✅ YES |
| "Set up a new Application for Zoom" | set up | application | Zoom | None | ✅ YES |
| "Make Application fact sheet for Slack" | make | application | Slack | None | ✅ YES |
| "New Application: Trello" | new | application | Trello | None | ✅ YES |
| "Can you create Application for Asana?" | create | application | Asana | None | ✅ YES |
| "I need to add Application for Monday.com" | add | application | Monday.com | None | ✅ YES |
| "Please create Application https://www.jira.com" | create | application | URL | None | ✅ YES |
| "Build Application for Confluence" | build | application | Confluence | None | ✅ YES |
| | | | | | |
| "Update Application Smartsheet" | update | application | Smartsheet | update | ❌ NO |
| "Edit Application Salesforce" | edit | application | Salesforce | edit | ❌ NO |
| "Research Application Asana" | research | application | Asana | research | ❌ NO |
| "What is Application Monday.com?" | what | application | Monday.com | what | ❌ NO |
| "Find Application Trello" | find | application | Trello | find | ❌ NO |
| "Show me Application Zoom" | show | application | Zoom | show | ❌ NO |
| "Tell me about Application Slack" | tell | application | Slack | tell | ❌ NO |
| "Create Provider for Smartsheet" | create | provider | Smartsheet | None | ❌ NO |
| "Add IT Component for X" | add | IT Component | X | None | ❌ NO |
| "Application for Smartsheet" | None | application | Smartsheet | None | ❌ NO |
| "Create Application" | create | application | None | None | ⚠️ ASK |

---

## User-Facing Documentation

### How to Use This Skill (For Users)

**To create a new Application fact sheet in LeanIX:**

Simply say:
```
Create Application for [Application Name or URL]
```

**Examples that work:**
- "Create Application for Smartsheet"
- "Create Application for https://www.salesforce.com/"
- "Add Application Zoom"
- "Set up Application for Slack"
- "New Application: Trello"
- "Make an Application fact sheet for Asana"

**What happens next:**
1. The agent reads the workflow documentation
2. Researches the Application using Perplexity and WebFetch
3. Validates all information
4. Creates the fact sheet in LeanIX
5. Returns the fact sheet URL

**You'll need to provide:**
- Application name OR
- Application homepage URL

**The agent will automatically research:**
- Official website URL
- Hosting Type (saas/paas/iaas/onPremise/hybrid/mobile with evaluation matrix)
- Hosting Description (technical classification reasoning)
- SSO Status (changelog-first detection)
- Pricing Type (6 models: free/freemium/subscription/perpetual/transaction/enterprise)
- Product Category (most specific from 50+ categories)
- Aliases and former names
- Application Subtype (application vs mobileApp)
- Description (30-90 words, marketing-filtered)
- Collection status, as-of date, deprecated flag

---

## Agent-Facing Instructions

### When to Trigger This Skill

**Trigger the create-application skill when:**
1. User message contains creation intent (create, add, set up, make, new)
2. User message mentions "Application" as the entity type
3. User provides a target (name or URL)
4. User message does NOT contain update/research intent

**Before triggering:**
1. Verify you understood the target correctly
2. Check if Application already exists (optional)
3. Confirm you have all required tools available

**After triggering:**
1. Follow WORKFLOW.md exactly
2. Read all 11 guidelines before starting
3. Execute parallel research (Perplexity + WebFetch)
4. Verify data and check quality
5. Create fact sheet and return URL

---

## Testing the Recognition Logic

### Test Cases for Agents

**Test 1: Basic Creation**
```
Input: "Create Application for Smartsheet"
Expected: ✅ Trigger skill with target="Smartsheet"
```

**Test 2: URL Input**
```
Input: "Create Application for https://www.smartsheet.com"
Expected: ✅ Trigger skill with target="https://www.smartsheet.com"
```

**Test 3: Conversational**
```
Input: "Can you create an Application fact sheet for Salesforce?"
Expected: ✅ Trigger skill with target="Salesforce"
```

**Test 4: Update Command**
```
Input: "Update Application for Trello"
Expected: ❌ Do NOT trigger (update, not create)
```

**Test 5: Research Query**
```
Input: "Research Application Asana"
Expected: ❌ Do NOT trigger (research, not create)
```

**Test 6: Missing Target**
```
Input: "Create Application"
Expected: ⚠️ Ask user: "Which Application would you like to create?"
```

**Test 7: Wrong Entity Type**
```
Input: "Create Provider for Smartsheet"
Expected: ❌ Do NOT trigger (Provider, not Application)
```

**Test 8: Ambiguous Intent**
```
Input: "What about Application for Smartsheet?"
Expected: ❌ Do NOT trigger (unclear intent, ask for clarification)
```

---

## Troubleshooting

### Problem: Skill triggers when it shouldn't

**Symptoms**: Skill triggers for research queries like "What is Application X?"

**Solution**: Ensure exclusion verbs are properly checked. "What" should block triggering.

**Fix**: Review recognition logic Step 2 - verify exclusion list includes query verbs.

---

### Problem: Skill doesn't trigger when it should

**Symptoms**: User says "Create Application for X" but agent doesn't recognize it

**Solution**:
1. Check if "Application" is properly detected (case-insensitive)
2. Verify action verb is in the creation list
3. Confirm target extraction logic works

**Fix**: Test with exact phrase in decision logic.

---

### Problem: Agent asks for clarification unnecessarily

**Symptoms**: User provides clear target but agent asks "Which Application?"

**Solution**: Target extraction regex may be failing.

**Fix**: Review Step 3 extraction patterns. Ensure "for", ":", "-" patterns work.

---

## Future Enhancements

As the skill repository grows, consider:

1. **Multi-Application Creation**: "Create Applications for Smartsheet, Salesforce, and Zoom"
2. **Batch Upload**: "Create Applications from this CSV file"
3. **Interactive Mode**: "Start Application creation wizard"
4. **Voice Commands**: Natural language variations for voice interfaces

---

## Summary Checklist

**For AI Agents - Before triggering create-application skill:**

- [ ] User message contains creation verb (create, add, set up, make, new, build, generate)
- [ ] User message mentions "Application" as entity type
- [ ] User message does NOT contain exclusion verbs (update, edit, research, find, what, show, tell)
- [ ] Target (application name or URL) is identifiable
- [ ] If target is missing, ask user for clarification
- [ ] Confirm you've read WORKFLOW.md before proceeding
- [ ] Verify all required tools are available (Perplexity MCP, WebFetch, LeanIX MCP)

**If all boxes checked → Trigger the create-application skill**

---

*Document created: 2026-02-22*
*Version: 1.0*
*Related: WORKFLOW.md, AGENT_INSTRUCTIONS.md, Application creation guidelines*
