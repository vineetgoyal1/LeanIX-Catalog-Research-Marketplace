# Application Webpage URL Guidelines

## Overview

This document provides guidelines for AI agents fetching and validating application webpage URLs. The goal is to ensure URLs point to the **specific application/product page**, not the provider's homepage, and that URLs are accurate, functional, and not hallucinated.

## Core Principles

### 1. **NEVER Hallucinate URLs**
- ❌ DO NOT construct URLs based on assumptions (e.g., "application-name.com")
- ❌ DO NOT guess domain extensions (.com, .io, .org, etc.)
- ❌ DO NOT fabricate URLs even if the application name seems obvious
- ✅ ONLY provide URLs that you can verify from actual search results or documentation

### 2. **Product Page, Not Provider Homepage**
The URL should point to the **specific application/product**, not the provider's main website.

**Examples**:
- ✅ **Good**: `https://www.adobe.com/products/photoshop.html` (Photoshop product page)
- ❌ **Bad**: `https://www.adobe.com` (Adobe homepage, not Photoshop-specific)

- ✅ **Good**: `https://slack.com` (Slack product has its own domain)
- ❌ **Bad**: `https://www.salesforce.com` (Salesforce homepage, even though they own Slack)

### 3. **Always Verify Before Returning**
Every URL must pass verification checks before being returned to the user.

---

## URL Retrieval Process

### Step 1: Search Strategy

When given an application name, use this search approach:

#### Primary Search Queries:

1. **Direct Product Search**: `"[Application Name]" official website`
   - Example: `"Smartsheet" official website`

2. **Product Page Search**: `"[Application Name]" product page`
   - Example: `"Adobe Photoshop" product page`

3. **Provider Context Search**: `"[Application Name]" [Provider Name]`
   - Example: `"Photoshop" Adobe`

#### Alternative Search Queries (if primary fails):

- `"[Application Name]" homepage`
- `"[Application Name]" site:[provider-domain]` (if provider known)
- `"[Application Name]" documentation`
- `"[Application Name]" download`
- `"[Application Name]" features`
- `"[Application Name]" pricing`

#### Use Multiple Sources:

Cross-reference results from:
- Search engine results (Google, Bing)
- Wikipedia entries
- Software review sites (G2, Capterra, TrustRadius)
- GitHub repositories (check README files)
- Software registries (npm, PyPI, Maven Central)
- Technology databases (Crunchbase, Product Hunt)
- App stores (Chrome Web Store, Microsoft Store, Mac App Store)

---

## Determining the Correct URL Type

Applications can have different URL patterns. Follow this decision tree:

### Pattern 1: Dedicated Product Domain
**When**: Product has its own domain separate from provider

**Examples**:
- Smartsheet → `https://www.smartsheet.com` (dedicated domain)
- Slack → `https://slack.com` (dedicated domain, even though owned by Salesforce)
- Trello → `https://trello.com` (dedicated domain, even though owned by Atlassian)

**How to identify**: Product name matches the domain name

### Pattern 2: Provider Domain with Product Path
**When**: Product page lives on provider's domain

**Examples**:
- Adobe Photoshop → `https://www.adobe.com/products/photoshop.html`
- Microsoft Teams → `https://www.microsoft.com/en-us/microsoft-teams/group-chat-software`
- Salesforce Marketing Cloud → `https://www.salesforce.com/products/marketing-cloud/`

**How to identify**: URL pattern is `[provider-domain]/products/[product-name]` or similar

### Pattern 3: Product Subdomain
**When**: Product has a subdomain under provider's domain

**Examples**:
- Google Analytics → `https://analytics.google.com`
- AWS Lambda → `https://aws.amazon.com/lambda/`
- Atlassian Confluence → `https://www.atlassian.com/software/confluence`

**How to identify**: Subdomain or clear product path under provider domain

### Pattern 4: GitHub/Open Source Project
**When**: Application is primarily distributed via GitHub

**Examples**:
- React → `https://reactjs.org` (dedicated docs site) OR `https://github.com/facebook/react`
- Kubernetes → `https://kubernetes.io` (dedicated docs site) OR `https://github.com/kubernetes/kubernetes`

