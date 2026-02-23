# Agent Instructions for Provider Creation

## Recognizing When to Use This Skill

This skill should be triggered when the user requests **Provider creation** (not updates, research, or other entity types).

**Valid invocation patterns:**
- "Create Provider for [name/URL]"
- "Add Provider [name]"
- "Set up Provider for [name/URL]"
- "Make a Provider fact sheet for [name]"
- "New Provider: [name]"

**Full pattern list**: See [SKILL_INVOCATION_PATTERNS.md](SKILL_INVOCATION_PATTERNS.md)

**Do NOT trigger for:**
- "Update Provider X" (modification, not creation)
- "Research Provider Y" (information gathering, not creation)
- "Create Application Z" (different entity type)

---

## YOU MUST READ THIS FIRST

When the user says: **"Create Provider for [X]"** or **"Create Provider for [URL]"**

### Step 0: Preparation (DO THIS FIRST)

1. **Read workflow documentation**
   - Read `WORKFLOW_V2.md` completely (all 436 lines)
   - Understand the 4-step process: Parallel Research → Agent Verification → Quality Check → Create & Update

2. **Read all guidelines**
   - `guidelines/Provider_Classification_Definitions.md`
   - `guidelines/Provider_URL_Validation_Guidelines.md`
   - `guidelines/Provider_Headquarters_Address_Guidelines.md`
   - `guidelines/Provider_Alias_Discovery_Guidelines.md`
   - `guidelines/Provider_Description_Guidelines.md`

3. **Verify tools are available**
   - Perplexity MCP (for web research)
   - WebFetch (for website scraping)
   - LeanIX MCP (for fact sheet creation)
   - Python CLI in `main.py` (for custom field updates)

### Step 1: Execute Parallel Research

