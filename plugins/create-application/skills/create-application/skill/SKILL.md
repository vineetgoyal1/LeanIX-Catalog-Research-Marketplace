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
- "Can you catalog [application] in LeanIX?"

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
Step 4: Create & Update (YOU run the GraphQL script)
```

---

## Multi-App Parallelism

When the user provides **more than one application** in a single request (e.g. "Create applications for Slack, Notion, and Figma"), **DO NOT process them sequentially**. Instead:

1. **Immediately spawn one subagent per application** using the Task tool — all in the same message:

```
For each app in [App1, App2, App3]:
  Task(
    subagent_type="general-purpose",
    description="Create LeanIX application for {App}",
    prompt="Read the SKILL.md at /Users/I756819/.claude/plugins/cache/leanix-catalog-research-marketplace/create-application/1.0.0/skills/create-application/skill/SKILL.md and execute the full 4-step workflow to create a LeanIX Application fact sheet for: {App}"
  )
```

2. **All subagents run in parallel** — N apps take the same time as 1 app.
3. **Collect results** from each subagent and report a combined summary.

**Single app**: Execute the 4-step workflow yourself (YOU ARE THE EXECUTOR).
**Multiple apps**: Spawn parallel subagents, one per app, all in one message.

---

## Pre-Flight Checklist

Before starting, YOU must:

1. **Verify tools are available**:
   - `mcp__perplexity-aicore__perplexity_search` — Perplexity search
   - `WebFetch` — fetch web pages
   - `LEANIX_API_TOKEN` and `LEANIX_SUBDOMAIN` set in environment (check with `echo $LEANIX_API_TOKEN`)

2. **Check if multiple apps requested** — if YES, see [Multi-App Parallelism](#multi-app-parallelism) below and spawn one subagent per app before doing anything else.

3. **Apply inline field rules** (no guideline file reads needed — rules are embedded below in each step).

**Self-Reflection**: If you're about to read guideline files or make queries sequentially, STOP — rules are inlined and research must be parallel.

---

## Step 1: Parallel Research

**YOU must execute ALL 13 queries in a SINGLE message** - this is critical for parallelism.

### Perplexity Queries (8 total)

```python
# Execute all 8 simultaneously in one message
mcp__perplexity-aicore__perplexity_search(query="[App Name] official website URL - find from authoritative sources", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="[App Name] hosting type: Is it SaaS, PaaS, or IaaS? Is it for developers, end-users, or IT teams? What cloud provider?", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="Does [App Name] support SSO (Single Sign-On)? Check for SAML, OAuth, Azure AD, Okta integration", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="[App Name] pricing model and costs - free tier, subscription, usage-based, or enterprise pricing?", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="What product category is [App Name]? Is it cloud platform, developer tool, CRM, project management, etc.?", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="[App Name] aliases, former names, abbreviations, or alternate names", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="Is [App Name] a web application or mobile app? Browser-based or native?", model="sonar")
mcp__perplexity-aicore__perplexity_search(query="[App Name] description - what does it do? Core capabilities? Factual description without marketing", model="sonar")
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

Everything is done with a **single GraphQL script** — no LeanIX MCP calls needed.
The script: creates the fact sheet, then immediately patches all fields (including description) in one operation.

**Required Environment** (already set in `~/.zshrc`):
- `LEANIX_API_TOKEN` — starts with `LXT_`
- `LEANIX_SUBDOMAIN` — e.g. `demo-eu-10`

**Fill in all `{placeholder}` values** from Step 2 verified data before running.
Leave any unknown optional fields as empty string `""` — they are filtered out automatically.

