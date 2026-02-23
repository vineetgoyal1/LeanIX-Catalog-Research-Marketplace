# Application Auto-Creation Workflow
## Parallel Research + Agent Verification

## ⚠️ AGENT PRE-FLIGHT CHECKLIST ⚠️

**Before proceeding with Application creation, verify you have:**

- [ ] Read this complete WORKFLOW.md document
- [ ] Read all 11 guidelines in `guidelines/` directory:
  - [ ] Application_Description_Guidelines.md
  - [ ] Application_Webpage_URL_Guidelines.md
  - [ ] Application_Hosting_Type_Guidelines.md (includes hostingDescription)
  - [ ] Application_SSO_Status_Guidelines.md
  - [ ] Application_Pricing_Guidelines.md
  - [ ] Application_Product_Category_Guidelines.md
  - [ ] Application_Alias_Guidelines.md
  - [ ] Application_Subtype_Guidelines.md
  - [ ] Application_SI_ID_Implementation.md
  - [ ] Application_As_Of_Date_Guidelines.md
  - [ ] Application_Collection_Status_and_Deprecated_Guidelines.md
- [ ] Confirmed Perplexity MCP is available (mcp__perplexity__perplexity_search)
- [ ] Confirmed WebFetch tool is available
- [ ] Confirmed LeanIX MCP is available (mcp__LeanIX_MCP_Server_Remote__)

**If ANY checkbox is unchecked, STOP and read documentation first.**

**Self-Reflection Question:**
If you're about to make ad-hoc Perplexity calls or skip parallel research, ask yourself:
*"Why am I not following the documented workflow? What step did I skip?"*

Then: Go back, read the documentation, and start from Step 1.

---

### Architecture Overview

```
User Input: "Create Application for Smartsheet"
    ↓
┌─────────────────────────────────────┐
│  Step 1: Parallel Research          │
│  (Run simultaneously)                │
├─────────────────────────────────────┤
│  ├─ Perplexity MCP                  │
│  │   ├─ URL research query          │
│  │   ├─ Hosting type research       │
│  │   ├─ SSO status research         │
│  │   ├─ Pricing type research       │
│  │   ├─ Product category research   │
│  │   ├─ Aliases discovery           │
│  │   ├─ Subtype identification      │
│  │   └─ Description generation      │
│  │                                   │
│  └─ WebFetch                         │
│      ├─ Homepage scrape              │
│      ├─ /security or /features      │
│      ├─ /pricing page scrape         │
│      ├─ /about page scrape           │
│      └─ /changelog or /updates      │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Step 2: Agent Verification         │
│  (Subagent analyzes both sources)   │
├─────────────────────────────────────┤
│  For each field:                     │
│  ├─ Compare Perplexity vs WebFetch  │
│  ├─ Identify conflicts               │
│  ├─ Apply resolution rules           │
│  ├─ Cross-check with additional     │
│  │   Perplexity query if needed     │
│  └─ Choose most reliable value       │
│                                      │
│  Output: Verified data + confidence │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Step 3: Quality Check              │
├─────────────────────────────────────┤
│  ├─ Overall confidence > 70%?       │
│  ├─ Critical fields present?        │
│  ├─ Any unresolved conflicts?       │
│  └─ User approval if low confidence │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Step 4: Create & Update            │
├─────────────────────────────────────┤
│  ├─ Create fact sheet (LeanIX MCP)  │
│  ├─ Update fields (Python CLI)      │
│  └─ Return URL                       │
└─────────────────────────────────────┘
```

---

## Detailed Workflow

### Step 1: Parallel Research

**Duration**: ~5-10 seconds (both run at same time)

#### 1A. Perplexity Research

```
Query 1 (URL):
- Search for official website
- Validate HTTP status
- Check SSL certificate
- Find in 2+ authoritative sources
Result: {url, confidence, sources, status_code}

Query 2 (Hosting Type + Description):
- Determine: saas/paas/iaas/onPremise/hybrid/mobile
- Check security pages for cloud provider
- Check product updates/changelog for hosting mentions
- Apply decision tree (check name first, then primary user)
Result: {hostingType, hostingDescription, confidence, reasoning}

Query 3 (SSO Status):
- Search security/enterprise pages for SSO
- Check product changelog for SSO announcements
- Look for SAML/OAuth mentions
- Search integration directories (Okta, Azure AD)
Result: {ssoStatus, confidence, source, changelog_date}

Query 4 (Pricing Type):
- Identify: free/freemium/subscription/perpetual/transaction/enterprise
- Check pricing page
- Verify pricing model from multiple sources
Result: {pricingType, confidence, source}

Query 5 (Product Category):
- Map to predefined categories
- Use category reference (377KB JSON)
- Match based on functionality
Result: {productCategory, confidence, reasoning}

Query 6 (Aliases):
- Search for alternate names/abbreviations
- Check for former names, acquisitions
- Verify from official sources
Result: {aliases_list, sources, confidence}

Query 7 (Subtype):
- Determine: application/mobileApp
- Check if mobile-native or web-based
Result: {subtype, confidence}

Query 8 (Description):
- Extract from official website
- 30-90 words
- Factual and objective
- Remove marketing language
Result: {description, word_count, source}
```

