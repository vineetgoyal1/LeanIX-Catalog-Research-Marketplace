# create-application

Automatically research and create LeanIX Application fact sheets with verified data through parallel research and agent verification.

## Features

- **Parallel Research**: 13 simultaneous queries (8 Perplexity + 5 WebFetch)
- **Agent Verification**: Cross-source validation and conflict resolution
- **Quality Checks**: Confidence scoring (>70% required)
- **Marketing Language Detection**: Removes buzzwords and rewrites to factual statements
- **SI ID Uniqueness**: Collision detection and resolution
- **Category Matching**: Matches against 3,120+ existing categories

## Fields Researched

| Field | Sources | Validation |
|-------|---------|------------|
| Description | Perplexity, Official Website | 30-90 words, no marketing language |
| Webpage URL | Official Website | Valid, accessible, canonical URL |
| Hosting Type | Analysis Matrix | SaaS, PaaS, IaaS, Mobile, On-Premise, Other |
| SSO Status | Changelog, Security Page, Pricing | Explicit evidence required |
| Pricing Type | Pricing Page | Free, Freemium, Paid, Usage-based, etc. |
| Product Category | G2, Capterra | Match existing 3,120+ categories |
| Aliases | Historical Research | Former names, abbreviations, variants |

## Usage

```
Create application for Watchwire
```

or

```
Add application for https://watchwire.ai
```

## Workflow

### Step 1: Parallel Research (YOU execute 13 queries simultaneously)
- 8 Perplexity queries for different fields
- 5 WebFetch queries (homepage, security, pricing, about, changelog)

### Step 2: Agent Verification (YOU compare sources and resolve conflicts)
- Extract values from both sources
- Compare and detect conflicts
- Apply resolution rules
- Record confidence levels

### Step 3: Quality Check (YOU validate against criteria)
- Overall confidence > 70%
- Description: 30-90 words, no marketing buzzwords
- Critical fields present
- SSO research: 5+ sources checked

### Step 4: Create & Update (YOU call LeanIX MCP and Python CLI)
- Create fact sheet via MCP
- Update custom fields via Python CLI
- Update description via MCP
- Report success with confidence breakdown

## Guidelines

This plugin includes 11 comprehensive guidelines:

1. **Application_Description_Guidelines.md** - 30-90 words, factual, organization-focused
2. **Application_Webpage_URL_Guidelines.md** - Never hallucinate, verify accessibility
3. **Application_Hosting_Type_Guidelines.md** - 6-type classification with decision matrix
4. **Application_SSO_Status_Guidelines.md** - Evidence-based, multiple sources required
5. **Application_Pricing_Guidelines.md** - Pricing type and URL validation
6. **Application_Product_Category_Guidelines.md** - Match 3,120+ existing categories
7. **Application_Alias_Guidelines.md** - 7 alias types with verification
8. **Application_Subtype_Guidelines.md** - Always "businessApplication"
9. **Application_SI_ID_Implementation.md** - Uniqueness with collision resolution
10. **Application_As_Of_Date_Guidelines.md** - ISO 8601 format (YYYY-MM-DD)
11. **Application_Collection_Status_and_Deprecated_Guidelines.md** - Fixed values

## Prerequisites

**Required:**
- LeanIX MCP Server
- Perplexity MCP Server
- Environment variables: `LEANIX_API_TOKEN`, `LEANIX_SUBDOMAIN`

**Optional:**
- WebFetch tool (for direct website scraping)

## Output Example

```
✅ Application Created Successfully!

Application: Watchwire
Overall Confidence: 95% (HIGH)

Verified Data Summary:
├─ Webpage URL: https://watchwire.ai ✓✓ (both sources)
├─ Hosting Type: saas ✓✓ (both sources)
├─ SSO Status: supported ✓✓✓ (changelog + docs)
├─ Pricing Type: paid ✓ (official page)
├─ Product Category: Energy Management Software ✓✓
├─ Aliases: (none found) ✓✓
└─ Description: 66 words ✓✓ (factual)

LeanIX URL: https://demo-eu-10.leanix.net/...
Status: Ready for review team approval
```

## Version

1.0.0

## Author

Vineet Goyal <vineet.goyal@sap.com>
