# Application Pricing Guidelines

## Purpose

This guideline helps AI agents determine the **Pricing URL** and **Pricing Type** for Application fact sheets in LeanIX. These two fields are intrinsically linked - the Pricing URL is the source, and the Pricing Type is the pricing model information extracted from that source.

## Field Overview

### Field 1: Pricing URL (`pricingUrl`)
- **Field Type**: URL (text)
- **Purpose**: Store the exact webpage where pricing information is displayed
- **Required**: Strongly recommended (if pricing information exists)

### Field 2: Pricing Type (`pricingType`)
- **Field Type**: Free text
- **Purpose**: Describe the pricing model/structure
- **Required**: Strongly recommended (95.3% of applications have this)

## Core Principles

### 1. **Official Website Only**

Pricing information must come from the **application's official website**, not third-party sources.

**Priority Order**:
1. Official pricing page (e.g., `https://app.com/pricing`)
2. Official product page with pricing section
3. Official documentation with pricing details

**Do NOT use**:
- G2 pricing information (may be outdated)
- Capterra pricing (may be incomplete)
- Review sites or comparison sites
- Wikipedia or unofficial sources

### 2. **Never Hallucinate URLs**

If no pricing page exists or is accessible, return `Not Publicly Available` for pricing type and leave URL empty. Do not construct or guess URLs.

### 3. **Descriptive Text Over Normalization**

**Keep descriptive text from the official source when it's clear**:
- ✅ "Pricing starts at $29/month per user with annual billing options"
- ✅ "Free for up to 10 users, then $12/user/month"
- ✅ "Usage-based pricing: $0.02 per API call, volume discounts available"

**Normalize only when source text is vague or generic**:
- ❌ "Contact us for pricing" → ✅ `Not Publicly Available`
- ❌ "See pricing page" → ✅ Research and extract actual details
- ❌ "Custom pricing" → ✅ `Enterprise Pricing (Contact for Quote)`

### 4. **Default to "Not Publicly Available" When Uncertain**

**CRITICAL RULE**: If after thorough research no reliable pricing information is found on the official website, you MUST:

- **pricingType**: `Not Publicly Available`
- **pricingUrl**: (empty/blank - leave field empty)

**Do NOT**:
- ❌ Guess or estimate pricing based on similar applications
- ❌ Use outdated information from cached pages
- ❌ Use third-party claims from G2, Capterra, or review sites
- ❌ Construct URLs that "might exist" (e.g., `https://app.com/pricing`) without verification
- ❌ Return uncertain or unverified pricing information
- ❌ Use information that requires login or account access (unless publicly documented elsewhere)

**When to use "Not Publicly Available"**:
- No pricing page found after exhaustive search
- Pricing page exists but only says "Contact us" with no details
- Pricing requires login/account to view
- Application is internal/custom with no public pricing
- Pricing information is outdated or contradictory across sources

**Example**:
```
Application: "Enterprise Internal Tool"
Research: No pricing page, no public information
Result:
  pricingUrl: (empty)
  pricingType: "Not Publicly Available"
```

### 5. **Deep Research Required**

Use Perplexity and WebFetch to thoroughly understand:
- "How does [Application Name] pricing work?"
- "[Application Name] pricing model"
- "[Application Name] pricing tiers"
- "[Application Name] cost structure"

**Accuracy over speed** - take time to find and verify pricing information. But if after exhaustive research nothing reliable is found, default to "Not Publicly Available".

## Step-by-Step Process

### Step 1: Search for Pricing Page

**Search Strategies**:

1. **Direct URL patterns** (try these first):
   - `https://[app-domain]/pricing`
   - `https://[app-domain]/plans`
   - `https://[app-domain]/pricing-plans`
   - `https://[app-domain]/buy`
   - `https://[app-domain]/purchase`
   - `https://[app-domain]/plans-pricing`

2. **Perplexity search**:
   ```
   Query: "[Application Name] official pricing page URL"
   Query: "[Application Name] pricing plans site:[domain]"
   Query: "How much does [Application Name] cost?"
   ```

3. **WebFetch homepage** → Look for pricing link:
   - Check navigation menu for "Pricing", "Plans", "Buy"
   - Check footer links
   - Check "Get Started" or "Sign Up" flows

4. **WebFetch common paths**:
   - Try the direct URL patterns listed above
   - Follow redirects to find canonical pricing page

