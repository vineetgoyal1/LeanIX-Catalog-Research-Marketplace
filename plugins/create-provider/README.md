# create-provider

Automatically research and create LeanIX Provider fact sheets with verified data through parallel research and agent verification.

## Features

- **Parallel Research**: Perplexity + WebFetch in parallel
- **Agent Verification**: Cross-source validation and conflict resolution
- **Never Hallucinate URLs**: Only uses verified, official sources
- **Classification Logic**: Enterprise, Community Based, or Individual
- **Partial Data Acceptable**: Returns state/country if full address unavailable
- **Alias Discovery**: 7 types of aliases with verification

## Fields Researched

| Field | Sources | Validation |
|-------|---------|------------|
| Description | Official Website, About Page | Organization-focused, not product-focused |
| URL | Official Website | Never hallucinated, verified from official sources |
| Classification | Business Research | Enterprise, Community Based, Individual |
| Headquarters Address | Official Sources, Business Registries | City, State/Region, Country (partial acceptable) |
| Aliases | Historical Research | 7 types: former names, abbreviations, domains, etc. |

## Usage

```
Create provider for Datadog
```

or

```
Research provider https://www.datadoghq.com
```

## Workflow

### Step 1: Parallel Research
- Perplexity query for all fields
- WebFetch queries (homepage, about, contact)

### Step 2: Agent Verification
- Cross-source validation
- Conflict resolution
- Confidence scoring

### Step 3: Quality Check
- Overall confidence > 70%
- URL never hallucinated
- Classification logic verified
- Description is organization-focused

### Step 4: Create & Update
- Create fact sheet via LeanIX MCP
- Update custom fields via Python CLI
- Report success

## Guidelines

This plugin includes 5 comprehensive guidelines:

1. **Provider_Description_Guidelines.md** - Organization-focused, not product-focused
2. **Provider_URL_Validation_Guidelines.md** - Never hallucinate, verify from official sources
3. **Provider_Classification_Definitions.md** - 3 categories with decision tree
4. **Provider_Headquarters_Address_Guidelines.md** - Official sources, partial data acceptable
5. **Provider_Alias_Discovery_Guidelines.md** - 7 alias types with examples

## Classification Decision Tree

```
1. Single named person/personal portfolio? → Individual
2. Commercial company with business operations? → Enterprise
3. Open-source project/foundation/community? → Community Based
```

## Alias Types

1. **Abbreviations/Acronyms** - Official or common short forms
2. **Former Names** - Pre-acquisition, pre-rebranding names
3. **Product Variations** - Different editions or related products
4. **Parent Company Variants** - Brand name changes, company prefixes
5. **Shortened Names** - Commonly used shortened versions
6. **Commonly Known Names** - Names users might search for
7. **Domain Variants** - Domain names commonly used to refer to the provider

## Prerequisites

**Required:**
- LeanIX MCP Server
- Perplexity MCP Server
- Environment variables: `LEANIX_API_TOKEN`, `LEANIX_SUBDOMAIN`

**Optional:**
- WebFetch tool (for direct website scraping)

## Output Example

```
✅ Provider Created Successfully!

Provider: Datadog
Overall Confidence: 95% (HIGH)

Verified Data Summary:
├─ URL: https://www.datadoghq.com ✓✓ (both sources)
├─ Classification: Enterprise ✓✓ (commercial company)
├─ Headquarters: New York, NY, United States ✓ (official source)
├─ Aliases: Datadog Inc. ✓
└─ Description: 82 words ✓✓ (organization-focused)

LeanIX URL: https://demo-eu-10.leanix.net/...
Status: Ready for review team approval
```

## Version

1.0.0

## Author

Vineet Goyal <vineet.goyal@sap.com>
