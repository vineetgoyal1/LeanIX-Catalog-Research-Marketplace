# Application Creation Checklist
## Agent must complete this file before proceeding to fact sheet creation

**Application Name**: _____________________
**Date**: _____________________
**Agent ID**: _____________________

---

## Pre-Flight Verification

- [ ] Read WORKFLOW.md completely (all 661 lines)
- [ ] Read all 11 guidelines in guidelines/ directory:
  - [ ] Application_Description_Guidelines.md
  - [ ] Application_Webpage_URL_Guidelines.md
  - [ ] Application_Hosting_Type_Guidelines.md
  - [ ] Application_SSO_Status_Guidelines.md
  - [ ] Application_Pricing_Guidelines.md
  - [ ] Application_Product_Category_Guidelines.md
  - [ ] Application_Alias_Guidelines.md
  - [ ] Application_Subtype_Guidelines.md
  - [ ] Application_SI_ID_Implementation.md
  - [ ] Application_As_Of_Date_Guidelines.md
  - [ ] Application_Collection_Status_and_Deprecated_Guidelines.md
- [ ] Verified Perplexity MCP available (mcp__perplexity__perplexity_search)
- [ ] Verified WebFetch tool available
- [ ] Verified LeanIX MCP available (mcp__LeanIX_MCP_Server_Remote__)

**If ANY checkbox unchecked → STOP and complete it first**

---

## Step 1: Parallel Research

### Perplexity Research
- [ ] Called Perplexity with comprehensive query (all 8 fields)
- [ ] Received response with citations
- [ ] Saved raw response to research_perplexity.json

**Perplexity Query Used**:
```
[PASTE EXACT QUERY HERE]
```

**Result**: Success / Failed (if failed, explain why and workaround used)

### WebFetch Research
- [ ] WebFetch homepage (/)
- [ ] Attempted WebFetch /security (or /features, /enterprise)
- [ ] Attempted WebFetch /pricing (or /plans)
- [ ] Attempted WebFetch /changelog (or /updates, /whats-new, /releases)
- [ ] Attempted WebFetch /about

**URLs Attempted**:
```
Homepage: [URL] - [Success/404/Error]
Security: [URL] - [Success/404/Error]
Pricing:  [URL] - [Success/404/Error]
Changelog: [URL] - [Success/404/Error]
About:     [URL] - [Success/404/Error]
```

**Data Collected**: [ ] Yes [ ] Partial [ ] No

---

## Step 2A: Hosting Type Evaluation Matrix (MANDATORY - DO NOT SKIP)

**⚠️ CRITICAL: Score ALL 6 types before making decision**

### Matrix Scoring

| Hosting Type | Score (0-10) | Reasoning |
|--------------|--------------|-----------|
| **SaaS** | ___/10 | [REQUIRED: Why this score? Check: Business users? Cloud-hosted? Multi-tenant?] |
| **PaaS** | ___/10 | [REQUIRED: Why this score? Check: For developers? Build/deploy platform? Infrastructure abstraction?] |
| **IaaS** | ___/10 | [REQUIRED: Why this score? Check: IT teams? VMs/compute? AWS/Azure/GCP type?] |
| **On-Premise** | ___/10 | [REQUIRED: Why this score? Check: Self-hosted? Customer servers? No cloud?] |
| **Hybrid** | ___/10 | [REQUIRED: Why this score? Check: Both cloud and on-premise? Customer choice?] |
| **Mobile** | ___/10 | [REQUIRED: Why this score? Check: Native app? App store? Mobile-first not web?] |

**Matrix Completed**: [ ] Yes [ ] No

**IF NO → STOP. Complete matrix above before proceeding.**

### Decision Logic Applied

**Highest Score**: _____ (which type?)

**Primary User Identified**:
- [ ] Business users (SaaS indicator)
- [ ] Developers (PaaS indicator)
- [ ] IT teams (IaaS indicator)
- [ ] Mixed/Other

**Name Check**:
- [ ] Contains "mobile app", "Desktop", "on-premise" indicators? (specify: _____)
- [ ] No special indicators in name

**If Scores Tied**:
- Tie-breaker used: _____________________
- Result: _____________________

