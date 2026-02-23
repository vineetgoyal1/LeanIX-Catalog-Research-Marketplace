# Provider Creation Skill - Invocation Patterns

## Overview
This document defines the keywords, phrases, and patterns that should trigger the **create-provider** skill. Use this as a reference for both AI agents (to recognize when to use this skill) and users (to know how to invoke it).

---

## Primary Invocation Pattern

### The Golden Pattern:
```
[ACTION_VERB] + "Provider" + ["for" | ":" | "-"] + [PROVIDER_NAME_OR_URL]
```

**Examples:**
- "Create Provider for Slack"
- "Create Provider for https://slack.com"
- "Add Provider: Microsoft"
- "New Provider - Adobe"

---

## Valid Action Verbs

These verbs indicate **creation intent** and should trigger the skill:

| Action Verb | Example Usage | Trigger? |
|-------------|---------------|----------|
| **Create** | "Create Provider for X" | ✅ YES |
| **Add** | "Add Provider X" | ✅ YES |
| **Set up** | "Set up Provider for X" | ✅ YES |
| **Make** | "Make a Provider for X" | ✅ YES |
| **New** | "New Provider: X" | ✅ YES |
| **Build** | "Build Provider fact sheet for X" | ✅ YES |
| **Generate** | "Generate Provider for X" | ✅ YES |

---

## Valid Invocation Patterns

### Pattern 1: Simple Creation
```
[ACTION] Provider for [NAME/URL]
```

**Examples:**
- "Create Provider for Slack"
- "Add Provider for Microsoft"
- "Set up Provider for Google"
- "Make Provider for Adobe"

---

### Pattern 2: With "fact sheet"
```
[ACTION] [a/new] Provider fact sheet for [NAME/URL]
```

**Examples:**
- "Create a Provider fact sheet for Salesforce"
- "Create new Provider fact sheet for Oracle"
- "Add a Provider fact sheet for IBM"

---

### Pattern 3: Colon/Dash Separator
```
[ACTION] Provider: [NAME/URL]
[ACTION] Provider - [NAME/URL]
```

**Examples:**
- "Create Provider: Atlassian"
- "New Provider: https://atlassian.com"
- "Add Provider - Zendesk"

---

### Pattern 4: With URL Emphasis
```
[ACTION] Provider for [URL]
```

**Examples:**
- "Create Provider for https://slack.com"
- "Add Provider for https://teamsmart.ai/"
- "Set up Provider for www.salesforce.com"

---

### Pattern 5: Explicit LeanIX Context
```
[ACTION] [a/new] Provider [fact sheet] in LeanIX for [NAME/URL]
```

**Examples:**
- "Create a Provider in LeanIX for Slack"
- "Add new Provider fact sheet in LeanIX for Microsoft"

---

### Pattern 6: Conversational Style
```
Can you [ACTION] Provider for [NAME/URL]
I need [a/to] [ACTION] Provider for [NAME/URL]
Please [ACTION] Provider for [NAME/URL]
```

**Examples:**
- "Can you create Provider for Slack?"
- "I need to add Provider for Microsoft"
- "Please create a Provider fact sheet for Google"
- "I need a new Provider for Adobe"

---

## Invalid Patterns (Should NOT Trigger)

### ❌ Update/Edit Commands
These indicate **modification**, not creation:

```
Update Provider X
Edit Provider Y
Modify Provider Z
Change Provider details for X
Fix Provider information for Y
```

**Why not trigger**: User wants to modify existing Provider, not create new one.

---

### ❌ Research/Query Commands
These indicate **information gathering**, not creation:

```
Research Provider X
What is Provider Y?
Find information about Provider Z
Tell me about Provider X
Search for Provider Y
Show me Provider Z
Look up Provider X
Get details about Provider Y
```

**Why not trigger**: User wants information, not to create a fact sheet.

---

### ❌ Other Entity Types
These are for **different fact sheet types**:

```
Create Application for X
Add IT Component for Y
Set up Product Family for Z
Make Business Capability for X
```

**Why not trigger**: Different entity type requires different skill/workflow.

---

### ❌ Ambiguous or Unclear Intent
These lack clear **creation intent**:

```
Provider for Slack
Slack Provider
What about Provider Microsoft?
Provider Adobe
```

**Why not trigger**: No action verb, unclear if user wants creation or information.

---

## Edge Cases and Clarifications

