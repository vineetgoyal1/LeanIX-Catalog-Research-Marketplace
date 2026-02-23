# Application Alias Guidelines

## Purpose

This guideline helps AI agents identify and document alternative names, abbreviations, former names, and commonly-used identifiers for Application fact sheets in LeanIX. Aliases help users discover applications regardless of which name they know the product by.

## Core Principles

### 1. **Multiple Names, Comma-Separated**
Separate multiple aliases with commas and spaces.

**Format**: `Alias1, Alias2, Alias3`

**Examples**:
- 2Checkout → `2Checkout subscription, Verifone, 2CO.com`
- Adobe Acrobat Sign → `Adobe EchoSign, Adobe eSign, Adobe Sign`
- Abstract → `Abstract Branches, Elastic Projects`

### 2. **Include Multiple Alias Types**
An application can have aliases from different categories:

**Categories**:
1. **Abbreviations/Acronyms** - Official or common short forms
2. **Former names** - Pre-acquisition, pre-rebranding names
3. **Product variations** - Different editions or related products
4. **Parent company variants** - Brand name changes, company prefixes
5. **Shortened names** - Commonly used shortened versions
6. **Commonly known names** - Names users might search for

### 3. **No Formatting**
Do not use bold, italics, asterisks, or other markdown formatting.

**Good**: `Accela ACA`
**Bad**: `**Accela ACA**`

### 4. **Deduplicate Similar Names**
Skip aliases that are identical or extremely similar to the main application name.

**Examples to Skip**:
- AdminDroid → ~~AdminDroid~~ (identical)
- Adobe Analytics Cloud → ~~Adobe Analytics Cloud~~ (identical)

### 5. **Minimum Length for Abbreviations**
If an abbreviation/acronym is the **only** alias, it should be **3+ characters**.

**Good**:
- Aptitude Accounting Hub → `AAH` (3 characters)
- 3DEXPERIENCE → `3DX` (3 characters)

