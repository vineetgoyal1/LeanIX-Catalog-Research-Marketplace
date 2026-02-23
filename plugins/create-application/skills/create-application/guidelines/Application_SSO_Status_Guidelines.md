# Application SSO Status Guidelines

## Purpose

This guideline helps AI agents determine the `ssoStatus` field for Application fact sheets in LeanIX. This field indicates whether an application supports Single Sign-On (SSO) authentication, enabling users to access the application using enterprise identity credentials.

**Critical:** Only set this field when you have explicit evidence from official sources. Do not guess or assume SSO support.

## Field Information

**LeanIX field name:** `ssoStatus`
**Type:** Enumerated value
**Required:** Optional (currently set for ~41% of applications)
**Allowed values:**
- `supported` - Application supports SSO authentication
- `notSupported` - Application does NOT support SSO authentication
- `null` (blank) - SSO support status is unknown or not applicable

## Quick Reference

### When to Set SSO Status

| Application Type | Guidance |
|------------------|----------|
| Enterprise SaaS (B2B) | High priority - check for SSO support |
| Consumer SaaS (B2C) | Low priority - typically doesn't support enterprise SSO |
| PaaS/IaaS | May support SSO for console access - check documentation |
| On-Premise | May support SSO - check enterprise features |
| Mobile Apps | Check if supports enterprise authentication |
| Desktop Apps | Usually not applicable (leave blank) |

### Research Priority

**High Priority (check SSO):**
- Enterprise collaboration tools (Teams, Slack, Zoom)
- Business applications (CRM, ERP, HR systems)
- Cloud services with admin consoles (AWS, Azure, GCP)
- Security/compliance-critical applications

**Low Priority (can skip):**
- Consumer-focused applications
- Development tools (IDEs running locally)
- Simple utilities or single-purpose tools
- Applications with no user authentication

---

## Understanding SSO

### What is Single Sign-On (SSO)?

Single Sign-On enables users to authenticate once with their organization's identity provider (e.g., Azure AD, Okta, Google Workspace) and gain access to multiple applications without re-entering credentials.

**Common SSO Protocols:**
- SAML 2.0 (Security Assertion Markup Language)
- OAuth 2.0 / OpenID Connect
- WS-Federation
- LDAP / Active Directory integration

### Why SSO Matters for Enterprise Applications

**Benefits:**
- Centralized user management
- Enhanced security (MFA, conditional access policies)
- Compliance requirements (audit trails, access control)
- Improved user experience (one set of credentials)

**Enterprise requirement:** Many large organizations require SSO support for security and compliance reasons.

---

## Decision Process

### Step 1: Determine if SSO is Applicable

**SSO is typically NOT applicable for:**
- Standalone desktop applications (e.g., Adobe Photoshop, JetBrains IDEs)
- Mobile games and consumer apps
- Local development tools with no cloud component
- Simple utilities without user authentication

**If not applicable → Leave blank (do not set to `notSupported`)**

**SSO is typically applicable for:**
- Enterprise SaaS applications
- Cloud platforms with multi-user access
- Business applications requiring authentication
- Applications marketed to enterprises

**If applicable → Proceed to Step 2**

---

### Step 2: Search for SSO Evidence

**Research priority order:**

#### 1. Official Security/Features Pages (Highest Priority)

Search for these pages on the official website:
- `/security`
- `/features`
- `/enterprise`
- `/integrations`
- `/authentication`
- `/trust` or `/trust-center`

**Look for explicit statements:**
- ✅ "Supports Single Sign-On (SSO)"
- ✅ "SAML 2.0 authentication"
- ✅ "OAuth / OpenID Connect"
- ✅ "Integrate with Azure AD, Okta, Google Workspace"
- ✅ "Enterprise SSO available"

#### 2. Product Updates / Changelog (High Priority) ⭐ NEW

Search for these pages:
- `/changelog`
- `/updates`
- `/release-notes`
- `/whats-new`
- `/blog` (product announcements)