**Final Decision**:
- **Selected Hosting Type**: _____________________
- **Confidence Level**: _____% (must be ≥70%)
- **Decision Reasoning**:
```
[REQUIRED: Explain why this type was chosen over others, referencing matrix scores and decision logic]
```

---

## Step 2B: Hosting Description

**Format Check**:
- [ ] Starts with "Classified as [type]:"
- [ ] Contains specific technical details
- [ ] NO hallucinated cloud providers (only if explicitly stated in sources)
- [ ] Confidence ≥90% for technical details (if <90%, use basic classification only)

**Hosting Description**:
```
[PASTE HOSTING DESCRIPTION HERE]
```

**Confidence in Technical Details**: _____% (must be ≥90% to include specific technical info)

---

## Step 2C: SSO Research (Exhaustive)

**URLs/Sources Attempted**:
- [ ] /changelog (or /updates, /whats-new, /releases, /blog, /news)
- [ ] /security
- [ ] /pricing (checked for SSO in plans)
- [ ] /enterprise (or /business)
- [ ] Perplexity search: "[App Name] SSO SAML OAuth"
- [ ] Integration directory search: "[App Name] Okta"
- [ ] Integration directory search: "[App Name] Azure AD"
- [ ] Integration directory search: "[App Name] Google Workspace SSO"

**Results**:
```
Changelog: [Found SSO announcement? Date? Details?]
Security page: [SSO mentioned? Details?]
Pricing: [SSO by plan? Which plans?]
Enterprise: [SSO features? Details?]
Perplexity: [SSO info? Sources?]
Okta: [Integration listed?]
Azure AD: [Integration listed?]
Google Workspace: [Integration listed?]
```

**SSO Status Decision**:
- [ ] Set to "supported" (found clear evidence)
- [ ] Leave blank (no evidence found, but not confirmed unsupported)
- [ ] Set to "notSupported" (explicitly stated as not available)

**Evidence Source**: _____________________

**IF LEAVING BLANK**: Confirmed exhausted all 8+ sources above? [ ] Yes [ ] No

---

## Step 2D: SI ID Generation

**Application Name**: _____________________

