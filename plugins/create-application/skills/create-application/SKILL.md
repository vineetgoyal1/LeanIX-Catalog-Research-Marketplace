---
name: create-application
description: Automatically research and create LeanIX Application fact sheets with verified data. Use this skill whenever the user mentions creating applications, adding applications, researching applications, or says phrases like "Create application for X", "Add Application X", "Research application X", or provides an application name/URL to add to the catalog. Also trigger when user mentions application data collection, application research, or app catalog management. This skill automates the entire workflow - always use it rather than doing ad-hoc research.
---

# Create Application Skill

## Critical Understanding

**YOU ARE THE EXECUTOR** - This skill contains the complete workflow that you must execute directly. When invoked:

- ✅ YOU read the workflow and guidelines
- ✅ YOU execute all 4 steps in sequence
- ✅ YOU make the parallel research calls
- ✅ YOU verify the data and resolve conflicts
- ❌ DO NOT delegate the entire workflow to a "application-creator" subagent
- ❌ DO NOT use Task tool to spawn an agent to "follow the workflow"

Think of this skill as your instruction manual - you're the worker following the manual, not a manager delegating to someone else.

---

## When to Use This Skill

Trigger this skill when the user says:
- "Create an application for [name]"
- "Add [application name] to the catalog"
- "Create an application entry for [website URL]"

**Do NOT trigger** for:
- General questions about applications
- Searching for existing applications
- Updating existing application entries (unless creating first)

---

## Workflow Overview

```
Step 1: Parallel Research (YOU execute 13 queries simultaneously)
   ↓
Step 2: Agent Verification (YOU compare sources and resolve conflicts)
   ↓
Step 3: Quality Check (YOU validate against criteria)
   ↓
Step 4: Create & Update (YOU call LeanIX MCP and Python CLI)
```

---

## Pre-Flight Checklist

Before starting, YOU must:

1. **Read the complete workflow**:
   ```
   Read WORKFLOW.md
   ```

2. **Read all 11 guidelines** (these are in the parent directory):
   ```
   Read guidelines/Application_Description_Guidelines.md
   Read guidelines/Application_Webpage_URL_Guidelines.md
   Read guidelines/Application_Hosting_Type_Guidelines.md
   Read guidelines/Application_SSO_Status_Guidelines.md
   Read guidelines/Application_Pricing_Guidelines.md
   Read guidelines/Application_Product_Category_Guidelines.md
   Read guidelines/Application_Alias_Guidelines.md
   Read guidelines/Application_Subtype_Guidelines.md
   Read guidelines/Application_SI_ID_Implementation.md
   Read guidelines/Application_As_Of_Date_Guidelines.md
   Read guidelines/Application_Collection_Status_and_Deprecated_Guidelines.md
   ```

3. **Verify tools are available**:
   - Check for `mcp__perplexity__perplexity_search` (load with ToolSearch if needed)
   - Check for `WebFetch` tool
   - Check for `mcp__LeanIX_MCP_Server_Remote__` tools (load with ToolSearch if needed)

**Self-Reflection**: If you're about to skip reading the guidelines or make ad-hoc queries, STOP and ask yourself: "Why am I not following the documented workflow?"

---

## Step 1: Parallel Research

**YOU must execute ALL 13 queries in a SINGLE message** - this is critical for parallelism.

### How to Use the Python Research Modules

The Python modules in `lib/` are **query templates** that show you exactly what to ask. **Read them first** to understand the correct query structure, then make parallel API calls.

**Step 1a: Read the Query Templates**

Before making ANY queries, read these files to see the exact query format:
- Read `lib/application_researcher.py` - Shows the 8 Perplexity query methods
- Read `lib/parallel_researcher.py` - Shows WebFetch extraction prompts

**Step 1b: Execute Parallel Research (Use the Templates)**

Now make **13 simultaneous tool calls** using the query formats from the modules.

**Example Pattern:**
```
# Read the template first
Read lib/application_researcher.py

# Then make the call using that query format
mcp__perplexity__perplexity_search(
    query="<exact query from get_url_research_query() method>"
)
```

