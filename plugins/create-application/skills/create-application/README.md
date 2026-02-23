# Application Auto-Creation Skill

Automatically research and create LeanIX Application fact sheets with minimal input using AI-powered research and verification.

## Quick Start (For Users)

Simply say to Claude Code:
```
Create Application for [Application Name or URL]
```

**Examples:**
- "Create Application for Smartsheet"
- "Create Application for https://www.salesforce.com/"
- "Add Application Zoom"

The agent will automatically research and populate all fields. See [SKILL_INVOCATION_PATTERNS.md](SKILL_INVOCATION_PATTERNS.md) for all supported phrases.

---

## What This Skill Does

This skill automates Application fact sheet creation through:

1. **Parallel Research**: Uses Perplexity MCP + WebFetch simultaneously
2. **Cross-Verification**: Compares multiple sources and resolves conflicts
3. **Quality Checks**: Validates data before creating fact sheets
4. **Auto-Population**: Fills 12 fields with verified information

**Fields Researched:**
- Webpage URL (validated from 2+ sources)
- Hosting Type (evaluated across 6 types with matrix scoring)
- Hosting Description (technical classification reasoning)
- SSO Status (changelog-first detection strategy)
- Pricing Type (6 pricing models: free/freemium/subscription/perpetual/transaction/enterprise)
- Product Category (most specific category from 50+ options)
- Aliases and former names
- Application Subtype (application vs mobileApp)
- Description (marketing language filtered, 30-90 words)
- Collection status, as-of date, deprecated flag

### Key Features

- **Hosting Type Evaluation Matrix**: Systematically evaluates all 6 hosting types (saas, paas, iaas, onPremise, hybrid, mobile) before classification
- **Changelog-First SSO Detection**: Checks product updates/changelog pages first for SSO announcements
- **Marketing Language Filter**: Detects and removes 18 marketing buzzwords from descriptions
- **90% Confidence Threshold**: Prevents hallucination in technical hosting descriptions

---

## Overview

This directory contains an Application auto-creation skill that combines:
- **AI Research** (Perplexity + WebFetch)
- **Python CLI Tool** (for LeanIX custom field updates via GraphQL API)
- **Comprehensive Guidelines** (11 guidelines for data quality)

The Python tool enables updating any custom field on LeanIX fact sheets, including fields not exposed by the standard MCP server:

1. **Discovery phase (one-time)**: Fetch available fields for each fact sheet type and save to a configuration file
2. **Update phase (fast)**: Validate fields against the configuration and execute GraphQL mutations

### Supported Fact Sheet Types

The Python CLI tool in `../create-provider/main.py` supports:
- **Application** - Standard LeanIX application fact sheets (this skill)
- **Provider** - Provider/vendor catalog fact sheets
- **ITComponent** - IT component fact sheets
- **ProductFamily** - Custom fact sheet types in your workspace

## Setup

### Prerequisites

- Python 3.10 or higher
- LeanIX technical user token (API token starting with `LXT_`)
- LeanIX workspace subdomain

### Installation

1. Install dependencies:
```bash
cd ../create-provider
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export LEANIX_API_TOKEN="LXT_your_token_here"
export LEANIX_SUBDOMAIN="your-subdomain"
```

Or create a `.env` file:
```bash
LEANIX_API_TOKEN=LXT_your_token_here
LEANIX_SUBDOMAIN=your-subdomain
```

## Usage

### For AI Agents (Claude Code)

Simply say: **"Create Application for [Name or URL]"**

The agent will follow the enforced workflow with validation checkpoints:

**Workflow with Enforcement**:
1. **Setup execution directory**:
   ```bash
   ./setup_execution.sh "Application Name"
   ```

2. **Read documentation** (mandatory):
   - [WORKFLOW.md](WORKFLOW.md) - Complete 4-step process
   - All 11 guidelines in [guidelines/](guidelines/)
   - [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md) - Quick reference

3. **Complete EXECUTION_CHECKLIST.md**:
   - Pre-flight verification
   - Parallel research documentation
   - **Hosting type evaluation matrix** (all 6 types scored)
   - SSO exhaustive research (5+ sources)
   - SI ID generation
   - Description quality check

4. **Complete hosting_matrix.md**:
   ```bash
   python lib/generate_matrix.py "Application Name" > executions/App_Name_DATE/hosting_matrix.md
   ```

5. **Run validation** (before creating fact sheet):
   ```bash
   python lib/validate_application.py \
     --checklist executions/App_Name_DATE/EXECUTION_CHECKLIST.md \
     --fields executions/App_Name_DATE/final_fields.json
   ```

6. **Create fact sheet** (only after validation passes)

7. **Run post-creation review**:
   ```bash
   ./lib/review_application.sh FACT_SHEET_ID "Application Name"
   ```