**Priority order**:
1. Official project website (if exists)
2. Official documentation site
3. GitHub organization page
4. GitHub repository

### Pattern 5: Documentation-First Projects
**When**: Application's main presence is documentation

**Examples**:
- FastAPI → `https://fastapi.tiangolo.com`
- Django → `https://www.djangoproject.com`

**How to identify**: docs subdomain or documentation-focused landing page

---

## URL Validation Checks

Before accepting a URL, verify ALL of the following:

### A. **Source Verification**
- ✅ URL appears in multiple authoritative sources
- ✅ URL is mentioned in official documentation, app stores, or software reviews
- ✅ URL domain matches what's commonly referenced for this application
- ❌ Reject URLs that appear in only one source or unreliable sources

### B. **Product-Specific Content Verification**
After retrieving the URL, verify the page content mentions the **application name**:

- ✅ Page title/heading mentions the application name (not just provider name)
- ✅ Page describes the specific application's features and capabilities
- ✅ Page has product-specific information (pricing, features, download, demo)
- ✅ If it's a provider domain path, the page is clearly about this specific product
- ❌ Reject if: Page only mentions provider, lists multiple products without focusing on this one, is a generic landing page

**Example validation**:
- For "Adobe Photoshop", the page should mention "Photoshop" prominently, not just "Adobe Creative Cloud"
- For "Salesforce Marketing Cloud", the page should focus on Marketing Cloud features, not general Salesforce CRM

### C. **URL Structure Validation**

Acceptable patterns:
- ✅ `https://product-name.com` (dedicated product domain)
- ✅ `https://www.product-name.com` (with www)
- ✅ `https://provider.com/products/product-name` (product page on provider domain)
- ✅ `https://product-name.provider.com` (product subdomain)
- ✅ `https://github.com/organization/product-name` (for open source)
- ✅ `https://docs.product-name.com` (documentation-first projects)