**DO NOT improvise queries. DO NOT skip reading the modules. The templates ensure consistency with the guidelines.**

### Perplexity Queries (8 total)

```python
# Execute all 8 simultaneously in one message
# Use query formats from lib/application_researcher.py methods:
# - get_url_research_query()
# - get_hosting_type_research_query()
# - get_sso_status_research_query()
# - get_pricing_research_query()
# - get_product_category_research_query()
# - get_aliases_research_query()
# - get_subtype_research_query()
# - get_description_research_query()

mcp__perplexity__perplexity_search(query="<use get_url_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_hosting_type_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_sso_status_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_pricing_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_product_category_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_aliases_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_subtype_research_query() format>")
mcp__perplexity__perplexity_search(query="<use get_description_research_query() format>")
```

### WebFetch Queries (5 total)

```python
# Execute all 5 simultaneously in the same message as Perplexity
WebFetch(url="https://[app-domain]", prompt="Extract: name, description, type indicators, hosting info, SSO mentions")
WebFetch(url="https://[app-domain]/security", prompt="Extract: SSO support, authentication methods, security features")
WebFetch(url="https://[app-domain]/pricing", prompt="Extract: pricing model, tiers, features by plan")
WebFetch(url="https://[app-domain]/about", prompt="Extract: company background, former names, aliases")
WebFetch(url="https://[app-domain]/changelog", prompt="Extract: SSO announcements, major features, hosting updates")
```

**Critical**: All 13 queries go in ONE message with 13 tool calls. This achieves true parallelism.

**Handle redirects**: If WebFetch returns a redirect, immediately make a new WebFetch call with the redirect URL in your next message.

---

## Step 2: Agent Verification

For each field, YOU compare Perplexity vs WebFetch and resolve conflicts:

### Verification Process

```
For each field:
1. Extract value from Perplexity
2. Extract value from WebFetch
3. Compare:
   - ✓ MATCH → Use agreed value (HIGH confidence)
   - ⚠ CONFLICT → Apply resolution rule (see below)
   - ❌ MISSING → Use available source (MEDIUM confidence)
4. Check for marketing language (descriptions only)
5. Record confidence level
```

### Resolution Rules

1. **Both agree** → Use agreed value, HIGH confidence
2. **One has data, other doesn't** → Use available data, MEDIUM confidence
3. **Both differ** → Apply field-specific guidelines:
   - **Description**: Prefer factual over marketing language
   - **Product Category**: Prefer more specific over general
   - **Hosting Type**: Complete evaluation matrix if ambiguous
   - **SSO**: Require explicit evidence from official sources
4. **Both fail** → Mark as "Not Found" or use fixed default

### Marketing Language Check

For descriptions, detect and remove:
- Buzzwords: "leading", "powerful", "innovative", "revolutionary", "seamless", "transform", "empower"
- Rewrite: "provides" not "empowers", "integrates" not "seamless integration"
- Focus on WHAT it does, not marketing claims

### Output Format

Create verified data with confidence tracking:

```json
{
  "webpageUrl": {"value": "...", "confidence": "high", "source": "both_agree"},
  "hostingType": {"value": "saas", "confidence": "high", "source": "both_agree"},
  "hostingDescription": {"value": "...", "confidence": "high", "source": "webfetch"},
  "ssoStatus": {"value": "supported", "confidence": "high", "source": "both_plus_changelog"},
  "pricingUrl": {"value": "...", "confidence": "high", "source": "webfetch_pricing"},
  "pricingType": {"value": "...", "confidence": "high", "source": "both_agree"},
  "productCategory": {"value": "...", "confidence": "high", "source": "webfetch"},
  "alias": {"value": "", "confidence": "high", "source": "both_agree_none"},
  "category": {"value": "businessApplication", "confidence": "high", "source": "fixed"},
  "description": {"value": "...", "confidence": "high", "source": "perplexity", "word_count": 66},
  "collectionStatus": {"value": "inReview", "confidence": "high", "source": "fixed"},
  "deprecated": {"value": "No", "confidence": "high", "source": "fixed"},
  "asOfDate": {"value": "YYYY-MM-DD", "confidence": "high", "source": "current_date"}
}
```

