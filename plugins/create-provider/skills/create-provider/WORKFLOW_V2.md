# Provider Auto-Creation Workflow V2
## Parallel Research + Agent Verification

## ⚠️ AGENT PRE-FLIGHT CHECKLIST ⚠️

**Before proceeding with Provider creation, verify you have:**

- [ ] Read this complete WORKFLOW_V2.md document
- [ ] Read all 5 guidelines in `guidelines/` directory:
  - [ ] Provider_Classification_Definitions.md
  - [ ] Provider_URL_Validation_Guidelines.md
  - [ ] Provider_Headquarters_Address_Guidelines.md
  - [ ] Provider_Alias_Discovery_Guidelines.md
  - [ ] Provider_Description_Guidelines.md
- [ ] Confirmed Perplexity MCP is available (mcp__perplexity__perplexity_search)
- [ ] Confirmed WebFetch tool is available
- [ ] Confirmed LeanIX MCP is available (mcp__LeanIX_MCP_Server_Remote__)
- [ ] Located `lib/provider_researcher.py` module
- [ ] Located `lib/parallel_researcher.py` module
- [ ] Located `lib/verification_agent.py` module

**If ANY checkbox is unchecked, STOP and read documentation first.**

**Self-Reflection Question:**
If you're about to make ad-hoc Perplexity calls or skip parallel research, ask yourself:
*"Why am I not following the documented workflow? What step did I skip?"*

Then: Go back, read the documentation, and start from Step 1.

---

### Architecture Overview

```
User Input: "Create Provider for TeamSmart AI"
    ↓
┌─────────────────────────────────────┐
│  Step 1: Parallel Research          │
│  (Run simultaneously)                │
├─────────────────────────────────────┤
│  ├─ Perplexity MCP                  │
│  │   ├─ URL research query          │
│  │   ├─ Category classification     │
│  │   ├─ Aliases discovery           │
│  │   ├─ Headquarters research       │
│  │   └─ Description generation      │
│  │                                   │
│  └─ WebFetch                         │
│      ├─ Homepage scrape              │
│      ├─ /about page scrape           │
│      └─ /contact page scrape         │
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

Query 2 (Category):
- Apply decision tree (Individual → Enterprise → Community)
- Find indicators
- Classify with reasoning
Result: {category, reasoning, confidence, evidence}

Query 3 (Aliases):
- Search 7 alias types
- Verify from official sources
- Check for rebrands/acquisitions
Result: {aliases_list, sources, confidence}

Query 4 (Headquarters):
- Search official website first
- Check business registries
- Accept partial data
Result: {address, address_level, confidence, source}

Query 5 (Description):
- Extract from official website
- 30-90 words
- Factual and objective
Result: {description, word_count, source}
```

#### 1B. WebFetch Research
```
Fetch 1: Homepage (/)
- Extract company name
- Get description
- Find location indicators
- Identify company type
Result: {name, description, type_indicators, location}

Fetch 2: About Page (/about)
- Company history
- Founders/team
- Headquarters
- Former names
Result: {history, founders, address, aliases}

Fetch 3: Contact Page (/contact)
- Physical address
- City, state, country
- Contact info
Result: {address, city, country, email, phone}
```

**Output of Step 1**:
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
  },
  "metadata": {
    "provider_name": "TeamSmart AI",
    "sources_used": ["perplexity", "webfetch"],
    "research_timestamp": "2026-02-18T..."
  }
}
```

---

### Step 2: Agent Verification

**Agent Task**: Compare both sources and resolve conflicts

**For Each Field**:

#### 2.1 Homepage URL
```
Perplexity says: https://teamsmart.ai/
WebFetch says: https://teamsmart.ai/

✓ MATCH - Use this value
Confidence: HIGH
Source: Both sources agree
```

#### 2.2 Provider Category
```
Perplexity says: enterprise (reasoning: business solutions, pricing, enterprise features)
WebFetch says: enterprise (indicators: professional services, business focus)

✓ MATCH - Use "enterprise"
Confidence: HIGH
Source: Both sources agree
```

#### 2.3 Aliases
```
Perplexity says: TeamSmart.ai, TeamSmart
WebFetch says: (none found on website)

⚠ PARTIAL CONFLICT
Agent action: Verify "TeamSmart.ai" vs "TeamSmart AI" are stylistic variations
Result: Use "TeamSmart.ai" (verified from sources)
Confidence: MEDIUM
Source: Perplexity with verification
```

#### 2.4 Headquarters
```
Perplexity says: San Francisco, CA, United States (city-level)
WebFetch says: San Francisco, CA, United States (from contact page)

✓ MATCH - Use this value
Confidence: HIGH
Source: Both sources agree, verified from official website
```

#### 2.5 Description
```
Perplexity says: "TeamSmart.ai provides AI agents..." (54 words)
WebFetch says: "TeamSmart.ai provides intelligent AI agents..." (44 words)

⚠ MINOR CONFLICT - Both are valid but slightly different
Agent action:
  1. Compare which is more accurate to official website
  2. Check for marketing buzzwords (seamless, transform, enhance, streamline, etc.)
  3. Remove marketing language if present
