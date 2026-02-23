## Provider Auto-Creation with Claude Code

### Overview

This guide explains how to create new Provider fact sheets in LeanIX with intelligent auto-research using Claude Code. The system researches and populates all required fields from just a provider name (and optionally a URL).

**What gets auto-populated:**
- Homepage URL (validated from multiple sources)
- Aliases (7 types discovered from official sources)
- Headquarters Address (from official website or business registries)
- Provider Category (Enterprise/Individual/Community Based)
- Collection Status (always "In Review")
- Description (30-90 words from provider's website)
- As-of Date (current date)
- Deprecated status (always "no")

**Workflow:**
1. You provide provider name (+ optional URL)
2. Claude researches all fields using Perplexity
3. Claude fact-checks the researched data
4. Claude creates the fact sheet in LeanIX
5. Claude updates custom fields via Python CLI
6. You get the fact sheet URL

---

## Prerequisites

### 1. Environment Setup

Set your LeanIX credentials as environment variables:

```bash
export LEANIX_API_TOKEN="LXT_your_token_here"
export LEANIX_SUBDOMAIN="your-subdomain"
```

To make these permanent, add to your `~/.zshrc` or `~/.bashrc`:

```bash
echo 'export LEANIX_API_TOKEN="LXT_your_token_here"' >> ~/.zshrc
echo 'export LEANIX_SUBDOMAIN="your-subdomain"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Claude Code with MCP Access

Ensure your Claude Code has access to:
- ✅ Perplexity MCP (for web research)
- ✅ LeanIX MCP (for fact sheet operations)

### 3. Python CLI Tool

The `create-provider` Python CLI must be available:

```bash
cd "/path/to/Catalog Research Skills/Catalog-Research-Skills/create-provider"
pip install -r requirements.txt
```

---

## Usage

### Basic Usage (Provider Name Only)

Simply ask Claude Code:

```
Create a new Provider fact sheet for [Provider Name]
```

**Examples:**

```
Create a new Provider fact sheet for Slack
```

```
Create a new Provider fact sheet for React
```

```
Create a new Provider fact sheet for DHH (David Heinemeier Hansson)
```

Claude will:
1. Research the provider using Perplexity
2. Discover homepage URL, aliases, headquarters, category
3. Fact-check all the data
4. Create and populate the fact sheet
5. Return the URL

### Advanced Usage (With Homepage URL)

If you already know the homepage URL:

```
Create a new Provider fact sheet for [Provider Name] with URL [website]
```

**Examples:**

```
Create a new Provider fact sheet for Slack with URL https://slack.com
```

```
Create a new Provider fact sheet for React with URL https://react.dev
```

This skips URL research and validates the provided URL instead.

---

## What Claude Does Behind the Scenes

### Step 1: Research (Perplexity MCP)

Claude uses Perplexity to research each field following strict guidelines:

**Homepage URL Research:**
- Searches for official website from multiple sources
- Validates HTTP status (200, 301, 302)
- Verifies SSL certificate
- Confirms page content mentions provider
- **Never hallucinates URLs** - returns null if uncertain

**Aliases Research:**
- Discovers 7 types: Abbreviations, Former Names, Legal Names, Product Names, Acquisition Names, Stylistic Variations
- Only includes verified aliases from official sources
- **Never fabricates** - only documents verified names

**Headquarters Research:**
- Searches official website (About, Contact, Footer, Legal/Imprint)
- Falls back to business registries and professional networks
- Accepts partial data (city-level or country-level if complete address unavailable)
- **For individuals:** Only provides city/country (privacy)
- **Never guesses addresses**

**Category Classification:**
- Applies strict decision tree:
  1. Single named person? → Individual
  2. Commercial company? → Enterprise
  3. Open-source/community? → Community Based
- Uses specific indicators for each category
- Provides reasoning for classification

**Description Research:**
- Extracts 30-90 word description from provider's own website
- Focuses on what they do, products/services, target audience
- Objective and factual (no marketing fluff)
- **Directly from provider's description** - not generated

### Step 2: Fact-Check (Perplexity MCP)

Claude runs verification queries to catch errors:

- **URL Verification:** Confirms URL is accessible and valid
- **Category Double-Check:** Reviews classification against decision tree
- **Alias Verification:** Removes unverifiable aliases
- **Description Quality:** Checks word count, accuracy, objectivity
- **Completeness Check:** Looks for inconsistencies or missing data

If issues are found, Claude corrects them before saving.

### Step 3: Create Fact Sheet (LeanIX MCP)

```
Uses: mcp__LeanIX_MCP_Server_Remote__create_fact_sheet
Creates: New Provider fact sheet in DRAFT state
Returns: Fact sheet ID
```

### Step 4: Update Custom Fields (Python CLI)

Claude calls the Python update tool:

```bash
python main.py update \
  --fact-sheet-id "{id}" \
  --type Provider \
  --fields '{
    "homePageUrl": "...",
    "aliases": "...",
    "headquartersAddress": "...",
    "providerCategory": "enterprise/individual/communityBased",
    "collectionStatus": "inReview",
    "description": "...",
    "asOfDate": "2026-02-18",
    "deprecated": "no"
  }'