**Example Process**:
```
Application: "Slack"
1. Try: https://slack.com/pricing → Success ✓
2. WebFetch this URL to extract pricing details
```

### Step 2: Validate Pricing URL

Before accepting a URL, verify:

#### A. **URL Accessibility**
- ✅ Returns 200 (OK) or 301/302 redirect to valid page
- ✅ Valid HTTPS certificate
- ❌ Returns 404 (Not Found) → Keep searching
- ❌ Paywall or login required → Document as `Requires Account Login`

#### B. **URL Specificity**
- ✅ Points to dedicated pricing page: `https://app.com/pricing`
- ✅ Product page with pricing section: `https://app.com/product#pricing`
- ⚠️ Homepage with embedded pricing: `https://app.com` (only if pricing is on homepage)
- ❌ Generic "contact sales" page with no pricing: Not acceptable

#### C. **Content Verification**
The page must contain actual pricing information:
- ✅ Specific prices (e.g., "$29/month")
- ✅ Pricing tiers/plans (e.g., "Free", "Pro", "Enterprise")
- ✅ Pricing model description (e.g., "per user", "usage-based")
- ❌ Only "Contact us for quote" with no details → Not a pricing page

#### D. **Official Source**
- ✅ URL is on official application domain
- ✅ URL is on official provider domain (if different)
- ❌ Third-party site (G2, Capterra, review sites)
- ❌ Affiliate or reseller pricing pages

**Acceptable URL Patterns**:
- `https://slack.com/pricing`
- `https://www.salesforce.com/products/sales-cloud/pricing/`
- `https://stripe.com/pricing#payment-links`
- `https://aws.amazon.com/ec2/pricing/`
- `https://www.adobe.com/products/photoshop/plans.html`

**Unacceptable URL Patterns**:
- `https://g2.com/products/slack/pricing` (third-party)
- `https://slack.com/contact-sales` (no pricing details)
- `https://slack.com` (homepage, unless pricing is clearly shown)

### Step 3: Extract Pricing Type

Once you have the validated pricing URL, extract the pricing model information.

#### Research Process:

1. **WebFetch the pricing URL**:
   ```
   Prompt: "Extract the pricing model, tiers, and cost structure.
           Include specific prices if mentioned.
           Describe how customers are charged (per user, per feature, usage-based, etc.)."
   ```

2. **Perplexity search for clarification**:
   ```
   Query: "How does [Application Name] pricing work?"
   Query: "[Application Name] pricing model explained"
   Query: "[Application Name] free vs paid plans"
   ```

3. **Combine information**: Use official page text as primary, Perplexity to clarify

#### Extraction Guidelines:

**Keep descriptive text when clear** (50-150 characters ideal):

✅ **Good examples** (descriptive, from official source):
- `Free for up to 10 users, then $6.67/user/month (billed annually) or $8/user/month (monthly)`
- `Usage-based: $0.002 per API request, $0.10 per GB storage, volume discounts available`
- `Three plans: Starter ($29/month), Professional ($99/month), Enterprise (custom pricing)`
- `Freemium model with paid plans starting at $12/user/month with annual commitment`
- `Per-seat pricing starting at $25/user/month, includes unlimited projects and 100GB storage`

✅ **Good examples** (clear model description):
- `Subscription-based with monthly and annual billing options across four tiers`
- `Pay-as-you-go pricing based on compute hours and data transfer`
- `One-time license purchase with optional annual support subscription`
- `Volume-based pricing: charged per 1,000 emails sent, tiered discounts apply`

**Normalize when vague** (official text is too generic):

❌ **Vague examples** (need normalization):
- "Contact us for pricing" → ✅ `Not Publicly Available`
- "Custom pricing" → ✅ `Enterprise Pricing (Contact for Quote)`
- "See website for details" → ✅ Research and extract actual model
- "Flexible pricing options" → ✅ Research and describe specific options
- "Pricing depends on usage" → ✅ Specify: `Usage-based pricing (contact for rates)`

### Step 4: Normalization Patterns (When Source is Vague)

Use these **only when official source text is too vague or generic**.

#### Pattern 1: Not Publicly Available

**When to use**: No pricing information is accessible on the official website.

**Triggers**:
- "Contact us for pricing"
- "Contact sales for quote"
- "Request a quote"
- No pricing page exists
- Pricing page requires login/account

**Normalized Text**: `Not Publicly Available`

---

#### Pattern 2: Freemium