Result: Rewrite to remove "transforms", "seamless integration", "enhance productivity"
Final: "TeamSmart AI provides a platform for accessing multiple AI models..."
Confidence: HIGH
Source: Official website (WebFetch), rewritten for objectivity
```

**Resolution Rules**:
1. **Both agree** → Use agreed value, check for marketing language, HIGH confidence
2. **One has data, other doesn't** → Use available data, check for marketing language, MEDIUM confidence
3. **Both differ** → Run verification query, choose most reliable, remove marketing language
4. **Both fail** → Mark as "Not Found", ask user

**Marketing Language Check** (applies to all descriptions):
- Detect buzzwords: "seamless", "transform", "enhance", "streamline", "empower", "revolutionary", "cutting-edge", "enterprise-grade", "leading", "innovative", "powerful"
- Rewrite to factual statements: "integrates with" instead of "seamless integration", "automates" instead of "transforms", remove qualifiers like "enterprise-grade"
- Goal: Pure factual description of what the provider does, not marketing claims about benefits

**Output of Step 2**:
```json
{
  "verified_data": {
    "homePageUrl": {
      "value": "https://teamsmart.ai/",
      "confidence": "high",
      "source": "both_agree",
      "conflicts": []
    },
    "providerCategory": {
      "value": "enterprise",
      "confidence": "high",
      "source": "both_agree",
      "reasoning": "Commercial company with business solutions..."
    },
    "aliases": {
      "value": "TeamSmart.ai",
      "confidence": "medium",
      "source": "perplexity_verified",
      "conflicts": ["webfetch_found_none"]
    },
    "headquartersAddress": {
      "value": "San Francisco, CA, United States",
      "confidence": "high",
      "source": "both_agree_official_website",
      "address_level": "city"
    },
    "description": {
      "value": "TeamSmart.ai provides intelligent AI agents...",
      "confidence": "high",
      "source": "webfetch_official_website",
      "word_count": 44
    }
  },
  "verification_metadata": {
    "overall_confidence": 0.88,
    "conflicts_resolved": 2,
    "conflicts_unresolved": 0,
    "fields_with_high_confidence": 4,
    "fields_with_medium_confidence": 1
  }
}
```

---

### Step 3: Quality Check

**Criteria**:
- ✅ Overall confidence > 70%? (88% ✓)
- ✅ Critical fields present? (URL, Category ✓)
- ✅ No unresolved conflicts? (0 ✓)
- ✅ Description word count valid? (44 words ✓)

**Decision**: PASS - Proceed to save

If any check fails:
```
⚠ Quality check failed:
- Overall confidence: 62% (below 70%)
- Missing field: headquarters address

Options:
1. Save with partial data
2. Manual input for missing fields
3. Cancel operation

Choose [1/2/3]:
```

---

### Step 4: Create & Update

```python
# 4.1 Create fact sheet
fact_sheet_id = create_fact_sheet_via_leanix_mcp(
    name="TeamSmart AI",
    type="Provider"
)

# 4.2 Update custom fields via Python CLI
update_custom_fields(
    fact_sheet_id=fact_sheet_id,
    fields={
        "homePageUrl": "https://teamsmart.ai/",
        "providerCategory": "enterprise",
        "aliases": "TeamSmart.ai",
        "headquartersAddress": "San Francisco, CA, United States",
        "description": "TeamSmart.ai provides...",
        "collectionStatus": "inReview",
        "asOfDate": "2026-02-18",
        "deprecated": "no"
    }
)

# 4.3 Return URL
return f"https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/{fact_sheet_id}"
```

**Output**:
```
✓ Provider created successfully!

Provider: TeamSmart AI
Overall Confidence: 88% (HIGH)

Verified Data:
├─ Homepage URL: https://teamsmart.ai/ ✓✓ (both sources)
├─ Category: enterprise ✓✓ (both sources)
├─ Aliases: TeamSmart.ai ✓ (perplexity verified)
├─ Headquarters: San Francisco, CA, US ✓✓ (both sources)
└─ Description: 44 words ✓✓ (official website)

Conflicts Resolved: 2
- Aliases: Used Perplexity (WebFetch found none)
- Description: Used WebFetch (more accurate to website)

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/833c25ce-fe4a-4288-bcff-07bb8cfc9dc2
```

---

## Advantages of V2 Workflow

### 1. Speed
- **V1**: Sequential (10-15 seconds per field × 5 = 50-75 seconds)
- **V2**: Parallel (all fields at once = 5-10 seconds)
- **Speedup**: 5-7x faster

### 2. Accuracy
- **V1**: Single source, no validation
- **V2**: Dual sources with cross-verification
- **Improvement**: Catches hallucinations, validates data

### 3. Reliability
- **V1**: Fails if one source fails
- **V2**: Fallback to working source
- **Improvement**: More resilient to source failures

### 4. Transparency
- **V1**: No visibility into data quality
- **V2**: Confidence scores per field
- **Improvement**: User knows data reliability

### 5. Conflict Resolution
- **V1**: Uses first result
- **V2**: Agent resolves conflicts intelligently
- **Improvement**: Better data quality decisions

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
User prompt: "Unable to research [Provider]. Please provide data manually or try again later."
```

### Scenario 4: Sources Conflict (No Resolution)
```
⚠ Perplexity: Category = "individual"
⚠ WebFetch: Category = "enterprise"

Agent action: Run verification query to Perplexity
If still unclear: Ask user to choose
```

---

## Implementation Notes

**For Claude Code Agent**:
1. Read this workflow document
2. Use ParallelResearcher to coordinate research
3. Use VerificationAgent to compare results
4. Execute verification queries via Perplexity when conflicts arise
5. Present results with confidence scores
6. Proceed with high-confidence data automatically
7. Ask user for low-confidence or missing fields

**Files Created**:
- `lib/parallel_researcher.py` - Parallel research coordinator
- `lib/verification_agent.py` - Verification and conflict resolution
- This workflow document

**Next Step**: Test with real provider to validate workflow