#### 1B. WebFetch Research

```
Fetch 1: Homepage (/)
- Extract application name
- Get description
- Identify application type
- Find hosting indicators
Result: {name, description, type_indicators}

Fetch 2: Security/Features Page (/security, /features, /enterprise)
- SSO support mentions
- Hosting infrastructure
- Enterprise features
- Authentication methods
Result: {sso_info, hosting_info, enterprise_features}

Fetch 3: Pricing Page (/pricing)
- Pricing tiers
- Free vs paid plans
- SSO availability by plan
- Feature comparison
Result: {pricing_model, plans, features_by_plan}

Fetch 4: About Page (/about)
- Company background
- Application history
- Former names/rebrands
Result: {history, aliases, background}

Fetch 5: Changelog (/changelog, /updates, /whats-new)
- SSO feature announcements
- Major feature releases
- Hosting updates
Result: {sso_announcement, feature_releases, dates}
```

**Output of Step 1**:
```json
{
  "perplexity": {
    "url": {...},
    "hosting": {...},
    "sso": {...},
    "pricing": {...},
    "category": {...},
    "aliases": {...},
    "subtype": {...},
    "description": {...}
  },
  "webfetch": {
    "homepage": {...},
    "security": {...},
    "pricing": {...},
    "about": {...},
    "changelog": {...}
  },
  "metadata": {
    "application_name": "Smartsheet",
    "sources_used": ["perplexity", "webfetch"],
    "research_timestamp": "2026-02-22T..."
  }
}
```

---

### Step 2: Agent Verification

**Agent Task**: Compare both sources and resolve conflicts

**For Each Field**:

#### 2.1 Webpage URL
```
Perplexity says: https://www.smartsheet.com/
WebFetch says: https://www.smartsheet.com/

✓ MATCH - Use this value
Confidence: HIGH
Source: Both sources agree
```

#### 2.2 Hosting Type
```
Perplexity says: saas (reasoning: end-user collaboration tool, hosted on AWS)
WebFetch says: saas (security page mentions cloud infrastructure)

✓ MATCH - Use "saas"
Confidence: HIGH
Source: Both sources agree

hostingDescription: "Classified as SaaS: end-user collaboration application hosted on AWS with multi-site data redundancy"
```

#### 2.3 SSO Status
```
Perplexity says: supported (found in enterprise features)
WebFetch says: supported (mentioned on security page)
Changelog says: (SSO added in 2019, Enterprise Grid launch)

✓ MATCH - Use "supported"
Confidence: HIGH
Source: Both sources + changelog confirmation
```

#### 2.4 Pricing Type
```
Perplexity says: freemium (free plan + paid plans)
WebFetch says: freemium (pricing page shows free tier + Pro/Business/Enterprise)

✓ MATCH - Use "freemium"
Confidence: HIGH
Source: Both sources agree, verified from pricing page
```

#### 2.5 Product Category
```
Perplexity says: Collaboration (matches "collaboration and work management")
WebFetch says: Project Management (homepage emphasizes project tracking)

⚠ CONFLICT - Both are valid but different categories
Agent action:
  1. Check Product_Category_Reference.json for hierarchy
  2. "Project Management" is more specific than "Collaboration"
  3. Use more specific category
Result: Use "Project Management"
Confidence: HIGH
Source: WebFetch homepage, verified against category reference
```

#### 2.6 Aliases
```
Perplexity says: None found
WebFetch says: None found (no former names or rebrands)

✓ MATCH - No aliases
Confidence: HIGH
Source: Both sources agree
Action: Leave alias field empty
```

#### 2.7 Subtype
```
Perplexity says: application (web-based SaaS)
WebFetch says: application (browser-based, not mobile-native)

✓ MATCH - Use "application"
Confidence: HIGH
Source: Both sources agree
```

