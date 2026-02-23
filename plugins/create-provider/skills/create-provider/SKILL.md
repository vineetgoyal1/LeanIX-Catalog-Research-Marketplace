---
name: create-provider
description: Automatically research and create LeanIX Provider fact sheets with verified data. Use this skill whenever the user mentions creating providers, adding providers, researching providers, or says phrases like "Create Provider for X", "Add Provider X", "Research provider X", or provides a provider name/URL to add to the catalog. Also trigger when user mentions provider data collection, provider research, or vendor catalog management. This skill automates the entire workflow - always use it rather than doing ad-hoc research.
---

# Provider Auto-Creation Skill

This skill automates the complete Provider fact sheet creation workflow using parallel research, cross-verification, and quality checks.

## ⚠️ CRITICAL: Read Before Proceeding ⚠️

**This is a RIGID skill. Follow the workflow exactly. No ad-hoc queries. No improvisation.**

Before doing ANYTHING, complete this checklist:

### Pre-Flight Checklist

- [ ] Read `WORKFLOW_V2.md` in this directory (complete workflow)
- [ ] Read all 5 guidelines in `guidelines/` directory:
  - [ ] `Provider_Classification_Definitions.md`
  - [ ] `Provider_URL_Validation_Guidelines.md`
  - [ ] `Provider_Headquarters_Address_Guidelines.md`
  - [ ] `Provider_Alias_Discovery_Guidelines.md`
  - [ ] `Provider_Description_Guidelines.md`
- [ ] Verify Perplexity MCP is available (`mcp__perplexity__perplexity_search`)
- [ ] Verify WebFetch tool is available
- [ ] Verify LeanIX MCP is available (`mcp__LeanIX_MCP_Server_Remote__`)
- [ ] **Read** Python query templates: `lib/provider_researcher.py`, `lib/parallel_researcher.py`, `lib/verification_agent.py` (these show the correct query formats to use)

**If you're about to skip reading WORKFLOW_V2.md or make ad-hoc Perplexity calls, STOP.**

Ask yourself: *"Why am I not following the documented workflow? What step did I skip?"*

Then: Go back, read the documentation, start from Step 1.

---

## When to Use This Skill

Trigger when user says:
- "Create Provider for [name/URL]"
- "Add Provider [name]"
- "Research provider [name]"
- "Create a provider entry for [name]"
- "I need to add [name] to the provider catalog"
- Provides a provider URL and asks to catalog it

Examples:
- "Create Provider for Slack"
- "Add Provider Microsoft"
- "Create Provider for https://teamsmart.ai/"

---

## What This Skill Does

Automates Provider fact sheet creation through a 4-step workflow:

1. **Parallel Research** - Perplexity MCP + WebFetch run simultaneously (5-10 seconds)
2. **Agent Verification** - Cross-verify data, resolve conflicts, assign confidence scores
3. **Quality Check** - Validate confidence > 70%, all critical fields present
4. **Create & Update** - Use LeanIX MCP + Python CLI to create fact sheet

**8 Fields Auto-Populated:**
- Homepage URL (validated from 2+ sources)
- Provider Category (Enterprise/Individual/Community)
- Aliases and former names
- Headquarters address
- Description (30-90 words, organization-focused)
- Collection status, as-of date, deprecated flag

---

## The Workflow (Read WORKFLOW_V2.md for Full Details)

### Step 1: Parallel Research

**IMPORTANT**: Read `WORKFLOW_V2.md` for the complete parallel research protocol.

#### How to Use the Python Research Modules

The Python modules in `lib/` are **query templates** that show you exactly what to ask. **Read them first** to understand the correct query structure, then make parallel API calls.

**Step 1a: Read the Query Templates**

Before making ANY queries, read these files to see the exact query format:
- Read `lib/provider_researcher.py` - Shows the 5 Perplexity query methods
- Read `lib/parallel_researcher.py` - Shows WebFetch extraction prompts

**Step 1b: Execute Parallel Research (Use the Templates)**

Now make **8 simultaneous tool calls** using the query formats from the modules:

**Perplexity Queries (5 calls):**
1. **URL Query** - Use `get_url_research_query()` format from `provider_researcher.py`
2. **Category Query** - Use `get_category_research_query()` format
3. **Aliases Query** - Use `get_aliases_research_query()` format
4. **Headquarters Query** - Use `get_headquarters_research_query()` format
5. **Description Query** - Use `get_description_research_query()` format

**WebFetch Queries (3 calls):**
6. **Homepage** - Use `_get_homepage_extraction_prompt()` format from `parallel_researcher.py`
7. **About Page** - Use `_get_about_extraction_prompt()` format
8. **Contact Page** - Use `_get_contact_extraction_prompt()` format