### Edge Case 1: "Create Provider" Without Target

**User says**: "Create Provider"

**Agent should**: Ask for clarification
```
"Which Provider would you like me to create? Please provide the provider name or URL."
```

**Do NOT**: Trigger the skill without a target.

---

### Edge Case 2: Multiple Providers

**User says**: "Create Provider for Slack and Microsoft"

**Agent should**:
- Option A: Ask if they want both created
- Option B: Create them sequentially
- Option C: Explain that skill handles one at a time

**Do NOT**: Attempt to create both simultaneously unless workflow supports it.

---

### Edge Case 3: Incomplete URL

**User says**: "Create Provider for slack"

**Agent should**: Interpret as provider name "Slack", not URL
- The workflow will research and validate the correct URL
- User doesn't need to provide perfect URLs

---

### Edge Case 4: Provider Already Exists

**User says**: "Create Provider for Slack" (but Slack already exists)

**Agent should**:
- Check if Provider exists in LeanIX first
- If exists: "Provider for Slack already exists. Would you like to update it instead?"
- If not exists: Proceed with creation

---

### Edge Case 5: Typos or Variations

**User says**: "Creat Provider for Slak" (typos)

**Agent should**:
- Use fuzzy matching for action verbs
- Ask for confirmation: "Did you mean 'Create Provider for Slack'?"
- Proceed if intent is clear

---

## Recognition Logic for AI Agents

### Step 1: Extract Components

From user message, identify:
1. **Action verb**: create, add, set up, make, new, build, generate
2. **Entity type**: "Provider" (case-insensitive)
3. **Target**: Provider name or URL
4. **Exclusions**: update, edit, modify, research, find, search, show, what, tell

### Step 2: Pattern Matching

```python
# Pseudo-code for agent decision logic

def should_trigger_create_provider_skill(user_message):
    message_lower = user_message.lower()

    # Required: Must mention "provider"
    if "provider" not in message_lower:
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

### Step 3: Extract Provider Target

```python
def extract_provider_target(user_message):
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
| "Create Provider for Slack" | create | provider | Slack | None | ✅ YES |
| "Create Provider for https://slack.com" | create | provider | URL | None | ✅ YES |
| "Add Provider Microsoft" | add | provider | Microsoft | None | ✅ YES |
| "Set up a new Provider for Adobe" | set up | provider | Adobe | None | ✅ YES |
| "Make Provider fact sheet for Google" | make | provider | Google | None | ✅ YES |
| "New Provider: Salesforce" | new | provider | Salesforce | None | ✅ YES |
| "Can you create Provider for Oracle?" | create | provider | Oracle | None | ✅ YES |
| "I need to add Provider for IBM" | add | provider | IBM | None | ✅ YES |
| "Please create Provider https://zendesk.com" | create | provider | URL | None | ✅ YES |
| "Build Provider for Atlassian" | build | provider | Atlassian | None | ✅ YES |
| | | | | | |
| "Update Provider Slack" | update | provider | Slack | update | ❌ NO |
| "Edit Provider Microsoft" | edit | provider | Microsoft | edit | ❌ NO |
| "Research Provider Oracle" | research | provider | Oracle | research | ❌ NO |
| "What is Provider IBM?" | what | provider | IBM | what | ❌ NO |
| "Find Provider Salesforce" | find | provider | Salesforce | find | ❌ NO |
| "Show me Provider Adobe" | show | provider | Adobe | show | ❌ NO |
| "Tell me about Provider Google" | tell | provider | Google | tell | ❌ NO |
| "Create Application for Slack" | create | application | Slack | None | ❌ NO |
| "Add IT Component for X" | add | IT Component | X | None | ❌ NO |
| "Provider for Slack" | None | provider | Slack | None | ❌ NO |
| "Create Provider" | create | provider | None | None | ⚠️ ASK |

---

## User-Facing Documentation

### How to Use This Skill (For Users)

**To create a new Provider fact sheet in LeanIX:**

Simply say:
```
Create Provider for [Provider Name or URL]
```

**Examples that work:**
- "Create Provider for Slack"
- "Create Provider for https://teamsmart.ai/"
- "Add Provider Microsoft"
- "Set up Provider for Salesforce"
- "New Provider: Adobe"
- "Make a Provider fact sheet for Google"

**What happens next:**
1. The agent reads the workflow documentation
2. Researches the Provider using Perplexity and WebFetch
3. Validates all information
4. Creates the fact sheet in LeanIX
5. Returns the fact sheet URL

