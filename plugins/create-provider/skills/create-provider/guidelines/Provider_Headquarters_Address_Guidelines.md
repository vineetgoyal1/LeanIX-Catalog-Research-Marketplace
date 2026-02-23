# Provider Headquarters Address Fetching Guidelines

## Overview
This document provides guidelines for AI agents fetching and validating provider headquarters addresses through web search. The goal is to obtain accurate, verifiable address information while prioritizing official sources.

---

## Core Principles

### 1. **NEVER Hallucinate Addresses**
- ❌ DO NOT construct addresses based on assumptions or partial information
- ❌ DO NOT guess city, state, or country based on provider name
- ❌ DO NOT fabricate street addresses, building numbers, or postal codes
- ✅ ONLY provide address information that you can verify from credible sources

### 2. **Prioritize Official Sources**
Always check these sources in order of priority:
1. **Provider's official website** (About Us, Contact, Legal/Imprint pages)
2. **Official press releases or news announcements**
3. **Company registration databases** (SEC filings, Companies House, etc.)
4. **Professional business databases** (LinkedIn, Crunchbase, Bloomberg)
5. **Verified news articles from reputable sources**
6. **Wikipedia** (only if properly cited)

### 3. **Accept Partial Information**
- ✅ Complete address is preferred but not mandatory
- ✅ Return whatever level of detail is verifiable
- ✅ Clearly indicate the level of detail available

---

## Address Information Hierarchy

### Level 1: Complete Address (Preferred)
```
Building/Office Name (if applicable)
Street Address with Number
City/Town, State/Province, Postal Code
Country
```
**Real Examples from Dataset**:
- "Via Cavour 2, Lomazzo, Italia 22074, IT"
- "18 King St. East, suite 1400, Toronto, Ontario M5C 1C4, Canada"
- "LiusenForum, 5. OG Kirchgasse 6, 65185 Wiesbaden, Germany"
- "3280 Peachtree Rd NE, Atlanta, Georgia 30305, USA"

**Address Format Variations**:
- **US Format**: Street, City, State ZIP, Country
  - Example: "150 2nd Ave N, Suite 1540, St. Petersburg, Florida 33701"
- **European Format**: Street, Postal Code City, Country
  - Example: "Große Bergstraße 219, Hamburg, 22767, Germany"
- **Asian Format**: Building, Street, City Postal Code
  - Example: "10 F, E Building, No. 19-11 San Chung Rd., Nankang, Taipei, 115"

### Level 2: City-Level Address
```
City/Town, State/Province, Country
```
**Real Examples from Dataset**:
- "Boston, Massachusetts, USA"
- "Palo Alto, California, United States"
- "London, WC1V 6RL, GB" (includes postal code when available)

### Level 3: State/Province-Level
```
State/Province, Country
```
**Example**: "California, United States"

### Level 4: Country-Level Only
```
Country
```
**Real Examples from Dataset**:
- "United States"
- "Germany"
- "India"

### Level 5: Building/Campus Name (for known locations)
```
Building/Campus Name, City, Country
```
**Real Example**: "3M Center, St. Paul, Minnesota, 55144-1000, United States"

---

## Address Format Standards

### Recognizing Different International Formats

When extracting and formatting addresses, recognize and preserve the local conventions:

**1. United States/Canada Format**:
```
[Building/Suite], [Street Number Street Name]
[City], [State/Province] [Postal Code]
[Country]
```
Examples:
- "555 Bryant Street #156 Palo Alto, California 94301 USA"
- "75 State St, Floor 26, Boston, Massachusetts 02109, USA"

**2. European Format (Germany, France, Italy)**:
```
[Building/Company Name]
[Street Name Street Number]
[Postal Code] [City]
[Country]
```
Examples:
- "Große Bergstraße 219, Hamburg, 22767, Germany"
- "53, Rue de Châteaudun, Paris, Île-de-France 75009"
- "Via Cavour 2, Lomazzo, Italia 22074, IT"

**3. UK Format**:
```
[Building/Company Name]
[Street Number] [Street Name]
[City], [Postal Code]
[Country]
```
Example:
- "High Holborn House, 1st Floor, 52-54 High Holborn, London, WC1V 6RL, GB"

