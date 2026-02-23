# Provider Category Classification Definitions

## Overview
This document provides definitions and rules for classifying software/technology providers into three categories: Enterprise, Community Based, and Individual. These definitions are derived from analysis of the "Provider Category.xlsx" dataset and are intended for use by AI agents performing automated classification.

---

## Category Definitions

### **Enterprise**
A provider is classified as **Enterprise** if it exhibits the following characteristics:
- **Registered commercial entity**: The provider is a formally established company, corporation, or business organization (Ltd, Inc, GmbH, etc.)
- **Commercial products/services**: Develops and sells proprietary software, products, or professional services with clear revenue/business models
- **Professional operations**: Has structured business operations including customer support, sales, marketing, and professional service delivery
- **Examples**: Technology companies, SaaS providers, software vendors, consulting firms, product manufacturers

**Key indicators**: Company website with professional branding, "About Us" pages mentioning employees/founders, commercial pricing/licensing, business registration, corporate structure, terms of service, customer support channels.

---

### **Community Based**
A provider is classified as **Community Based** if it exhibits the following characteristics:
- **Collaborative development**: Projects developed and maintained by a community, group of contributors, or foundation (not a single individual)
- **Open source/public goods**: Software, standards, or tools that are freely available, typically under open-source licenses
- **Non-profit or community governance**: May be backed by foundations, working groups, or volunteer-driven organizations
- **Collective contribution**: Multiple maintainers, contributors, or organizational sponsors working together

**Key indicators**: Open source licenses, GitHub organizations with multiple contributors, foundation backing (e.g., Apache, Linux Foundation), community forums/documentation, phrases like "open-source project," "community-driven," "collaborative initiative," "working group," or "foundation."

---

### **Individual**
A provider is classified as **Individual** if it exhibits the following characteristics:
- **Single person**: Software, tools, or services developed and maintained by one identifiable person
- **Personal attribution**: Uses personal names, personal websites/blogs, or individual GitHub accounts
- **Solo projects**: The work is attributed to an individual developer, not a company or collaborative group
- **Personal portfolio**: May include personal projects, side projects, or consulting work by that individual

**Key indicators**: Personal name in provider name, URLs to personal websites/blogs, GitHub profiles of individuals, descriptions mentioning "individual developer," single maintainer on projects, personal LinkedIn profiles, phrases like "developed by [Name]" or "[Name] is a developer who..."

---

## Classification Decision Tree

When classifying a new provider, ask these questions in order:

1. **Is this a single named person or personal portfolio?** → If YES → **Individual**
2. **Is this a commercial company with business operations?** → If YES → **Enterprise**
3. **Is this an open-source project, foundation, or community collaboration?** → If YES → **Community Based**
4. **Default when unclear**: If ambiguous, prefer **Community Based** for open-source projects, **Enterprise** for commercial entities, and only use **Individual** when clearly attributed to one person.

---

## Edge Cases

- **Small companies or startups run by 1-2 people**: Classify as **Enterprise** (if formally registered business)
- **Individual contributing to a larger open-source project**: Classify as **Community Based** (project level, not contributor level)
- **Acquired projects**: Use current organizational structure (e.g., originally individual, now maintained by a company → **Enterprise**)

---

## Dataset Statistics

Based on the "Provider Category.xlsx" dataset (269 providers):
- **Community Based**: 65 providers (Rows 2-66)
- **Enterprise**: 110 providers (Rows 67-176)
- **Individual**: 94 providers (Rows 177-270)

---

*Document generated: 2026-02-16*