**You'll need to provide:**
- Provider name OR
- Provider homepage URL

**The agent will automatically research:**
- Official website URL
- Provider category (Enterprise/Community/Individual)
- Headquarters address
- Aliases and former names
- Company description

---

## Agent-Facing Instructions

### When to Trigger This Skill

**Trigger the create-provider skill when:**
1. User message contains creation intent (create, add, set up, make, new)
2. User message mentions "Provider" as the entity type
3. User provides a target (name or URL)
4. User message does NOT contain update/research intent

**Before triggering:**
1. Verify you understood the target correctly
2. Check if Provider already exists (optional)
3. Confirm you have all required tools available

**After triggering:**
1. Follow WORKFLOW_V2.md exactly
2. Read all 5 guidelines before starting
3. Execute parallel research (Perplexity + WebFetch)
4. Verify data and check quality
5. Create fact sheet and return URL

---

## Testing the Recognition Logic

### Test Cases for Agents

**Test 1: Basic Creation**
```
Input: "Create Provider for TeamSmart.ai"
Expected: ✅ Trigger skill with target="TeamSmart.ai"
```

**Test 2: URL Input**
```
Input: "Create Provider for https://slack.com"
Expected: ✅ Trigger skill with target="https://slack.com"
```

**Test 3: Conversational**
```
Input: "Can you create a Provider fact sheet for Microsoft?"
Expected: ✅ Trigger skill with target="Microsoft"
```

**Test 4: Update Command**
```
Input: "Update Provider for Salesforce"
Expected: ❌ Do NOT trigger (update, not create)
```

**Test 5: Research Query**
```
Input: "Research Provider Oracle"
Expected: ❌ Do NOT trigger (research, not create)
```

**Test 6: Missing Target**
```
Input: "Create Provider"
Expected: ⚠️ Ask user: "Which Provider would you like to create?"
```

**Test 7: Wrong Entity Type**
```
Input: "Create Application for Slack"
Expected: ❌ Do NOT trigger (Application, not Provider)
```

**Test 8: Ambiguous Intent**
```
Input: "What about Provider for Slack?"
Expected: ❌ Do NOT trigger (unclear intent, ask for clarification)
```

---

## Troubleshooting

### Problem: Skill triggers when it shouldn't

**Symptoms**: Skill triggers for research queries like "What is Provider X?"

**Solution**: Ensure exclusion verbs are properly checked. "What" should block triggering.

**Fix**: Review recognition logic Step 2 - verify exclusion list includes query verbs.

---

### Problem: Skill doesn't trigger when it should

**Symptoms**: User says "Create Provider for X" but agent doesn't recognize it

**Solution**:
1. Check if "Provider" is properly detected (case-insensitive)
2. Verify action verb is in the creation list
3. Confirm target extraction logic works

**Fix**: Test with exact phrase in decision logic.

---

### Problem: Agent asks for clarification unnecessarily

**Symptoms**: User provides clear target but agent asks "Which Provider?"

**Solution**: Target extraction regex may be failing.

**Fix**: Review Step 3 extraction patterns. Ensure "for", ":", "-" patterns work.

---

## Future Enhancements

As the skill repository grows, consider:

1. **Multi-Provider Creation**: "Create Providers for Slack, Microsoft, and Adobe"
2. **Batch Upload**: "Create Providers from this CSV file"
3. **Interactive Mode**: "Start Provider creation wizard"
4. **Voice Commands**: Natural language variations for voice interfaces

---

## Summary Checklist

**For AI Agents - Before triggering create-provider skill:**

- [ ] User message contains creation verb (create, add, set up, make, new, build, generate)
- [ ] User message mentions "Provider" as entity type
- [ ] User message does NOT contain exclusion verbs (update, edit, research, find, what, show, tell)
- [ ] Target (provider name or URL) is identifiable
- [ ] If target is missing, ask user for clarification
- [ ] Confirm you've read WORKFLOW_V2.md before proceeding
- [ ] Verify all required tools are available (Perplexity MCP, WebFetch, LeanIX MCP)

**If all boxes checked → Trigger the create-provider skill**

---

*Document created: 2026-02-18*
*Version: 1.0*
*Related: WORKFLOW_V2.md, AGENT_INSTRUCTIONS.md, Provider creation guidelines*