**Why this matters:**
- SSO is often announced as a major feature release
- "We're excited to announce SSO support!"
- Especially useful for newer/growing SaaS products

**Look for:**
- ✅ "SSO now available"
- ✅ "Announcing SAML support"
- ✅ "New: Single Sign-On integration"
- ✅ "Enterprise authentication released"

**Search within changelog:**
- Search for "SSO", "SAML", "OAuth", "authentication", "enterprise"
- Check last 1-2 years of updates

#### 3. Product Documentation (High Priority)

Search documentation for:
- Authentication setup guides
- Admin console documentation
- Enterprise deployment guides

**Look for:**
- SSO configuration instructions
- Identity provider integration guides
- SAML/OAuth setup documentation

#### 4. Pricing Pages (Medium Priority)

Check if SSO is mentioned as:
- Enterprise plan feature
- Premium add-on
- Business tier feature

**Pattern:**
- If SSO listed as paid feature → `supported`
- Even if gated behind pricing, it's still supported

#### 5. Integration Directories (Medium Priority)

Check if application appears in:
- Okta Integration Network
- Azure AD App Gallery
- Google Workspace Marketplace (with SSO tag)

**If listed → Likely `supported`**

---

### Step 3: Evaluate Evidence

Based on research, determine status:

**Set to `supported` if ANY of these are true:**
- Website explicitly states "SSO support" or "Single Sign-On"
- Changelog/updates announce SSO feature release
- Documentation includes SSO/SAML/OAuth setup instructions
- Listed in identity provider directories (Okta, Azure AD)
- Pricing page lists SSO as a feature (even premium-only)
- Security page mentions SAML, OAuth, OpenID Connect
- Integration page mentions "connect with Azure AD/Okta"

**Set to `notSupported` if:**
- Website explicitly states "SSO not supported" or "Coming soon"
- Documentation clearly lacks SSO options
- Product is consumer-focused with only social logins (Google, Facebook)
- Enterprise features listed explicitly exclude SSO

**Leave blank if:**
- No clear evidence found after reasonable research
- Application type makes SSO not applicable (desktop apps, utilities)
- Insufficient information available
- **Do not guess based on application size or type**

---

### Step 4: Document Confidence

Track your confidence level:

- **High (90-100%):** Explicit statement on official website or changelog
- **Medium (70-89%):** Found in documentation or integration directory
- **Low (< 70%):** Indirect evidence or unclear

**Only set ssoStatus if confidence ≥ 70%**

---

## Common Patterns

### Pattern 1: Enterprise SaaS (Usually Supported)

**Applications like:** Salesforce, Workday, ServiceNow, Slack, Microsoft Teams

**Typical evidence locations:**
- Security page explicitly lists SSO
- Enterprise plan includes SSO
- Admin documentation has SSO setup
- **Changelog announces SSO launch** (for newer products)

**Default assumption:** Check first, but expect `supported`

**Example search strategy:**
1. Visit smartsheet.com/security or smartsheet.com/enterprise
2. Check smartsheet.com/changelog or smartsheet.com/updates
3. Search pages for "SSO", "SAML", "single sign-on"
4. If found → `supported`

---

### Pattern 2: Cloud Infrastructure (Console SSO)

**Applications like:** AWS, Azure, GCP, Oracle Cloud

**SSO applies to:** Admin console access, not end-user applications

**Typical evidence:**
- Identity federation documentation
- SAML/OAuth integration for console access
- Enterprise identity management features

**Usually:** `supported`

---

### Pattern 3: Consumer Applications (Usually Not Supported)

**Applications like:** Instagram, TikTok, consumer games, personal productivity apps

**Characteristics:**
- Social logins only (Google, Facebook, Apple)
- No enterprise plans
- Consumer-focused marketing

**If only social logins (no SAML/enterprise SSO):**
- Set to `notSupported` OR leave blank
- Social login ≠ enterprise SSO

---

### Pattern 4: Small Business / Startup SaaS (Mixed)