```bash
python3 << 'PYEOF'
import urllib.request, urllib.parse, json, ssl, base64, os

API_TOKEN = os.environ['LEANIX_API_TOKEN']
SUBDOMAIN = os.environ['LEANIX_SUBDOMAIN']

# ── 1. Authenticate ──────────────────────────────────────────────────────────
ctx = ssl.create_default_context()
auth_data = urllib.parse.urlencode({'grant_type': 'client_credentials'}).encode()
credentials = base64.b64encode(f'apitoken:{API_TOKEN}'.encode()).decode()
with urllib.request.urlopen(urllib.request.Request(
    f'https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token',
    data=auth_data,
    headers={'Authorization': f'Basic {credentials}', 'Content-Type': 'application/x-www-form-urlencoded'}
), context=ctx) as r:
    bearer = json.loads(r.read())['access_token']

def gql(query, variables=None):
    payload = json.dumps({'query': query, 'variables': variables or {}}).encode()
    with urllib.request.urlopen(urllib.request.Request(
        f'https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql',
        data=payload,
        headers={'Authorization': f'Bearer {bearer}', 'Content-Type': 'application/json'}
    ), context=ctx) as r:
        return json.loads(r.read())

# ── 2. Create fact sheet ─────────────────────────────────────────────────────
APP_NAME = "{appName}"

create_result = gql('''
mutation createFS($input: BaseFactSheetInput!, $patches: [Patch]) {
  createFactSheet(input: $input, patches: $patches) {
    factSheet { id name }
  }
}''', {
    'input': {'name': APP_NAME, 'type': 'Application'},
    'patches': []
})

if 'errors' in create_result:
    # Fact sheet may already exist — look it up
    print(f"Create error (may already exist): {create_result['errors'][0]['message']}")
    search_result = gql('''
    { allFactSheets(filter: {facetFilters: [{facetKey: "FactSheetTypes", keys: ["Application"]}], fullTextSearch: "%s"}) {
        edges { node { id name } }
    }}''' % APP_NAME)
    matches = [e['node'] for e in search_result['data']['allFactSheets']['edges']
               if e['node']['name'].lower() == APP_NAME.lower()]
    if not matches:
        print("ERROR: Could not find or create fact sheet. Aborting.")
        exit(1)
    fact_sheet_id = matches[0]['id']
    print(f"Found existing fact sheet: {fact_sheet_id}")
else:
    fact_sheet_id = create_result['data']['createFactSheet']['factSheet']['id']
    print(f"✓ Created fact sheet: {APP_NAME} ({fact_sheet_id})")

# ── 3. Build patches (all fields in one mutation) ────────────────────────────
fields = {
    '/description':       "{description}",
    '/webpageUrl':        "{webpageUrl}",
    '/hostingType':       "{hostingType}",
    '/hostingDescription':"{hostingDescription}",
    '/ssoStatus':         "{ssoStatus}",
    '/pricingUrl':        "{pricingUrl}",
    '/pricingType':       "{pricingType}",
    '/productCategory':   "{productCategory}",
    '/collectionStatus':  "inReview",
    '/deprecated':        "No",
    '/asOfDate':          "{asOfDate}",
}
patches = [{'op': 'replace', 'path': k, 'value': v} for k, v in fields.items() if v]

# ── 4. Apply all patches in one call ─────────────────────────────────────────
update_result = gql('''
mutation updateFS($id: ID!, $patches: [Patch]!) {
  updateFactSheet(id: $id, patches: $patches, validateOnly: false) {
    factSheet { id name
      ... on Application {
        description webpageUrl hostingType pricingType
        productCategory collectionStatus asOfDate
      }
    }
  }
}''', {'id': fact_sheet_id, 'patches': patches})

if 'errors' in update_result:
    print('UPDATE ERRORS:', json.dumps(update_result['errors'], indent=2))
else:
    fs = update_result['data']['updateFactSheet']['factSheet']
    print(f"✓ All fields updated: {fs['name']} ({fs['id']})")
    print(f"  hostingType    : {fs.get('hostingType')}")
    print(f"  pricingType    : {fs.get('pricingType')}")
    print(f"  productCategory: {fs.get('productCategory')}")
    print(f"  collectionStatus: {fs.get('collectionStatus')}")
    print(f"  asOfDate       : {fs.get('asOfDate')}")
    print(f"  LeanIX URL     : https://{SUBDOMAIN}.leanix.net/factsheet/Application/{fs['id']}")
PYEOF
```

### 4.2: Report Success

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

Action: Source ~/.zshrc first:
  source ~/.zshrc
  python3 << 'PYEOF' ...

If still missing, ask user for token (starts with 'LXT_').
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

**Reference**: ../guidelines/Application_Product_Category_Guidelines.md (top 50 categories listed)

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