**Enforcement Mechanisms**:
- ✅ Mandatory checklist completion
- ✅ Validation script catches errors automatically
- ✅ Hosting matrix must be completed (all 6 types scored)
- ✅ Checkpoints before setting hosting type and creating fact sheet
- ✅ Execution records for audit trail

See [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md) for detailed agent workflow with checkpoints.

### For Manual Updates (Python CLI)

The Python CLI tool is shared with create-provider. Use it from the parent directory:

```bash
cd ../create-provider

# Update Application fact sheet
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "webpageUrl": "https://www.smartsheet.com/",
    "hostingType": "saas",
    "hostingDescription": "Classified as SaaS: end-user collaboration application",
    "ssoStatus": "supported",
    "pricingType": "freemium",
    "productCategory": "Project Management",
    "alias": "",
    "type": "application",
    "description": "Smartsheet provides an online application for collaboration...",
    "collectionStatus": "inReview",
    "deprecated": "no",
    "asOfDate": "2026-02-22"
  }'
```

## Supported Fields

The tool dynamically discovers available fields during the discovery phase. Application-specific fields include:

### Application Fields (Auto-Researched)

- `webpageUrl` - Official application website URL
- `hostingType` - Hosting classification (saas/paas/iaas/onPremise/hybrid/mobile)
- `hostingDescription` - Technical reasoning for classification
- `ssoStatus` - Single sign-on support (supported/notSupported)
- `pricingType` - Pricing model (free/freemium/subscription/perpetual/transaction/enterprise)
- `productCategory` - Application category from LeanIX taxonomy
- `alias` - Alternative names (comma-separated)
- `type` - Application subtype (application/mobileApp)
- `description` - Application description (30-90 words, marketing-filtered)
- `collectionStatus` - Data collection workflow status (fixed: "inReview")
- `deprecated` - Deprecation flag (fixed: "no")
- `asOfDate` - Date of last research (fixed: current date YYYY-MM-DD)

### Other Available Fields

The Application fact sheet type supports 170+ fields. Use the discovery command to see all available fields:

```bash
cd ../create-provider
python main.py discover --type Application
```

This creates/updates `field_config.json` with all available fields for Application.

## Field Configuration

### Shared field_config.json

The field configuration is shared across all skills and located at `../create-provider/field_config.json`. It contains discovered fields for multiple fact sheet types:

```json
{
  "Application": {
    "fields": [
      "webpageUrl",
      "hostingType",
      "hostingDescription",
      "ssoStatus",
      "pricingType",
      "productCategory",
      "alias",
      "type",
      "description",
      "collectionStatus",
      "deprecated",
      "asOfDate"
      // ... and 158 more fields
    ]
  },
  "Provider": { "fields": [...] },
  "ITComponent": { "fields": [...] },
  "ProductFamily": { "fields": [...] }
}
```

## Error Handling

### Common Errors

**1. Missing Environment Variables**
```
Error: LEANIX_API_TOKEN environment variable is required.
```
**Solution:** Set the required environment variables.

**2. Configuration File Not Found**
```
Error: Configuration file not found: field_config.json
Run 'python main.py discover --type Application' to generate it.
```
**Solution:** Run the discovery command from `../create-provider/`.

**3. Invalid Field Name**
```
Validation failed:
  Invalid field 'invalidField' for type Application.
  Allowed fields: webpageUrl, hostingType, ssoStatus, ...
```
**Solution:** Check the field name spelling and ensure it exists in `field_config.json`.

**4. Authentication Failed**
```
Error: httpx.HTTPStatusError: 401 Unauthorized
```
**Solution:** Verify your API token is valid and has not expired.

**5. Fact Sheet Not Found**
```
GraphQL errors: Fact sheet with ID 'uuid' not found
```
**Solution:** Verify the fact sheet ID is correct and exists in your workspace.

## Architecture

### Components

