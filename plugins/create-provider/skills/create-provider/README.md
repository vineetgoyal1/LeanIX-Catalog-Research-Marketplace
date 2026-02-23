# Provider Auto-Creation Skill

Automatically research and create LeanIX Provider fact sheets with minimal input using AI-powered research and verification.

## Quick Start (For Users)

Simply say to Claude Code:
```
Create Provider for [Provider Name or URL]
```

**Examples:**
- "Create Provider for Slack"
- "Create Provider for https://teamsmart.ai/"
- "Add Provider Microsoft"

The agent will automatically research and populate all fields. See [SKILL_INVOCATION_PATTERNS.md](SKILL_INVOCATION_PATTERNS.md) for all supported phrases.

---

## What This Skill Does

This skill automates Provider fact sheet creation through:

1. **Parallel Research**: Uses Perplexity MCP + WebFetch simultaneously
2. **Cross-Verification**: Compares multiple sources and resolves conflicts
3. **Quality Checks**: Validates data before creating fact sheets
4. **Auto-Population**: Fills 8 fields with verified information

**Fields Researched:**
- Homepage URL (validated from 2+ sources)
- Provider Category (Enterprise/Individual/Community)
- Aliases and former names
- Headquarters address
- Company description (organization-focused, 30-90 words)
- Collection status, as-of date, deprecated flag

---

## Overview

This directory contains a Provider auto-creation skill that combines:
- **AI Research** (Perplexity + WebFetch)
- **Python CLI Tool** (for LeanIX custom field updates via GraphQL API)
- **Comprehensive Guidelines** (5 guidelines for data quality)

The Python tool enables updating any custom field on LeanIX fact sheets, including fields not exposed by the standard MCP server:

1. **Discovery phase (one-time)**: Fetch available fields for each fact sheet type and save to a configuration file
2. **Update phase (fast)**: Validate fields against the configuration and execute GraphQL mutations

### Supported Fact Sheet Types

- **Application** - Standard LeanIX application fact sheets
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

### Step 1: Discover Available Fields (One-Time Setup)

Before updating fact sheets, discover the available fields for each type:

```bash
# Discover Provider fields
python main.py discover --type Provider

# Discover Application fields
python main.py discover --type Application

# Discover custom type fields
python main.py discover --type ProductFamily
```

This creates/updates `field_config.json` with all available fields.

**Example output:**
```
Discovering fields for fact sheet type: Provider
Using subdomain: demo-eu-10

✓ Discovered 45 fields for Provider:

  - aliases
  - description
  - displayName
  - headquartersAddress
  - homePageUrl
  - id
  - lifecycle
  - name
  - providerCategory
  - status
  ...

✓ Configuration saved to: field_config.json
```

### Step 2: Update Fact Sheets

Update any field on a fact sheet by providing the fact sheet ID, type, and fields to update:

```bash
python main.py update \
  --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \
  --type Provider \
  --fields '{"homePageUrl": "https://example.com", "aliases": "Alias1, Alias2"}'
```

**Example output:**
```
Updating fact sheet: e7630643-c87c-4def-87f2-0ca6d53ef798
Type: Provider
Fields: homePageUrl, aliases

✓ Update successful!

Result:
{
  "id": "e7630643-c87c-4def-87f2-0ca6d53ef798",
  "name": "Example Provider",
  "type": "Provider",
  "displayName": "Example Provider",
  "status": "active"
}
```

### Advanced Options

#### Validate Without Committing (Dry Run)

Test your update without making changes:

```bash
python main.py update \
  --fact-sheet-id "uuid" \
  --type Provider \
  --fields '{"homePageUrl": "https://example.com"}' \
  --validate-only
```

#### Verbose Mode

Enable detailed logging for debugging:

```bash
python main.py update \
  --fact-sheet-id "uuid" \
  --type Provider \
  --fields '{"description": "New description"}' \
  --verbose
```

#### Custom Configuration File

Use a different configuration file:

```bash
python main.py update \
  --fact-sheet-id "uuid" \
  --type Provider \
  --fields '{"name": "New Name"}' \
  --config my_config.json
```

## Supported Fields by Type

The tool dynamically discovers available fields during the discovery phase. Common fields include:

### Provider
- `homePageUrl` - Provider website URL
- `aliases` - Alternative names (comma-separated)
- `headquartersAddress` - Physical address
- `providerCategory` - Category classification
- `description` - Text description
- `lifecycle` - Lifecycle status
- Standard fields: `name`, `displayName`, `status`

### Application
- `description` - Application description
- `lifecycle` - Application lifecycle
- `functionalSuitability` - Functional fit score
- Custom fields specific to your workspace

### ITComponent
- `description` - Component description
- `lifecycle` - Component lifecycle
- `technicalSuitability` - Technical fit score
- Custom fields specific to your workspace

### ProductFamily (Custom Type)
- Fields specific to your workspace configuration
- Discovered during the discovery phase

## Field Configuration

### field_config.json Structure

After running discovery, `field_config.json` contains:

```json
{
  "Provider": {
    "fields": [
      "aliases",
      "description",
      "displayName",
      "headquartersAddress",
      "homePageUrl",
      "id",
      "lifecycle",
      "name",
      "providerCategory",
      "status"
    ]
  },
  "Application": {
    "fields": [...]
  }
}
```