**Warning signs** (require additional verification):
- ⚠️ Provider homepage: `https://provider.com` (too generic, unless product IS the provider's only product)
- ⚠️ Deep subpages: `https://example.com/en/us/products/category/subcategory/product` (try to find simpler product page)
- ⚠️ Third-party sites: `https://g2.com/products/...` (review sites, not official)
- ⚠️ Download-only pages: `https://example.com/downloads` (prefer product marketing page)

### D. **Domain Pattern Validation**

Check if the domain makes sense:
- ✅ Product domains typically use `.com`, `.io`, `.ai` (for tech products)
- ✅ Open source projects often use `.org`, `github.io`, or dedicated docs domains
- ✅ Provider-hosted products use provider's domain with product path
- ✅ Country-specific products may use country TLDs (`.de`, `.fr`, `.co.uk`)
- ❌ Be suspicious of generic domains or obviously incorrect TLDs

### E. **HTTP Response Validation**

Verify the URL is actually accessible:

```
1. Check HTTP status code:
   ✅ 200 (OK) - Accept
   ✅ 301/302 (Redirect) - Follow and verify destination
   ⚠️ 403 (Forbidden) - May be valid but blocking automated access, verify manually
   ❌ 404 (Not Found) - Reject
   ❌ 500+ (Server Error) - May be temporary, mark for retry
   ❌ Connection Timeout - Reject or mark as unreachable

2. Check redirect chains:
   ✅ Single redirect (http → https) - Normal, accept
   ✅ www → non-www or vice versa - Normal, accept
   ✅ Localized redirect (e.g., → /en-us/) - Normal, accept
   ⚠️ Multiple redirects - Verify final destination is legitimate
   ❌ Redirects to completely different domain - Likely invalid

3. Verify SSL/TLS:
   ✅ Valid HTTPS certificate - Preferred for enterprise
   ⚠️ HTTP only - Acceptable for older projects, but verify legitimacy
   ❌ SSL certificate errors - May indicate invalid or compromised site
```

---

## Distinguishing Application URL from Provider URL

**Critical Rule**: The URL should point to the **application**, not the provider.

### Decision Logic:

```
IF application has dedicated domain (e.g., slack.com for Slack)
  THEN use dedicated domain
ELSE IF application has product page on provider domain
  THEN use product page URL (e.g., adobe.com/products/photoshop)
ELSE IF application page is provider homepage AND application is provider's only product
  THEN provider homepage is acceptable
ELSE
  THEN continue searching for product-specific URL
```

### Examples:

| Application | Provider | Application URL | Provider URL |
|------------|----------|-----------------|--------------|
| Smartsheet | Smartsheet Inc. | `https://www.smartsheet.com` | `https://www.smartsheet.com` (same) |
| Photoshop | Adobe Inc. | `https://www.adobe.com/products/photoshop.html` | `https://www.adobe.com` |
| Slack | Salesforce | `https://slack.com` | `https://www.salesforce.com` |
| Google Analytics | Google | `https://analytics.google.com` | `https://www.google.com` |
| GitHub Copilot | GitHub | `https://github.com/features/copilot` | `https://github.com` |

### When Application = Provider's Main Product:

If the application IS the provider's primary/only product, the provider homepage is acceptable.

**Examples**:
- Smartsheet (application) = Smartsheet Inc. (provider) → `https://www.smartsheet.com` is correct for both
- Notion (application) = Notion Labs (provider) → `https://www.notion.so` is correct for both

---

## Red Flags: Signs of Hallucinated or Invalid URLs

### 🚩 **Critical Red Flags** (Reject immediately)
- URL domain has no search results or mentions
- URL returns 404 or doesn't resolve
- Page content doesn't mention the application name
- Page content is about a different product/application
- Domain is a parked/for-sale page
- Domain is obviously misspelled vs. application name in a suspicious way
- URL was constructed by the AI without any source verification
- URL points to provider homepage when application is clearly a separate product

### ⚠️ **Warning Signs** (Requires extra verification)
- URL found in only one source
- URL is a deep subpage or blog post, not a main product page
- Page lists multiple products without focusing on this specific one
- No HTTPS/SSL for modern enterprise application
- Generic landing page with no application-specific information
- Third-party site (G2, Capterra) rather than official source

---

## Handling Edge Cases

### Case 1: Application Name Has Multiple Products
**Example**: "Portal" could be many different products

**Solution**:
- Include provider context: `"Portal" Salesforce` or `"Portal" Microsoft`
- Search: `"[Application Name]" [Provider Name] official`
- Verify the URL content matches the specific application + provider combination

### Case 2: Application Website is Down/Unreachable
**Solution**:
- Try Web Archive (archive.org) to verify historical existence
- Check software review sites (G2, Capterra) for official links
- Check app stores (Chrome Web Store, Microsoft Store) for links
- Search for official social media accounts that may link to website
- If no verification possible, return: `"Unable to verify working URL"`
- **NEVER** fabricate a URL just because the site is down

### Case 3: Application Has Multiple Official URLs
**Example**: Application has both dedicated domain and provider product page

**Solution**:
- Prefer the dedicated product domain if it exists
- Priority order:
  1. Dedicated product domain (e.g., `slack.com`)
  2. Product page on provider domain (e.g., `adobe.com/products/photoshop`)
  3. Product subdomain (e.g., `analytics.google.com`)
  4. Official documentation site
  5. GitHub repository (for open source)

### Case 4: Application is Part of a Suite
**Example**: "Excel" is part of Microsoft 365

**Solution**:
- Search for the specific application within the suite
- Try: `"Excel" Microsoft official page`
- Acceptable URLs:
  - ✅ Dedicated page: `https://www.microsoft.com/en-us/microsoft-365/excel`
  - ⚠️ Suite page mentioning this app: `https://www.microsoft.com/microsoft-365` (if no specific page exists)
- Prefer application-specific page over suite page

### Case 5: Application is Acquired/Rebranded
**Solution**:
- Research current status: `"[Application] acquisition"` or `"[Application] rebranded"`
- If acquired: Use current product page under new ownership
  - Example: Slack acquired by Salesforce → Still use `https://slack.com`, not Salesforce homepage
- If rebranded: Use new product name and new URL
  - Example: "Google Hangouts" rebranded to "Google Chat" → Use Google Chat URL
- Document the status in notes: `"Acquired by X in 20XX"` or `"Rebranded to Y"`

### Case 6: Application is Open Source with Multiple Homes
**Example**: React has both reactjs.org and github.com/facebook/react

**Solution**:
- Prefer official project website over GitHub
- Priority order:
  1. Official project website (e.g., `https://reactjs.org`)
  2. Official documentation site (e.g., `https://docs.react.dev`)
  3. GitHub organization page (e.g., `https://github.com/facebook`)
  4. GitHub repository (e.g., `https://github.com/facebook/react`)

### Case 7: Application Name is Common Term
**Example**: "Select2", "Portal", "Realm"

**Solution**:
- Add technology context: `"Select2" jQuery plugin`
- Add provider context: `"Realm" MongoDB`
- Use quotes in search: `"Select2"` to exact match
- Cross-reference with package registries (npm, PyPI, etc.)

---

## Response Format

When returning URL information, use this structure:

```json
{
  "application_name": "Adobe Photoshop",
  "url": "https://www.adobe.com/products/photoshop.html",
  "url_type": "product_page_on_provider_domain",
  "url_status": "verified",
  "status_code": 200,
  "verification_method": "multiple_sources",
  "sources": ["official_website", "wikipedia", "g2_review"],
  "provider_url": "https://www.adobe.com",
  "confidence": "high",
  "notes": "Product page on Adobe domain with Photoshop-specific content",
  "last_verified": "2026-02-18"
}
```

### URL Type Values:
- `dedicated_domain` - Product has its own domain
- `product_page_on_provider_domain` - Product page on provider's website
- `product_subdomain` - Subdomain of provider (e.g., analytics.google.com)
- `documentation_site` - Documentation-first project
- `github_repository` - Open source project on GitHub
- `provider_homepage` - Provider homepage (only when application IS the provider's main product)

### Confidence Levels:
- **high**: URL verified from 3+ authoritative sources, returns 200, content matches application
- **medium**: URL verified from 2 sources, accessible, content mostly matches
- **low**: URL verified from 1 source or has minor issues (redirects, slow load)
- **unverified**: Cannot confirm URL validity

### When Unable to Verify:

If you cannot find a working, verified URL:

```json
{
  "application_name": "Example App",
  "url": null,
  "url_status": "not_found",
  "verification_method": "exhaustive_search",
  "confidence": "none",
  "notes": "No verifiable URL found. Possible reasons: discontinued product, name change, insufficient information, or application is only available through enterprise channels.",
  "last_verified": "2026-02-18"
}
```

**CRITICAL**: Return `null` or `"not_found"` rather than guessing or hallucinating a URL.

---

## Verification Checklist

Before returning any URL, confirm:

- [ ] URL was found through search/research, not constructed
- [ ] URL appears in at least 2 independent sources
- [ ] URL returns successful HTTP response (200 or valid redirect)
- [ ] Page content mentions the **application name** (not just provider)
- [ ] Page is application-specific (not provider homepage, unless application IS the provider's main product)
- [ ] Domain pattern is appropriate for application type
- [ ] No obvious red flags or suspicious patterns
- [ ] URL is the most direct/official application page available

If ANY checkbox is unchecked and cannot be resolved, either:
1. Continue searching with alternative queries, OR
2. Return `url_status: "unverified"` with explanation

---

## Tools and Methods

### Recommended Verification Tools:
1. **Perplexity AI**: For comprehensive web search with source citations
2. **Web Search APIs**: Google Custom Search, Bing Search API
3. **HTTP Checkers**: Test URL accessibility and response codes
4. **Software Review Sites**: G2, Capterra, TrustRadius (for official links)
5. **App Stores**: Chrome Web Store, Microsoft Store, Mac App Store
6. **Web Archive**: Check historical website data
7. **Package Registries**: npm, PyPI, Maven Central, NuGet (for dev tools)
8. **GitHub API**: Check repository metadata and README files

### Search Query Templates:
```
"[Application Name]" official website
"[Application Name]" product page
"[Application Name]" [Provider Name]
"[Application Name]" features
"[Application Name]" download
"[Application Name]" documentation
site:[provider-domain] "[Application Name]"
site:wikipedia.org "[Application Name]"
site:github.com "[Application Name]"
```

---

## Example Scenarios

### ✅ Good Example 1: Dedicated Domain
**Application**: Smartsheet

**Process**:
1. Search: `"Smartsheet" official website`
2. Found in: Wikipedia, G2 reviews, official website
3. URL: `https://www.smartsheet.com`
4. Verified: Returns 200, content clearly about Smartsheet product, multiple sources confirm
5. Provider URL: Same (Smartsheet Inc.'s main product)
6. Result: ✅ **Verified URL - Dedicated Domain**

### ✅ Good Example 2: Product Page on Provider Domain
**Application**: Adobe Photoshop

**Process**:
1. Search: `"Adobe Photoshop" official website`
2. Found in: Wikipedia, Adobe website, software review sites
3. URL: `https://www.adobe.com/products/photoshop.html`
4. Verified: Returns 200, page specifically about Photoshop features/pricing
5. Provider URL: `https://www.adobe.com` (different from application URL)
6. Result: ✅ **Verified URL - Product Page**

### ✅ Good Example 3: Open Source with Dedicated Docs
**Application**: React

**Process**:
1. Search: `"React" official website`
2. Found in: GitHub README, npm registry, official docs
3. URL: `https://reactjs.org` (or `https://react.dev`)
4. Verified: Returns 200, official React documentation site
5. Alternative URL: `https://github.com/facebook/react` (secondary)
6. Result: ✅ **Verified URL - Dedicated Docs Site (preferred over GitHub)**

### ❌ Bad Example 1: Hallucinated URL
**Application**: MyCoolTechApp

**Process**:
1. Search: `"MyCoolTechApp" official website`
2. No clear results found
3. AI constructs: `https://mycooltechapp.com` (WRONG!)
4. URL returns 404 or unrelated content
5. Result: ❌ **Hallucinated URL - REJECTED**

**Correct Approach**: Return `"url_status": "not_found"`

### ❌ Bad Example 2: Provider Homepage Instead of Product Page
**Application**: Adobe Photoshop

**Process**:
1. Search: `"Adobe Photoshop" official website`
2. AI returns: `https://www.adobe.com` (provider homepage)
3. Page doesn't focus on Photoshop specifically
4. Result: ❌ **Wrong URL - Provider Homepage, Not Product Page**

**Correct Approach**: Return `https://www.adobe.com/products/photoshop.html`

---

## Common Mistakes to Avoid

❌ **Returning provider homepage when application is a separate product**
  - Example: Returning `salesforce.com` for "Slack" (wrong - use `slack.com`)

❌ **Hallucinating product URLs based on name**
  - Example: Assuming "CoolApp" has `coolapp.com` without verification

❌ **Using third-party review sites as official URL**
  - Example: Returning G2 or Capterra page instead of official product page

❌ **Using generic marketing pages instead of product-specific pages**
  - Example: Returning `/products/` landing page listing multiple products

❌ **Not following redirects to verify final destination**
  - Example: Accepting a URL without checking where it redirects

❌ **Accepting deep subpages when simpler product page exists**
  - Example: `/en-us/products/category/subcategory/product` when `/products/product` exists

❌ **Confusing documentation URL with product marketing URL**
  - Prefer marketing/product page over docs (unless docs-first project)

---

## Summary

**DO**:
- Find application-specific URLs (not provider homepage)
- Verify URLs from multiple authoritative sources
- Prefer dedicated product domains when they exist
- Check that page content mentions the application name
- Use product pages on provider domains when no dedicated domain exists
- Follow redirects and verify final destination
- Return `null` if unable to verify

**DON'T**:
- Hallucinate or construct URLs without verification
- Return provider homepage when application is separate product
- Accept URLs from single unreliable source
- Use third-party sites (review sites) as official URL
- Guess domain extensions or paths
- Return generic pages that don't focus on the specific application

**Remember**: The URL should clearly lead to information about the **specific application**, not just the provider or a list of products. When in doubt, verify the page content mentions the application name prominently.

---

*Document created: 2026-02-18*
*Version: 1.0*