**Acceptable** (if combined with other aliases):
- Adobe Experience Cloud → `Adobe Marketing Cloud, AEC` (2 characters OK because there's another alias)

**Avoid** (if it's the only alias):
- Application X → ~~AX~~ (too short, only 2 characters)

### 6. **Exclude Internal/Numeric IDs**
Do not include internal product IDs, SKU numbers, or numeric identifiers.

**Exclude**:
- SAP product numeric IDs like `73554900100800000872`
- Internal codes or SKU numbers
- Database IDs

## Alias Type Categories

### 1. Abbreviations and Acronyms

**Official abbreviations** - Provided by the vendor

**Examples**:
- Accela Citizen Access → `Accela ACA`
- Ten Thousand Coffees → `10KC`
- 3DEXPERIENCE → `3DX`
- Accuris Engineering Workbench → `Accuris EWB`
- Adobe Identity Management → `Adobe IMS`

**Common unofficial abbreviations** - Widely used by customers/community

**Examples**:
- Adobe Experience Cloud → `AEC` (commonly used in documentation)
- Aptitude Accounting Hub → `AAH`

**Guidelines**:
- ✅ Include official vendor abbreviations
- ✅ Include widely-used community abbreviations
- ✅ 3+ characters if it's the only alias
- ❌ Don't create abbreviations not found in official sources
- ❌ Avoid single-letter abbreviations

### 2. Former Names (Pre-Acquisition/Rebranding)

**Critical for discovery** - Users often know the old name

**Examples**:
- Everest → `250ok` (former company name)
- Shift4Shop → `3dcart` (rebranded from)
- Paycor Talent Development → `7Geese` (acquired)
- Kiteworks → `Accellion` (rebranded from)
- Workday Adaptive Planning → `Adaptive Insights` (acquired)
- Adobe Learning Manager → `Adobe Captivate Prime` (rebranded from)
- Adobe Commerce → `Adobe Magento` (Magento acquired by Adobe)
- Adobe Express → `Adobe Spark` (rebranded from)
- Adobe Stock → `Fotolia` (acquired)
- Boltive → `AdLightning` (rebranded from)

**Guidelines**:
- ✅ Always include pre-acquisition names
- ✅ Include rebranded names
- ✅ Include names from company mergers
- ✅ Multiple historical names if multiple changes occurred
- ❌ Don't include if company explicitly deprecated the old name and removed all traces

### 3. Product Variations and Editions

**Different versions or editions** of the same product

**Examples**:
- 10Duke Entitlements → `10Duke` (shortened/parent product)
- 1E → `1E Tachyon` (specific edition)
- Actifio → `Actifio GO` (specific edition)
- Acronis Backup → `Acronis Cyber Backup` (edition name)
- Adobe Document Cloud → `Adobe Acrobat DC, Adobe Media Optimizer, Adobe Acrobat DC Standard subscription`
- Acquia → `Acquia Drupal Cloud, Acquia Cloud Platform` (platform variations)
- Abstract → `Abstract Branches, Elastic Projects` (related features/products)

**Guidelines**:
- ✅ Include commonly-used product variations
- ✅ Include specific editions if widely known
- ✅ Include related products in the same suite if associated
- ❌ Don't list every minor SKU or version number

### 4. Parent Company or Brand Name Variants

**Company prefix changes** or brand associations

**Examples**:
- 2Checkout → `Verifone` (acquired by Verifone)
- Acronis Cloud Manager → `5Nine Cloud Manager` (formerly 5Nine)
- Glofox → `ABC Glofox` (ABC acquired Glofox)
- Abnormal AI → `Abnormal Security` (company name variant)
- PeopleXD → `Access PeopleXD` (Access is parent company)
- EMS → `Accruent EMS` (Accruent is parent company)
- myConcerto → `Accenture myConcerto Intelligent Data Quality`

**Guidelines**:
- ✅ Include former company/brand names
- ✅ Include parent company prefixes if commonly used
- ✅ Include brand name variants
- ❌ Don't include if it's just marketing repackaging without actual name change

### 5. Shortened Names

**Commonly used shortened versions** of long product names

**Examples**:
- SurveySparrow 360 Degree Assessment → `360 Degree Assessment`
- AddPay → `AddPay e-Commerce` (full product name)
- Hyland Acuo VNA → `Acuo Vendor Neutral Archive` (expanded abbreviation)
- Adobe Real-Time CDP → `Adobe Real-Time Customer Data Platform` (expanded)
- aDolus FACT → `aDolus Framework for Analysis and Coordinated Trust` (expanded)

**Guidelines**:
- ✅ Include if users commonly use the short form
- ✅ Include expanded forms of abbreviations in product names
- ❌ Don't create arbitrary shortened names

### 6. Commonly Known Names

**Names users might search for** even if not official

**Examples**:
- Guideline → `401k software` (descriptive, commonly searched)
- Absorb Software → `Absorb LMS` (commonly known as)
- Aceyus → `Aceyus VUE` (product line)

**Guidelines**:
- ✅ Include if it's a well-known alternative people search for
- ✅ Include descriptive names if official and commonly used
- ⚠️ Use sparingly - must be verifiable and common
- ❌ Don't include generic descriptive terms
- ❌ Don't include category names (e.g., "CRM software")

### 7. Related Products in Same Suite

**Associated products** that are closely related

**Examples**:
- Smartsheet → `10,000ft` (10,000ft was separate, now integrated)
- Resource Management by Smartsheet → `10,000ft, Artefact Product Group SaaS product`
- Adobe Document Cloud → `Adobe Acrobat DC, Adobe Media Optimizer`

**Guidelines**:
- ✅ Include if the products are commonly confused or associated
- ✅ Include if one was a separate product now integrated
- ❌ Don't list every product in a large suite

## Context-Dependent: Subscription Naming

**"subscription" suffix** appears in many examples but is not a standard convention.

**When to include "subscription"**:
- ✅ If the vendor officially uses "subscription" in the product name
- ✅ If there are multiple offerings and "subscription" distinguishes them
- ✅ If users commonly search for "[Product] subscription"

**When NOT to include**:
- ❌ If it's obvious the product is subscription-based
- ❌ If adding "subscription" doesn't add value for discovery
- ❌ If the vendor doesn't use it officially

**Examples from data**:
- Adobe Illustrator → `Adobe Illustrator subscription` (likely user added, probably not needed)
- 2Checkout → `2Checkout subscription, Verifone, 2CO.com` (combined with other aliases)

**Recommendation**: Generally avoid adding "subscription" unless context requires it.

## Special Cases

### Case 1: Multiple Historical Names (Acquisition Chain)

If a product changed names multiple times, list all previous names.

**Example**:
- Adobe Acrobat Sign → `Adobe EchoSign, Adobe eSign, Adobe Sign`
  - Started as EchoSign
  - Became Adobe eSign after acquisition
  - Now called Adobe Acrobat Sign

**Format**: List in chronological order (oldest to newest) if known, otherwise any order.

### Case 2: Product Line vs Individual Product

If the application name is very specific, but it's part of a known product line:

**Example**:
- 7SIGNAL Endpoint Agents → `7SIGNAL Mobile Eye` (former product name in the line)

**Guideline**: Include the product line name if commonly used.

### Case 3: Long Descriptive Names

For applications with very long official names, include the shortened version users actually use:

**Example**:
- SAP Integration Suite, managed gateway for spend management and SAP Business Network → (Users likely say "Ariba Cloud Integration Gateway" - include if verified)

### Case 4: Hyphenation and Spacing Variants

Include variants with different spacing or hyphenation if both are commonly used:

**Example**:
- Accessit Library → `Access-It Library` (hyphenation variant)

### Case 5: Domain Names vs Product Names

Include domain names only if they're commonly used to refer to the product:

**Example**:
- 2Checkout → `2CO.com` (their domain, commonly used)

**Guideline**: Include only if it's an alias people search by, not every domain the company owns.

## Research Process

### Step 1: Official Sources
Check the provider's official website for:
- Product page - Look for alternate names, editions
- About page - Historical information, former names
- Documentation - Common abbreviations used
- Press releases - Acquisition announcements, rebranding

### Step 2: Historical Research
- Search "[Product name] formerly known as" or "previously called"
- Check Crunchbase, Wikipedia for acquisition history
- Look for press releases about name changes
- Check domain WHOIS history for rebranding

### Step 3: Community Usage
- Check product reviews, forums, user communities
- See what abbreviations users commonly use
- Look at social media hashtags and discussions

### Step 4: Verify Each Alias
- Confirm each alias is real and verifiable
- Ensure it's commonly used enough to aid discovery
- Check if it's current or historical

## Quality Checklist

Before finalizing aliases, verify:

- [ ] **Comma-separated** - Multiple aliases separated by `, `
- [ ] **No formatting** - No bold, italics, or markdown
- [ ] **No duplicates** - Skipped identical or very similar names
- [ ] **Minimum length** - 3+ characters for standalone abbreviations
- [ ] **No internal IDs** - Excluded numeric product IDs and SKUs
- [ ] **Verifiable** - All aliases found in official sources or common usage
- [ ] **Former names included** - All pre-acquisition/rebranding names listed
- [ ] **Abbreviations included** - Official and common unofficial abbreviations
- [ ] **No generic terms** - Avoided category names or overly generic descriptors

## Decision Tree

```
1. Check official vendor sources
   → Product page, documentation, about page
   ↓
2. Identify alias types:
   □ Official abbreviation/acronym? (e.g., AAH, 3DX)
   □ Former company/product name? (e.g., 7Geese, Adaptive Insights)
   □ Product variation/edition? (e.g., Actifio GO)
   □ Parent company variant? (e.g., Accruent EMS)
   □ Shortened/expanded name? (e.g., 360 Degree Assessment)
   □ Commonly known as? (e.g., Absorb LMS)
   □ Related product in suite? (e.g., 10,000ft)
   ↓
3. Verify each alias:
   → Is it verifiable from official sources?
   → Is it commonly used for discovery?
   → Is it 3+ characters (if standalone abbreviation)?
   → Is it NOT just a numeric ID?
   → Is it NOT identical to main name?
   ↓
4. Format aliases:
   → Comma-separated: "Alias1, Alias2, Alias3"
   → No formatting
   → No "subscription" unless context requires
   ↓
5. Quality check → Verify checklist above
```

## Examples by Pattern

### Pattern 1: Simple Abbreviation
**Application**: Accela Citizen Access
**Alias**: `Accela ACA`
**Why**: Official abbreviation commonly used

### Pattern 2: Acquisition/Rebranding
**Application**: Paycor Talent Development
**Alias**: `7Geese`
**Why**: Previously known as 7Geese before acquisition

### Pattern 3: Multiple Aliases (Mixed Types)
**Application**: 2Checkout
**Alias**: `2Checkout subscription, Verifone, 2CO.com`
**Why**:
- Product has subscription offering
- Acquired by Verifone (parent company)
- Commonly known by domain 2CO.com

### Pattern 4: Edition/Variation
**Application**: Adobe Document Cloud
**Alias**: `Adobe Acrobat DC, Adobe Media Optimizer, Adobe Acrobat DC Standard subscription`
**Why**: Multiple products/editions in the Document Cloud suite

### Pattern 5: Former Name + Abbreviation
**Application**: Adobe Acrobat Sign
**Alias**: `Adobe EchoSign, Adobe eSign, Adobe Sign`
**Why**:
- Originally EchoSign
- Became Adobe eSign after acquisition
- Later rebranded to Adobe Acrobat Sign
- Also still called "Adobe Sign" informally

### Pattern 6: Expanded Abbreviation
**Application**: aDolus FACT
**Alias**: `aDolus Framework for Analysis and Coordinated Trust`
**Why**: FACT is an acronym; full name helps discovery

### Pattern 7: Related Product
**Application**: Smartsheet
**Alias**: `10,000ft`
**Why**: 10,000ft was acquired and integrated into Smartsheet; users still know it by original name

## Anti-Patterns to Avoid

❌ **Internal IDs**: `73554900100800000872`
❌ **Identical names**: Application Name → Application Name
❌ **Single letters**: X → `X` (too short if standalone)
❌ **Made-up abbreviations**: Not found in any official source
❌ **Generic categories**: "Project Management Software"
❌ **Every domain**: Don't list every URL the company owns
❌ **Marketing slogans**: Not actual product names
❌ **Version numbers**: v2.0, 2023 edition (unless part of official name)
❌ **Overly descriptive**: "The application that manages projects"
❌ **Bold/formatting**: **Alias Name** or *Alias Name*

## Summary

**DO**:
- Comma-separate multiple aliases
- Include former names (pre-acquisition, rebranding)
- Include official and common abbreviations
- Include product variations/editions
- Verify all aliases from official sources
- Use 3+ character abbreviations (standalone)

**DON'T**:
- Include numeric/internal IDs
- Duplicate the main application name
- Add formatting (bold, italics)
- Create unverifiable aliases
- Use generic category names
- Add "subscription" unnecessarily
- Use single/two-letter abbreviations (standalone)

**Remember**: Aliases are for **discovery**. Include names that help users find the application regardless of which name they know it by.