**4. Asian Format (varies by country)**:
```
[Building/Floor], [Street Name/Number]
[District], [City] [Postal Code]
[Country]
```
Examples:
- "10 F, E Building, No. 19-11 San Chung Rd., Nankang, Taipei, 115" (Taiwan)
- "Mid Plaza 2, Jl. Jenderal Sudirman No.4, Kel. Karet Tengsin, Kec. Tanah Abang, Kota Jakarta Pusat, Jakarta 10220" (Indonesia)
- "19H Maxgrand Plaza, No.3 Tai Yau Street, San Po Kong, Kowloon Hong Kong" (Hong Kong)

**5. India Format**:
```
[Building/Company], [Floor/Suite]
[Street/Area], [Landmark]
[City], [State] [Postal Code], [Country]
```
Example:
- "Sopan baug, Balewadi, 303, Archway, Pune, Maharashtra 411045, India"

### Address Formatting Guidelines

1. **Preserve Original Format**: Keep the address in the format found on the official source
2. **Include All Components**: Building names, floor numbers, suite numbers if provided
3. **Multiline Addresses**: Accept multiline format when that's how it appears on official sources
4. **Country Codes**: Use full country names preferred, but accept ISO codes (US, GB, DE, etc.)
5. **Postal Codes**: Include when available, position according to local convention
6. **Special Characters**: Preserve special characters (ß, ä, ö, ü, é, ñ, etc.)

### Common Patterns Observed

From the dataset analysis:
- **Enterprise companies**: Usually have complete street addresses
- **Asian companies**: Often include detailed floor/building information
- **European companies**: Frequently use postal code before city
- **US companies**: State abbreviations common (CA, NY, TX) but full names also acceptable
- **Individual developers**: Rarely have addresses (privacy)
- **Some providers**: No address found despite thorough search (null values acceptable)

---

## Provider Aliases and Name Variations

### Understanding Aliases

Providers often operate under multiple names. When searching for headquarters addresses:

**Common Alias Patterns**:
1. **Brand vs Legal Name**: Display name differs from legal entity
   - Display: "Mekari" → Legal: "Mid Solusi Nusantara"
   - Display: "Uptempo" → Former: "BrandMaker"

2. **Shortened Names/Acronyms**:
   - "Ten Thousand Coffees" → Alias: "10KC"
   - "American Express Global Business Travel" → Alias: "GBT Travel Services"
   - "Advanced Markets" → Alias: "AMG"

3. **Product Names vs Company Names**:
   - Company: "Altirnao" → Product: "AODocs"
   - Company: "Wonder Idea Technology" → Product: "AnyFlip"
   - Company: "Wangxu Technology" → Brand: "Apowersoft"

4. **Rebrands/Name Changes**:
   - "Sign In Scheduling" (formerly "10to8")
   - "Xurrent" (formerly "4me")
   - "data.ai" (formerly "App Annie")

5. **Formatting Variations**:
   - "SoftDigital" → Alias: "Alias Digital"
   - "AVTECH SECURITY" → Alias: "AV TECH"
   - "Seibert Group" → Alias: "//SEIBERT/MEDIA"

### Search Strategy with Aliases

When searching for headquarters address:

1. **Try Primary Name First**: Use the display name provided
2. **Check for Aliases**: If primary search fails, try known aliases
3. **Search with Quotes**: Use exact match searches for unusual names
4. **Try Multiple Variations**: Search both "10 times" and "Ten Times Online"
5. **Check Legal Name**: Official addresses often listed under legal entity name
6. **Look for "formerly known as"**: May indicate recent rebrand with old addresses still listed

**Example Search Progression**:
```
Primary: "Uptempo" headquarters address
Alias: "BrandMaker" headquarters address
Combined: "Uptempo formerly BrandMaker" headquarters
Legal: "Uptempo marketing operations" headquarters
```

### Recording Alias Information

When documenting addresses, include alias information for future reference:

```json
{
  "provider_name": "Mekari",
  "legal_name": "Mid Solusi Nusantara",
  "aliases": ["Mekari", "PT Mid Solusi Nusantara"],
  "address": "Mid Plaza 2, Jl. Jenderal Sudirman No.4, Jakarta 10220",
  "notes": "Company branded as Mekari, legal name is PT Mid Solusi Nusantara"
}
```

---

## Search Strategy

### Step 1: Check Provider's Official Website First