**When to use**: Free tier exists with paid upgrade options.

**Triggers**:
- "Free plan available"
- "Free for individuals, paid for teams"
- "Free trial, then paid"

**Normalized Text**: `Freemium (free tier available, paid plans starting at $X/[period])`

**Example**: `Freemium (free for up to 10 users, paid plans from $8/user/month)`

---

#### Pattern 3: Free (Open Source / No Cost)

**When to use**: Completely free to use.

**Triggers**:
- "Free and open source"
- "100% free"
- "No cost"

**Normalized Text**: `Free` or `Free (Open Source)`

---

#### Pattern 4: Per User / Seat-Based

**When to use**: Pricing scales with number of users.

**Triggers**:
- "Per user pricing"
- "Per seat"
- "$X/user/month"

**Normalized Text**: `Per-user pricing starting at $X/user/[period]` (include specific price if available)

**Example**: `Per-user pricing starting at $15/user/month with annual billing`

---

#### Pattern 5: Usage-Based / Pay-As-You-Go

**When to use**: Pricing based on consumption/usage.

**Triggers**:
- "Pay for what you use"
- "Usage-based"
- "Pay as you go"
- "Per API call", "Per GB", "Per transaction"

**Normalized Text**: `Usage-based pricing` (add specifics if available)

**Example**: `Usage-based pricing ($0.01 per API call, tiered discounts available)`

---

#### Pattern 6: Subscription (Tiered Plans)

**When to use**: Multiple subscription tiers/plans.

**Triggers**:
- "Basic, Pro, Enterprise plans"
- "Monthly or annual subscription"
- Multiple pricing tiers listed

**Normalized Text**: `Subscription-based with [X] tiers` (include price range if available)

**Example**: `Subscription-based with 3 tiers ($29-$299/month)`

---

#### Pattern 7: Enterprise / Custom Pricing

**When to use**: Only enterprise/custom pricing available.

**Triggers**:
- "Enterprise pricing only"
- "Contact for custom quote"
- "Pricing based on requirements"

**Normalized Text**: `Enterprise Pricing (Contact for Quote)`

---

#### Pattern 8: One-Time Purchase / License

**When to use**: Pay once, own forever (not subscription).

**Triggers**:
- "One-time payment"
- "Perpetual license"
- "Buy once"

**Normalized Text**: `One-time purchase` (include price if available)

**Example**: `One-time purchase ($199 per license)`

---

#### Pattern 9: Feature-Based / Tiered by Features

**When to use**: Pricing varies based on features enabled.

**Triggers**:
- "Pricing based on features"
- "Different features at each tier"
- "Add-on based pricing"

**Normalized Text**: `Feature-based pricing across [X] tiers` (add specifics if clear)

**Example**: `Feature-based pricing: Core ($49/month), Plus ($99/month), Premium ($199/month)`

---

#### Pattern 10: Hybrid / Complex Models

**When to use**: Combination of multiple pricing models.

**Triggers**:
- Base subscription + usage fees
- Per-user + per-feature
- Multiple pricing dimensions

**Normalized Text**: Describe both components clearly

**Example**: `Hybrid pricing: $10/user/month base + usage charges ($0.05 per transaction)`

## Decision Tree

```
Input: Application Name

1. Search for pricing page URL
   → Direct URL patterns (/pricing, /plans)
   → Perplexity: "[App] official pricing page"
   → WebFetch homepage → Find pricing link
   ↓
2. Validate URL
   → Accessible (200 OK)?
   → Official domain?
   → Contains actual pricing info?
     ├─ YES → Proceed to Step 3
     └─ NO → Continue searching
            → If exhausted → pricingType = "Not Publicly Available", pricingUrl = (empty)
   ↓
3. Extract pricing type from validated URL
   → WebFetch pricing page
   → Extract pricing model description
   → Is the extracted text descriptive and clear?
     ├─ YES → Use official text as-is
     └─ NO → Apply normalization pattern
   ↓
4. Research clarification (if needed)
   → Perplexity: "How does [App] pricing work?"
   → Verify extracted information accuracy
   → Add specifics if official page was vague
   ↓
5. Return both fields:
   pricingUrl: "https://..."
   pricingType: "[Descriptive text or normalized pattern]"
```

## Example Workflows

### Example 1: Clear Pricing Page (Descriptive Text)

**Input**: "Slack"

