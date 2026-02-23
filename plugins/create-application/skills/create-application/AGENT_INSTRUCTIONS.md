# Agent Instructions for Application Creation

## Recognizing When to Use This Skill

This skill should be triggered when the user requests **Application creation** (not updates, research, or other entity types).

**Valid invocation patterns:**
- "Create Application for [name/URL]"
- "Add Application [name]"
- "Set up Application for [name/URL]"
- "Make an Application fact sheet for [name]"
- "New Application: [name]"

**Full pattern list**: See [SKILL_INVOCATION_PATTERNS.md](SKILL_INVOCATION_PATTERNS.md)

**Do NOT trigger for:**
- "Update Application X" (modification, not creation)
- "Research Application Y" (information gathering, not creation)
- "Create Provider Z" (different entity type)

---

## YOU MUST READ THIS FIRST

When the user says: **"Create Application for [X]"** or **"Create Application for [URL]"**

### Step 0: Preparation (DO THIS FIRST)

1. **Read workflow documentation**
   - Read `WORKFLOW.md` completely (all 661 lines)
   - Understand the 4-step process: Parallel Research → Agent Verification → Quality Check → Create & Update

2. **Read all guidelines**
   - `guidelines/Application_Description_Guidelines.md`
   - `guidelines/Application_Webpage_URL_Guidelines.md`
   - `guidelines/Application_Hosting_Type_Guidelines.md` (includes hostingDescription)
   - `guidelines/Application_SSO_Status_Guidelines.md`
   - `guidelines/Application_Pricing_Guidelines.md`
   - `guidelines/Application_Product_Category_Guidelines.md`
   - `guidelines/Application_Alias_Guidelines.md`
   - `guidelines/Application_Subtype_Guidelines.md`
   - `guidelines/Application_SI_ID_Implementation.md`
   - `guidelines/Application_As_Of_Date_Guidelines.md`
   - `guidelines/Application_Collection_Status_and_Deprecated_Guidelines.md`

3. **Verify tools are available**
   - Perplexity MCP (for web research)
   - WebFetch (for website scraping)
   - LeanIX MCP (for fact sheet creation)
   - Python CLI in `../create-provider/main.py` (for custom field updates)

### Step 1: Execute Parallel Research