**Applications like:** Newer SaaS tools, niche solutions

**Challenge:** May not have SSO yet

**Research strategy:**
- **Check changelog/updates first** (SSO often announced as milestone)
- Verify enterprise plan existence
- Check integration directories
- Look for "Enterprise features coming soon"

**If SSO not found:**
- DO NOT assume `notSupported`
- Leave blank (may add later)

**Tip:** Changelog is especially valuable for startups that recently added SSO

---

### Pattern 5: Open Source / Self-Hosted (Varies)

**Applications like:** GitLab, Confluence, Jira (on-premise)

**Depends on:**
- Enterprise edition vs community edition
- Self-hosted typically supports SSO (LDAP, SAML)
- Cloud versions definitely support SSO

**Research carefully** - check edition-specific features

---

## Special Cases

### Case 1: SSO Available Only in Enterprise Plan

**Question:** If SSO requires paid/enterprise plan, is it "supported"?

**Answer:** YES - set to `supported`
- SSO existence is what matters, not pricing tier
- Many enterprises use paid plans with SSO

**Example:**
- Slack offers SSO in Enterprise Grid plan only
- Still set to `supported` (SSO exists)

---

### Case 2: Multiple Applications from Same Vendor

**Question:** If Vendor X supports SSO in App A, does App B also support it?

**Answer:** NO - do not assume
- Each application must be verified independently
- Vendors may have different features across products

**Example:**
- Google Workspace (supports SSO)
- Google Photos (consumer app, no enterprise SSO)
- Verify each separately

---

### Case 3: SSO "Coming Soon" or "Roadmap"

**Question:** If vendor says "SSO coming in Q3" or changelog shows it's planned, what should I set?

**Answer:** Leave blank OR set to `notSupported` with caution
- "Coming soon" = not currently available
- "Planned" ≠ "Available"
- Re-check after announced release date
- **Check recent changelog** - may have been released

**Better:** Leave blank until actually available

---

### Case 4: LDAP but Not SAML

**Question:** Application supports LDAP/Active Directory but not SAML. Is this SSO?

**Answer:** YES - set to `supported`
- LDAP integration counts as SSO capability
- Enterprise authentication via directory services = SSO

**LDAP/AD integration = SSO support**

---

### Case 5: API Authentication Only

**Question:** Application has OAuth for API access but no user SSO. Supported?

**Answer:** Depends on context
- OAuth for API authentication only ≠ user SSO
- If no user-facing SSO login → typically NOT supported
- Check if OAuth enables user authentication (not just API)

**If only API OAuth (no user SSO) → `notSupported` or leave blank**

---

### Case 6: Mobile Apps

**Question:** How to determine SSO for mobile applications?

**Answer:** Check enterprise features
- Enterprise mobile apps often support SSO (Outlook, Teams, Salesforce)
- Consumer apps typically don't
- Look for "enterprise authentication" or "MDM integration"

**If mobile app connects to enterprise backend with SSO → `supported`**

---

### Case 7: SSO Announced in Changelog but Not on Features Page

**Question:** Changelog announces SSO launch, but it's not mentioned on features/security pages. Is it supported?

**Answer:** YES - set to `supported`
- Changelog is authoritative source for features
- Features pages may not be updated yet
- Product updates are official announcements

**Changelog announcement = valid evidence**

---

## Research Examples

### Example 1: Slack

**Research process:**

1. **Visit slack.com/security**
   - Found: "Single sign-on" mentioned under Identity Management

2. **Check slack.com/enterprise**
   - Found: "SAML-based SSO" listed as enterprise feature

3. **Verify in documentation**
   - Found: SSO setup guide in admin documentation

**Decision:** `supported`
**Confidence:** 100% (explicit mentions across multiple pages)

---

### Example 2: Newer SaaS Startup Tool

**Research process:**

1. **Visit website security page**
   - Security page exists but no SSO mention

2. **Check changelog (example.com/changelog)** ⭐
   - Found in October 2025 update: "🎉 We're excited to announce SAML SSO support!"