**Priority Search Locations** (in order):
1. **"About Us" or "About" page**
2. **"Contact Us" or "Contact" page**
3. **"Legal" or "Imprint" page** (especially for European companies)
4. **"Locations" or "Offices" page**
5. **Footer of homepage** (many companies list HQ address)
6. **Press/Media page** (often has contact/address info)
7. **Investor Relations page** (for public companies)
8. **Terms of Service or Privacy Policy** (may include registered address)

**Search Pattern on Official Website**:
- Look for keywords: "headquarters", "HQ", "head office", "registered office", "corporate office", "main office"
- Check meta tags and schema.org structured data
- Look for physical addresses (not P.O. Boxes unless that's the only option)

### Step 2: External Search Queries

If official website doesn't have address information, use these search queries:

**Primary Queries**:
```
"[Provider Name]" headquarters address
"[Provider Name]" head office location
"[Provider Name]" corporate office address
"[Provider Name]" registered office
```

**For Specific Entity Types**:

**Enterprise/Companies**:
```
"[Provider Name]" company address headquarters
"[Provider Name]" site:linkedin.com headquarters
"[Provider Name]" site:crunchbase.com headquarters
"[Provider Name]" SEC filing address (for US public companies)
"[Provider Name]" investor relations address
```

**Community-Based/Foundations**:
```
"[Provider Name]" foundation registered address
"[Provider Name]" organization location
"[Provider Name]" nonprofit address
"[Provider Name]" site:guidestar.org (for US nonprofits)
```

**Individual Developers**:
```
"[Provider Name]" developer location
"[Provider Name]" based in
"[Provider Name]" site:linkedin.com location
"[Provider Name]" site:github.com location
```

### Step 3: Secondary Sources

If primary sources fail, check:

1. **Business Registries**:
   - US: SEC EDGAR database, state business registries
   - UK: Companies House
   - EU: Company registers by country
   - Other: Local business registration databases

2. **Professional Networks**:
   - LinkedIn company pages
   - Crunchbase profiles
   - AngelList profiles

3. **News and Press**:
   - Company press releases
   - News articles mentioning headquarters
   - Acquisition or funding announcements

4. **Technology Databases**:
   - GitHub organization profiles
   - Product Hunt company pages
   - Tech news sites (TechCrunch, VentureBeat)

---

## Validation Checks

### A. **Source Credibility**
- ✅ Official website information (highest credibility)
- ✅ Government/regulatory filings
- ✅ Verified business databases (LinkedIn, Crunchbase with citations)
- ✅ Reputable news sources with recent dates
- ⚠️ Wikipedia (verify citations and check multiple sources)
- ❌ User-generated content without verification
- ❌ Outdated information (>3 years old for companies, >5 years for individuals)

### B. **Address Consistency**
- ✅ Address appears in multiple independent sources
- ✅ Address format matches country conventions
- ✅ City/state/country combinations are valid
- ⚠️ Multiple addresses found (may indicate multiple offices)
- ❌ Conflicting addresses from different sources (requires investigation)

### C. **Address Type Verification**
Identify and note the type of address:

- **Corporate Headquarters**: Main operational center
- **Registered Office**: Legal/mailing address (may differ from HQ)
- **Branch Office**: Secondary location (not HQ)
- **Mailing Address**: P.O. Box or mail forwarding service
- **Virtual Office**: Co-working or virtual office service
- **Personal Address**: Individual's home/residence (handle with privacy care)

**Preference Order**: Corporate HQ > Registered Office > Mailing Address

### D. **Recency Check**
- ✅ Information from last 1-2 years (current)
- ⚠️ Information from 2-5 years ago (may be outdated, verify)
- ❌ Information older than 5 years (likely outdated)

**Note**: Check for company relocations, acquisitions, or name changes

---

## Handling Different Provider Types

### Enterprise Companies

**Best Sources**:
1. Official website (Contact/About pages)
2. SEC filings (for US public companies)
3. Company registration documents
4. LinkedIn company page
5. Annual reports

**What to Look For**:
- Full street address with suite/floor number
- Corporate headquarters vs. registered office distinction
- Multiple locations (identify which is HQ)

**Example Output**:
```json
{
  "address_level": "complete",
  "address": "1600 Amphitheatre Parkway, Mountain View, CA 94043, United States",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "https://abc.xyz/contact/",
  "verified_date": "2026-02-16",
  "confidence": "high"
}
```

### Community-Based Organizations

**Best Sources**:
1. Official website (often in footer or About page)
2. Foundation registration documents
3. Nonprofit databases (GuideStar, Charity Navigator)
4. GitHub organization profile
5. Conference/event announcements

**What to Look For**:
- Registered address (often required for legal entities)
- Physical vs. virtual presence
- Host organization or fiscal sponsor address

**Common Scenarios**:
- **Scenario 1**: Foundation with physical office → Provide full address
- **Scenario 2**: Decentralized project with no physical HQ → Indicate "No physical headquarters" + project origin country if known
- **Scenario 3**: Hosted by another organization → Provide host organization address + note relationship

**Example Output**:
```json
{
  "address_level": "city",
  "address": "San Francisco, California, United States",
  "address_type": "registered_office",
  "source": "foundation_website",
  "source_url": "https://foundation.org/about",
  "verified_date": "2026-02-16",
  "confidence": "medium",
  "notes": "Decentralized project, no physical headquarters. Address is fiscal sponsor location."
}
```

### Individual Developers

**Best Sources**:
1. Personal website or portfolio (if they choose to share)
2. LinkedIn profile (location field)
3. GitHub profile (location field)
4. Conference speaking bios
5. Author bios in technical publications

**Privacy Considerations**:
- ⚠️ **DO NOT** provide residential addresses
- ✅ City and country level is usually sufficient
- ✅ Respect privacy settings on social platforms
- ❌ DO NOT dig for personal addresses not publicly shared

**What to Provide**:
- City and country (if publicly stated)
- "Remote" or "Distributed" if indicated
- Nothing if individual hasn't shared location publicly

**Example Output**:
```json
{
  "address_level": "city",
  "address": "Berlin, Germany",
  "address_type": "developer_location",
  "source": "github_profile",
  "source_url": "https://github.com/username",
  "verified_date": "2026-02-16",
  "confidence": "medium",
  "notes": "Individual developer - city level only for privacy"
}
```

---

## Special Cases and Edge Cases

### Case 1: Multiple Offices/Locations
**Situation**: Company has multiple offices

**Solution**:
- Identify which is the corporate headquarters (HQ)
- Look for terms: "headquarters", "head office", "main office", "global HQ"
- If multiple are labeled as HQ (e.g., regional HQs), note all with labels
- Prioritize the original/founding location if unclear

**Example**:
```json
{
  "headquarters": {
    "address": "Seattle, Washington, United States",
    "address_type": "global_headquarters"
  },
  "other_locations": [
    {
      "address": "San Francisco, California, United States",
      "address_type": "regional_office"
    }
  ]
}
```

### Case 2: Company Relocated
**Situation**: Address information conflicts due to relocation

**Solution**:
- Prioritize most recent information
- Check for press releases about relocation
- Look for "formerly known as" or "previously located at"
- Include move date if available

**Example**:
```json
{
  "current_address": "Austin, Texas, United States",
  "previous_address": "Palo Alto, California, United States",
  "relocation_date": "2021-12",
  "source": "press_release"
}
```

### Case 3: Acquired/Merged Company
**Situation**: Provider was acquired by another company

**Solution**:
- Check if provider maintains separate headquarters
- If absorbed, provide parent company HQ + note acquisition
- Include acquisition date and parent company name

**Example**:
```json
{
  "address": "Redmond, Washington, United States",
  "address_type": "parent_company_headquarters",
  "notes": "Acquired by Microsoft in 2018. Now operates as part of Microsoft.",
  "parent_company": "Microsoft Corporation"
}
```

### Case 4: Virtual/Distributed Company
**Situation**: Company has no physical headquarters (fully remote)

**Solution**:
- Note that company is distributed/remote
- Provide registered address if available (often legal requirement)
- Indicate country of incorporation

**Example**:
```json
{
  "address_level": "country",
  "address": "United States",
  "address_type": "distributed_company",
  "registered_address": "Delaware, United States",
  "notes": "Fully remote company with no physical headquarters. Registered in Delaware."
}
```

### Case 5: Defunct/Discontinued Provider
**Situation**: Provider is no longer active

**Solution**:
- Provide last known address with date
- Mark status as "defunct" or "discontinued"
- Note closure date if available

**Example**:
```json
{
  "address": "San Francisco, California, United States",
  "address_type": "former_headquarters",
  "status": "defunct",
  "last_known_date": "2020-06",
  "notes": "Company ceased operations in 2020"
}
```

### Case 6: Incomplete or Minimal Information
**Situation**: Only partial address available despite thorough search

**Solution**:
- Return whatever level is verifiable
- Clearly indicate information gaps
- Document search efforts

**Example**:
```json
{
  "address_level": "country",
  "address": "Germany",
  "address_type": "approximate_location",
  "source": "github_profile",
  "confidence": "low",
  "notes": "Only country-level information available from public sources. No official address found."
}
```

---

## Response Format

### Standard Response Structure

```json
{
  "provider_name": "Example Provider",
  "address_level": "complete|city|state|country|building|none",
  "address": "Full or partial address string",
  "address_type": "corporate_headquarters|registered_office|developer_location|distributed_company",
  "source": "official_website|linkedin|sec_filing|github|etc",
  "source_url": "URL where information was found",
  "verified_date": "YYYY-MM-DD",
  "confidence": "high|medium|low",
  "notes": "Additional context or caveats",
  "additional_info": {
    "relocated": false,
    "relocation_date": null,
    "multiple_locations": false,
    "acquired": false,
    "parent_company": null
  }
}
```

### Confidence Levels

- **high**:
  - Found on official website or government filing
  - Verified from 2+ authoritative sources
  - Information is recent (<2 years old)
  - Complete or city-level address available

- **medium**:
  - Found on professional platform (LinkedIn, Crunchbase)
  - Verified from 1 authoritative source
  - Information is somewhat recent (2-5 years old)
  - State or city-level address available

- **low**:
  - Found on user-generated content or unverified sources
  - Single source without corroboration
  - Information may be outdated (>5 years)
  - Only country-level information available

### When No Address Found

```json
{
  "provider_name": "Example Provider",
  "address_level": "none",
  "address": null,
  "address_type": "unknown",
  "source": "exhaustive_search",
  "verified_date": "2026-02-16",
  "confidence": "none",
  "notes": "No verifiable address information found after checking official website, business databases, and public records.",
  "search_attempts": [
    "Checked official website (about, contact, legal pages)",
    "Searched LinkedIn, Crunchbase",
    "Searched business registries",
    "No results found"
  ]
}
```

**CRITICAL**: Return `null` or `"none"` rather than guessing an address.

### Common Reasons for Missing Addresses (Based on Dataset Analysis)

From the "Alias & address.xlsx" dataset, several legitimate scenarios result in null addresses:

1. **Individual Developers** (Most Common):
   - Privacy: Personal addresses not publicly disclosed
   - Example: "Achal Dhir" - individual provider, no address found
   - Example: "Anil Mujagic" - individual developer, address not shared
   - **Action**: Return null with note about privacy respect

2. **New/Emerging Companies**:
   - Recently launched, minimal online presence
   - Example: "PagoNxt Merchant Solutions" (Getnet) - enterprise but no address found
   - **Action**: Return null with note about limited public information

3. **Fully Virtual/Distributed Companies**:
   - No physical headquarters, remote-first
   - May have registered address in one jurisdiction but no operational HQ
   - **Action**: Search for registered address, note if company is distributed

4. **Acquired/Merged Entities**:
   - Address may be under parent company
   - Old addresses may be outdated post-acquisition
   - **Action**: Search for parent company address, note relationship

5. **Name Changes/Rebrands**:
   - Addresses may be listed under old name
   - Example: "AnyFlip" - address not found under current name
   - **Action**: Try searching with former names/aliases

6. **Non-Corporate Entities**:
   - Open source projects without legal entity
   - Community projects with no central office
   - **Action**: Note that entity has no physical headquarters

### Percentage Expectations

Based on the dataset:
- **~90-95%** of enterprise companies should have verifiable addresses
- **~5-10%** of enterprises may legitimately have no public address
- **~60-70%** of individual developers will have no address (privacy)
- **~80-85%** of community-based projects may have addresses (if foundation-backed)

**Note**: Null values are acceptable and expected in certain categories. Do not fabricate addresses to avoid null returns.

---

## Verification Checklist

Before returning address information, confirm:

- [ ] Information was found through verified sources, not assumed
- [ ] Source is authoritative (official website, government filing, professional database)
- [ ] Address format is valid for the stated country
- [ ] Information is reasonably current (<5 years for companies, <3 years preferred)
- [ ] Address type is correctly identified (HQ vs. registered vs. branch)
- [ ] For individuals, privacy considerations are respected
- [ ] Source URL is documented for future reference
- [ ] Confidence level accurately reflects verification quality

If ANY checkbox is unchecked and cannot be resolved:
1. Lower confidence level, OR
2. Provide partial information with appropriate caveats, OR
3. Return `address_level: "none"` if information cannot be verified

---

## Search Query Examples

### For Official Website Search
```
site:[provider-website.com] headquarters
site:[provider-website.com] head office
site:[provider-website.com] contact address
site:[provider-website.com] about location
site:[provider-website.com] imprint (for EU companies)
```

### For External Search
```
"[Provider Name]" headquarters address
"[Provider Name]" corporate office location
"[Provider Name]" "head office" address
"[Provider Name]" registered office address
"[Provider Name]" site:linkedin.com location
"[Provider Name]" site:crunchbase.com headquarters
"[Provider Name]" site:sec.gov address
```

### For Different Regions
```
"[Provider Name]" site:companies.gov.uk (UK)
"[Provider Name]" site:unternehmensregister.de (Germany)
"[Provider Name]" site:infogreffe.fr (France)
"[Provider Name]" handelsregister (Switzerland/Austria)
```

---

## Tools and Resources

### Official Source Checkers
1. **Website Crawlers**: Check About, Contact, Legal, Footer sections
2. **WHOIS Lookup**: Domain registration may include address
3. **SSL Certificate Info**: Sometimes includes organization address

### Business Databases
1. **LinkedIn**: Company pages often list headquarters
2. **Crunchbase**: Comprehensive startup/company database
3. **Bloomberg Terminal**: For large public companies
4. **PitchBook**: For private companies and startups

### Government/Regulatory Databases
1. **US**: SEC EDGAR, State Secretary of State websites
2. **UK**: Companies House (companieshouse.gov.uk)
3. **EU**: European Business Register, national registers
4. **International**: Local business registries by country

### Non-Profit Databases
1. **GuideStar** (US nonprofits)
2. **Charity Navigator** (US charities)
3. **National charity registers** (by country)

---

## Privacy and Ethics Guidelines

### For Individual Developers:
1. **Never** publish residential street addresses
2. Respect privacy settings on social platforms
3. City/country level is sufficient
4. If location is not publicly stated, don't search for it
5. Mark individual addresses differently from corporate addresses

### For All Providers:
1. Prefer business addresses over personal addresses
2. Don't publish information marked as "private" or "confidential"
3. Respect GDPR and data protection regulations
4. If in doubt about privacy, provide less detail rather than more

---

## Error Handling

### If address fetch encounters issues:

```
1. Official website has no address:
   → Check external sources in order of priority
   → Document that official website was checked but had no address

2. Conflicting addresses found:
   → Prioritize official website over external sources
   → Verify which is more recent
   → Note discrepancy in response

3. Only P.O. Box found:
   → Accept P.O. Box if that's the only official address
   → Note address_type as "mailing_address"
   → Continue searching for physical address

4. Address format unclear:
   → Research country-specific address formats
   → Standardize to: Street, City, State/Province, Postal Code, Country
   → Use local conventions when appropriate

5. Complete search failure:
   → Document all sources checked
   → Return structured "not found" response
   → NEVER guess or fabricate an address
```

---

## Examples (From Real Dataset)

### Example 1: Complete Enterprise Address - US Format ✅
```json
{
  "provider_name": "Ten Thousand Coffees",
  "alias": "10KC",
  "address_level": "complete",
  "address": "18 King St. East, suite 1400, Toronto, Ontario M5C 1C4, Canada",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "https://www.tenthousandcoffees.com",
  "verified_date": "2026-02-16",
  "confidence": "high",
  "notes": null
}
```

### Example 2: Complete Enterprise Address - European Format ✅
```json
{
  "provider_name": "Seibert Group",
  "alias": "//SEIBERT/MEDIA",
  "address_level": "complete",
  "address": "LiusenForum, 5. OG Kirchgasse 6, 65185 Wiesbaden, Germany",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "https://seibert.group/en/",
  "verified_date": "2026-02-16",
  "confidence": "high",
  "notes": null
}
```

### Example 3: Complete Enterprise Address - Asian Format ✅
```json
{
  "provider_name": "AVTECH SECURITY",
  "alias": "AV TECH",
  "address_level": "complete",
  "address": "10 F, E Building, No. 19-11 San Chung Rd., Nankang, Taipei, 115",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "http://www.avtech.com.tw/",
  "verified_date": "2026-02-16",
  "confidence": "high",
  "notes": "Taiwan address format"
}
```

### Example 4: City-Level Address ✅
```json
{
  "provider_name": "Ambassador",
  "alias": "Ambassador Labs, Datawire",
  "address_level": "city",
  "address": "Boston, Massachusetts, USA",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "https://www.getambassador.io/",
  "verified_date": "2026-02-16",
  "confidence": "medium",
  "notes": "Only city-level address publicly available"
}
```

### Example 5: Individual Developer - No Address ✅
```json
{
  "provider_name": "Open TFTP Server Project",
  "alias": "Achal Dhir",
  "address_level": "none",
  "address": null,
  "address_type": "individual_developer",
  "source": "sourceforge_profile",
  "source_url": "https://sourceforge.net/u/achaldhir/profile",
  "verified_date": "2026-02-16",
  "confidence": "none",
  "notes": "Individual developer. No public address information available. Privacy respected."
}
```

### Example 6: No Address Found - Enterprise ✅
```json
{
  "provider_name": "PagoNxt Merchant Solutions",
  "alias": "Getnet",
  "address_level": "none",
  "address": null,
  "address_type": "unknown",
  "source": "exhaustive_search",
  "source_url": "https://www.getnetworld.com/",
  "verified_date": "2026-02-16",
  "confidence": "none",
  "notes": "Enterprise company. Official website checked but no headquarters address found.",
  "search_attempts": [
    "Official website (about, contact pages)",
    "LinkedIn company page",
    "Crunchbase search",
    "No verifiable address found"
  ]
}
```

### Example 7: Multiline Address Format ✅
```json
{
  "provider_name": "CODESYS",
  "alias": "3S-Smart Software Solutions",
  "address_level": "complete",
  "address": "CODESYS GmbH\nA member of the CODESYS Group\nMemminger Strabe 151, 87439 Kempten\nGermany",
  "address_type": "corporate_headquarters",
  "source": "official_website",
  "source_url": "https://www.codesys.com/",
  "verified_date": "2026-02-16",
  "confidence": "high",
  "notes": "Address provided in multiline format from official source"
}
```

---

## Quick Reference Checklist

### Before Returning ANY Address:

✅ **VERIFICATION**
- [ ] Found on official website OR verified from 2+ sources
- [ ] Address format matches country convention
- [ ] Information is reasonably current (<5 years)
- [ ] No hallucination - actual source exists

✅ **FORMATTING**
- [ ] Preserved original formatting from source
- [ ] Included all components (building, street, city, postal, country)
- [ ] Special characters preserved (ß, é, ñ, etc.)
- [ ] Multiline format maintained if that's how it appeared

✅ **PRIVACY**
- [ ] For individuals: Only city/country level (NO residential addresses)
- [ ] For enterprises: Business address only
- [ ] Respect GDPR and privacy regulations

✅ **DOCUMENTATION**
- [ ] Source URL recorded
- [ ] Confidence level assigned
- [ ] Provider name and aliases noted
- [ ] Address type identified (HQ, registered, etc.)

### When to Return NULL:

Return `address: null` when:
- Individual developer with no public location
- Exhaustive search yields no results
- Only unverified/conflicting information found
- Privacy concerns prevent disclosure

**NEVER** guess or construct an address!

---

## Dataset Statistics (From "Alias & address.xlsx")

Based on analysis of the reference dataset:

**Total Providers Analyzed**: 144 entries

**Address Availability**:
- Complete addresses found: ~85% of enterprises
- City-level addresses: ~10% of enterprises
- No address (null): ~5% of enterprises, ~95% of individuals

**Geographic Distribution** (Sample):
- United States: Largest representation
- Germany: Strong European presence
- Other: UK, Canada, France, India, China, Taiwan, Hong Kong, Sweden, Finland

**Address Format Patterns**:
- US/Canada format: ~40%
- European format: ~35%
- Asian format: ~15%
- UK format: ~5%
- Other/Mixed: ~5%

---

*Document created: 2026-02-16*
*Version: 2.0 (Refined with dataset analysis)*
*Dataset Reference: "Alias & address.xlsx" (144 providers)*