#### 2.8 Description
```
Perplexity says: "Smartsheet provides an online application for collaboration and work management..." (41 words)
WebFetch says: "Smartsheet is the leading platform that empowers teams to transform work..." (38 words, marketing language)

⚠ CONFLICT - WebFetch has marketing language
Agent action:
  1. Identify marketing buzzwords: "leading", "empowers", "transform"
  2. Use Perplexity version (more factual)
  3. Verify against guidelines (30-90 words, factual)
Result: Use Perplexity version
Confidence: HIGH
Source: Perplexity, factual and objective
```

**Resolution Rules**:
1. **Both agree** → Use agreed value, check for marketing language, HIGH confidence
2. **One has data, other doesn't** → Use available data, check for marketing language, MEDIUM confidence
3. **Both differ** → Apply field-specific guidelines, run verification query if needed, remove marketing language
4. **Both fail** → Mark as "Not Found", leave blank or use default (collectionStatus, deprecated, asOfDate)

**Marketing Language Check** (applies to descriptions):
- Detect buzzwords: "leading", "powerful", "innovative", "cutting-edge", "revolutionary", "seamless", "transform", "empower", "enterprise-grade"
- Rewrite to factual: "provides" instead of "empowers", "integrates" instead of "seamless integration"
- Focus on WHAT the application does, not marketing claims

**Output of Step 2**:
```json
{
  "verified_data": {
    "webpageUrl": {
      "value": "https://www.smartsheet.com/",
      "confidence": "high",
      "source": "both_agree"
    },
    "hostingType": {
      "value": "saas",
      "confidence": "high",
      "source": "both_agree",
      "reasoning": "End-user collaboration tool hosted on cloud"
    },
    "hostingDescription": {
      "value": "Classified as SaaS: end-user collaboration application hosted on AWS with multi-site data redundancy",
      "confidence": "high",
      "source": "webfetch_security_page"
    },
    "ssoStatus": {
      "value": "supported",
      "confidence": "high",
      "source": "both_agree_plus_changelog"
    },
    "pricingType": {
      "value": "freemium",
      "confidence": "high",
      "source": "both_agree_pricing_page"
    },
    "productCategory": {
      "value": "Project Management",
      "confidence": "high",
      "source": "webfetch_homepage",
      "note": "More specific than Collaboration"
    },
    "alias": {
      "value": "",
      "confidence": "high",
      "source": "both_agree_none_found"
    },
    "type": {
      "value": "application",
      "confidence": "high",
      "source": "both_agree"
    },
    "description": {
      "value": "Smartsheet provides an online application for collaboration and work management...",
      "confidence": "high",
      "source": "perplexity_factual",
      "word_count": 41
    },
    "collectionStatus": {
      "value": "inReview",
      "confidence": "high",
      "source": "fixed_value"
    },
    "deprecated": {
      "value": "no",
      "confidence": "high",
      "source": "fixed_value"
    },
    "asOfDate": {
      "value": "2026-02-22",
      "confidence": "high",
      "source": "current_date"
    }
  },
  "verification_metadata": {
    "overall_confidence": 0.95,
    "conflicts_resolved": 2,
    "conflicts_unresolved": 0,
    "fields_with_high_confidence": 11,
    "fields_with_medium_confidence": 0
  }
}
```

---

### Step 3: Quality Check

**MANDATORY: Run Validation Script First**

Before proceeding to Step 4, you MUST run the validation script to ensure all workflow requirements are met:

```bash
cd create-application
python lib/validate_application.py \
  --checklist ./executions/[App_Name]/EXECUTION_CHECKLIST.md \
  --fields ./executions/[App_Name]/final_fields.json
```

**Validation Script Checks**:
- ✅ Hosting type evaluation matrix completed (all 6 types scored)
- ✅ Description 30-90 words
- ✅ No marketing buzzwords in description
- ✅ category = "businessApplication"
- ✅ deprecated = "No" (capital N)
- ✅ collectionStatus = "inReview"
- ✅ SI ID generated
- ✅ Overall confidence > 70%
- ✅ SSO research exhaustive (5+ sources checked)
- ✅ Critical fields present (webpageUrl, description, hostingType)

**IF VALIDATION FAILS → FIX ISSUES BEFORE PROCEEDING TO STEP 4**

---

**Manual Quality Criteria** (in addition to validation script):
- ✅ Overall confidence > 70%? (95% ✓)
- ✅ Critical fields present? (webpageUrl, description, hostingType ✓)
- ✅ No unresolved conflicts? (0 ✓)
- ✅ Description word count valid? (41 words, within 30-90 range ✓)
- ✅ Fixed fields set? (collectionStatus, deprecated, asOfDate ✓)
- ✅ Hosting matrix completed? (all 6 types scored ✓)

