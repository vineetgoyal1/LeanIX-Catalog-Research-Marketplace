# Provider Alias Discovery Guidelines

## Overview
This document provides guidelines for AI agents to discover and document provider aliases through web search. Aliases include former names, abbreviations, legal names, brand names, product names, and other name variations that providers operate under.

---

## Core Principles

### 1. **NEVER Fabricate Aliases**
- ❌ DO NOT create abbreviations or acronyms without verification
- ❌ DO NOT assume shortened names without evidence
- ❌ DO NOT guess former company names
- ✅ ONLY provide aliases found from credible sources

### 2. **Prioritize Official Sources**
Always check these sources in order of priority:
1. **Provider's official website** (About Us, "formerly known as", legal notices)
2. **Company descriptions** (self-reported on profiles)
3. **Press releases** (acquisitions, rebrands, name changes)
4. **Business registries** (legal entity names)
5. **LinkedIn/Crunchbase** (company name fields and "also known as")
6. **Wikipedia** (with proper citations)
7. **News articles** (about rebrands or acquisitions)

### 3. **Document All Variations**
- ✅ Capture all aliases found, not just the most common
- ✅ Note the relationship type (former name, abbreviation, brand name, etc.)
- ✅ Include dates when name changes occurred (if available)

---

## Types of Aliases

### Type 1: Abbreviations and Acronyms

**Description**: Shortened forms of the full provider name, typically using initial letters.

**Pattern Recognition**:
- Usually 2-5 characters
- All uppercase or mixed case
- Often used in casual/industry reference

**Examples from Dataset**:
- "Ten Thousand Coffees" → **10KC**
- "American Express Global Business Travel" → **GBT**
- "Agenzia Dogane e Monopoli" → **ADM**
- "Advanced Markets" → **AMG**
- "Automated Payment Transfer" → **APT**

**Search Strategy**:
```
"[Provider Full Name]" acronym
"[Provider Full Name]" abbreviated as
"[Provider Full Name]" also known as
"[Provider Full Name]" ([XX]) where XX is potential acronym
```

**Example**:
```
Search: "Ten Thousand Coffees" also known as
Result: "10KC" commonly used abbreviation
```

---

### Type 2: Former Names (Pre-Rebrand)

**Description**: Previous company names before rebranding, often indicated by "formerly", "previously known as", or "rebranded from".

**Pattern Recognition**:
- Keywords: "formerly", "previously", "used to be", "rebranded from"
- Often found in About pages, press releases, Wikipedia
- May include acquisition-related name changes