### Customizing Available Fields

You can manually edit `field_config.json` to:
- Remove fields you don't use (faster validation)
- Add custom fields not discovered automatically
- Maintain a curated list of frequently used fields

If the LeanIX schema changes, re-run the discovery command to refresh the configuration.

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
Run 'python main.py discover --type <TYPE>' to generate it.
```
**Solution:** Run the discovery command for the fact sheet type.

**3. Invalid Field Name**
```
Validation failed:
  Invalid field 'invalidField' for type Provider.
  Allowed fields: aliases, description, displayName, ...
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

**6. Invalid JSON in --fields**
```
Error: Invalid JSON in --fields argument: Expecting property name enclosed in double quotes
```
**Solution:** Ensure the JSON is properly formatted with double quotes around keys and string values.

## Architecture

### Components

1. **main.py** - CLI entry point with `discover` and `update` commands
2. **lib/client.py** - GraphQL client with OAuth2 authentication
3. **lib/schema_fetcher.py** - Schema introspection and configuration management
4. **lib/field_validator.py** - Fast validation against configuration file
5. **lib/patch_builder.py** - JSON Patch operation builder

### Authentication Flow

1. Exchange technical user token (API token) for Bearer token via OAuth2
2. Cache Bearer token for the session
3. Use Bearer token for all GraphQL requests

### Update Flow

1. Load `field_config.json` (no API call)
2. Validate field names against configuration (instant)
3. If validation passes:
   - Authenticate via OAuth2
   - Build JSON Patch operations
   - Execute `updateFactSheet` GraphQL mutation
   - Return results

### Why This Approach?

- **Fast validation** - No API calls during field validation
- **User control** - Edit `field_config.json` to customize available fields
- **Supports custom types** - Discovers workspace-specific fact sheet types
- **Simple maintenance** - Re-run discovery if schema changes

## Examples

### Update Provider Homepage and Aliases

```bash
python main.py update \
  --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \
  --type Provider \
  --fields '{
    "homePageUrl": "https://example.com",
    "aliases": "Example Inc, Example Corp"
  }'
```

### Update Provider Headquarters Address

```bash
python main.py update \
  --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \
  --type Provider \
  --fields '{
    "headquartersAddress": "123 Main St, San Francisco, CA 94105, United States"
  }'
```

### Update Provider Category

```bash
python main.py update \
  --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \
  --type Provider \
  --fields '{
    "providerCategory": "Enterprise"
  }'
```

### Update Application Description

```bash
python main.py update \
  --fact-sheet-id "app-uuid-here" \
  --type Application \
  --fields '{
    "description": "Customer relationship management system"
  }'
```

### Update Multiple Fields at Once

```bash
python main.py update \
  --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \
  --type Provider \
  --fields '{
    "homePageUrl": "https://example.com",
    "aliases": "Example Inc, Example Corp",
    "headquartersAddress": "123 Main St, San Francisco, CA 94105, United States",
    "providerCategory": "Enterprise",
    "description": "Leading provider of enterprise software solutions"
  }'
```

## Development

### Project Structure

```
create-provider/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── field_config.json            # Generated configuration (gitignore)
├── main.py                      # CLI entry point
├── lib/                         # Provider-specific modules
│   ├── provider_researcher.py
│   ├── parallel_researcher.py
│   ├── verification_agent.py
│   └── perplexity_client.py
└── guidelines/                  # Provider research guidelines
    ├── schema_fetcher.py        # Schema discovery
    ├── field_validator.py       # Field validation
    └── patch_builder.py         # JSON Patch builder
```

### Testing

Test the tool with your LeanIX workspace:

1. Run discovery for all types you use:
```bash
python main.py discover --type Provider
python main.py discover --type Application
```

2. Test validation (should fail):
```bash
python main.py update \
  --fact-sheet-id "test-id" \
  --type Provider \
  --fields '{"invalidField": "value"}'
```

3. Test dry run (validate only):
```bash
python main.py update \
  --fact-sheet-id "real-uuid" \
  --type Provider \
  --fields '{"description": "Test"}' \
  --validate-only
```

4. Test actual update:
```bash
python main.py update \
  --fact-sheet-id "real-uuid" \
  --type Provider \
  --fields '{"description": "Updated description"}'
```

## Future Enhancements

Potential improvements for future versions:

- Batch updates (multiple fact sheets at once)
- CSV import for bulk updates
- Field type validation (string, number, enum, etc.)
- Support for nested field updates (relations, tags)
- Integration with LeanIX MCP server as a tool
- Support for `add` and `remove` operations (beyond `replace`)

## Troubleshooting

### Enable Verbose Mode

For detailed debugging information:
```bash
python main.py update --fact-sheet-id "uuid" --type Provider --fields '{}' --verbose
```

### Verify Configuration

Check what fact sheet types are configured:
```bash
cat field_config.json | python -m json.tool
```

### Test Authentication

Run discovery with verbose mode to test authentication:
```bash
python main.py discover --type Provider --verbose
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
1. Check this README for common solutions
2. Run with `--verbose` flag to see detailed error messages
3. Verify environment variables are set correctly
4. Re-run discovery if schema has changed