**Decision**: PASS - Proceed to Step 4

If any check fails:
```
⚠ Quality check failed:
- Overall confidence: 62% (below 70%)
- Missing field: SSO status
- Hosting matrix incomplete

Options:
1. Fix issues and re-run validation
2. Save with partial data (not recommended)
3. Manual input for missing fields
4. Cancel operation

Choose [1/2/3/4]:
```

---

### Step 4: Create & Update

```python
# 4.1 Create fact sheet
fact_sheet_id = create_fact_sheet_via_leanix_mcp(
    name="Smartsheet",
    type="Application"
)

# 4.2 Update custom fields via Python CLI
update_custom_fields(
    fact_sheet_id=fact_sheet_id,
    fields={
        "siId": "Smartsheet",
        "webpageUrl": "https://www.smartsheet.com/",
        "description": "Smartsheet provides an online application for collaboration...",
        "hostingType": "saas",
        "hostingDescription": "Classified as SaaS: end-user collaboration application...",
        "ssoStatus": "supported",
        "pricingType": "freemium",
        "productCategory": "Project Management",
        "alias": "",
        "category": "businessApplication",
        "collectionStatus": "inReview",
        "deprecated": "No",
        "asOfDate": "2026-02-22"
    }
)

# ACTUAL COMMAND TO RUN:
# Export environment variables and execute Python CLI
export LEANIX_API_TOKEN='LXT_...' && \
export LEANIX_SUBDOMAIN='demo-eu-10' && \
cd "../../create-provider" && \
python main.py update \
    --fact-sheet-id "{fact_sheet_id}" \
    --type Application \
    --fields '{
        "siId": "Smartsheet",
        "webpageUrl": "https://www.smartsheet.com/",
        "description": "Smartsheet provides...",
        "hostingType": "saas",
        "hostingDescription": "Classified as SaaS...",
        "ssoStatus": "supported",
        "pricingType": "freemium",
        "productCategory": "Project Management",
        "alias": "",
        "category": "businessApplication",
        "collectionStatus": "inReview",
        "deprecated": "No",
        "asOfDate": "2026-02-22"
    }'

# ALTERNATIVE: Save fields to JSON file first (recommended for complex data)
cat > /tmp/app_fields.json << EOF
{
  "siId": "Smartsheet",
  "webpageUrl": "https://www.smartsheet.com/",
  "description": "Smartsheet provides...",
  "hostingType": "saas",
  "hostingDescription": "Classified as SaaS...",
  "ssoStatus": "supported",
  "pricingType": "freemium",
  "productCategory": "Project Management",
  "alias": "",
  "category": "businessApplication",
  "collectionStatus": "inReview",
  "deprecated": "No",
  "asOfDate": "2026-02-22"
}
EOF

export LEANIX_API_TOKEN='LXT_...' && \
export LEANIX_SUBDOMAIN='demo-eu-10' && \
cd "../../create-provider" && \
python main.py update \
    --fact-sheet-id "{fact_sheet_id}" \
    --type Application \
    --fields "$(cat /tmp/app_fields.json)"

# 4.3 Return URL
return f"https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/{fact_sheet_id}"
```

**Output**:
```
✓ Application created successfully!

Application: Smartsheet
Overall Confidence: 95% (HIGH)

Verified Data:
├─ Webpage URL: https://www.smartsheet.com/ ✓✓ (both sources)
├─ Hosting Type: saas ✓✓ (both sources)
├─ SSO Status: supported ✓✓✓ (both + changelog)
├─ Pricing Type: freemium ✓✓ (both sources)
├─ Product Category: Project Management ✓ (webfetch)
├─ Aliases: (none found) ✓✓
├─ Subtype: application ✓✓ (both sources)
└─ Description: 41 words ✓✓ (perplexity, factual)

Conflicts Resolved: 2
- Product Category: Used "Project Management" (more specific than Collaboration)
- Description: Used Perplexity (WebFetch had marketing language)

Fixed Fields Set:
├─ Collection Status: inReview ✓
├─ Deprecated: no ✓
└─ As-of Date: 2026-02-22 ✓

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/abc-123-def
```

---

## Field-Specific Research Strategies

### Hosting Type (Critical Field)
**Priority research locations:**
1. Security page (/security) - often mentions cloud provider
2. Enterprise page (/enterprise) - hosting infrastructure details
3. Changelog (/changelog) - hosting announcements
4. Name check - "mobile app", "Desktop", "Private Edition" keywords

