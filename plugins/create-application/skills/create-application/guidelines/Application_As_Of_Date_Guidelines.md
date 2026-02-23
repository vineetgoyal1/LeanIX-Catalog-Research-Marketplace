# Application As-of Date Guidelines

## Purpose

This guideline helps AI agents set the `asOfDate` field for Application fact sheets in LeanIX. This field records when the application information was last researched, verified, or updated, serving as a data freshness indicator.

## Field Information

**LeanIX field name:** `asOfDate`
**Type:** Date (ISO 8601 format: YYYY-MM-DD)
**Required:** Yes (recommended to always set)
**Purpose:** Track when the application data was last verified/researched

## Quick Reference

**What to set:** Current date in YYYY-MM-DD format
**When to set:** Always, when creating or updating application information
**Example:** `2026-02-22` (for February 22, 2026)

---

## What is As-of Date?

The `asOfDate` field captures **when the information in the fact sheet was last verified or researched**. It serves as a data quality indicator, helping users understand how current and reliable the information is.

**This field answers:** "When was this information last confirmed to be accurate?"

### Why It Matters

**Data freshness tracking:**
- Organizations can identify stale information that needs updating
- Audit teams can verify data quality based on recency
- Users can trust information based on how recently it was verified

**Quality assurance:**
- Enables tracking of data collection/update activities
- Helps prioritize which fact sheets need refreshing
- Provides accountability for research activities

---

## When to Set As-of Date

### Always Set When:

1. **Creating a new Application fact sheet**
   - Set to the date you performed the research
   - Typically the current date

2. **Updating Application information**
   - Set to the date you verified/updated the information
   - Even if only updating one field

3. **Verifying existing information**
   - Even if no changes made, update asOfDate to confirm data is still accurate
   - Indicates "checked and verified on this date"

### Format Requirements

**Required format:** ISO 8601 date format
```
YYYY-MM-DD
```

**Examples:**
- ✅ `2026-02-22` (February 22, 2026)
- ✅ `2025-12-31` (December 31, 2025)
- ✅ `2026-01-05` (January 5, 2026)

**Invalid formats:**
- ❌ `22-02-2026` (wrong order)
- ❌ `02/22/2026` (wrong separators)
- ❌ `2026-2-22` (missing leading zero on month)
- ❌ `Feb 22, 2026` (not ISO format)

---

## How to Determine As-of Date

### Simple Rule

**Set to the current date when you research/update the application.**

### Decision Process

```
When did you research/verify this application information?
  ↓
TODAY → Set to today's date (YYYY-MM-DD)
  ↓
SPECIFIC PAST DATE → Set to that date (if updating based on past research)
  ↓
Format the date as YYYY-MM-DD
  ↓
Done
```

### Common Scenarios

#### Scenario 1: Creating New Application

**Situation:** You're researching a new application and creating its fact sheet today.

**Action:** Set `asOfDate` to today's date

**Example:**
- Today is February 22, 2026
- You research "Smartsheet" and create the fact sheet
- Set: `asOfDate: "2026-02-22"`

---

#### Scenario 2: Updating Existing Application

**Situation:** Existing fact sheet needs updating (e.g., SSO status changed).

**Action:** Set `asOfDate` to today's date (date of verification/update)

**Example:**
- Previous `asOfDate: "2025-11-15"`
- Today is February 22, 2026
- You verify SSO support was added
- Update: `asOfDate: "2026-02-22"`

---

#### Scenario 3: Verifying Without Changes

**Situation:** You check existing information and confirm it's still accurate, but make no changes.

**Action:** Update `asOfDate` to today's date anyway

**Reason:** This indicates "information verified as current on this date"

**Example:**
- Previous `asOfDate: "2025-06-10"`
- Today is February 22, 2026
- You verify description, URLs, SSO status are still accurate
- Update: `asOfDate: "2026-02-22"` (even though no other fields changed)

---

#### Scenario 4: Batch Research with Different Dates

**Situation:** You researched multiple applications over several days.

