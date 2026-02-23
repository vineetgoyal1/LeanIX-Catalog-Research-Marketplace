# Application Subtype Guidelines

## Purpose

This guideline helps AI agents set the correct Application Subtype (category field) for Application fact sheets in LeanIX. This field categorizes the type of application being created.

## Field Mapping

- **API Field Name**: `category`
- **User-Facing Name**: "Application Subtype"
- **Field Type**: Enum (predefined values)
- **Required**: Yes

## Core Principle

### **Always Use "businessApplication"**

For all Application fact sheets created through the Create Application skill, the Application Subtype must **always** be set to:

**Value**: `businessApplication`

This is the **default and only value** to use.

## Why This Value?

The `businessApplication` subtype indicates that the application is used for business operations, which covers the vast majority of applications in an enterprise architecture catalog, including:

- SaaS applications (Salesforce, Slack, Adobe products)
- Web applications (internal portals, custom apps)
- Desktop applications (Microsoft Office, design tools)
- Mobile applications (business apps)
- Enterprise software (ERP, CRM, HR systems)

## No Decision Logic Required

Unlike other fields (Description, Alias, etc.) that require research and decision-making, the Application Subtype field has **no conditional logic**.

**Rule**: Always set to `businessApplication` regardless of:
- Application name
- Provider
- Hosting type
- Pricing type
- Product category
- Any other field values

## Implementation

### In Code

When creating or updating an Application fact sheet:

```python
fact_sheet_data = {
    "name": application_name,
    "description": description,
    "alias": aliases,
    "category": "businessApplication",  # Always this value
    # ... other fields
}
```

### In JSON Payload

```json
{
  "name": "Salesforce",
  "description": "Salesforce is a cloud-based CRM platform...",
  "category": "businessApplication",
  "siId": "Salesforce"
}
```

## Quality Checklist

Before finalizing Application creation, verify:

- [ ] **category field is set** - Field must not be empty
- [ ] **Value is "businessApplication"** - Exact string match
- [ ] **No other value used** - Do not use any other enum value

## Common Mistakes to Avoid

❌ **Leaving field empty** - Field is required
❌ **Using a different value** - Only `businessApplication` is valid for this skill
❌ **Conditional logic** - Do not try to determine subtype based on other fields
❌ **Case sensitivity errors** - Must be exactly `businessApplication` (camelCase)

## Examples

All these applications use the same subtype:

| Application Name | Provider | Category |
|------------------|----------|----------|
| Salesforce | Salesforce | `businessApplication` |
| Slack | Slack Technologies | `businessApplication` |
| Microsoft Teams | Microsoft | `businessApplication` |
| Adobe Photoshop | Adobe Inc. | `businessApplication` |
| SAP ERP | SAP | `businessApplication` |
| Custom Internal Portal | Internal | `businessApplication` |

**Pattern**: Every Application = `businessApplication`

## Edge Cases

### Case 1: Infrastructure Software
**Question**: What about infrastructure applications like Docker, Kubernetes?

**Answer**: Still use `businessApplication`. These are business tools used by the organization.

### Case 2: Developer Tools
**Question**: What about IDEs, compilers, development tools?

**Answer**: Still use `businessApplication`. If it's being cataloged as an Application fact sheet, use `businessApplication`.

### Case 3: Mobile Apps
**Question**: Different subtype for mobile applications?

**Answer**: No. Mobile applications are `businessApplication`.

### Case 4: Custom Internal Applications
**Question**: Internal vs. external applications?

**Answer**: Both use `businessApplication`.

## Future Considerations

If additional enum values are introduced in the future (e.g., `infrastructureApplication`, `utilityApplication`), this guideline will be updated with:
- Complete list of enum values
- Decision logic for when to use each value
- Examples per category

**Until then**: Always use `businessApplication`.

## Summary

**DO**:
- Always set `category` to `businessApplication`
- Include this field in every Application creation
- Use exact string: `businessApplication` (camelCase)

**DON'T**:
- Leave the field empty
- Use any other value
- Create conditional logic for this field
- Overthink it

**Remember**: This is the simplest field in Application creation. Always `businessApplication`. No exceptions. No decision tree. Fixed value.

---

*Document created: 2026-02-22*
*Version: 1.0*