3. **Verify in pricing**
   - SSO listed under "Enterprise" plan

**Decision:** `supported`
**Confidence:** 95% (changelog announcement + pricing confirmation)
**Key insight:** Changelog revealed SSO that wasn't prominent on main pages

---

### Example 3: AWS (Amazon Web Services)

**Research process:**

1. **Visit aws.amazon.com/iam**
   - Found: "Identity federation" documentation

2. **Check AWS documentation**
   - Found: SAML 2.0, OAuth integration for console access

3. **Verify AWS SSO service exists**
   - AWS offers both incoming SSO (console access) and AWS SSO service

**Decision:** `supported`
**Confidence:** 100% (well-documented feature)

---

### Example 4: Small SaaS Tool (No SSO Evidence)

**Research process:**

1. **Visit website security page**
   - Security page exists but no SSO mention

2. **Check pricing**
   - Only one plan, no enterprise tier

3. **Check changelog/updates** ⭐
   - No mention of SSO in past updates

4. **Search documentation**
   - Authentication page shows only email/password

5. **Check integration directories**
   - Not found in Okta or Azure AD galleries

**Decision:** Leave blank
**Confidence:** Low (no evidence, but don't assume it's not supported)
**Rationale:** May add SSO in future, insufficient evidence to mark `notSupported`

---

### Example 5: Consumer Mobile Game

**Research process:**

1. **Check application type**
   - Consumer mobile game, not enterprise tool

2. **SSO applicability**
   - No enterprise use case, consumer-only

**Decision:** Leave blank (not applicable)
**Confidence:** N/A
**Rationale:** SSO not relevant for consumer games

---

## Where to Find SSO Information

### Official Website Pages

**High-value pages (check in order):**

1. `/security` - Security overview often lists SSO
2. `/enterprise` - Enterprise features highlight SSO
3. **`/changelog` or `/updates`** - Product announcements ⭐ NEW
4. **`/whats-new` or `/release-notes`** - Feature releases ⭐ NEW
5. `/features` - Feature comparison may include SSO
6. `/pricing` - Plan comparison shows SSO availability
7. `/integrations` - Identity provider integrations
8. `/trust` or `/compliance` - Trust center documentation
9. `/blog` - Look for "Announcing SSO" posts

**Search within pages for:**
- "SSO"
- "Single Sign-On"
- "SAML"
- "OAuth"
- "OpenID"
- "Azure AD"
- "Okta"
- "Identity Provider"
- "Enterprise authentication"

---

### Changelog / Product Updates (HIGH VALUE) ⭐

**Why check changelog:**
- SSO is a major feature, usually announced
- Provides proof of when SSO was added
- Shows feature is available (not just planned)
- Often more up-to-date than static pages

**Common URL patterns:**
- `[domain]/changelog`
- `[domain]/updates`
- `[domain]/release-notes`
- `[domain]/whats-new`
- `[domain]/blog` (filter for product updates)

**What to look for:**
```
Example changelog entries:

✅ "October 2025 - Enterprise SSO: We now support SAML 2.0 authentication"
✅ "Q2 2025 Update - Single Sign-On is now available for all Business plans"
✅ "Version 2.5 - Added: Azure AD and Okta integration"
✅ "New Feature: Enterprise Authentication"
```

**Search changelog for:**
- "SSO"
- "SAML"
- "authentication"
- "Okta"
- "Azure AD"
- "single sign-on"

**Time range:** Check last 1-2 years (SSO may be recent addition)

---

### Documentation Sites

**Check these sections:**

1. **Admin Guides**
   - User management
   - Authentication setup
   - Enterprise configuration

2. **Integration Guides**
   - Identity provider setup
   - SAML configuration
   - OAuth/OpenID Connect setup

3. **Security Documentation**
   - Authentication methods
   - Access control

**Search documentation for:**
- "authentication"
- "SSO setup"
- "SAML configuration"
- "identity provider"

---

### Third-Party Directories