---

## Step 3: Quality Check

Validate before proceeding:

### Validation Criteria

- [ ] Overall confidence > 70%
- [ ] Description: 30-90 words
- [ ] Description: No marketing buzzwords
- [ ] category = "businessApplication"
- [ ] deprecated = "No" (capital N)
- [ ] collectionStatus = "inReview"
- [ ] SI ID generated (PascalCase, no spaces)
- [ ] Critical fields present: webpageUrl, description, hostingType
- [ ] SSO research: 5+ sources checked (official docs, security page, changelog, pricing, integrations)

### Decision

If all checks pass:
```
✓ Quality check PASSED - Proceeding to Step 4
Overall confidence: 95%
All critical fields present
```

If any check fails:
```
⚠ Quality check FAILED:
- Issue: Description too short (22 words, need 30-90)
- Issue: Marketing language detected: "revolutionary", "cutting-edge"

Action: Fix issues before proceeding
```

---

## Step 4: Create & Update

### 4.1: Create Application

```python
result = mcp__LeanIX_MCP_Server_Remote__create_fact_sheet(
    name="[Application Name]",
    type="Application"
)
fact_sheet_id = result["id"]
```

### 4.2: Update Custom Fields via Python CLI

**Required Environment**:
- `LEANIX_API_TOKEN` - Get from user if not set
- `LEANIX_SUBDOMAIN` - Usually "demo-eu-10"

**Method 1: Direct JSON**
```bash
export LEANIX_API_TOKEN='LXT_...' && \
export LEANIX_SUBDOMAIN='demo-eu-10' && \
cd ../create-provider && \
python main.py update \
    --fact-sheet-id "{fact_sheet_id}" \
    --type Application \
    --fields '{...json...}'
```

**Method 2: From File (Recommended)**
```bash
# 1. Write fields to JSON file
Write: ../create-application/executions/[App_Name]/final_fields.json

# 2. Execute update
export LEANIX_API_TOKEN='LXT_...' && \
export LEANIX_SUBDOMAIN='demo-eu-10' && \
cd ../create-provider && \
python main.py update \
    --fact-sheet-id "{fact_sheet_id}" \
    --type Application \
    --fields "$(cat ../create-application/executions/[App_Name]/final_fields.json)"
```

### 4.3: Update Description via MCP

```python
mcp__LeanIX_MCP_Server_Remote__update_fact_sheet(
    id=fact_sheet_id,
    description="[verified description]"
)
```

### 4.4: Report Success

```
✅ Application Created Successfully!

Application: [Name]
Overall Confidence: 95% (HIGH)

Verified Data Summary:
├─ Webpage URL: https://... ✓✓ (both sources)
├─ Hosting Type: paas ✓✓ (both sources)
├─ SSO Status: supported ✓✓✓ (both + changelog)
├─ Pricing Type: usage-based ✓ (official page)
├─ Product Category: Development / DevOps ✓✓
├─ Aliases: (none found) ✓✓
└─ Description: 66 words ✓✓ (factual)

Conflicts Resolved: 1
- Pricing model: Used official page over general description

Fixed Fields Set:
├─ Collection Status: inReview ✓
├─ Deprecated: No ✓
└─ As-of Date: 2026-02-23 ✓

LeanIX URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/{id}

Status: Ready for review team approval
```

---

## Error Handling

### Scenario: Perplexity Fails

```
✗ Perplexity MCP unavailable
✓ WebFetch working

Action: Use WebFetch data only
Confidence: Downgraded to MEDIUM
Proceed: YES (website is official source)
```

### Scenario: WebFetch Fails

```
✓ Perplexity working with citations
✗ WebFetch timeout/blocked

Action: Use Perplexity data only
Confidence: MEDIUM to HIGH (depends on citations)
Proceed: YES (authoritative sources cited)
```