```

This bypasses the LeanIX MCP server's limitations and uses GraphQL directly.

### Step 5: Return URL

```
https://{subdomain}.leanix.net/ltlsCollectionTesting/factsheet/Provider/{id}
```

---

## Expected Results

### Enterprise Example: Slack

**Input:**
```
Create a new Provider fact sheet for Slack
```

**Output:**
```
✓ Provider created successfully!

Provider: Slack
Category: enterprise
Homepage: https://slack.com
Aliases: Slack Technologies, Slack Technologies Inc
Headquarters: 500 Howard Street, San Francisco, CA 94105, United States
Description: Slack is a cloud-based team collaboration platform that provides messaging, file sharing, and integrations with various business applications. It serves businesses of all sizes seeking to improve team communication and productivity.

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/{id}
```

### Community Example: React

**Input:**
```
Create a new Provider fact sheet for React
```

**Output:**
```
✓ Provider created successfully!

Provider: React
Category: communityBased
Homepage: https://react.dev
Aliases: ReactJS, React.js
Headquarters: Menlo Park, CA, United States (Meta/Facebook)
Description: React is an open-source JavaScript library for building user interfaces, particularly single-page applications. Created and maintained by Facebook (Meta) and a large community of contributors, it uses a component-based architecture and virtual DOM for efficient rendering.

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/{id}
```

### Individual Example: DHH

**Input:**
```
Create a new Provider fact sheet for DHH
```

**Output:**
```
✓ Provider created successfully!

Provider: DHH
Category: individual
Homepage: https://dhh.dk
Aliases: David Heinemeier Hansson
Headquarters: Copenhagen, Denmark
Description: DHH is a Danish programmer and creator of Ruby on Rails framework. He is also co-founder and CTO of Basecamp, an independent software company. Known for his influential writings on software development and business philosophy.

URL: https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/{id}
```

---

## Error Handling

### Research Failures

**URL Not Found:**
```
⚠ Could not verify homepage URL from authoritative sources.

Please provide the homepage URL manually:
URL: [you type it here]
```

**Classification Uncertain:**
```
⚠ Provider category unclear - found indicators for both Enterprise and Community Based

Please select:
1. enterprise
2. individual
3. communityBased
Choice: [you type 1, 2, or 3]
```

**Incomplete Data:**
```
⚠ Some fields could not be researched:
- Headquarters address: Not found
- Aliases: No aliases discovered

Continue with partial data? [y/N]: y
```

### API Failures

**Perplexity MCP Unavailable:**
```
✗ Research failed: Perplexity MCP unreachable

Steps to fix:
- Check internet connection
- Verify Perplexity MCP is configured in Claude Code
- Try again in a few minutes
```

**LeanIX API Issues:**
```
✗ Update failed: LeanIX API authentication error