**Use the documented approach:**
- Use `lib/application_researcher.py` to generate structured queries (don't write ad-hoc queries)
- Call Perplexity and WebFetch **in parallel** (single message, multiple tool calls)
- Research ALL fields simultaneously:
  - Webpage URL (validate from 2+ sources)
  - Hosting Type (evaluate ALL 6 types with matrix)
  - Hosting Description (technical reasoning, 90% confidence threshold)
  - SSO Status (check changelog FIRST)
  - Pricing Type (6 models: free/freemium/subscription/perpetual/transaction/enterprise)
  - Product Category (most specific from 50+ categories)
  - Aliases (verified from official sources only)
  - Application Subtype (application vs mobileApp)
  - Description (30-90 words, marketing language filtered)

**Application-Specific Research Rules:**

1. **Hosting Type - MUST Complete Evaluation Matrix:**
   - Score ALL 6 types (saas, paas, iaas, onPremise, hybrid, mobile)
   - Don't pick first match - complete matrix first
   - Identify primary user (business users, developers, IT teams)
   - Check name for indicators ("mobile app", "Desktop", "Platform")
   - Research sources:
     - Security page (/security) - often mentions cloud provider
     - Enterprise page (/enterprise) - hosting infrastructure
     - Changelog (/changelog) - hosting announcements
     - Product page - deployment options
   - Apply decision logic: If scores tie, use primary user test
   - Examples:
     - AWS Lambda → paas (for developers, not saas)
     - Slack Desktop → saas (client for cloud service)
     - Instagram → mobile (native mobile-first)

2. **SSO Status - CHECK CHANGELOG FIRST ⭐ CRITICAL:**
   - Priority source: /changelog, /updates, /whats-new, /releases
   - SSO is often announced as milestone feature
   - Look for: "SSO support added", "SAML integration", "Enterprise authentication"
   - Note date if found
   - Then check: security page, enterprise page, pricing page
   - Integration directories: Okta, Azure AD, Google Workspace
   - If no clear evidence → Leave blank (better than guessing)
   - DO NOT mark "notSupported" unless explicitly stated

3. **Hosting Description - 90% Confidence Threshold:**
   - Format: "Classified as [type]: [specific technical details]"
   - Include: primary user, cloud provider (if explicitly stated), deployment model
   - Examples:
     - "Classified as SaaS: end-user collaboration application hosted on AWS with multi-site data redundancy"
     - "Classified as PaaS: developer platform for building serverless functions with integrated CI/CD"
   - Anti-hallucination rules:
     - Don't guess cloud provider if not explicitly stated
     - Don't infer technical details from absence of information
     - Don't use marketing language
     - If confidence < 90% → Use basic classification: "Classified as [type]: [basic reasoning without specific technical details]"

4. **Description - Marketing Language Filter ⚠️ MANDATORY:**
   - Detect 18 buzzwords:
     - "leading", "powerful", "innovative", "cutting-edge", "revolutionary"
     - "seamless", "transform", "empower", "streamline", "enhance"
     - "enterprise-grade", "best-in-class", "world-class", "industry-leading"
     - "award-winning", "groundbreaking", "game-changing", "next-generation"
   - Rewrite to factual alternatives:
     - ❌ "transforms operations" → ✅ "automates workflows"
     - ❌ "empowers teams" → ✅ "enables teams to"
     - ❌ "seamless integration" → ✅ "integrates with"
     - ❌ "powerful analytics" → ✅ "analytics features"
   - 30-90 words exactly
   - Focus on WHAT it does, not how good it is
   - Use neutral verbs: "provides", "enables", "allows", "supports", "includes"

**Collect results from both sources:**
```json
{
  "perplexity": {
    "url": {...},
    "hosting_type": {...},
    "hosting_description": {...},
    "sso_status": {...},
    "pricing_type": {...},
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
  }
}
```

### Step 2: Execute Agent Verification

**Use the documented verification logic:**
- Compare Perplexity vs WebFetch results for each field
- Apply resolution rules from WORKFLOW.md:
  1. Both agree → Use agreed value (HIGH confidence), check for marketing language
  2. One has data, other doesn't → Use available data (MEDIUM confidence), check for marketing language
  3. Both differ → Apply field-specific guidelines, run verification query if needed, remove marketing language
  4. Both fail → Mark as "Not Found", leave blank or use default

**Application-Specific Verification Rules:**

- **Hosting Type**: Prefer source with completed evaluation matrix
- **Hosting Description**: Prefer source with ≥90% confidence, avoid hallucination
- **SSO Status**: Prefer changelog source (strongest evidence), then security/enterprise pages
- **Pricing Type**: Prefer source that scraped /pricing page directly
- **Product Category**: Use most specific category (e.g., "Project Management" > "Collaboration")
- **Description**: Apply marketing language filter to BOTH sources, prefer factual over marketing

**Generate confidence scores per field:**
```json
{
  "verified_data": {
    "webpageUrl": {"value": "...", "confidence": "high", "source": "both_agree"},
    "hostingType": {"value": "saas", "confidence": "high", "source": "perplexity_matrix"},
    "hostingDescription": {"value": "...", "confidence": "high", "source": "perplexity_90_percent"},
    "ssoStatus": {"value": "supported", "confidence": "high", "source": "webfetch_changelog"},
    "pricingType": {"value": "freemium", "confidence": "high", "source": "both_agree"},
    "productCategory": {"value": "...", "confidence": "high", "source": "most_specific"},
    "alias": {"value": "", "confidence": "high", "source": "both_agree_none"},
    "type": {"value": "application", "confidence": "high", "source": "both_agree"},
    "description": {"value": "...", "confidence": "high", "source": "perplexity_factual", "marketing_buzzwords_removed": 3}
  },
  "verification_metadata": {
    "overall_confidence": 0.92,
    "conflicts_resolved": 2,
    "fields_with_high_confidence": 9
  }
}
```

### Step 3: Quality Check

**⚠️ CHECKPOINT: Before Setting Hosting Type**

**STOP. Answer these questions:**
- [ ] Have I scored all 6 hosting types (SaaS, PaaS, IaaS, On-Premise, Hybrid, Mobile)?
- [ ] Do I have a score (0-10) and reasoning for EACH type?
- [ ] Have I documented the matrix in executions/[App_Name]/hosting_matrix.md?
- [ ] Have I applied the decision logic (primary user test, name check)?

**IF ANY ANSWER IS NO → GO BACK AND COMPLETE MATRIX**

Use the matrix generator to help:
```bash
python lib/generate_matrix.py "[Application Name]" > executions/[App_Name]/hosting_matrix.md
```

---

**⚠️ CHECKPOINT: Before Creating Fact Sheet**

**STOP. Verify these fields:**
- [ ] siId generated (removed spaces, special chars, length <60)
- [ ] category = "businessApplication" (exactly this value)
- [ ] deprecated = "No" (capital N, NOT "no")
- [ ] description is 30-90 words
- [ ] description has NO marketing buzzwords (checked all 18)
- [ ] hostingType has completed matrix justification
- [ ] collectionStatus = "inReview" (exactly, camelCase)
- [ ] asOfDate = current date (YYYY-MM-DD)

**IF ANY CHECKBOX UNCHECKED → FIX IT BEFORE PROCEEDING**

---

**MANDATORY: Run Validation Script**

Before proceeding to Step 4, run the validation script:

```bash
cd create-application
python lib/validate_application.py \
  --checklist executions/[App_Name]/EXECUTION_CHECKLIST.md \
  --fields executions/[App_Name]/final_fields.json
```

**Script will check:**
- ✅ Hosting matrix completed (all 6 types scored)
- ✅ Description 30-90 words, no buzzwords
- ✅ Correct enum values (deprecated="No", category="businessApplication")
- ✅ SI ID generated
- ✅ SSO research exhaustive (5+ sources)
- ✅ Overall confidence > 70%

**IF VALIDATION FAILS → FIX ERRORS AND RE-RUN**

---

**Quality Criteria** (manual verification):
- ✅ Overall confidence > 70%?
- ✅ Critical fields present? (webpageUrl, description, hostingType)
- ✅ No unresolved conflicts?
- ✅ Description word count 30-90?
- ✅ Hosting type evaluation matrix completed?
- ✅ Description has no marketing buzzwords?
- ✅ Fixed fields set? (collectionStatus="inReview", deprecated="No", asOfDate=today)

**If quality check fails:**
- Inform user about low confidence or missing data
- Run validation script to identify specific issues
- Offer options: Fix and re-validate, Save with partial data, manual input, or cancel

**If quality check passes:**
- Proceed to Step 4 automatically

### Step 4: Create & Update

**Execute in order:**
1. Create fact sheet via LeanIX MCP:
   ```
   mcp__LeanIX_MCP_Server_Remote__create_fact_sheet(
     name="Application Name",
     type="Application"
   )
   ```

2. Update custom fields via Python CLI:
   ```bash
   cd ../create-provider
   python main.py update \
     --fact-sheet-id "uuid" \
     --type Application \
     --fields '{
       "webpageUrl": "https://...",
       "hostingType": "saas",
       "hostingDescription": "Classified as SaaS: ...",
       "ssoStatus": "supported",
       "pricingType": "freemium",
       "productCategory": "Project Management",
       "alias": "",
       "type": "application",
       "description": "...",
       "collectionStatus": "inReview",
       "asOfDate": "2026-02-22",
       "deprecated": "No"
     }'
   ```

3. Return fact sheet URL to user:
   ```
   https://{subdomain}.leanix.net/{workspace}/factsheet/Application/{id}
   ```

---

## ❌ What NOT To Do

**General:**
- ❌ Don't make ad-hoc Perplexity calls without reading guidelines
- ❌ Don't skip parallel research (must use both sources)
- ❌ Don't skip verification step
- ❌ Don't proceed with confidence < 70% without user approval
- ❌ Don't improvise research queries - use `application_researcher.py` logic
- ❌ Don't call Perplexity and WebFetch sequentially - use parallel tool calls

**Application-Specific:**
- ❌ Don't skip hosting type evaluation matrix (must score all 6 types)
- ❌ Don't ignore changelog when researching SSO status
- ❌ Don't accept descriptions with marketing buzzwords
- ❌ Don't hallucinate cloud providers in hosting descriptions
- ❌ Don't pick first matching hosting type - complete matrix first
- ❌ Don't mark SSO as "notSupported" without explicit evidence
- ❌ Don't use confidence < 90% for hosting description with technical details

---

## Self-Correction Protocol

**If you catch yourself about to:**
- Make an ad-hoc Perplexity call
- Skip reading the workflow documentation
- Bypass parallel research
- Skip the verification step
- Proceed without quality check
- Skip hosting type evaluation matrix
- Not check changelog for SSO
- Accept marketing language in description

**STOP and ask yourself:**

1. **"Why am I not following the documented workflow?"**
   - Did I skip reading WORKFLOW.md?
   - Am I trying to take shortcuts?
   - Am I improvising instead of using documented modules?
   - Did I skip Application-specific rules?

2. **"What step did I miss?"**
   - Did I read the complete workflow? (No → Read it now)
   - Did I read all 11 guidelines? (No → Read them now)
   - Am I using application_researcher.py logic? (No → Use it)
   - Am I doing parallel research? (No → Do it properly)
   - Did I complete hosting type evaluation matrix? (No → Complete it)
   - Did I check changelog for SSO? (No → Check it)
   - Did I filter marketing language? (No → Filter it)

3. **"What should I do now?"**
   - Go back to Step 0
   - Read WORKFLOW.md completely
   - Read all 11 guidelines
   - Start from Step 1 properly

**Then acknowledge to user:**
"I didn't follow the documented workflow. Let me start over properly by reading WORKFLOW.md and executing the parallel research workflow with all Application-specific rules."

---

## Success Indicators

**You're doing it right if:**
- ✅ You read WORKFLOW.md before making any tool calls
- ✅ You read all 11 guidelines before researching
- ✅ You call Perplexity and WebFetch in parallel (same message)
- ✅ You completed hosting type evaluation matrix for all 6 types
- ✅ You checked changelog first for SSO status
- ✅ You detected and removed all marketing buzzwords from description
- ✅ You used 90% confidence threshold for hosting description
- ✅ You compare both sources and generate confidence scores
- ✅ You present verified data with conflict resolution notes
- ✅ You check quality before creating the fact sheet

**You're doing it wrong if:**
- ❌ You make Perplexity calls before reading documentation
- ❌ You skip WebFetch and only use Perplexity
- ❌ You pick first matching hosting type without completing matrix
- ❌ You don't check changelog for SSO
- ❌ You accept descriptions with marketing buzzwords
- ❌ You hallucinate technical details in hosting description
- ❌ You don't compare sources or verify data
- ❌ You proceed without confidence scores
- ❌ You create fact sheets without quality checks

---

## Example Execution Trace

```
User: "Create Application for https://www.smartsheet.com/"

Agent:
1. ✓ Read WORKFLOW.md (661 lines)
2. ✓ Read 11 guidelines
3. ✓ Verified tools available

Step 1: Parallel Research
- ✓ Called Perplexity + WebFetch in parallel
- ✓ Perplexity: Completed hosting type evaluation matrix (all 6 types scored)
- ✓ WebFetch: Checked changelog for SSO (found announcement from 2019)
- ✓ Collected results from both sources

Step 2: Agent Verification
- ✓ Compared URL: Both agree → HIGH confidence
- ✓ Compared Hosting Type: Both say "saas", matrix completed → HIGH confidence
- ✓ Compared Hosting Description: 92% confidence, no hallucination → HIGH confidence
- ✓ Compared SSO: Both say "supported", changelog evidence → HIGH confidence
- ✓ Compared Pricing: Both say "freemium" → HIGH confidence
- ✓ Compared Category: Perplexity="Collaboration", WebFetch="Project Management" → Use "Project Management" (more specific) → HIGH confidence
- ✓ Compared Aliases: Both found none → HIGH confidence
- ✓ Compared Subtype: Both say "application" → HIGH confidence
- ✓ Compared Description: Filtered 3 marketing buzzwords → HIGH confidence
- Overall confidence: 95%

Step 3: Quality Check
- ✓ Confidence 95% > 70%
- ✓ Critical fields present (webpageUrl, description, hostingType)
- ✓ No unresolved conflicts
- ✓ Description: 41 words (within 30-90 range)
- ✓ Hosting matrix completed for all 6 types
- ✓ Description has no marketing buzzwords
- ✓ Fixed fields set (collectionStatus, deprecated, asOfDate)
- PASS → Proceed

Step 4: Create & Update
- ✓ Created fact sheet via LeanIX MCP
- ✓ Updated 12 custom fields via Python CLI
- ✓ Returned URL

Result: https://demo-eu-10.leanix.net/.../factsheet/Application/{id}

Verification Report:
✓ Webpage URL: https://www.smartsheet.com/ (both sources)
✓ Hosting Type: saas (matrix completed, primary user: business users)
✓ Hosting Description: "Classified as SaaS: end-user collaboration application hosted on AWS with multi-site data redundancy" (92% confidence)
✓ SSO Status: supported (changelog: Enterprise Grid 2019)
✓ Pricing Type: freemium (both sources, pricing page verified)
✓ Product Category: Project Management (more specific than Collaboration)
✓ Aliases: (none found)
✓ Subtype: application (web-based)
✓ Description: 41 words, 3 buzzwords removed ("leading", "powerful", "seamless")
✓ Fixed fields: collectionStatus=inReview, deprecated=no, asOfDate=2026-02-22

Conflicts Resolved: 2
- Product Category: Used "Project Management" (more specific)
- Description: Used Perplexity version (WebFetch had marketing language)
```

---

## Final Reminder

**Every single time you create an Application:**
1. Read WORKFLOW.md
2. Read 11 guidelines
3. Execute 4 steps in order
4. Apply Application-specific rules:
   - Complete hosting type evaluation matrix
   - Check changelog first for SSO
   - Filter marketing language
   - Use 90% confidence threshold for hosting description
5. No shortcuts, no improvisation

**If you deviate, self-correct immediately.**
