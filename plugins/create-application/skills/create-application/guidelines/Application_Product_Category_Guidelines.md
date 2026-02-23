# Application Product Category Guidelines

## Purpose

This guideline helps AI agents determine the correct Product Category for Application fact sheets in LeanIX. The Product Category describes what the application does at a functional level (e.g., "CRM Software", "Project Management Software", "Accounting Software").

## Field Overview

- **API Field Name**: `productCategory`
- **User-Facing Name**: "Product Category"
- **Field Type**: Free text
- **Required**: Strongly recommended (99.9% of applications have this field populated)

## Core Principles

### 1. **Match Existing Categories First (Accuracy Priority)**

There are **3,120+ existing Product Categories** in the database from 16,056 applications. Before creating a new category, thoroughly search for an existing match.

**Why this matters**:
- Maintains consistency across the catalog
- Enables better reporting and analytics
- Avoids duplicate categories with slight variations

### 2. **Hierarchical Structure**

Many categories use a hierarchical format with "/" separators:

**Pattern**: `[Broad Category] / [Specific Subcategory]`

**Examples**:
- `Accounting & Finance Software / Accounting Software`
- `Talent Management Software / Corporate Learning Management Systems`
- `Marketing Automation Software`
- `CRM Software`

**Guidelines**:
- Use hierarchy when the application fits a specific subcategory
- Use broad category alone if application spans multiple subcategories
- Match the existing pattern in the database

### 3. **Accuracy Over Speed**

Take time to research thoroughly:
- Check product website
- Review G2 listing
- Check Capterra categorization
- Analyze existing similar applications
- Verify category matches functionality

**Do NOT** rush to create new categories. Most applications will match existing ones.

## Step-by-Step Process

### Step 1: Search Existing Categories

**Reference File**: `Product_Category_Reference.json` (contains all 3,120 categories with frequency counts)

**Search Strategy**:

1. **Exact keyword match**: Search for key terms from application name/description
   - Example: For "Salesforce" → Search: "CRM", "Customer", "Sales"
   - Found: `CRM Software` (94 applications use this)

2. **Fuzzy matching**: Account for variations
   - `HR / Talent Management` (107 apps)
   - `Talent Management Software` (variations exist)
   - `Core HR Software` (83 apps)
   - Choose the most common variant

3. **Check similar applications**: Find comparable apps in the database
   - Example: For "HubSpot" → Find "Salesforce" category → `CRM Software`
   - Example: For "Asana" → Find "Monday.com" category → `Project Management Software`

4. **Hierarchical search**: Look for both broad and specific categories
   - Search: "Accounting" → Find multiple:
     - `Accounting & Finance Software / Accounting Software` (54 apps)
     - `Accounting Software` (standalone, less common)
     - `Accounting & Finance Software / Accounts Payable Automation Software`
   - Choose based on specificity

**Top 50 Most Common Categories** (for quick reference):

| Count | Category |
|-------|----------|
| 107 | HR / Talent Management |
| 94 | CRM Software |
| 87 | Commerce / E-Commerce Software |
| 83 | Core HR Software |
| 82 | Project, Portfolio & Program Management Software / Project Management Software |
| 79 | SAP Store Software |
| 65 | E-Signature Software |
| 64 | ERP / Accounting |
| 60 | Talent Management Software / Corporate Learning Management Systems |
| 60 | Analytics Platforms |
| 58 | ERP Systems |
| 57 | Workforce Management Software |
| 56 | Marketing Automation Software |
| 56 | Email Marketing Software |
| 55 | Process Automation Software / Business Process Management Software |
| 55 | Development / DevOps |
| 54 | Accounting & Finance Software / Accounting Software |
| 51 | Vertical Industry / Education |
| 49 | Other Development Software |
| 49 | Financial Services Software / Other Finance & Insurance Software |

### Step 2: If No Match Found → Research

**Only if absolutely no existing category matches**, research to create a new category.

**Research Sources (in priority order)**:

1. **G2 Product Page** (Primary)
   - Go to `g2.com` → Search for application
   - Check "Categories" section
   - Use G2's primary category designation