**Decision tree:**
1. Check name for obvious indicators (mobile app, Desktop, etc.)
2. Identify primary user (business users → saas, developers → paas, IT teams → iaas)
3. For cloud services (AWS/Azure/GCP), use specific classification tree
4. Complete evaluation matrix if ambiguous

### SSO Status (Enterprise Feature)
**Priority research locations:**
1. Security page (/security) - explicit SSO mentions
2. Enterprise page (/enterprise) - enterprise features list
3. **Changelog (/changelog, /updates)** - SSO announcements ⭐
4. Pricing page (/pricing) - SSO as paid feature
5. Integration directories (Okta, Azure AD)

**Research strategy:**
- Always check changelog first (SSO often announced as milestone)
- Look for "SAML", "OAuth", "SSO", "single sign-on"
- Verify from multiple sources if found
- Leave blank if no clear evidence (don't guess)

### Pricing Type
**Priority research locations:**
1. Pricing page (/pricing) - primary source
2. Homepage - may mention "free" or "get started"
3. About/company page - pricing model description

**Common patterns:**
- Free tier + paid plans = freemium
- Multiple subscription tiers = subscription
- Enterprise contact = enterprise
- Per-transaction = transaction
- One-time purchase = perpetual

### Product Category
**Source:** Product_Category_Reference.json (377KB, 50+ categories)
**Strategy:**
1. Identify application functionality from description
2. Match to category from reference JSON
3. Use most specific category (Project Management > Collaboration)
4. Verify against category definitions

---

## Advantages of Workflow

### 1. Speed
- **Sequential**: 10-15 seconds per field × 8 = 80-120 seconds
- **Parallel**: All fields at once = 5-10 seconds
- **Speedup**: 8-12x faster

### 2. Accuracy
- Dual sources with cross-verification
- Catches hallucinations
- Validates data quality

### 3. Field-Specific Expertise
- Each field has dedicated guideline
- Hosting type uses evaluation matrix
- SSO checks changelog (unique to applications)
- Pricing verified from pricing page

### 4. Marketing Language Removal
- Automatic detection of buzzwords
- Rewrite to factual statements
- Maintains objectivity

### 5. Confidence Tracking
- Per-field confidence scores
- Overall confidence calculation
- Transparent data quality

---

## Error Handling

### Scenario 1: Perplexity Fails, WebFetch Works
```
✓ WebFetch: Successfully scraped website
✗ Perplexity: MCP connection failed

Agent action: Use WebFetch data only
Confidence: Downgraded to MEDIUM (single source)
Proceed: YES (sufficient data from official website)
```

### Scenario 2: WebFetch Fails, Perplexity Works
```
✗ WebFetch: Website blocking/timeout
✓ Perplexity: Got results with citations

Agent action: Use Perplexity data only
Confidence: MEDIUM to HIGH (depends on citation quality)
Proceed: YES (Perplexity provides authoritative sources)
```

### Scenario 3: Both Fail
```
✗ Perplexity: MCP error
✗ WebFetch: Website not accessible

Agent action: Cannot proceed
User prompt: "Unable to research [Application]. Please provide data manually or try again later."
```

### Scenario 4: SSO Status Unclear
```
⚠ No clear SSO evidence found
⚠ Not explicitly stated as "not supported"

Agent action: Leave ssoStatus blank (better than guessing)
Note: "Blank is acceptable when information is unavailable"
```

### Scenario 5: Hosting Type Ambiguous
```
⚠ Description says "platform" but unclear if for developers or end users
⚠ Perplexity and WebFetch give different signals

Agent action:
1. Complete evaluation matrix for all 6 hosting types
2. Apply primary user test
3. Run verification query if still unclear
4. Use web search (mandatory for confidence < 85%)
```

---

## Implementation Notes

**For Claude Code Agent**:
1. Read this workflow document
2. Read all 11 guidelines in `guidelines/` directory
3. Use parallel research (Perplexity + WebFetch) simultaneously
4. Use verification agent to compare and resolve conflicts
5. Execute verification queries via Perplexity when conflicts arise
6. **Always check changelog for SSO announcements** (unique to applications)
7. **Complete hosting type evaluation matrix** if uncertain
8. Present results with confidence scores
9. Proceed with high-confidence data automatically
10. Ask user for low-confidence or missing fields

**Fixed Values** (no research needed):
- `collectionStatus`: Always "inReview"
- `deprecated`: Always "no"
- `asOfDate`: Always current date (YYYY-MM-DD)

