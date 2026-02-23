# Provider Website URL Validation Guidelines

## Overview
This document provides guidelines for AI agents fetching and validating provider website URLs. The goal is to ensure URLs are accurate, functional, and not hallucinated.

---

## Core Principles

### 1. **NEVER Hallucinate URLs**
- ❌ DO NOT construct URLs based on assumptions (e.g., "company-name.com")
- ❌ DO NOT guess domain extensions (.com, .io, .org, etc.)
- ❌ DO NOT fabricate URLs even if the provider name seems obvious
- ✅ ONLY provide URLs that you can verify from actual search results or documentation

### 2. **Always Verify Before Returning**
Every URL must pass verification checks before being returned to the user.

---

## URL Retrieval Process

### Step 1: Search Strategy
When given a provider name, use this search approach:

1. **Primary Search Query**: `"[Provider Name]" official website`
   - Example: `"SimpleSAMLphp" official website`

2. **Alternative Search Queries** (if primary fails):
   - `"[Provider Name]" homepage`
   - `"[Provider Name]" site:github.com` (for open source projects)
   - `"[Provider Name]" documentation`
   - `"[Provider Name]" about`

3. **Use Multiple Sources**: Cross-reference results from:
   - Search engine results (Google, Bing)
   - Wikipedia entries
   - GitHub repositories (check README files)
   - Software registries (npm, PyPI, Maven Central)
   - Technology databases (Crunchbase, Product Hunt)

### Step 2: URL Validation Checks

Before accepting a URL, verify ALL of the following:

#### A. **Source Verification**
- ✅ URL appears in multiple authoritative sources
- ✅ URL is mentioned in official documentation, GitHub repos, or registry listings
- ✅ URL domain matches what's commonly referenced for this provider
- ❌ Reject URLs that appear in only one source or unreliable sources

#### B. **Domain Pattern Validation**
Check if the domain makes sense:
- ✅ Company names typically use `.com`, `.io`, `.ai` (for tech companies)
- ✅ Open source projects often use `.org`, `github.io`, or `.org.io`
- ✅ Academic/research institutions use `.edu`, `.ac.uk`, or institution domains
- ✅ Country-specific companies may use country TLDs (`.de`, `.fr`, `.co.uk`)
- ❌ Be suspicious of generic domains or obviously incorrect TLDs

#### C. **URL Structure Validation**
- ✅ URL should be the homepage/root domain or a clear official subdomain
- ✅ Acceptable patterns:
  - `https://example.com`
  - `https://www.example.com`
  - `https://docs.example.com` (for documentation-first projects)
  - `https://github.com/organization/project` (for GitHub-based projects)
- ⚠️ **Warning signs** (require additional verification):
  - Subpages: `https://example.com/products/specific-tool` (try to get root domain)
  - Deep links: `https://example.com/en/us/products/...`
  - Third-party hosted: `https://wordpress.com/user/...`

#### D. **Content Verification**
After retrieving the URL, verify the page content:
- ✅ Page title/heading mentions the provider name
- ✅ Page clearly describes the provider's products/services
- ✅ Page has "About," "Contact," or "Documentation" sections
- ✅ Page shows recent activity or updates (not abandoned)
- ❌ Reject if: Page is a 404, parked domain, unrelated content, or spam

### Step 3: HTTP Response Validation

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
   ⚠️ Multiple redirects - Verify final destination is legitimate
   ❌ Redirects to completely different domain - Likely invalid

3. Verify SSL/TLS:
   ✅ Valid HTTPS certificate - Preferred for enterprise
   ⚠️ HTTP only - Acceptable for older projects, but verify legitimacy
   ❌ SSL certificate errors - May indicate invalid or compromised site