1. **WORKFLOW.md** - Detailed workflow documentation (661 lines)
2. **guidelines/** - 11 field-specific research guidelines
3. **lib/** - Application-specific research modules
   - `application_researcher.py` - Field-specific query generators
   - `parallel_researcher.py` - Parallel research orchestration
   - `verification_agent.py` - Cross-verification with marketing language filter
4. **../create-provider/main.py** - Shared Python CLI for LeanIX updates
5. **../lib/leanix_client/** - Shared GraphQL client and helpers

### Authentication Flow

1. Exchange technical user token (API token) for Bearer token via OAuth2
2. Cache Bearer token for the session
3. Use Bearer token for all GraphQL requests

### Update Flow

1. Load `../create-provider/field_config.json` (no API call)
2. Validate field names against configuration (instant)
3. If validation passes:
   - Authenticate via OAuth2
   - Build JSON Patch operations
   - Execute `updateFactSheet` GraphQL mutation
   - Return results

## Examples

### Update Application Hosting Information

```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "hostingType": "saas",
    "hostingDescription": "Classified as SaaS: end-user collaboration tool hosted on AWS"
  }'
```

### Update Application SSO Status

```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "ssoStatus": "supported"
  }'
```

### Update Application Category and Description

```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "productCategory": "Project Management",
    "description": "Smartsheet provides an online application for collaboration and work management with features for project tracking, task assignment, and team coordination."
  }'
```

### Update Multiple Application Fields

```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "webpageUrl": "https://www.smartsheet.com/",
    "hostingType": "saas",
    "hostingDescription": "Classified as SaaS: end-user collaboration application hosted on AWS",
    "ssoStatus": "supported",
    "pricingType": "freemium",
    "productCategory": "Project Management",
    "alias": "",
    "type": "application",
    "description": "Smartsheet provides an online application for collaboration and work management.",
    "collectionStatus": "inReview",
    "deprecated": "no",
    "asOfDate": "2026-02-22"
  }'
```

## Development

### Project Structure

```
create-application/
├── README.md                         # This file
├── WORKFLOW.md                       # Detailed workflow (661 lines)
├── QUICK_START.md                    # Getting started guide
├── AGENT_INSTRUCTIONS.md             # AI agent quick reference
├── SKILL_INVOCATION_PATTERNS.md      # Invocation patterns
├── lib/                              # Application-specific modules
│   ├── application_researcher.py     # Field query generators
│   ├── parallel_researcher.py        # Parallel research
│   └── verification_agent.py         # Cross-verification
└── guidelines/                       # Application research guidelines (11 files)
    ├── Application_Hosting_Type_Guidelines.md
    ├── Application_SSO_Status_Guidelines.md
    ├── Application_Description_Guidelines.md
    └── ... (8 more)

Shared Resources (from parent directory):
../create-provider/
├── main.py                           # Shared Python CLI
├── requirements.txt                  # Shared dependencies
└── field_config.json                 # Shared field configuration

../lib/leanix_client/                 # Shared GraphQL client
├── client.py
├── schema_fetcher.py
├── field_validator.py
└── patch_builder.py
```

### Testing

Test the tool with your LeanIX workspace:

1. Verify configuration exists:
```bash
cd ../create-provider
cat field_config.json | grep -A 5 '"Application"'
```

2. Test validation (should fail):
```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "test-id" \
  --type Application \
  --fields '{"invalidField": "value"}'
```

3. Test dry run (validate only):
```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "real-uuid" \
  --type Application \
  --fields '{"description": "Test"}' \
  --validate-only
```

4. Test actual update:
```bash
cd ../create-provider
python main.py update \
  --fact-sheet-id "real-uuid" \
  --type Application \
  --fields '{"description": "Updated application description"}'
```

## Application-Specific Research Guidelines

This skill follows 11 comprehensive guidelines to ensure data quality:

1. **Webpage URL** - Validate from 2+ authoritative sources
2. **Hosting Type** - Complete evaluation matrix for all 6 types
3. **Hosting Description** - Technical reasoning with 90% confidence threshold
4. **SSO Status** - Changelog-first detection strategy
5. **Pricing Type** - 6 pricing models with pricing page verification
6. **Product Category** - Most specific category from 50+ options
7. **Aliases** - Verified from official sources only
8. **Subtype** - application vs mobileApp classification
9. **Description** - Marketing language filter (18 buzzwords removed)
10. **Collection Status** - Fixed value: "inReview"
11. **As-of Date** - Fixed value: current date (YYYY-MM-DD)

See [guidelines/](guidelines/) directory for complete details.

## Troubleshooting

### Enable Verbose Mode

For detailed debugging information:
```bash
cd ../create-provider
python main.py update --fact-sheet-id "uuid" --type Application --fields '{}' --verbose
```

### Verify Configuration

Check if Application fields are configured:
```bash
cd ../create-provider
cat field_config.json | python -m json.tool | grep -A 20 '"Application"'
```

### Test Authentication

Run discovery with verbose mode to test authentication:
```bash
cd ../create-provider
python main.py discover --type Application --verbose
```

### Check API Token

Verify your token has the correct permissions:
- Read access to fact sheets
- Write access to fact sheets
- GraphQL API access

## License

Internal tool for LeanIX workspace management.

## Support

For issues or questions:
1. Check [WORKFLOW.md](WORKFLOW.md) for complete workflow details
2. Check [AGENT_INSTRUCTIONS.md](AGENT_INSTRUCTIONS.md) for agent-specific guidance
3. Run with `--verbose` flag to see detailed error messages
4. Verify environment variables are set correctly
5. Check that `../create-provider/field_config.json` includes Application fields