2. **Capterra Listing**
   - Go to `capterra.com` → Search for application
   - Check "Category" on product page
   - Note: May differ from G2, cross-reference both

3. **Product Website**
   - Check "Features" or "Solutions" page
   - Look for self-described category
   - Check meta tags/SEO descriptions

4. **Software Review Sites**
   - SourceForge, Product Hunt, AlternativeTo
   - See how the product is categorized

**Research Process**:

```
1. Search G2 for "[Application Name]"
   ↓
2. Find product listing
   ↓
3. Note primary category (e.g., "CRM Software")
   ↓
4. Check if this category already exists in our database
   ↓
5. If exists → Use it (even with slight variations)
6. If not → Verify with Capterra
   ↓
7. If both agree → Create new category using G2 format
```

### Step 3: Format the Category

**Formatting Rules**:

1. **Capitalization**: Title Case for each word
   - ✅ `CRM Software`
   - ❌ `crm software` or `CRM software`

2. **Hierarchy Separator**: Use ` / ` (space-slash-space)
   - ✅ `Accounting & Finance Software / Accounting Software`
   - ❌ `Accounting & Finance Software/Accounting Software` (no spaces)
   - ❌ `Accounting & Finance Software - Accounting Software` (wrong separator)

3. **Ampersand vs. "and"**: Follow existing pattern
   - Use `&` for common phrases: `HR & Payroll`, `Accounting & Finance Software`
   - Use `and` for other cases: `Project and Portfolio Management`

4. **"Software" suffix**: Include when it's the standard pattern
   - ✅ `CRM Software`, `Marketing Automation Software`
   - ✅ `Analytics Platforms` (uses "Platforms" instead)
   - Consistency: Follow what existing similar categories use

5. **Plurals**: Check existing usage
   - `Analytics Platforms` (plural)
   - `Marketing Automation Software` (singular)
   - Match the existing pattern

## Common Category Patterns

### Pattern 1: Broad Functional Category

Simple, single-level categories for widely-known application types:

**Examples**:
- `CRM Software`
- `ERP Systems`
- `Analytics Platforms`
- `Marketing Automation Software`
- `Project Management Software`

**When to use**: Application is a well-known category that doesn't need subcategorization.

### Pattern 2: Hierarchical Category

Two-level categories for more specific functional areas:

**Examples**:
- `Accounting & Finance Software / Accounting Software`
- `Talent Management Software / Corporate Learning Management Systems`
- `E-Commerce Software / E-Commerce Platforms`
- `Video Software / Video Editing Software`

**When to use**: Application fits a specific subcategory within a broader domain.

### Pattern 3: Industry Vertical Category

Categories that indicate industry-specific solutions:

**Examples**:
- `Vertical Industry / Education`
- `Financial Services Software / Other Finance & Insurance Software`
- `Healthcare Software / Medical Practice Management Software`

**When to use**: Application is designed for a specific industry.

### Pattern 4: Technology/Infrastructure Category

Categories for developer tools and infrastructure:

**Examples**:
- `Development / DevOps`
- `API Management Software`
- `Cloud Infrastructure Software`
- `Database Software`

**When to use**: Application is a technical tool or infrastructure component.

### Pattern 5: Multi-Function Category

Some applications span multiple categories, indicated by multiple slashes:

**Examples**:
- `Project, Portfolio & Program Management Software / Project Management Software`
- `Accounting & Finance Software / Travel & Expense Software / Travel Management Software`

**When to use**: Application has multiple distinct functional areas. Use sparingly.

## Decision Tree

```
Input: Application Name + Description

1. Extract key functional terms
   ↓
2. Search existing 3,120 categories
   → Found exact or close match?
     ├─ YES → Use existing category
     └─ NO → Continue to Step 3
   ↓
3. Find similar applications in database
   → Comparable app exists?
     ├─ YES → Use their category
     └─ NO → Continue to Step 4
   ↓
4. Research on G2
   → G2 listing exists?
     ├─ YES → Check G2 primary category
     │         → Category exists in our DB?
     │           ├─ YES → Use it
     │           └─ NO → Continue to Step 5
     └─ NO → Continue to Step 5
   ↓
5. Research on Capterra
   → Capterra listing exists?
     ├─ YES → Check Capterra category
     │         → Matches G2 or close variation?
     │           ├─ YES → Create new category (G2 format preferred)
     │           └─ NO → Use most specific/common format
     └─ NO → Continue to Step 6
   ↓
6. Check product website
   → Self-described category clear?
     ├─ YES → Create new category based on description
     └─ NO → Use generic category
               (e.g., "Business Software", "Productivity Software")
```