**Action:** Set each application's `asOfDate` to the date you researched that specific application

**Example:**
- Researched App A on Feb 20, 2026 → `asOfDate: "2026-02-20"`
- Researched App B on Feb 22, 2026 → `asOfDate: "2026-02-22"`
- Researched App C on Feb 22, 2026 → `asOfDate: "2026-02-22"`

---

#### Scenario 5: Information from Past Research

**Situation:** You're entering information that was researched on a specific past date.

**Action:** Set `asOfDate` to the date the research was performed (if known and recent)

**Guideline:**
- If research is recent (within last 30 days) → Use research date
- If research is old (>30 days) → Consider re-verifying and using today's date
- If research date unknown → Use today's date

**Example:**
- You have research notes from Feb 15, 2026
- Today is Feb 22, 2026
- Set: `asOfDate: "2026-02-15"` (acceptable, recent)

---

## Format Validation

### ISO 8601 Date Format

**Components:**
```
YYYY-MM-DD
│    │  │
│    │  └─ Day (01-31, with leading zero)
│    └──── Month (01-12, with leading zero)
└───────── Year (4 digits)
```

**Always use:**
- 4-digit year
- 2-digit month (with leading zero if needed: 01, 02, ..., 12)
- 2-digit day (with leading zero if needed: 01, 02, ..., 31)
- Hyphens as separators

### Examples by Month

| Month | Correct Format | Incorrect Format |
|-------|----------------|------------------|
| January 5, 2026 | `2026-01-05` | `2026-1-5` ❌ |
| February 22, 2026 | `2026-02-22` | `2026-2-22` ❌ |
| March 30, 2026 | `2026-03-30` | `03/30/2026` ❌ |
| April 1, 2026 | `2026-04-01` | `2026-04-1` ❌ |
| May 15, 2026 | `2026-05-15` | `May 15, 2026` ❌ |
| December 31, 2026 | `2026-12-31` | `12-31-2026` ❌ |

---

## Getting Current Date

### If You Have Access to System Date

Most environments provide access to the current date. Use it to automatically set `asOfDate`.

**Example (conceptual):**
```
current_date = get_current_date()  # Returns "2026-02-22"
fact_sheet["asOfDate"] = current_date
```

### If Manual Entry Required

1. Determine today's date
2. Format as YYYY-MM-DD
3. Verify format is correct

**Checklist:**
- [ ] Year is 4 digits
- [ ] Month is 2 digits (with leading zero)
- [ ] Day is 2 digits (with leading zero)
- [ ] Separators are hyphens (-)
- [ ] Format is YYYY-MM-DD

---

## Common Mistakes

### Mistake 1: Wrong Date Format

**Wrong:**
```
asOfDate: "02/22/2026"  ❌ (US format)
asOfDate: "22-02-2026"  ❌ (European format)
asOfDate: "2026/02/22"  ❌ (wrong separators)
```

**Correct:**
```
asOfDate: "2026-02-22"  ✅
```

---

### Mistake 2: Missing Leading Zeros

**Wrong:**
```
asOfDate: "2026-2-5"    ❌ (missing leading zeros)
asOfDate: "2026-02-5"   ❌ (day missing leading zero)
asOfDate: "2026-2-22"   ❌ (month missing leading zero)
```

**Correct:**
```
asOfDate: "2026-02-05"  ✅
```

---

### Mistake 3: Not Updating When Verifying

**Wrong reasoning:**
> "I checked the information and it's still accurate, so I don't need to update asOfDate."

**Why wrong:**
- asOfDate should reflect when information was last VERIFIED
- Even if no changes, updating asOfDate shows information was checked

**Correct approach:**
- Update asOfDate to today's date when verifying information
- This indicates "verified as current on this date"

---

### Mistake 4: Using Future Dates

**Wrong:**
```
Today: 2026-02-22
asOfDate: "2026-03-15"  ❌ (future date)
```

**Why wrong:**
- Can't verify information that doesn't exist yet
- asOfDate should be today or earlier

