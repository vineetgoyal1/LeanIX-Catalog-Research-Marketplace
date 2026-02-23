# Application Collection Status and Deprecated Guidelines

## Purpose

This guideline helps AI agents set the `collectionStatus` and `deprecated` fields for Application fact sheets in LeanIX. These fields track the data collection workflow status and whether the application is still actively maintained.

**Note:** Both fields have fixed values for current workflow. No decision-making required.

## Fields Covered

### 1. collectionStatus (Enum Field)
**LeanIX field name:** `collectionStatus`
**Type:** Enumerated value
**Required:** Yes
**Current value:** Always set to `inReview`

### 2. deprecated (Enum Field)
**LeanIX field name:** `deprecated`
**Type:** Enumerated value (or boolean in some contexts)
**Required:** Yes
**Current value:** Always set to `no`

---

## Quick Reference

| Field | Set To | Always? |
|-------|--------|---------|
| `collectionStatus` | `inReview` | Yes |
| `deprecated` | `no` | Yes |

**No exceptions. No decision-making required.**

---

## Field 1: Collection Status

### What is Collection Status?

The `collectionStatus` field tracks the data collection and review workflow stage for the Application fact sheet. It indicates where the application is in the data quality assurance process.

**Possible values (in typical workflow):**
- `inReview` - Information has been collected and is pending review
- `approved` - Information has been reviewed and approved
- `draft` - Work in progress, incomplete
- Other workflow-specific values

### Current Instruction

**ALWAYS set to:** `inReview`

**Why `inReview`?**
- Indicates information has been collected and is ready for review
- Follows the standard data collection workflow
- Allows data quality team to review and approve
- Maintains audit trail of data collection activities

### When to Set

**Always set when:**
- Creating a new Application fact sheet
- Updating an existing Application fact sheet
- No exceptions

### Format

**Correct:**
```json
{
  "collectionStatus": "inReview"
}
```

**Incorrect:**
```json
{
  "collectionStatus": "approved"    // ❌ Don't set to approved
}
{
  "collectionStatus": "draft"       // ❌ Don't set to draft
}
{
  "collectionStatus": "in-review"   // ❌ Wrong format (hyphen)
}
{
  "collectionStatus": "InReview"    // ❌ Wrong capitalization
}
{
  "collectionStatus": ""            // ❌ Don't leave blank
}
```

### Important Notes

**Do NOT:**
- Set to any other value besides `inReview`
- Leave blank
- Try to determine the "correct" workflow status
- Set to `approved` (review team will do this)

**Workflow context:**
- You set: `inReview` (data collected, needs review)
- Review team sets: `approved` (after verification)
- This maintains proper workflow and accountability

---

## Field 2: Deprecated

### What is Deprecated?

The `deprecated` field indicates whether an application has been discontinued, retired, or is no longer actively maintained by its provider.

**Possible values:**
- `no` - Application is active and maintained
- `yes` - Application is deprecated/discontinued

### Current Instruction

**ALWAYS set to:** `no`

**Why `no`?**
- Assumes applications being added are currently active
- Deprecated applications typically don't need new fact sheets
- If an application was deprecated, it wouldn't normally be added to the catalog
- Existing applications may be marked as deprecated later by administrators

### When to Set

**Always set when:**
- Creating a new Application fact sheet
- Updating an existing Application fact sheet (unless changing deprecation status)
- No exceptions for new applications

### Format

**Correct:**
```json
{
  "deprecated": "no"
}
```

**Incorrect:**
```json
{
  "deprecated": "yes"        // ❌ Don't mark new apps as deprecated
}
{
  "deprecated": "false"      // ❌ Use "no" not "false"
}
{
  "deprecated": "No"         // ❌ Wrong capitalization
}
{
  "deprecated": ""           // ❌ Don't leave blank
}
{
  "deprecated": null         // ❌ Don't leave null
}
```

### Important Notes

**Do NOT:**
- Set to any value besides `no` for new applications
- Try to determine if application is deprecated
- Leave blank