**Integration marketplaces that indicate SSO:**

1. **Okta Integration Network** (okta.com/integrations)
   - If application listed → likely SSO supported
   - Check integration type (SSO vs API only)

2. **Azure AD App Gallery** (azuremarketplace.microsoft.com)
   - Pre-integrated applications support SAML/OAuth
   - If listed → supported

3. **Google Workspace Marketplace**
   - Check if SSO integration available

**Note:** Absence from directories ≠ no SSO support (many apps support SSO but aren't listed)

---

## Anti-Patterns and Common Mistakes

### Mistake 1: Assuming Large Companies Support SSO

**Wrong reasoning:**
> "This is a major SaaS company, so they must support SSO."

**Why wrong:**
- Not all SaaS applications have enterprise features
- Consumer-focused products from large vendors may lack SSO

**Correct approach:**
- Verify with actual evidence
- Check changelog, security pages, documentation
- Don't assume based on company size

---

### Mistake 2: Social Login = SSO

**Wrong reasoning:**
> "Application supports Google login, so SSO is supported."

**Why wrong:**
- Social login (Google, Facebook, Apple) ≠ Enterprise SSO
- Consumer OAuth ≠ SAML/enterprise identity federation
- SSO means enterprise identity providers (Azure AD, Okta, etc.)

**Correct approach:**
- Check if SAML, enterprise OAuth, or LDAP is supported
- Social login only → NOT enterprise SSO

---

### Mistake 3: Marking "notSupported" Without Evidence

**Wrong reasoning:**
> "I didn't find SSO mentioned, so I'll mark it as notSupported."

**Why wrong:**
- Absence of evidence ≠ evidence of absence
- May support SSO but not prominently advertised
- Small/new companies may add SSO later

**Correct approach:**
- Only mark `notSupported` if explicitly stated OR
- Clear evidence it's a consumer-only app with only social logins
- When uncertain → leave blank

---

### Mistake 4: Checking Only the Homepage

**Wrong reasoning:**
> "Homepage doesn't mention SSO, so it's not supported."

**Why wrong:**
- SSO is an enterprise feature, not homepage marketing
- Typically found on /security, /enterprise, /pricing, or **changelog** pages

**Correct approach:**
- Check security, enterprise, pricing, **changelog**, documentation pages
- SSO is often buried in features list or announced in updates

---

### Mistake 5: Ignoring Changelog

**Wrong reasoning:**
> "I checked the features page, no SSO, so it's not supported."

**Why wrong:**
- Changelog may announce SSO that's not yet on features page
- Product updates are more current than static pages
- Missing valuable source of evidence

**Correct approach:**
- **Always check changelog/updates** before concluding
- Especially for newer/growing SaaS products
- Changelog = authoritative source for feature releases

---

### Mistake 6: Assuming Desktop Apps Don't Support SSO

**Wrong reasoning:**
> "It's a desktop application, so no SSO."

**Why wrong:**
- Many enterprise desktop apps support SSO (Microsoft Office, Adobe Creative Cloud)
- Desktop clients for cloud services often use SSO

**Correct approach:**
- Check if desktop app connects to cloud service
- Enterprise desktop tools may support SSO

---

### Mistake 7: API OAuth = User SSO

**Wrong reasoning:**
> "Application has OAuth for API access, so it supports SSO."

**Why wrong:**
- OAuth for API authentication ≠ user SSO
- May have API keys but no user-facing SSO

**Correct approach:**
- Verify OAuth is for user authentication, not just API access
- Check if users can log in via enterprise identity provider

---

## Quality Checklist

Before setting ssoStatus, verify:

- [ ] I checked official website (security, enterprise, features pages)
- [ ] **I checked changelog/updates/release notes** ⭐ NEW
- [ ] I searched for explicit SSO/SAML/OAuth mentions
- [ ] If `supported`, I found clear evidence (not assumption)
- [ ] If `notSupported`, I have explicit evidence (not lack of evidence)
- [ ] I did NOT confuse social login with enterprise SSO
- [ ] I did NOT assume based on company size or application type
- [ ] My confidence level is ≥ 70%
- [ ] If confidence < 70%, I left the field blank
- [ ] I checked if SSO is even applicable (not a consumer-only app)

---

## Data Quality Notes

**Current state of data:**
- Only 40.8% of applications have ssoStatus set
- Of those set: 98% are `supported`, 2% are `notSupported`
- This suggests: Setting blank when uncertain is common and acceptable

**Your task:**
- Set ssoStatus when you have clear evidence
- DO NOT feel pressure to always set a value
- Blank is better than incorrect

**Goal:**
- Increase completion rate by setting when evidence exists
- Maintain data quality by not guessing
- Focus on enterprise/business applications (high priority)

---

## Summary Decision Tree

```
START
  ↓
Is application enterprise/business-focused?
  ├─ NO (consumer app, game, utility) → Leave blank (not applicable)
  │
  └─ YES → Continue
      ↓
Check official website (security, enterprise, pricing pages)
  ↓
Found explicit SSO/SAML/OAuth mention?
  ├─ YES → supported (confidence ≥ 70%)
  │
  └─ NO → Check changelog/updates ⭐ NEW
      ↓
Found SSO announcement in changelog?
  ├─ YES → supported (confidence ≥ 70%)
  │
  └─ NO → Check documentation
      ↓
Found SSO setup in documentation?
  ├─ YES → supported (confidence ≥ 70%)
  │
  └─ NO → Check integration directories (Okta, Azure AD)
      ↓
Found in integration directory?
  ├─ YES → supported (confidence ≥ 70%)
  │
  └─ NO → Is it consumer-only with only social logins?
      ├─ YES → notSupported (explicit evidence)
      │
      └─ NO → Leave blank (insufficient evidence)
```

---

## Priority Guidelines for Research Effort

**High Priority - Invest time researching:**
- Enterprise collaboration (Slack, Teams, Zoom)
- Business applications (CRM, ERP, HR)
- Cloud platforms (AWS, Azure, GCP)
- Security/compliance tools
- Applications with >1000 users in organization
- **Growing SaaS startups (check changelog for recent SSO additions)** ⭐

**Low Priority - Quick check only:**
- Consumer apps
- Games
- Small utilities
- Personal productivity tools
- Applications with <100 users

**Not Applicable - Skip:**
- Standalone desktop apps (Photoshop, IDEs)
- Developer tools (local CLI tools)
- Mobile games
- Simple calculators/converters

---

## Examples Summary

| Application | Type | SSO Status | Key Evidence Source |
|-------------|------|------------|---------------------|
| Slack | Enterprise SaaS | `supported` | Security page + SAML docs |
| AWS | Cloud Platform | `supported` | Identity federation docs |
| Salesforce | Enterprise SaaS | `supported` | Enterprise standard feature |
| Newer SaaS Startup | Small SaaS | `supported` | **Changelog announcement** ⭐ |
| Instagram | Consumer Social | Leave blank | Consumer app, not applicable |
| Smartsheet | Business SaaS | `supported` | Enterprise plan + security page |
| Adobe Photoshop (desktop) | Desktop App | Leave blank | Standalone app, not applicable |
| Small Tool (no evidence) | Small SaaS | Leave blank | No evidence found after search |
| Zoom | Video Conferencing | `supported` | Enterprise features + SAML |

---

## Key Takeaways

1. **Check changelog/updates** - Often announces SSO as major milestone ⭐
2. **Evidence required** - Don't guess, find explicit proof
3. **Social login ≠ SSO** - Consumer OAuth is not enterprise SSO
4. **Blank is acceptable** - Better than incorrect
5. **Focus on enterprise apps** - Higher priority, more likely to have SSO
6. **Changelog especially useful for startups** - Recent SSO additions announced there

---

## Revision History

- **Version 1.0** (2026-02-22): Initial creation with evidence-based approach, added changelog/product updates as key research source