**Example Pattern:**
```
# Read the template first
Read lib/provider_researcher.py

# Then make the call using that query format
mcp__perplexity__perplexity_search(
    query="<exact query from get_url_research_query() method>"
)
```

**DO NOT improvise queries. DO NOT skip reading the modules. The templates ensure consistency with the guidelines.**

### Step 2: Agent Verification

**IMPORTANT**: Read `WORKFLOW_V2.md` for complete verification protocol.

Use `lib/verification_agent.py` to:
- Compare Perplexity vs WebFetch for each field
- Identify conflicts
- Apply resolution rules:
  - Both agree → Use agreed value (HIGH confidence)
  - One has data → Use available data (MEDIUM confidence)
  - Both differ → Run verification query, choose most reliable
  - Both fail → Mark "Not Found", ask user

**Marketing Language Filter**: For ALL descriptions, check for buzzwords:
- Detect: "seamless", "transform", "enhance", "streamline", "empower", "revolutionary", "cutting-edge", "enterprise-grade", "leading", "innovative", "powerful"
- Rewrite: Factual statements only ("integrates with" not "seamless integration")
- Read `MARKETING_LANGUAGE_FILTER.md` for complete list

Output: Verified data with confidence scores per field

### Step 3: Quality Check

Before creating fact sheet, verify:
- ✅ Overall confidence > 70%
- ✅ Critical fields present (URL, Category)
- ✅ No unresolved conflicts
- ✅ Description word count valid (30-90 words)

If any check fails, present options:
1. Save with partial data
2. Manual input for missing fields
3. Cancel operation

### Step 4: Create & Update

```python
# 4.1 Create fact sheet via LeanIX MCP
fact_sheet_id = mcp__LeanIX_MCP_Server_Remote__create_fact_sheet(
    name=provider_name,
    type="Provider"
)

# 4.2 Update custom fields via Python CLI
# Run: python create-provider/main.py update --fact-sheet-id {id} --type Provider --fields '{...}'
update_fields = {
    "homePageUrl": verified_data.url,
    "providerCategory": verified_data.category,
    "aliases": verified_data.aliases,
    "headquartersAddress": verified_data.headquarters,
    "description": verified_data.description,
    "collectionStatus": "inReview",
    "asOfDate": today's date,
    "deprecated": "no"
}

# 4.3 Return URL
return f"https://{subdomain}.leanix.net/{workspace}/factsheet/Provider/{fact_sheet_id}"
```

---

## Guidelines (Must Read)

Before researching ANY field, read the corresponding guideline:

### Provider Classification
**File**: `guidelines/Provider_Classification_Definitions.md`

3 categories with decision tree:
1. **Individual**: Single named person/personal portfolio
2. **Enterprise**: Commercial company with formal business operations
3. **Community Based**: Open-source projects, foundations, collaborative initiatives

**Decision order matters**: Check Individual first, then Enterprise, then Community.

### URL Validation
**File**: `guidelines/Provider_URL_Validation_Guidelines.md`

**NEVER HALLUCINATE URLS**. Core principles:
- Find in 2+ authoritative sources
- Validate HTTP status code (200 OK)
- Check SSL certificate
- Return "Not Found" if uncertain

### Headquarters Address
**File**: `guidelines/Provider_Headquarters_Address_Guidelines.md`

Priority order:
1. Official website (best)
2. Business registries (good)
3. News articles (acceptable)

**Partial data is OK**: "San Francisco, CA, United States" is better than guessing full street address.

### Alias Discovery
**File**: `guidelines/Provider_Alias_Discovery_Guidelines.md`

7 alias types to check:
1. URL variations (with/without www)
2. Former company names (pre-rebrand)
3. Acquisition history (acquired companies)
4. Abbreviations (IBM for International Business Machines)
5. Legal entity names (Inc, Corp, Ltd)
6. DBA names (Doing Business As)
7. Stylistic variations (capitalization, punctuation)

### Description Writing
**File**: `guidelines/Provider_Description_Guidelines.md`

Requirements:
- 30-90 words
- Organization-focused (not product-focused)
- Factual and objective (no marketing language)
- Extract from official website
- Remove buzzwords (see MARKETING_LANGUAGE_FILTER.md)

---

## Python Modules

### lib/provider_researcher.py
Executes single-provider research via Perplexity with 5 specialized queries.

**Use when**: You need to research one provider using Perplexity MCP.

### lib/parallel_researcher.py
Coordinates parallel research across Perplexity + WebFetch.

**Use when**: Starting Step 1 of the workflow.

### lib/verification_agent.py
Compares results from multiple sources and resolves conflicts.

**Use when**: Starting Step 2 of the workflow (after parallel research completes).