**If you discover an application IS deprecated:**
- Do NOT create a fact sheet for it (typically)
- Consult with catalog administrators
- Deprecated applications are usually not added to active catalog

**Exception scenario:**
- If specifically instructed to add a deprecated application (rare)
- Then you may set to `yes`, but this is unusual

---

## Combined Workflow Example

### Creating New Application Fact Sheet

**Scenario:** You're creating a fact sheet for "Smartsheet"

**Required fields to set:**
```json
{
  "name": "Smartsheet",
  "description": "Smartsheet provides an online application for collaboration...",
  "hostingType": "saas",
  "collectionStatus": "inReview",  // Always this value
  "deprecated": "no",              // Always this value
  "asOfDate": "2026-02-22"
}
```

**Why these values?**
- `collectionStatus: "inReview"` - Following standard workflow, data ready for review
- `deprecated: "no"` - Smartsheet is an active, maintained application

---

### Updating Existing Application

**Scenario:** Updating SSO status for "AWS Lambda"

**Fields to update:**
```json
{
  "ssoStatus": "supported",        // Updated information
  "collectionStatus": "inReview",  // Set to inReview (even if previously approved)
  "deprecated": "no",              // Keep as no
  "asOfDate": "2026-02-22"         // Update to today
}
```

**Why reset `collectionStatus` to `inReview`?**
- New information has been added
- Requires review/approval again
- Maintains data quality workflow

---

## Common Mistakes

### Mistake 1: Trying to Set "Approved" Status

**Wrong reasoning:**
> "I thoroughly researched this application, so I'll mark it as 'approved'."

**Why wrong:**
- `approved` status is set by review team, not data collectors
- Maintains separation of duties (collection vs. review)
- Your role is to collect data, review team validates it

**Correct approach:**
- Always set to `inReview`
- Let review team approve

---

### Mistake 2: Marking Active Application as Deprecated

**Wrong reasoning:**
> "This application is old (launched in 2010), so I'll mark it as deprecated."

**Why wrong:**
- Age ≠ deprecated
- Deprecated means discontinued/no longer maintained
- Many older applications are still actively maintained

**Correct approach:**
- Always set to `no` for new fact sheets
- Only mark `yes` if explicitly confirmed discontinued

**Example:**
- Microsoft Excel (launched 1985) → Still active, `deprecated: "no"`
- Google Reader (discontinued 2013) → Deprecated, but wouldn't create new fact sheet

---

### Mistake 3: Leaving Fields Blank

**Wrong:**
```json
{
  "collectionStatus": "",
  "deprecated": null
}
```

**Why wrong:**
- These fields should always have values
- Blank values cause data quality issues

**Correct:**
```json
{
  "collectionStatus": "inReview",
  "deprecated": "no"
}
```

---

### Mistake 4: Wrong Capitalization

**Wrong:**
```json
{
  "collectionStatus": "InReview",   // ❌
  "deprecated": "No"                // ❌
}
```

**Correct:**
```json
{
  "collectionStatus": "inReview",   // ✅ (camelCase)
  "deprecated": "no"                // ✅ (lowercase)
}
```

---

### Mistake 5: Using Boolean for Deprecated

**Wrong:**
```json
{
  "deprecated": false               // ❌ (boolean)
}
```

**Correct:**
```json
{
  "deprecated": "no"                // ✅ (string)
}
```

**Note:** While some systems might accept boolean, use string `"no"` for consistency.

---

## Quality Checklist

Before finalizing, verify:

### For collectionStatus:
- [ ] Set to `inReview` (exactly this value)
- [ ] Lowercase "i" in "in", capital "R" in "Review" (camelCase)
- [ ] Not blank
- [ ] Not set to any other value

### For deprecated:
- [ ] Set to `no` (exactly this value)
- [ ] Lowercase "no"
- [ ] Not blank
- [ ] Not set to "yes"
- [ ] Not using boolean (false/true)

---

## Special Cases

