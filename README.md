# LeanIX Catalog Research Marketplace

A Claude Code plugin marketplace for LeanIX catalog research and data collection. Automate provider and application fact sheet creation with verified, high-quality data through parallel research and agent verification.

## Quick Start

Install this marketplace in Claude Code:

```bash
claude plugin marketplace add https://github.com/vineetgoyal1/LeanIX-Catalog-Research-Marketplace.git
```

Then browse and install plugins:

```bash
claude plugin install create-application@leanix-catalog-research-marketplace
claude plugin install create-provider@leanix-catalog-research-marketplace
```

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| **create-application** | Automatically research and create LeanIX Application fact sheets with verified data through parallel research (Perplexity + WebFetch) and agent verification | 1.0.0 |
| **create-provider** | Automatically research and create LeanIX Provider fact sheets with verified data through parallel research and agent verification | 1.0.0 |

## What's Included

- **Automated Research** — Parallel data collection from multiple sources (Perplexity API, web scraping)
- **Agent Verification** — Cross-source validation and conflict resolution
- **Quality Checks** — Confidence scoring and validation before fact sheet creation
- **LeanIX Integration** — Direct fact sheet creation via LeanIX MCP server
- **Comprehensive Guidelines** — 11+ guideline documents covering all field types

## Plugin Features

### create-application

**Researches and creates Application fact sheets with:**
- Description (factual, 30-90 words, no marketing language)
- Webpage URL (official validation)
- Hosting Type (SaaS, PaaS, IaaS, Mobile, On-Premise, Other)
- SSO Status (with evidence from multiple sources)
- Pricing Type and URL
- Product Category (matched against 3,120+ existing categories)
- Aliases (former names, abbreviations, variants)
- SI ID (unique identifier with collision detection)

**Workflow:**
1. Parallel Research (13 simultaneous queries)
2. Agent Verification (conflict resolution)
3. Quality Check (>70% confidence required)
4. LeanIX Creation (MCP + Python CLI)

### create-provider

**Researches and creates Provider fact sheets with:**
- Description (organization-focused, not product-focused)
- URL (never hallucinated, verified from official sources)
- Classification (Enterprise, Community Based, Individual)
- Headquarters Address (city, state/region, country)
- Aliases (7 types: abbreviations, former names, domains, etc.)

**Workflow:**
1. Parallel Research (Perplexity + WebFetch)
2. Agent Verification (cross-source validation)
3. Quality Check (confidence scoring)
4. LeanIX Creation (MCP + Python CLI)

## Prerequisites

**Required MCP Servers:**
- LeanIX MCP Server (for fact sheet creation)
- Perplexity MCP Server (for AI-powered research)

**Required Environment Variables:**
- `LEANIX_API_TOKEN` - Your LeanIX API token (starts with LXT_)
- `LEANIX_SUBDOMAIN` - Your LeanIX subdomain (e.g., demo-eu-10)

**Optional:**
- WebFetch tool (for direct website scraping)

## Usage Examples

### Create an Application

```
Create application for Watchwire
```

or

```
Add application for https://watchwire.ai
```

### Create a Provider

```
Create provider for Datadog
```

or

```
Research provider https://www.datadoghq.com
```

## Contributing

Want to contribute? See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Quick Steps

1. Fork the repository
2. Create your plugin in `plugins/your-plugin-name/`
3. Add plugin metadata in `.claude-plugin/plugin.json`
4. Update `.claude-plugin/marketplace.json`
5. Submit a pull request

## Project Structure

```
LeanIX-Catalog-Research-Marketplace/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace metadata
├── plugins/
│   ├── create-application/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json       # Plugin metadata
│   │   └── skills/
│   │       └── create-application/
│   │           ├── SKILL.md      # Main skill instructions
│   │           ├── WORKFLOW.md   # Detailed workflow
│   │           ├── guidelines/   # 11 field-specific guidelines
│   │           └── lib/          # Python modules for research
│   └── create-provider/
│       └── [similar structure]
└── README.md
```

## Support

- **Questions**: Create an issue in this repository
- **Maintainer**: Vineet Goyal (@vineetgoyal1)

## License

MIT License - See [LICENSE](./LICENSE) for details

---

**Built for LeanIX Catalog Research Automation**