### Scenario: Both Fail

```
✗ Perplexity error
✗ WebFetch blocked

Action: CANNOT PROCEED
Tell user: "Unable to research [App]. Please provide data manually or try later."
```

### Scenario: SSO Unclear

```
⚠ No explicit SSO evidence found
⚠ Not stated as "not supported"

Action: Leave ssoStatus blank
Rationale: Better blank than guessing
```

### Scenario: API Token Missing

```
Error: LEANIX_API_TOKEN not set

Action: Ask user for token
Prompt: "I need your LeanIX API token to create the application. It starts with 'LXT_'."
```

---

## Field-Specific Strategies

### Hosting Type (Complex Decision)

**Decision Tree**:
1. Check name for keywords: "Mobile App", "Desktop", "Cloud", "Private Edition"
2. Identify primary user: Business users → SaaS, Developers → PaaS, IT teams → IaaS
3. For AWS/Azure/GCP services: Check if they provide infrastructure or applications
4. If ambiguous: Complete evaluation matrix (score all 6 types)

**Examples**:
- Smartsheet → SaaS (end-users, collaboration)
- AWS Lambda → PaaS (developers, deploy code)
- AWS EC2 → IaaS (IT teams, provision VMs)
- Slack Desktop → Mobile (desktop/mobile native)

### SSO Status (Must Be Explicit)

**Search Priority**:
1. **Changelog first** ⭐ - SSO often announced as milestone
2. Security page - explicit SSO mentions
3. Enterprise page - enterprise features list
4. Pricing page - SSO as paid feature
5. Integration directories - Okta, Azure AD listings

**Evidence Required**:
- Keywords: "SSO", "SAML", "OAuth", "single sign-on"
- From official sources only
- Multiple confirmations preferred
- Blank if no clear evidence

### Product Category

**Reference**: guidelines/Application_Product_Category_Guidelines.md (top 50 categories listed)

**Strategy**:
1. Extract functionality from description
2. Match to existing categories (3,120 total)
3. Use most specific (e.g., "Project Management" over "Collaboration")
4. Common categories:
   - HR / Talent Management (107 apps)
   - CRM Software (94 apps)
   - Development / DevOps (55 apps)
   - Marketing Automation Software (56 apps)
   - Project Management Software (82 apps)

---

## Fixed Fields (No Research Needed)

These always use the same values:

```json
{
  "category": "businessApplication",
  "collectionStatus": "inReview",
  "deprecated": "No",
  "asOfDate": "2026-02-23"  // Today's date in ISO format
}
```

---

## Common Mistakes to Avoid

❌ **Delegating to subagent**: YOU execute the workflow, don't spawn an "application-creator" agent
❌ **Sequential research**: All 13 queries must run in parallel (one message, 13 tool calls)
❌ **Skipping guidelines**: Must read all 11 before starting
❌ **Accepting marketing language**: Detect and rewrite to factual statements
❌ **Guessing SSO status**: Leave blank if no clear evidence
❌ **Using generic categories**: Be specific ("Project Management" not "Business Software")
❌ **Skipping quality check**: Validate before proceeding to Step 4
❌ **Wrong date format**: Must be YYYY-MM-DD (ISO 8601)

---

## Execution Workspace

Create workspace for tracking:

```bash
mkdir -p ../executions/[App_Name]
```

Save outputs:
- `final_fields.json` - Verified data ready for LeanIX
- `COMPLETION_REPORT.md` - Full research summary
- `parallel_research.json` - Raw research data (optional)

---

## Summary

**Your role**: Execute the 4-step workflow directly
**Key principle**: Parallel research → Verification → Quality check → Create
**Success criteria**: 95%+ confidence, all validations passed, LeanIX entry created
**Time commitment**: ~2-3 minutes total (most time in Step 1 parallelism)

**Remember**: YOU are the executor following this workflow, not a coordinator delegating to others. Read, execute, verify, create - that's your job.