Steps to fix:
- Verify LEANIX_API_TOKEN is set correctly
- Check token has not expired
- Ensure LEANIX_SUBDOMAIN is correct
```

---

## Guidelines

The research process follows 4 comprehensive guideline documents:

1. **Provider_Classification_Definitions.md**
   - Decision tree: Individual → Enterprise → Community Based
   - Specific indicators for each category
   - Real examples from 269 provider dataset

2. **Provider_URL_Validation_Guidelines.md**
   - Multi-source verification (2+ authoritative sources)
   - HTTP status validation
   - SSL certificate checking
   - **Never hallucinate URLs** principle

3. **Provider_Headquarters_Address_Guidelines.md**
   - Official website first (About, Contact, Footer, Legal)
   - Business registries second (SEC, Companies House)
   - Accept partial data (city-level, country-level)
   - Privacy for individuals (city/country only)
   - **Never guess addresses** principle

4. **Provider_Alias_Discovery_Guidelines.md**
   - 7 alias types with verification requirements
   - Official sources prioritized
   - Cross-referencing required
   - **Never fabricate aliases** principle

These guidelines are located in:
```
/path/to/Catalog-Research-Skills/create-provider/guidelines/
```

---

## Fact Sheet Enum Values

**Important:** Use exact enum values for these fields:

### providerCategory
- `"enterprise"` - Commercial companies
- `"individual"` - Personal projects
- `"communityBased"` - Open-source/community

### collectionStatus
- `"inReview"` - Always set to this for new providers

### deprecated
- `"no"` - Always set to this for new providers

---

## Tips for Best Results

### 1. Provide Clear Provider Names

**Good:**
```
Create Provider for Slack
Create Provider for React
Create Provider for David Heinemeier Hansson
```

**Avoid:**
```
Create Provider for that chat app (ambiguous)
Create Provider for JS framework (too generic)
```

### 2. Include URL When Known

If you already know the official website, include it:

```
Create Provider for Acme Corp with URL https://acme.com
```

This saves research time and ensures accuracy.

### 3. Review the Output

Claude will show you all researched data before saving. Review:
- ✅ Category makes sense (Enterprise/Individual/Community)
- ✅ URL is correct
- ✅ Headquarters address is accurate
- ✅ Description is factual and 30-90 words

### 4. Manual Corrections

If any field is wrong after creation, you can update it:

```bash
python main.py update \
  --fact-sheet-id "{id}" \
  --type Provider \
  --fields '{"headquartersAddress": "Corrected address"}'
```

---

## Frequently Asked Questions

### Q: Can I create multiple providers at once?

Not yet. Create them one at a time. Each takes about 30-60 seconds.

### Q: What if the provider doesn't have a website?

The tool will mark the URL as "not found" and continue with other fields. You can add the URL later if you find it.

### Q: Can I use this for updating existing providers?

Currently, this is for creating NEW providers only. For updates, use the manual `update` command.

### Q: What happens if Perplexity can't find information?

Claude will inform you which fields couldn't be researched and ask if you want to:
1. Provide the data manually
2. Continue with partial data
3. Cancel the operation

### Q: How accurate is the auto-research?

The fact-checking layer catches most errors, but you should still review:
- Provider category classification
- Homepage URL validity
- Headquarters address accuracy

The system prioritizes **not hallucinating data** over completeness.

### Q: Can colleagues in different LeanIX workspaces use this?

Yes! Each colleague:
1. Sets their own LEANIX_API_TOKEN
2. Sets their own LEANIX_SUBDOMAIN
3. Uses their own Claude Code with Perplexity MCP

The tool will work with their workspace.

---

## Troubleshooting

### Issue: "Python CLI not found"

**Solution:**
```bash
cd "/path/to/Catalog-Research-Skills/create-provider"
pip install -r requirements.txt
```

### Issue: "Field validation failed"

**Solution:** Re-run discovery to update field_config.json:
```bash
python main.py discover --type Provider
```

### Issue: "Perplexity MCP not available"

**Solution:** Check Claude Code MCP configuration:
1. Verify Perplexity MCP is installed
2. Check MCP settings in Claude Code
3. Restart Claude Code if needed

### Issue: "Custom fields not updating"

**Solution:** The Python CLI updates custom fields via GraphQL. Verify:
1. LEANIX_API_TOKEN has write permissions
2. Python CLI is accessible in PATH
3. Field names in field_config.json are correct

---

## Advanced Usage

### Batch Creation (Coming Soon)

Future version will support:
```
Create Provider fact sheets for: Slack, Zoom, Microsoft Teams
```

### Custom Field Updates (Available Now)

After creation, update any field:

```bash
python main.py update \
  --fact-sheet-id "{id}" \
  --type Provider \
  --fields '{
    "yearFounded": "2013",
    "city": "San Francisco",
    "country": "United States"
  }'
```

---

## Support

For issues or questions:
1. Check this guide's Troubleshooting section
2. Review the guideline documents in `guidelines/`
3. Test with `--verbose` flag for detailed output
4. Check Claude Code logs for MCP errors

Remember: The system prioritizes **accuracy over speed** and **verification over guessing**.