**Correct:**
```
asOfDate: "2026-02-22"  ✅ (today or past date only)
```

---

### Mistake 5: Using Very Old Dates

**Wrong reasoning:**
> "I found research notes from 6 months ago, I'll use that date."

**Why wrong:**
- Old information may be stale
- Better to re-verify and use current date

**Correct approach:**
- If research is recent (<30 days) → Can use research date
- If research is old (>30 days) → Re-verify information and use today's date
- When in doubt → Use today's date

---

### Mistake 6: Leaving Field Blank

**Wrong:**
```
asOfDate: null  ❌
asOfDate: ""    ❌
```

**Why wrong:**
- asOfDate should always be set
- Helps track data quality

**Correct:**
```
asOfDate: "2026-02-22"  ✅ (always set)
```

---

## Integration with Other Fields

### Relationship to Other Date Fields

**asOfDate** is different from:
- `createdAt` - When the fact sheet was first created in LeanIX (system-managed)
- `updatedAt` - When the fact sheet was last modified in LeanIX (system-managed)

**asOfDate specifically tracks:** When the INFORMATION was last researched/verified (user-managed)

### Example Distinction

```
Fact sheet created: 2025-05-10 (createdAt)
Last system update: 2026-01-15 (updatedAt - someone edited a field)
Information verified: 2026-02-22 (asOfDate - you researched and confirmed data)
```

**asOfDate reflects research activity, not system activity.**

---

## Workflow Integration

### When Creating New Application

```
1. Research application (description, SSO, hosting, etc.)
2. Gather all information
3. Set asOfDate to today's date (date of research)
4. Create fact sheet with all fields including asOfDate
```

### When Updating Existing Application

```
1. Review existing information
2. Research/verify current status
3. Update relevant fields
4. Update asOfDate to today's date (date of verification)
5. Save fact sheet
```

---

## Quality Checklist

Before finalizing, verify:

- [ ] asOfDate is set (not blank)
- [ ] Format is YYYY-MM-DD (ISO 8601)
- [ ] Year is 4 digits
- [ ] Month has leading zero (01-12)
- [ ] Day has leading zero (01-31)
- [ ] Date is today or recent past (not future)
- [ ] Date reflects when information was researched/verified
- [ ] Separators are hyphens (-)

---

## Examples Summary

| Scenario | Today's Date | Action | Set asOfDate To |
|----------|--------------|--------|-----------------|
| Creating new application | 2026-02-22 | Researched today | `2026-02-22` |
| Updating SSO status | 2026-02-22 | Verified today | `2026-02-22` |
| Verifying (no changes) | 2026-02-22 | Checked today | `2026-02-22` |
| Using 5-day-old research | 2026-02-22 | Research from Feb 17 | `2026-02-17` (acceptable) |
| Using 60-day-old research | 2026-02-22 | Research from Dec 24 | `2026-02-22` (re-verify, use today) |

---

## Summary

**Simple rule:** Set `asOfDate` to the date you researched or verified the application information, formatted as YYYY-MM-DD.

**Most common case:** Set to today's date when creating or updating applications.

**Format:** Always use ISO 8601 (YYYY-MM-DD) with leading zeros.

**Purpose:** Track data freshness and research activity for quality assurance.

---

## Quick Reference Card

```
Field: asOfDate
Format: YYYY-MM-DD
When: Always (when creating or updating)
Value: Current date (or date of research)
Example: 2026-02-22

✅ DO:
- Set to today's date when researching
- Use ISO 8601 format (YYYY-MM-DD)
- Include leading zeros (02, not 2)
- Update when verifying existing info

❌ DON'T:
- Use US format (MM/DD/YYYY)
- Use European format (DD-MM-YYYY)
- Skip leading zeros
- Leave blank
- Use future dates
- Use very old dates without re-verifying
```

---

## Revision History

- **Version 1.0** (2026-02-22): Initial creation with ISO 8601 format requirements and verification guidance