**Process**:
1. Try: `https://slack.com/pricing` → ✓ Accessible
2. WebFetch: Extracts clear pricing structure
3. Official text: "Free for small teams, then $7.25/user/month (Pro) or $12.50/user/month (Business+)"
4. Text is descriptive → Use as-is

**Result**:
- `pricingUrl`: `https://slack.com/pricing`
- `pricingType`: `Free for small teams, then $7.25/user/month (Pro) or $12.50/user/month (Business+)`

---

### Example 2: Vague Official Text (Normalization Needed)

**Input**: "Enterprise SaaS Tool"

**Process**:
1. Found: `https://enterprisetool.com/pricing`
2. WebFetch: Page says "Contact sales for custom pricing"
3. Official text is vague → Normalize
4. Apply Pattern 7: Enterprise Pricing

**Result**:
- `pricingUrl`: `https://enterprisetool.com/pricing`
- `pricingType`: `Enterprise Pricing (Contact for Quote)`

---

### Example 3: Usage-Based with Details

**Input**: "Stripe"

**Process**:
1. Found: `https://stripe.com/pricing`
2. WebFetch: Complex usage-based structure
3. Perplexity: "How does Stripe pricing work?" → Clarifies model
4. Official text: "2.9% + $0.30 per successful card charge, volume discounts available"

**Result**:
- `pricingUrl`: `https://stripe.com/pricing`
- `pricingType`: `Usage-based: 2.9% + $0.30 per successful card charge, volume discounts available`

---

### Example 4: Freemium with Clear Tiers

**Input**: "Notion"

**Process**:
1. Found: `https://www.notion.so/pricing`
2. WebFetch: Clear tier structure
3. Official text: "Free for individuals, Plus at $8/user/month, Business at $15/user/month, Enterprise with custom pricing"

**Result**:
- `pricingUrl`: `https://www.notion.so/pricing`
- `pricingType`: `Freemium (free for individuals, Plus at $8/user/month, Business at $15/user/month, Enterprise custom)`

---

### Example 5: No Pricing Available

**Input**: "Custom Internal Tool"

**Process**:
1. Searched: No pricing page exists
2. Perplexity: No public pricing information found
3. Official website: Only "Contact us" page

**Result**:
- `pricingUrl`: (empty)
- `pricingType`: `Not Publicly Available`

---

### Example 6: Open Source / Free

**Input**: "VS Code"

**Process**:
1. Found: `https://code.visualstudio.com`
2. WebFetch: No pricing page, mentions "Free and open source"
3. Confirmed: Completely free

**Result**:
- `pricingUrl`: `https://code.visualstudio.com`
- `pricingType`: `Free (Open Source)`

---

### Example 7: Complex Hybrid Model

**Input**: "AWS EC2"

**Process**:
1. Found: `https://aws.amazon.com/ec2/pricing/`
2. WebFetch: Very complex pricing structure
3. Perplexity: "AWS EC2 pricing model explained"
4. Extract key model: "Pay-as-you-go for compute hours + data transfer + storage, multiple instance types"

**Result**:
- `pricingUrl`: `https://aws.amazon.com/ec2/pricing/`
- `pricingType`: `Usage-based: pay per compute hour (varies by instance type), plus data transfer and storage fees`

## Quality Checklist

Before finalizing, verify:

### Pricing URL:
- [ ] **URL is from official source** - Application's own website or official provider domain
- [ ] **URL is accessible** - Returns 200 or valid redirect
- [ ] **URL contains actual pricing** - Not just "contact sales" page
- [ ] **URL is specific** - Points to pricing page, not generic homepage
- [ ] **No hallucination** - URL was found through research, not constructed

### Pricing Type:
- [ ] **Information is from official source** - Not from G2, Capterra, or review sites
- [ ] **Text is descriptive** - Clearly explains pricing model
- [ ] **Length appropriate** - 20-150 characters (concise but complete)
- [ ] **Accurate** - Reflects current pricing model
- [ ] **Normalized only if needed** - Official text used when clear, normalized when vague
- [ ] **No marketing language** - Removed phrases like "flexible", "competitive", "affordable"
- [ ] **If no reliable pricing found** - Used "Not Publicly Available" and left URL blank (did not guess or fabricate)

## Common Mistakes to Avoid

### URL Mistakes:

❌ **Using third-party URLs**
- Wrong: `https://g2.com/products/slack/pricing`
- Correct: `https://slack.com/pricing`