```

---

## Red Flags: Signs of Hallucinated or Invalid URLs

### 🚩 **Critical Red Flags** (Reject immediately)
- URL domain has no search results or mentions
- URL returns 404 or doesn't resolve
- Page content is completely unrelated to the provider
- Domain is a parked/for-sale page
- Domain is obviously misspelled vs. provider name in a suspicious way
- URL was constructed by the AI without any source verification

### ⚠️ **Warning Signs** (Requires extra verification)
- URL found in only one source
- Domain extension doesn't match provider type (e.g., `.com` for foundation)
- Very recent domain registration for supposedly established provider
- No HTTPS/SSL for modern enterprise provider
- Generic landing page with no specific information
- Aggressive ads or suspicious redirects

---

## Handling Edge Cases

### Case 1: Provider Name Has Multiple Entities
**Example**: "Apple" could be Apple Inc. or Apache Software Foundation's Apple project

**Solution**:
- Include context from the description/category in search
- Search: `"Apple Inc" official website technology`
- Verify the URL content matches the specific provider context

### Case 2: Provider Website is Down/Unreachable
**Solution**:
- Try Web Archive (archive.org) to verify historical existence
- Check GitHub repo for links in README
- Search for official social media accounts that may link to website
- If no verification possible, return: `"Unable to verify working URL"`
- **NEVER** fabricate a URL just because the site is down

### Case 3: Provider Has Multiple Official URLs
**Example**: Project has both GitHub page and official website

**Solution**:
- Prefer the official website over GitHub if both exist
- Priority order:
  1. Official company/project website
  2. Official documentation site
  3. GitHub organization page
  4. GitHub repository (as last resort)

### Case 4: Provider Name is Common Term
**Example**: "Select2" or "Realm"

**Solution**:
- Add technology context: `"Select2" jQuery plugin official`
- Use quotes in search: `"Select2"` to exact match
- Cross-reference with package registries (npm, Maven, etc.)

### Case 5: Provider is Acquired/Discontinued
**Solution**:
- Research current status: `"[Provider] acquisition"` or `"[Provider] discontinued"`
- If acquired: Use acquiring company's page for the product
- If discontinued: Use archived site or last known working URL + note discontinuation
- Document the status in metadata: `status: "acquired"` or `status: "discontinued"`

---

## Response Format

When returning URL information, use this structure:

```json
{
  "provider_name": "Example Provider",
  "url": "https://example.com",
  "url_status": "verified",
  "status_code": 200,
  "verification_method": "multiple_sources",
  "sources": ["official_website", "github_readme", "npm_registry"],
  "confidence": "high",
  "notes": "Active project with recent updates",
  "last_verified": "2026-02-16"
}
```

### Confidence Levels
- **high**: URL verified from 3+ authoritative sources, returns 200, content matches
- **medium**: URL verified from 2 sources, accessible, content mostly matches
- **low**: URL verified from 1 source or has minor issues (redirects, slow load)
- **unverified**: Cannot confirm URL validity

### When Unable to Verify
If you cannot find a working, verified URL:

```json
{
  "provider_name": "Example Provider",
  "url": null,
  "url_status": "not_found",
  "verification_method": "exhaustive_search",
  "confidence": "none",
  "notes": "No verifiable URL found. Possible reasons: discontinued project, name change, or insufficient information.",
  "last_verified": "2026-02-16"
}
```

**CRITICAL**: Return `null` or `"not_found"` rather than guessing or hallucinating a URL.

---

## Verification Checklist

Before returning any URL, confirm:

- [ ] URL was found through search/research, not constructed
- [ ] URL appears in at least 2 independent sources
- [ ] URL returns successful HTTP response (200 or valid redirect)
- [ ] Page content mentions the provider name
- [ ] Page content matches expected provider type (enterprise/community/individual)
- [ ] Domain pattern is appropriate for provider type
- [ ] No obvious red flags or suspicious patterns

If ANY checkbox is unchecked and cannot be resolved, either:
1. Continue searching with alternative queries, OR
2. Return `url_status: "unverified"` with explanation

---

## Tools and Methods

### Recommended Verification Tools
1. **Perplexity AI**: For comprehensive web search with source citations
2. **Web Search APIs**: Google Custom Search, Bing Search API
3. **HTTP Checkers**: Test URL accessibility and response codes
4. **Domain WHOIS**: Verify domain registration and age
5. **Web Archive**: Check historical website data
6. **Package Registries**: npm, PyPI, Maven Central, NuGet (for tech packages)
7. **GitHub API**: Check repository metadata and README files

### Search Query Templates
```
"[Provider Name]" official website
"[Provider Name]" homepage
"[Provider Name]" documentation
"[Provider Name]" github repository
"[Provider Name]" about company
site:github.com "[Provider Name]"
site:wikipedia.org "[Provider Name]"
```

---

## Example Scenarios

### ✅ Good Example
**Provider**: SimpleSAMLphp

**Process**:
1. Search: `"SimpleSAMLphp" official website`
2. Found in: Wikipedia, GitHub README, official documentation
3. URL: `https://simplesamlphp.org`
4. Verified: Returns 200, content matches, multiple sources confirm
5. Result: ✅ **Verified URL**

### ❌ Bad Example (Hallucination)
**Provider**: MyCoolTechTool

**Process**:
1. Search: `"MyCoolTechTool" official website`
2. No clear results found
3. AI constructs: `https://mycooltool.com` (WRONG!)
4. URL returns 404 or unrelated content
5. Result: ❌ **Hallucinated URL - REJECTED**

**Correct Approach**: Return `"url_status": "not_found"` with note about inability to verify

---

## Error Handling

### If URL fetch fails during validation:
```
1. Retry once after 2-second delay
2. If still fails, try alternative search query
3. If no working URL found, document:
   - Search queries attempted
   - Sources checked
   - Reason for failure
4. Return structured error response (see Response Format above)
5. NEVER return an unverified URL
```

---

*Document created: 2026-02-16*
*Version: 1.0*