## Example Workflows

### Example 1: Exact Match Found

**Input**: "Salesforce"
**Description**: "CRM platform for managing customer relationships..."

**Process**:
1. Search existing categories: "CRM"
2. Found: `CRM Software` (94 applications)
3. **Result**: `CRM Software` ✓

---

### Example 2: Similar Application Match

**Input**: "HubSpot"
**Description**: "Marketing and sales platform..."

**Process**:
1. Search existing categories: "Marketing", "CRM"
2. Found multiple:
   - `CRM Software` (94 apps)
   - `Marketing Automation Software` (56 apps)
3. Check similar apps: Salesforce uses `CRM Software`
4. HubSpot has both CRM and Marketing features
5. Research G2: HubSpot is primarily categorized as "Marketing Automation"
6. **Result**: `Marketing Automation Software` ✓

---

### Example 3: Hierarchical Match

**Input**: "QuickBooks"
**Description**: "Accounting software for small businesses..."

**Process**:
1. Search existing categories: "Accounting"
2. Found:
   - `Accounting Software` (standalone, less common)
   - `Accounting & Finance Software / Accounting Software` (54 apps) ← More common
3. **Result**: `Accounting & Finance Software / Accounting Software` ✓

---

### Example 4: Fuzzy Match Required

**Input**: "Notion"
**Description**: "All-in-one workspace for notes, docs, projects..."

**Process**:
1. Search existing categories: "Workspace", "Collaboration", "Notes"
2. Found variations:
   - `Collaboration Software`
   - `Note-Taking Software`
   - `Project Management Software`
3. Check similar apps: Confluence, Evernote categories
4. Research G2: Notion is "Knowledge Management Software"
5. Search our DB: `Knowledge Management Software` exists? → Check
6. **Result**: Use existing match or closest variation

---

### Example 5: New Category Needed

**Input**: "Runway ML"
**Description**: "AI-powered video editing and creation tool..."

**Process**:
1. Search existing categories: "AI", "Video"
2. Found:
   - `AI Video Generators` (exists)
   - `Video Software / Video Editing Software` (44 apps)
3. Check G2: Listed under "AI Video Generators"
4. Search our DB: `AI Video Generators` exists? → **YES**
5. **Result**: `AI Video Generators` ✓ (existing category)

---

### Example 6: Truly New Category

**Input**: "BrandNewTech AI"
**Description**: "Revolutionary AI-powered quantum blockchain..."

**Process**:
1. Search existing categories: None match
2. Find similar apps: None found
3. Research G2: Not listed
4. Research Capterra: Not listed
5. Check website: Self-described as "Enterprise AI Platform"
6. Search our DB: `AI Platforms` exists? → Check variations
7. Found: `AI & Machine Learning Platforms` (exists)
8. **Result**: `AI & Machine Learning Platforms` ✓

## Quality Checklist

Before finalizing Product Category, verify:

- [ ] **Searched existing 3,120 categories thoroughly** - Used keyword search, fuzzy matching
- [ ] **Checked similar applications** - Found comparable apps and their categories
- [ ] **Researched if no match** - Checked G2, Capterra, product website
- [ ] **Correct formatting** - Title Case, proper hierarchy separator (` / `)
- [ ] **No duplicate creation** - Verified category doesn't exist with slight variation
- [ ] **Matches functionality** - Category accurately describes what the application does
- [ ] **Consistency** - Follows existing patterns in the database

## Common Mistakes to Avoid

❌ **Creating duplicate categories with variations**
- Existing: `CRM Software`
- Wrong: `CRM Systems` (different from existing)
- Correct: Use `CRM Software`

❌ **Being too specific when broader category exists**
- Wrong: `Customer Relationship Management Software for Small Businesses`
- Correct: `CRM Software`