**Use the documented approach:**
- Use `lib/provider_researcher.py` to generate structured queries (don't write ad-hoc queries)
- Call Perplexity and WebFetch **in parallel** (single message, multiple tool calls)
- Research ALL fields simultaneously:
  - Homepage URL (validate from 2+ sources)
  - Provider Category (Enterprise/Individual/Community)
  - Aliases (7 types per guidelines)
  - Headquarters Address (official sources only)
  - Description (30-90 words, no marketing language)

**Collect results from both sources:**
```json
{
  "perplexity": {
    "url": {...},
    "category": {...},
    "aliases": {...},
    "headquarters": {...},
    "description": {...}
  },
  "webfetch": {
    "homepage": {...},
    "about": {...},
    "contact": {...}
  }
}
```

### Step 2: Execute Agent Verification

**Use the documented verification logic:**
- Compare Perplexity vs WebFetch results for each field
- Apply resolution rules from WORKFLOW_V2.md:
  1. Both agree → Use agreed value (HIGH confidence)
  2. One has data, other doesn't → Use available data (MEDIUM confidence)
  3. Both differ → Run verification query, choose most reliable
  4. Both fail → Mark as "Not Found"
- Filter marketing language from descriptions (seamless, transform, enhance, etc.)
- Generate confidence scores per field

**Output verified data:**
```json
{
  "verified_data": {
    "homePageUrl": {"value": "...", "confidence": "high", "source": "both_agree"},
    "providerCategory": {"value": "...", "confidence": "high", "source": "..."},
    "aliases": {"value": "...", "confidence": "medium", "source": "..."},
    "headquartersAddress": {"value": "...", "confidence": "high", "source": "..."},
    "description": {"value": "...", "confidence": "high", "source": "..."}
  },
  "verification_metadata": {
    "overall_confidence": 0.88,
    "conflicts_resolved": 2
  }
}
```

### Step 3: Quality Check

**Verify quality criteria:**
- ✅ Overall confidence > 70%?
- ✅ Critical fields present? (URL, Category)
- ✅ No unresolved conflicts?
- ✅ Description word count 30-90?

**If quality check fails:**
- Inform user about low confidence or missing data
- Offer options: Save with partial data, manual input, or cancel

**If quality check passes:**
- Proceed to Step 4 automatically

### Step 4: Create & Update

**Execute in order:**
1. Create fact sheet via LeanIX MCP:
   ```
   mcp__LeanIX_MCP_Server_Remote__create_fact_sheet(
     name="Provider Name",
     type="Provider"
   )
   ```

2. Update custom fields via Python CLI:
   ```bash
   cd create-provider
   python main.py update \
     --fact-sheet-id "uuid" \
     --type Provider \
     --fields '{
       "homePageUrl": "https://...",
       "providerCategory": "enterprise",
       "aliases": "...",
       "headquartersAddress": "...",
       "description": "...",
       "collectionStatus": "inReview",
       "asOfDate": "2026-02-18",
       "deprecated": "no"
     }'
   ```

3. Return fact sheet URL to user:
   ```
   https://{subdomain}.leanix.net/{workspace}/factsheet/Provider/{id}
   ```

---

## ❌ What NOT To Do

- ❌ Don't make ad-hoc Perplexity calls without reading guidelines
- ❌ Don't skip parallel research (must use both sources)
- ❌ Don't skip verification step
- ❌ Don't proceed with confidence < 70% without user approval
- ❌ Don't improvise research queries - use `provider_researcher.py` logic
- ❌ Don't call Perplexity and WebFetch sequentially - use parallel tool calls
- ❌ Don't hallucinate URLs or addresses
- ❌ Don't include marketing language in descriptions

---

## Self-Correction Protocol

**If you catch yourself about to:**
- Make an ad-hoc Perplexity call
- Skip reading the workflow documentation
- Bypass parallel research
- Skip the verification step
- Proceed without quality check

**STOP and ask yourself:**

1. **"Why am I not following the documented workflow?"**
   - Did I skip reading WORKFLOW_V2.md?
   - Am I trying to take shortcuts?
   - Am I improvising instead of using documented modules?

2. **"What step did I miss?"**
   - Did I read the complete workflow? (No → Read it now)
   - Did I read the guidelines? (No → Read them now)
   - Am I using provider_researcher.py logic? (No → Use it)
   - Am I doing parallel research? (No → Do it properly)

3. **"What should I do now?"**
   - Go back to Step 0
   - Read WORKFLOW_V2.md completely
   - Read all 4 guidelines
   - Start from Step 1 properly

**Then acknowledge to user:**
"I didn't follow the documented workflow. Let me start over properly by reading WORKFLOW_V2.md and executing the parallel research workflow."

---

## Success Indicators

**You're doing it right if:**
- ✅ You read WORKFLOW_V2.md before making any tool calls
- ✅ You read all 4 guidelines before researching
- ✅ You call Perplexity and WebFetch in parallel (same message)
- ✅ You compare both sources and generate confidence scores
- ✅ You present verified data with conflict resolution notes
- ✅ You check quality before creating the fact sheet
- ✅ You filter marketing language from descriptions

**You're doing it wrong if:**
- ❌ You make Perplexity calls before reading documentation
- ❌ You skip WebFetch and only use Perplexity
- ❌ You don't compare sources or verify data
- ❌ You proceed without confidence scores
- ❌ You create fact sheets without quality checks

---

## Example Execution Trace

```
User: "Create Provider for https://teamsmart.ai/"

Agent:
1. ✓ Read WORKFLOW_V2.md (436 lines)
2. ✓ Read 4 guidelines
3. ✓ Verified tools available

Step 1: Parallel Research
- ✓ Called Perplexity + WebFetch in parallel
- ✓ Collected results from both sources

Step 2: Agent Verification
- ✓ Compared URL: Both agree → HIGH confidence
- ✓ Compared Category: Both say "enterprise" → HIGH confidence
- ✓ Compared Aliases: Perplexity found 2, WebFetch found 0 → MEDIUM confidence
- ✓ Compared HQ: Both say "San Francisco, CA, US" → HIGH confidence
- ✓ Compared Description: Filtered marketing language → HIGH confidence
- Overall confidence: 88%

Step 3: Quality Check
- ✓ Confidence 88% > 70%
- ✓ Critical fields present
- ✓ No unresolved conflicts
- PASS → Proceed

Step 4: Create & Update
- ✓ Created fact sheet via LeanIX MCP
- ✓ Updated custom fields via Python CLI
- ✓ Returned URL

Result: https://demo-eu-10.leanix.net/.../factsheet/Provider/{id}
```

---

## Final Reminder

**Every single time you create a Provider:**
1. Read WORKFLOW_V2.md
2. Read 4 guidelines
3. Execute 4 steps in order
4. No shortcuts, no improvisation

**If you deviate, self-correct immediately.**