### Case 1: Updating Previously Approved Application

**Question:** If I'm updating an application that was previously `collectionStatus: "approved"`, what should I set?

**Answer:** Reset to `inReview`

**Reason:**
- New information requires re-review
- Maintains data quality workflow
- Review team will re-approve after verification

---

### Case 2: Application is Actually Deprecated

**Question:** I discovered an application is no longer maintained. Should I still create a fact sheet with `deprecated: "no"`?

**Answer:** Do NOT create the fact sheet

**Reason:**
- Deprecated applications typically not added to active catalog
- Focus on current, active applications
- If there's a specific business need, consult administrators

**Exception:**
- If explicitly instructed to add deprecated application
- Then set `deprecated: "yes"`
- Document deprecation details in comments/notes

---

### Case 3: Application Has "Beta" or "Preview" Status

**Question:** Application is in beta/preview. Should I mark as deprecated?

**Answer:** NO - set `deprecated: "no"`

**Reason:**
- Beta/preview ≠ deprecated
- Beta means early access, still active
- Deprecated means discontinued/retired

**Beta applications are active, just early-stage.**

---

### Case 4: Free Tier Discontinued, Paid Tier Active

**Question:** Application discontinued free tier but paid tier is active. Deprecated?

**Answer:** NO - set `deprecated: "no"`

**Reason:**
- Application still exists and is maintained
- Pricing changes ≠ deprecation
- Only mark deprecated if entire application discontinued

---

## Integration with Other Fields

### Relationship to Other Status Fields

**collectionStatus** tracks data collection workflow:
- `inReview` - You've done your part, waiting for review
- `approved` - Review team verified and approved

**deprecated** tracks application lifecycle:
- `no` - Application is active
- `yes` - Application is discontinued

**These are independent:**
- An active application can be `inReview` or `approved` (based on workflow)
- A deprecated application could theoretically be `approved` (if added for historical reasons)

---

## Workflow Summary

### Standard Workflow

```
1. You research application
   ↓
2. Create/update fact sheet
   ↓
3. Set collectionStatus: "inReview"
   Set deprecated: "no"
   ↓
4. Submit for review
   ↓
5. Review team validates
   ↓
6. Review team sets collectionStatus: "approved"
   (deprecated stays "no" unless app is actually deprecated)
```

**Your responsibility:** Steps 1-3
**Review team responsibility:** Steps 5-6

---

## Examples Summary

| Scenario | collectionStatus | deprecated | Notes |
|----------|------------------|------------|-------|
| New active application | `inReview` | `no` | Standard case |
| Updating existing app | `inReview` | `no` | Reset to inReview |
| Beta/preview application | `inReview` | `no` | Beta is still active |
| Old but maintained app | `inReview` | `no` | Age doesn't matter |
| Actually deprecated app | N/A | N/A | Don't create fact sheet |

---

## Summary

### Simple Rules

**collectionStatus:**
- Always set to: `inReview`
- No exceptions
- No decision-making

**deprecated:**
- Always set to: `no`
- No exceptions for new applications
- Assumes application is active

### Format

```json
{
  "collectionStatus": "inReview",
  "deprecated": "no"
}
```

### Remember

- Don't try to set `approved` (review team does this)
- Don't mark active applications as deprecated
- Don't leave blank
- Use exact capitalization shown

---

## Quick Reference Card

```
Field: collectionStatus
Value: "inReview"
Always: Yes
Format: camelCase (inReview)

Field: deprecated
Value: "no"
Always: Yes (for new apps)
Format: lowercase (no)

✅ DO:
- Set collectionStatus to "inReview"
- Set deprecated to "no"
- Use exact capitalization
- Set both fields always

❌ DON'T:
- Set collectionStatus to "approved"
- Set deprecated to "yes" (unless app actually discontinued)
- Leave fields blank
- Use wrong capitalization
- Use boolean for deprecated
```

---

## Revision History

- **Version 1.0** (2026-02-22): Initial creation with fixed-value instructions for current workflow