**Transformation Steps**:
1. Remove spaces: _____________________
2. Remove special characters (. , - ' ( ) / & :): _____________________
3. Remove domain extensions (.com, .io, .ai, etc.): _____________________
4. Remove "by [Company]": _____________________
5. Remove version numbers: _____________________
6. Length check: _____ characters (must be <60)

**Generated SI ID**: _____________________

- [ ] SI ID follows transformation rules
- [ ] Length <60 characters
- [ ] No spaces or special characters remain

---

## Step 2E: Description Quality

**Description**:
```
[PASTE FINAL DESCRIPTION HERE]
```

**Word Count**: _____ words (must be 30-90)

**Marketing Buzzword Check** (must check all 18):
- [ ] "leading" - Found? Remove/rewrite
- [ ] "powerful" - Found? Remove/rewrite
- [ ] "innovative" - Found? Remove/rewrite
- [ ] "cutting-edge" - Found? Remove/rewrite
- [ ] "revolutionary" - Found? Remove/rewrite
- [ ] "seamless" - Found? Remove/rewrite
- [ ] "transform" - Found? Remove/rewrite
- [ ] "empower" - Found? Remove/rewrite
- [ ] "streamline" - Found? Remove/rewrite
- [ ] "enhance" - Found? Remove/rewrite
- [ ] "enterprise-grade" - Found? Remove/rewrite
- [ ] "best-in-class" - Found? Remove/rewrite
- [ ] "world-class" - Found? Remove/rewrite
- [ ] "industry-leading" - Found? Remove/rewrite
- [ ] "award-winning" - Found? Remove/rewrite
- [ ] "groundbreaking" - Found? Remove/rewrite
- [ ] "game-changing" - Found? Remove/rewrite
- [ ] "next-generation" - Found? Remove/rewrite

**Buzzwords Found**: _____ (list them: _______________)
**Buzzwords Removed/Rewritten**: [ ] Yes [ ] N/A (none found)

**Product State Verification**:
- [ ] Description reflects CURRENT product state (2026)
- [ ] Verified product hasn't evolved/changed (not outdated info from 2-3 years ago)
- [ ] If product changed, description updated to current state

---

## Step 3: Agent Verification

**For Each Field, Compare Perplexity vs WebFetch**:

### Webpage URL
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low

### Hosting Type
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low
- **Matrix completed?**: [ ] Yes [ ] No

### SSO Status
- Perplexity: _____________________
- WebFetch: _____________________
- Changelog: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low

### Pricing Type
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low

### Product Category
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low
- **Most specific category chosen?**: [ ] Yes [ ] No

### Aliases
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low

### Subtype
- Perplexity: _____________________
- WebFetch: _____________________
- **Decision**: _____________________ (source: _______)
- **Confidence**: High / Medium / Low

### Description
- Perplexity: _____________________ (marketing language? Y/N)
- WebFetch: _____________________ (marketing language? Y/N)
- **Decision**: _____________________ (source: _______)
- **Marketing language filtered?**: [ ] Yes [ ] N/A
- **Confidence**: High / Medium / Low

**Conflicts Resolved**: _____ (number)
**Conflicts Unresolved**: _____ (number)

---

## Step 4: Quality Check

**Overall Confidence Calculation**:
- High confidence fields: _____
- Medium confidence fields: _____
- Low confidence fields: _____
- **Overall confidence**: _____%

**Quality Criteria**:
- [ ] Overall confidence > 70%
- [ ] Critical fields present (webpageUrl, description, hostingType)
- [ ] No unresolved conflicts
- [ ] Description word count 30-90
- [ ] Hosting type evaluation matrix completed
- [ ] Description has no marketing buzzwords
- [ ] Fixed fields set (collectionStatus, deprecated, asOfDate)
- [ ] SI ID generated

**Quality Check Result**: [ ] PASS [ ] FAIL

**IF FAIL**:
- Issues identified: _____________________
- Resolution plan: _____________________

---

## Step 5: Fixed Fields Verification

- [ ] **category**: Set to "businessApplication" (exactly this value)
- [ ] **collectionStatus**: Set to "inReview" (exactly this value, camelCase)
- [ ] **deprecated**: Set to "No" (capital N, NOT "no")
- [ ] **asOfDate**: Set to current date in YYYY-MM-DD format (_____ _____ _____)

**All fixed fields correct?**: [ ] Yes [ ] No

---

## Step 6: Final Field Values

**Complete field list for upload**:
```json
{
  "siId": "_____",
  "category": "businessApplication",
  "webpageUrl": "_____",
  "hostingType": "_____",
  "hostingDescription": "_____",
  "ssoStatus": "_____ or blank",
  "pricingType": "_____",
  "productCategory": "_____",
  "alias": "_____",
  "description": "_____",
  "collectionStatus": "inReview",
  "deprecated": "No",
  "asOfDate": "_____"
}
```

---

## Step 7: Fact Sheet Creation & Update

**Fact Sheet Created**:
- [ ] Created via mcp__LeanIX_MCP_Server_Remote__create_fact_sheet
- **Fact Sheet ID**: _____________________
- **Creation timestamp**: _____________________

**Custom Fields Updated**:
- [ ] Update attempted via Python CLI
- [ ] Update successful (or documented if any fields failed)
- **Fields updated**: _____ out of _____
- **Fields failed (if any)**: _____________________

**Final URL**:
```
https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/_____
```

---

## Validation & Sign-Off

**Validation Script Run**:
- [ ] Ran validate_application.py
- [ ] All checks passed
- [ ] Issues found (if any): _____________________

**Self-Assessment**:
- [ ] I followed the documented workflow
- [ ] I did NOT skip the evaluation matrix
- [ ] I did NOT make ad-hoc decisions
- [ ] I exhausted SSO research (5+ sources)
- [ ] I filtered marketing language
- [ ] I verified product current state
- [ ] I used correct enum values (deprecated="No", not "no")

**Agent Signature**: _____________________
**Completion Date**: _____________________

---

## Post-Creation Notes

**Issues Encountered**:
```
[Document any issues, tool failures, workarounds used]
```

**Lessons Learned**:
```
[What went well? What would you do differently?]
```

**Recommendations for Future Agents**:
```
[Any tips or warnings for agents who work on similar applications?]
```
