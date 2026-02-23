# Provider Auto-Creation - Quick Start

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
- Example: In `https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/123`
  - Subdomain: `demo-eu-10`
  - Workspace: `ltlsCollectionTesting` ← This is what you need

## Usage

Just ask Claude Code:

```
Create a new Provider fact sheet for [Provider Name]
```

or

```
Create a new Provider fact sheet for [Provider Name] with URL [website]
```

## Examples

```
Create a new Provider fact sheet for Slack
```

```
Create a new Provider fact sheet for React with URL https://react.dev
```

```
Create a new Provider fact sheet for David Heinemeier Hansson
```

## What Gets Created

- ✅ Homepage URL (researched & validated)
- ✅ Aliases (discovered from multiple sources)
- ✅ Headquarters Address (official sources)
- ✅ Provider Category (Enterprise/Individual/Community)
- ✅ Description (30-90 words from their website)
- ✅ Collection Status: "In Review"
- ✅ As-of Date: Today's date
- ✅ Deprecated: "no"

## Result

You get a fact sheet URL:
```
https://{your-subdomain}.leanix.net/{your-workspace}/factsheet/Provider/{id}
```

Example: `https://demo-eu-10.leanix.net/ltlsCollectionTesting/factsheet/Provider/abc123`

## Need More Info?

See full guide: `PROVIDER_CREATION_GUIDE.md`
