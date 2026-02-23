# Application Auto-Creation - Quick Start

## Setup (One-Time)

```bash
# 1. Set your LeanIX credentials
export LEANIX_API_TOKEN="LXT_your_token_here"
export LEANIX_SUBDOMAIN="your-subdomain"
export LEANIX_WORKSPACE="your-workspace-name"

# 2. Ensure Python CLI is ready
cd "/Users/I529175/Desktop/Claude/Catalog Research Skills/Catalog-Research-Skills/create-provider"
pip install -r requirements.txt
```

**How to find your workspace name:**
- Open any fact sheet in LeanIX
- Look at the URL: `https://{subdomain}.leanix.net/{workspace}/factsheet/...`
- The part between the subdomain and `/factsheet/` is your workspace name
- Example: In `https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/123`
  - Subdomain: `demo-eu-10`
  - Workspace: `ltlsCollectionTesting` ← This is what you need

## Usage

Just ask Claude Code:

```
Create a new Application fact sheet for [Application Name]
```

or

```
Create a new Application fact sheet for [Application Name] with URL [website]
```

## Examples

```
Create a new Application fact sheet for Smartsheet
```

```
Create a new Application fact sheet for Salesforce with URL https://www.salesforce.com
```

```
Create a new Application fact sheet for Zoom
```

## What Gets Created

- ✅ Webpage URL (researched & validated from 2+ sources)
- ✅ Hosting Type (evaluated with 6-type matrix: saas/paas/iaas/onPremise/hybrid/mobile)
- ✅ Hosting Description (technical classification reasoning)
- ✅ SSO Status (changelog-first detection)
- ✅ Pricing Type (free/freemium/subscription/perpetual/transaction/enterprise)
- ✅ Product Category (most specific from 50+ categories)
- ✅ Aliases (discovered from multiple sources)
- ✅ Application Subtype (application vs mobileApp)
- ✅ Description (marketing-filtered, 30-90 words)
- ✅ Collection Status: "inReview"
- ✅ As-of Date: Today's date (YYYY-MM-DD)
- ✅ Deprecated: "no"

## Result

You get a fact sheet URL:
```
https://{your-subdomain}.leanix.net/{your-workspace}/factsheet/Application/{id}
```

Example: `https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Application/abc123`

## Need More Info?

See full guide: `WORKFLOW.md`