**Examples from Dataset**:
- "Sign In Scheduling" (formerly **10to8**)
- "Xurrent" (formerly **4me**)
- "Uptempo" (formerly **BrandMaker**, **Allocadia**, **Hive9**)
- "Ambassador" (formerly **Datawire**)
- "data.ai" (formerly **App Annie**)
- "Scopevisio Retail Solutions" (formerly **act'o-soft**)
- "Saasty" (formerly **Agile Toolkit**)

**Search Strategy**:
```
"[Provider Name]" formerly known as
"[Provider Name]" previously called
"[Provider Name]" rebranded from
"[Provider Name]" used to be
"[Provider Name]" acquisition history
site:[provider-website.com] formerly
```

**Critical**: When former names are found, try to determine:
- When the name change occurred (year/date)
- Reason for change (rebrand, acquisition, merger)
- Whether old addresses/documentation still use old name

---

### Type 3: Legal Name vs. Brand Name

**Description**: The registered legal entity name differs from the marketing/brand name.

**Pattern Recognition**:
- Legal names often include: Ltd, LLC, GmbH, Inc., Corp, S.A., B.V., etc.
- Brand names are simpler, more memorable
- Legal name often found in: Terms of Service, Privacy Policy, Legal/Imprint pages, footer

**Examples from Dataset**:
- Brand: **"Mekari"** → Legal: "Mid Solusi Nusantara"
- Brand: **"Alias Digital"** → Display: "SoftDigital"
- Brand: **"Apowersoft"** → Legal: "Wangxu Technology"
- Brand: **"Accept SBR Online"** → Legal: "Accept Development B.V."
- Brand: **"AnyFlip"** → Legal: "Wonder Idea Technology"

**Search Strategy**:
```
site:[provider-website.com] legal notice
site:[provider-website.com] imprint
site:[provider-website.com] privacy policy
site:[provider-website.com] terms of service
"[Brand Name]" legal entity
"[Brand Name]" registered as
"[Brand Name]" is a trademark of
```

**Where to Find**:
1. Website footer (often shows legal entity)
2. Legal/Imprint page (required in EU)
3. Privacy Policy (data controller name)
4. Terms of Service (contracting entity)
5. Company registration databases

---

### Type 4: Product Names vs. Company Names

**Description**: The company may be known by its flagship product name rather than the corporate entity.

**Pattern Recognition**:
- Company makes one dominant product
- Product name becomes synonymous with company
- Description mentions "provider of [Product]" or "[Product] is developed by [Company]"

**Examples from Dataset**:
- Company: **"Altirnao"** → Product: "AODocs"
- Company: **"Kovan Studio"** → Product: "AnnounceKit"
- Company: **"Go-Cort"** → Product: "Apptoto"
- Company: **"Steady Space"** → Products: "8012 Labs", "Status Hero"
- Company: **"Data Discovery Solutions"** → Product: "ActiveNav"

**Search Strategy**:
```
"[Product Name]" developed by
"[Product Name]" created by
"[Product Name]" company
"[Product Name]" is a product of
"[Company Name]" produces
"[Company Name]" is the maker of
```

**Note**: Sometimes the product becomes so dominant the company rebrands to match (e.g., company adopts product name).

---

### Type 5: Acquisition-Related Aliases

**Description**: Names change after acquisition, merger, or spin-off. Company may operate under parent name or maintain separate brand.

**Pattern Recognition**:
- Keywords: "acquired by", "part of", "subsidiary of", "division of", "merged with"
- May show: "Company X, a [Parent] company"
- Parent company name may become prefix/suffix

**Examples from Dataset**:
- **"Kiteworks"** (formerly "Accellion")
- **"Hewlett Packard Enterprise / HPE Aruba Networking"** (formerly "Aruba Networks")
- **"CaseWare Germany"** (formerly "Audicon")
- **"SimonsVoss Technologies"** (now under "Allegion")
- **"CODESYS GmbH"** (member of "CODESYS Group")

**Search Strategy**:
```
"[Provider Name]" acquired by
"[Provider Name]" acquisition
"[Provider Name]" part of
"[Provider Name]" subsidiary
"[Provider Name]" merged with
"[Provider Name]" parent company
```

**Documentation**: Note both the acquired brand and parent company, as searches may use either name.

---

### Type 6: Stylistic Variations and Formatting

**Description**: Same name with different formatting, spacing, capitalization, or special characters.

**Pattern Recognition**:
- Different capitalization: "softdigital" vs "SoftDigital"
- Spacing differences: "Ten Times" vs "TenTimes"
- Special characters: "//SEIBERT/MEDIA" vs "Seibert Media"
- Domain-based: "pdfforge.org" vs "pdfforge"
- Numeric substitutions: "10times" vs "Ten Times"

**Examples from Dataset**:
- "Seibert Group" → **//SEIBERT/MEDIA**
- "AVTECH SECURITY" → **AV TECH**
- "Ten Times Online" → **10times**, **10times Online**
- "Avanquest pdfforge" → **pdfforge.org**
- "Petri Lehtinen" → **akheron**, **akhern** (username variations)

**Search Strategy**:
```
"[Provider Name]" (try variations)
[ProviderName] (no spaces)
[PROVIDERNAME] (all caps)
[Provider-Name] (with dashes)
Check: Twitter handle, GitHub username, domain name
```

---

### Type 7: Multiple Aliases (Consolidated)

**Description**: Providers may have multiple aliases from different sources (mergers, products, rebrands).

**Examples from Dataset**:
- "Uptempo" → **Allocadia**, **Hive9**, **BrandMaker**
- "3M" → **3M Global**, **3M Visual Attention Software**
- "Channelscaler" → **Allbound**, **Channel Mechanics**
- "Ambassador" → **Ambassador Labs**, **Datawire**
- "OFA" → **Actradis**, **OnceForAll**

**How to Handle**:
- Document all aliases found
- Note the relationship for each (e.g., "Allocadia: acquired and merged into Uptempo")
- Maintain list format, comma or newline separated

---

## Alias Discovery Workflow

### Step 1: Check Official Website

**Priority Locations**:
1. **About Us page** - Look for:
   - "Formerly known as..."
   - "Previously..."
   - Company history/timeline
   - Merger and acquisition mentions

2. **Homepage** - Check:
   - Tagline or subtitle (may mention products)
   - Footer legal name
   - Logo variations

3. **Legal/Imprint page** (EU companies) - Shows:
   - Registered legal entity name
   - Company registration number
   - May differ from brand name

4. **Press/News section** - Look for:
   - Rebrand announcements
   - Acquisition news
   - Name change press releases

5. **Terms of Service / Privacy Policy** - Contains:
   - Legal entity name as data controller
   - Contracting party name

### Step 2: Search External Sources

**Professional Databases**:
```
site:linkedin.com "[Provider Name]" also known as
site:crunchbase.com "[Provider Name]" formerly
site:wikipedia.org "[Provider Name]" also called
```

**News and Press**:
```
"[Provider Name]" rebrand
"[Provider Name]" formerly known as
"[Provider Name]" acquired by
"[Provider Name]" changes name
```

**Business Registries**:
- Check company registration databases for legal names
- SEC filings (for US public companies)
- Companies House (for UK companies)
- National business registers

### Step 3: Cross-Reference Multiple Sources

- ✅ Verify alias appears in 2+ sources when possible
- ✅ Check if alias is still actively used or historical
- ✅ Determine timeline of alias usage
- ⚠️ Be cautious of user-generated content (verify from official sources)

---

## Validation Checks

### Before Documenting an Alias:

**A. Source Verification**
- ✅ Alias found on official website OR verified from 2+ authoritative sources
- ✅ Clear evidence of relationship (not speculation)
- ✅ Source is credible (official, business database, reputable news)
- ❌ Do not include aliases from unreliable sources only

**B. Relationship Clarity**
- ✅ Understand WHY this is an alias (former name, abbreviation, legal name, etc.)
- ✅ Know WHEN the alias was used (if former name, when did it change?)
- ✅ Determine if ACTIVELY USED or historical

**C. Formatting Standards**
- ✅ Preserve original formatting/capitalization from official sources
- ✅ Include special characters if that's the official form
- ✅ Note if multiple format variations exist

---

## Response Format

### Standard Alias Documentation

```json
{
  "provider_name": "Example Provider",
  "aliases": [
    {
      "alias": "EP",
      "type": "abbreviation",
      "status": "active",
      "source": "official_website",
      "source_url": "https://example.com/about",
      "verified_date": "2026-02-16"
    },
    {
      "alias": "OldCorp",
      "type": "former_name",
      "status": "historical",
      "date_changed": "2020-03",
      "reason": "rebrand",
      "source": "press_release",
      "source_url": "https://example.com/news/rebrand",
      "verified_date": "2026-02-16"
    },
    {
      "alias": "Example Provider Ltd",
      "type": "legal_name",
      "status": "active",
      "source": "company_registry",
      "source_url": "https://companieshouse.gov.uk/...",
      "verified_date": "2026-02-16"
    }
  ],
  "primary_name": "Example Provider",
  "confidence": "high",
  "notes": "Company rebranded from OldCorp in March 2020. Legal entity remains Example Provider Ltd."
}
```

### Alias Types Classification

- **abbreviation**: Acronym or shortened form
- **former_name**: Previous company name before rebrand
- **legal_name**: Official registered business name
- **brand_name**: Marketing/consumer-facing name
- **product_name**: Known by product rather than company
- **parent_company**: Acquired, now part of larger org
- **subsidiary**: Operates under parent but maintains name
- **stylistic_variation**: Different formatting of same name
- **dba**: "Doing Business As" name
- **trademark**: Registered trademark name

### Status Values

- **active**: Currently in use
- **historical**: Used in the past, no longer active
- **concurrent**: Multiple names used simultaneously
- **regional**: Used in specific geographic regions

---

## Common Scenarios

### Scenario 1: Simple Abbreviation
**Provider**: "American Express Global Business Travel"
**Alias Found**: "GBT" (on website, in marketing materials)

**Result**:
```json
{
  "aliases": [
    {
      "alias": "GBT",
      "type": "abbreviation",
      "status": "active"
    }
  ]
}
```

### Scenario 2: Recent Rebrand
**Provider**: "Sign In Scheduling"
**Alias Found**: Description says "formerly 10to8"

**Result**:
```json
{
  "aliases": [
    {
      "alias": "10to8",
      "type": "former_name",
      "status": "historical",
      "reason": "rebrand",
      "notes": "Rebranded to Sign In Scheduling, old name still recognized"
    }
  ]
}
```

### Scenario 3: Legal vs Brand Name
**Provider**: "Mekari" (brand)
**Legal Entity**: "Mid Solusi Nusantara"

**Result**:
```json
{
  "provider_name": "Mekari",
  "aliases": [
    {
      "alias": "Mid Solusi Nusantara",
      "type": "legal_name",
      "status": "active",
      "notes": "PT Mid Solusi Nusantara is the legal entity, branded as Mekari"
    },
    {
      "alias": "PT Mid Solusi Nusantara",
      "type": "legal_name",
      "status": "active"
    }
  ]
}
```

### Scenario 4: Multiple Acquisitions
**Provider**: "Uptempo"
**Aliases**: Formerly "BrandMaker", also acquired "Allocadia" and "Hive9"

**Result**:
```json
{
  "aliases": [
    {
      "alias": "BrandMaker",
      "type": "former_name",
      "status": "historical",
      "reason": "rebrand"
    },
    {
      "alias": "Allocadia",
      "type": "former_name",
      "status": "historical",
      "reason": "acquired_and_merged",
      "notes": "Allocadia acquired and merged into Uptempo platform"
    },
    {
      "alias": "Hive9",
      "type": "former_name",
      "status": "historical",
      "reason": "acquired_and_merged",
      "notes": "Hive9 acquired and merged into Uptempo platform"
    }
  ]
}
```

### Scenario 5: Product Known Better Than Company
**Provider**: "Altirnao"
**Product**: "AODocs" (more widely known)

**Result**:
```json
{
  "provider_name": "Altirnao",
  "aliases": [
    {
      "alias": "AODocs",
      "type": "product_name",
      "status": "active",
      "notes": "AODocs is the main product, often used interchangeably with company name"
    }
  ]
}
```

### Scenario 6: No Aliases Found
**Provider**: Individual developer with single name

**Result**:
```json
{
  "provider_name": "John Developer",
  "aliases": [],
  "confidence": "medium",
  "notes": "Individual developer. No aliases, former names, or abbreviations found after exhaustive search.",
  "search_attempts": [
    "Official website checked",
    "GitHub profile checked",
    "LinkedIn profile checked",
    "No aliases found"
  ]
}
```

---

## Special Considerations

### For Individual Developers

- **Username Variations**: Check GitHub, Twitter, LinkedIn usernames
  - Example: "Petri Lehtinen" uses "akheron" on GitHub, "akhern" elsewhere
- **Legal vs. Username**: May be known by username in community
- **No Fabrication**: Don't create nicknames - only document what's publicly used

### For Acquired Companies

- **Dual Identity Period**: Company may use both old and new names during transition
- **Legacy Documentation**: Old name may appear in older docs, support articles
- **URL Redirects**: Old domain often redirects to new (check for former domains)
- **Press Releases**: Acquisition announcements are goldmines for alias information

### For International Companies

- **Regional Names**: May operate under different names in different countries
- **Translation Variations**: Same company, different language names
- **Legal Requirements**: Some countries require local legal entities
  - Example: "Adobe Systems" in US, local subsidiaries elsewhere

### For Rebrands

- **Gradual Transition**: Both names may coexist for months/years
- **Legacy Products**: Old products may keep old branding
- **Customer Confusion**: Aliases help customers find provider under old name
- **Date Documentation**: Try to find when rebrand occurred

---

## Red Flags: Invalid Aliases

### ❌ Do NOT Include:

1. **Competitor Names**: Just because they're in same industry doesn't make them aliases
2. **Partner Companies**: Integration partners are not aliases
3. **Customer References**: "Used by Microsoft" doesn't make Microsoft an alias
4. **Generic Terms**: "CRM software" is not an alias
5. **Unverified Speculation**: Forum posts guessing at former names
6. **Domain Squatters**: Someone registered similar domain ≠ alias
7. **Typos/Misspellings**: "Microsft" is not an alias of "Microsoft"

### ⚠️ Requires Extra Verification:

1. **User-Generated Content**: Wikipedia without citations, forum posts
2. **Outdated Information**: Check if alias is still current
3. **Regional Variations**: Confirm it's actually used, not just registered
4. **Trademark Disputes**: Company may have changed name due to legal issues

---

## Verification Checklist

Before returning alias information, confirm:

- [ ] Alias found through credible sources (official website, business database, verified news)
- [ ] Relationship type clearly understood (abbreviation, former name, etc.)
- [ ] Status determined (active, historical, concurrent)
- [ ] Timeline understood (when name was used, when it changed)
- [ ] Source URL documented for verification
- [ ] No fabrication or speculation involved
- [ ] Formatting preserved from official source
- [ ] Multiple aliases properly categorized

If ANY checkbox is unchecked and cannot be resolved:
1. Lower confidence level, OR
2. Mark alias as "unverified" with caveats, OR
3. Exclude alias if verification impossible

---

## Search Query Templates

### For Abbreviations/Acronyms
```
"[Full Provider Name]" acronym
"[Full Provider Name]" abbreviated as
"[Full Provider Name]" also known as
"[Full Provider Name]" ([XX])
"[XX]" stands for "[Full Provider Name]"
```

### For Former Names
```
"[Provider Name]" formerly
"[Provider Name]" previously known as
"[Provider Name]" rebranded from
"[Provider Name]" used to be called
"[Provider Name]" changed name
site:[provider-website.com] formerly
```

### For Legal Names
```
site:[provider-website.com] legal notice
site:[provider-website.com] imprint
site:[provider-website.com] privacy policy "controller"
site:[provider-website.com] terms "contracting party"
"[Brand Name]" registered as
"[Brand Name]" is a trademark of
"[Brand Name]" LLC OR "Ltd" OR "GmbH" OR "Inc"
```

### For Acquisitions
```
"[Provider Name]" acquired by
"[Provider Name]" acquisition announcement
"[Provider Name]" part of
"[Provider Name]" subsidiary of
"[Parent Company]" acquires "[Provider]"
```

### For Product-Company Relationship
```
"[Product Name]" developed by
"[Product Name]" company behind
"[Company Name]" makes "[Product]"
"[Company Name]" is the provider of "[Product]"
```

---

## Dataset Insights

Based on analysis of the "Alias & address.xlsx" dataset (143 providers with aliases):

### Alias Type Distribution (Approximate)
- **Former names/Rebrands**: ~25%
- **Abbreviations/Acronyms**: ~20%
- **Legal vs Brand names**: ~20%
- **Product names**: ~15%
- **Multiple aliases (mergers/acquisitions)**: ~15%
- **Stylistic variations**: ~5%

### Common Patterns
1. **Enterprise companies** typically have 1-3 aliases
2. **Recently acquired companies** often have 2-5 aliases (old names + parent)
3. **Individual developers** usually have 0-1 aliases (username)
4. **Startups/Scale-ups** frequently rebrand (multiple former names)

### Expected Alias Availability
- Enterprise: ~80-90% have at least one alias
- Community-based: ~50-60% have aliases
- Individual: ~20-30% have aliases (mostly usernames)

---

## Examples from Real Dataset

### Example 1: Simple Abbreviation ✅
```
Display Name: "Ten Thousand Coffees"
Alias: "10KC"
Type: Abbreviation
Status: Active
```

### Example 2: Rebrand ✅
```
Display Name: "Xurrent"
Alias: "4me"
Type: Former Name
Status: Historical
Context: Rebranded from 4me to Xurrent
```

### Example 3: Legal vs Brand ✅
```
Display Name: "SoftDigital"
Alias: "Alias Digital"
Type: Brand Name
Status: Active
Context: Marketed as "Alias Digital", company is SoftDigital
```

### Example 4: Multiple Aliases (Acquisition) ✅
```
Display Name: "Uptempo"
Aliases: "Allocadia, Hive9, BrandMaker"
Types: Former Names (multiple acquisitions/rebrand)
Status: Historical
Context: Merged multiple companies, formerly known as BrandMaker
```

### Example 5: Product Name ✅
```
Display Name: "Data Discovery Solutions"
Alias: "ActiveNav"
Type: Product Name
Status: Active
Context: Company makes ActiveNav product, known by product name
```

### Example 6: Stylistic Variation ✅
```
Display Name: "Seibert Group"
Alias: "//SEIBERT/MEDIA"
Type: Stylistic Variation
Status: Active
Context: Different formatting with special characters
```

---

## Quick Reference

### Must-Check Sources (in order):
1. ✅ Official website About/History page
2. ✅ Official website footer (legal name)
3. ✅ Legal/Imprint page
4. ✅ Company description (LinkedIn, Crunchbase)
5. ✅ Press releases (acquisitions, rebrands)
6. ✅ Business registries

### Key Search Terms:
- "formerly known as"
- "previously called"
- "rebranded from"
- "acquired by"
- "also known as"
- "abbreviated as"
- "is a trademark of"

### When to Return Empty Aliases:
- Individual developer with no username variations
- New company with no history
- No aliases found after thorough search
- **NEVER fabricate aliases to avoid empty returns**

---

*Document created: 2026-02-16*
*Version: 1.0*
*Dataset Reference: "Alias & address.xlsx" (143 providers analyzed)*