### main.py (Python CLI)
Updates custom fields via GraphQL API.

**Use when**: Step 4, after fact sheet is created via LeanIX MCP.

**Command format**:
```bash
cd create-provider
python main.py update \
  --fact-sheet-id "uuid-here" \
  --type Provider \
  --fields '{"homePageUrl": "...", "providerCategory": "...", ...}'
```

---

## Output Format

After completing workflow, present results like this:

```
✓ Provider created successfully!

Provider: TeamSmart AI
Overall Confidence: 88% (HIGH)

Verified Data:
├─ Homepage URL: https://teamsmart.ai/ ✓✓ (both sources)
├─ Category: Enterprise ✓✓ (both sources)
├─ Aliases: TeamSmart.ai ✓ (perplexity verified)
├─ Headquarters: San Francisco, CA, US ✓✓ (both sources)
└─ Description: 44 words ✓✓ (official website, marketing language removed)

Conflicts Resolved: 2
- Aliases: Used Perplexity (WebFetch found none)
- Description: Rewrote to remove "seamless", "transforms", "enhance"

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/{id}
```

---

## Error Handling

### Scenario 1: Perplexity Fails, WebFetch Works
```
✓ WebFetch: Successfully scraped website
✗ Perplexity: MCP connection failed

Action: Use WebFetch data only
Confidence: Downgraded to MEDIUM (single source)
Proceed: YES (sufficient data from official website)
```

### Scenario 2: WebFetch Fails, Perplexity Works
```
✗ WebFetch: Website blocking/timeout
✓ Perplexity: Got results with citations

Action: Use Perplexity data only
Confidence: MEDIUM to HIGH (depends on citation quality)
Proceed: YES (Perplexity provides authoritative sources)
```

### Scenario 3: Both Fail
```
✗ Perplexity: MCP error
✗ WebFetch: Website not accessible

Action: Cannot proceed
User prompt: "Unable to research [Provider]. Please provide data manually or try again later."
```

### Scenario 4: Sources Conflict
```
⚠ Perplexity: Category = "Individual"
⚠ WebFetch: Category = "Enterprise"

Action: Run verification query to Perplexity
If still unclear: Present evidence to user and ask them to choose
```

---

## Anti-Patterns (What NOT to Do)

❌ **Making ad-hoc Perplexity queries** instead of using provider_researcher.py
❌ **Skipping WORKFLOW_V2.md** and improvising the workflow
❌ **Not reading guidelines** before researching fields
❌ **Hallucinating URLs** instead of finding authoritative sources
❌ **Using marketing language** in descriptions (always filter buzzwords)
❌ **Creating fact sheet before quality check** (validate confidence first)
❌ **Bypassing verification step** (always cross-check sources)

---

## Why This Workflow Matters

**Without this workflow**, you get:
- Hallucinated URLs
- Inconsistent categorization
- Marketing language in descriptions
- No confidence scores
- Single source (no validation)

**With this workflow**, you get:
- Verified data from 2+ sources
- Consistent classification using decision tree
- Factual, objective descriptions
- Confidence scores per field
- Conflict resolution with transparency

**Speed**: 5-10 seconds total (parallelized)
**Accuracy**: 88%+ confidence typical
**Reliability**: Fallback if one source fails

---

## Self-Check Questions

Before creating a Provider, ask yourself:

1. Did I read WORKFLOW_V2.md completely?
2. Did I read the relevant guidelines for each field?
3. Am I using the documented modules (provider_researcher.py, verification_agent.py)?
4. Am I running parallel research, or making ad-hoc queries?
5. Did I verify data from 2+ sources?
6. Did I check for marketing language in descriptions?
7. Did I run quality checks before creating the fact sheet?

If answer to ANY question is "no" → **STOP** and read documentation first.

---

## References

- `WORKFLOW_V2.md` - Complete workflow with examples
- `guidelines/` - 5 field-specific guidelines
- `MARKETING_LANGUAGE_FILTER.md` - Buzzword detection
- `FIELD_REFERENCE.md` - LeanIX field specifications
- `README.md` - Python CLI usage
- `lib/` - Python modules for research and verification

---

## Getting Started

When user says "Create Provider for [name]":

1. **Read WORKFLOW_V2.md** (don't skip this)
2. **Read guidelines** for all 5 fields
3. **Execute Step 1**: Parallel research (use parallel_researcher.py)
4. **Execute Step 2**: Agent verification (use verification_agent.py)
5. **Execute Step 3**: Quality check (confidence > 70%?)
6. **Execute Step 4**: Create & update (LeanIX MCP + Python CLI)
7. **Present results** with confidence scores and verification details

**Remember**: This is a RIGID workflow. Follow it exactly. No shortcuts.