❌ **Using generic contact pages**
- Wrong: `https://app.com/contact-sales` (no pricing info)
- Correct: Find actual pricing page or mark as "Not Publicly Available"

❌ **Hallucinating URLs**
- Wrong: Assuming `https://app.com/pricing` exists without verification
- Correct: Try the URL, verify it's accessible and contains pricing

❌ **Using homepage when pricing page exists**
- Wrong: `https://slack.com` when `https://slack.com/pricing` exists
- Correct: Use the specific pricing page

### Pricing Type Mistakes:

❌ **Copying vague text without normalization**
- Wrong: "Flexible pricing options available"
- Correct: Research specifics or normalize: `Not Publicly Available` or `Contact for Quote`

❌ **Using third-party information**
- Wrong: G2 says "$50/month" but official site says "Contact sales"
- Correct: Use official source: `Not Publicly Available`

❌ **Being too verbose**
- Wrong: "This application offers a comprehensive pricing structure with multiple tiers designed for businesses of all sizes, featuring a free trial period followed by monthly subscription options that can be paid annually for a discount..."
- Correct: "Freemium with subscription tiers from $29-$299/month (annual discount available)"

❌ **Over-normalizing when text is clear**
- Wrong: Official says "Free for up to 10 users, $12/user/month after" → You write "Freemium"
- Correct: Keep the descriptive official text

❌ **Including marketing language**
- Wrong: "Competitive pricing with flexible options to meet your needs"
- Correct: Remove marketing fluff, describe actual model

❌ **Not researching thoroughly**
- Wrong: Couldn't find pricing page in 30 seconds → Mark as "Not Public"
- Correct: Try multiple search strategies, Perplexity queries, common URL patterns

## Handling Edge Cases

### Case 1: Pricing Requires Login/Account

**Example**: Pricing page is behind authentication

**Solution**:
- `pricingUrl`: `https://app.com/pricing` (if URL exists)
- `pricingType`: `Pricing Available After Account Creation` or `Not Publicly Available`
- Try Perplexity to find if pricing info is discussed elsewhere

### Case 2: Regional Pricing Variations

**Example**: Different prices for US, EU, etc.

**Solution**:
- `pricingUrl`: Use main pricing page URL
- `pricingType`: Mention variation if significant: `Subscription-based ($29-$49/month, varies by region)`
- Or use base/primary market pricing

### Case 3: Multiple Products on One Pricing Page

**Example**: Provider has multiple products, all on one /pricing page

**Solution**:
- `pricingUrl`: `https://provider.com/pricing#product-name` (use anchor if available)
- `pricingType`: Extract pricing for this specific application, not all products

### Case 4: Deprecated/Archived Pricing

**Example**: Product is discontinued or legacy

**Solution**:
- Research if still available for purchase
- If truly deprecated: `pricingType`: `No Longer Available (Deprecated)`
- If still available to existing customers: Extract available pricing info

### Case 5: Only Annual Billing Available

**Example**: No monthly option, only yearly

**Solution**:
- Be specific: `$1,200/year per user (annual billing only, no monthly option)`
- Don't falsely represent as monthly

### Case 6: Freemium with No Public Paid Pricing

**Example**: Free tier public, paid tier is "contact sales"

**Solution**:
- `pricingType`: `Freemium (free tier available, paid plans require contact for pricing)`

## Summary

**DO**:
- Search thoroughly for official pricing page
- Validate URL accessibility and content
- Extract descriptive text from official source
- Keep clear official text as-is (don't over-normalize)
- Normalize only when source text is vague
- Use Perplexity + WebFetch to understand pricing model
- Prioritize accuracy over speed
- Return both pricingUrl and pricingType together
- **Default to "Not Publicly Available" when no reliable pricing is found**

**DON'T**:
- Use third-party pricing information (G2, Capterra)
- Hallucinate or construct URLs
- Copy vague text without normalization
- Be overly verbose or include marketing language
- Rush the research process
- Return pricing type without the source URL
- Use generic contact pages as pricing URLs
- **Guess or fabricate pricing when information isn't available**
- **Return uncertain or unverified pricing information**
- **Use outdated or third-party pricing claims as a fallback**

**Remember**: Pricing URL and Pricing Type are linked. The URL is your source of truth, and the pricing type is extracted from that source. Always research thoroughly, validate the URL, and provide descriptive pricing information that helps users understand how the application is priced.

---

*Document created: 2026-02-22*
*Version: 1.0*