❌ **Using marketing language**
- Wrong: `AI-Powered Revolutionary Marketing Automation`
- Correct: `Marketing Automation Software`

❌ **Incorrect hierarchy separator**
- Wrong: `Accounting Software - Financial Management`
- Wrong: `Accounting Software/Financial Management` (no spaces)
- Correct: `Accounting & Finance Software / Financial Management Software`

❌ **Inconsistent capitalization**
- Wrong: `crm software`
- Wrong: `Crm Software`
- Correct: `CRM Software`

❌ **Not checking if category already exists**
- Before creating `Project Collaboration Tools`, check if `Collaboration Software` or `Project Management Software` exists

❌ **Using product name in category**
- Wrong: `Salesforce CRM Software`
- Correct: `CRM Software`

❌ **Overly generic categories**
- Avoid: `Business Software`, `Enterprise Tools`
- Use specific functional categories instead

## Handling Edge Cases

### Case 1: Application with Multiple Functions

**Example**: Notion (notes, docs, projects, wikis)

**Solution**: Choose the **primary** function or **most specific** category
- Check G2 primary category
- If truly multi-functional, use most common existing multi-category format
- Prefer single category over complex hierarchies

### Case 2: Category Exists with Slight Variation

**Example**:
- Existing: `E-Commerce Software / E-Commerce Platforms`
- Found on G2: `Ecommerce Platforms`

**Solution**: Use **existing** category format, even if G2 differs slightly
- Database consistency > External source consistency

### Case 3: Very Niche Application

**Example**: "Specialized Drone Fleet Management for Agriculture"

**Solution**:
1. Check if `Agriculture Software` category exists → Yes
2. Check if more specific exists: `Agriculture Software / Precision Agriculture Software` → Yes
3. Use existing specific category

### Case 4: Application Category Changed Over Time

**Example**: Slack (started as chat, now full collaboration)

**Solution**: Use **current** primary function, not historical
- Research current G2/Capterra categorization
- Reflect what the application does today

### Case 5: Regional/Language Variations

**Example**: "E-Commerce" vs "eCommerce" vs "E commerce"

**Solution**: Follow **existing database pattern**
- Search: Find most common variation
- Use consistent formatting

## Tips for Efficient Matching

### 1. Start with Keywords

Extract key terms from application name and description:
- "Salesforce CRM" → Keywords: "CRM", "Customer", "Sales"
- "QuickBooks Online" → Keywords: "Accounting", "Finance", "Bookkeeping"

### 2. Use Frequency as a Guide

High-frequency categories are more likely to be correct for common applications:
- `CRM Software` (94 apps) is very common
- `Specialized Niche Category` (1 app) is less reliable as a match

### 3. Check Competitor Categories

Find direct competitors and use their category:
- HubSpot → Check Salesforce, Pipedrive
- Asana → Check Monday.com, Trello, Jira

### 4. Cross-Reference Multiple Sources

If G2 says "Marketing Automation" and Capterra says "CRM", check:
- Which is the **primary** function?
- What do similar apps use?
- What's most accurate for current state?

### 5. When in Doubt, Go Broader

Better to use a broader existing category than create a hyper-specific new one:
- Existing: `Project Management Software`
- Don't create: `Agile Sprint Planning Software for Remote Teams`

## Summary

**DO**:
- Search existing 3,120 categories thoroughly before creating new ones
- Check similar applications for category consistency
- Research G2 and Capterra when no match exists
- Use proper formatting (Title Case, ` / ` separator)
- Prioritize accuracy over speed
- Match exact existing categories when close variations exist

**DON'T**:
- Create duplicate categories with slight variations
- Rush to create new categories
- Use marketing language in categories
- Ignore hierarchical structure
- Make up categories without research
- Use inconsistent capitalization or formatting

**Remember**: 99.9% of applications will match one of the existing 3,120 categories. Take time to find the right match. New categories should be rare and well-researched.

---

## Reference Files

- **Product_Category_Reference.json** - Complete list of 3,120 existing categories with frequency counts
- **Applications.xlsx** - Source data with all 16,056 applications and their categories

---

*Document created: 2026-02-22*
*Version: 1.0*
