# Application Description Guidelines

## Purpose

This guideline helps AI agents create functional, concise descriptions for Application fact sheets in LeanIX. The description should clearly explain what the application does or enables users to do, based on information from the provider's official website.

## Core Principles

### 1. **Functional Focus**
Describe what the application **does** and what users can **accomplish** with it, not marketing claims about how good it is.

**Good**: "Smartsheet provides an online application for collaboration and work management. It is used to assign tasks, track project progress, manage calendars, share documents, and manage other work, using a tabular user interface."

**Bad**: "Smartsheet is the leading collaboration platform that revolutionizes the way teams work together with cutting-edge technology."

### 2. **Remove Marketing Language**
Strip out superlatives, marketing buzzwords, and promotional language.

**Remove**:
- Superlatives: "leading", "best", "premier", "top", "world-class", "revolutionary"
- Marketing buzzwords: "innovative", "cutting-edge", "next-generation", "game-changing", "transformative"
- Vague claims: "comprehensive", "robust", "powerful", "seamless", "intuitive"
- Emotional language: "empower", "delight", "revolutionize"

**Accept** functional descriptors:
- "secure", "scalable", "cloud-based", "web-based", "integrated"
- When these describe actual architectural characteristics, not marketing

### 3. **Source from Official Website**
Use the provider's official website as the primary source, specifically:
- Homepage
- About page
- Product page
- Official product documentation

**Never hallucinate** features or capabilities not found on the official website.

### 4. **Describe the Specific Application**
Focus on the specific application/product, not the entire product suite or company.

**Example**: "Resource Management by Smartsheet" ≠ "Smartsheet"
- Describe Resource Management features specifically
- Don't describe the broader Smartsheet platform

## Description Structure

### Format
1. **Opening statement**: What the application is (1 sentence)
2. **Core capabilities**: What it enables users to do (1-3 sentences)
3. **Ownership note** (optional): Historical acquisitions or rebranding (1 sentence)

### Word Count
- **Target**: 30-90 words
- **Acceptable range**: Can extend to ~150 words for complex applications
- **Minimum**: 30 words - describe the core capabilities even if the application is simple

## Analysis of Examples

### Excellent Descriptions (30-75 words)

**Smartsheet** (41 words):
> "Smartsheet provides an online application for collaboration and work management. It is used to assign tasks, track project progress, manage calendars, share documents, and manage other work, using a tabular user interface."

✅ Clear functional description
✅ Lists specific capabilities
✅ Concise and direct

**absence.io** (28 words):
> "absence.io is an online solution to keep track of teams absences. It helps to monitor employee absence, work hours, and overtime."

✅ Simple, direct
✅ Focused on core function
✅ No marketing fluff

**Acronis Cloud Manager** (37 words):
> "Acronis Cloud Manager provides monitoring, management, migration, and recovery for Microsoft Cloud environments of all shapes and sizes, including single and multitenant public, private, and hybrid cloud configurations."

✅ Technical and specific
✅ Clear scope (Microsoft Cloud)
✅ Lists key functions

### Good Descriptions with Ownership Context

**Resource Management by Smartsheet** (44 words):
> "Resource Management by Smartsheet helps organizations to plan and manage resources across a portfolio of projects, track time by initiative, and build forecasts using real-time insights. 10000ft was acquired by Smartsheet Inc. in 2019."

✅ Functional description first
✅ Ownership history at the end
✅ Separates function from history

**Paycor Talent Development** (38 words):
> "Paycor Talent Development (formerly 7Geese) is a goal setting and performance management software that helps organizations improve goal visibility, engage talent, focus on career growth, and enhance their company culture."

✅ Former name noted in parentheses
✅ Clear capabilities listed
✅ Functional focus maintained

### Descriptions to Avoid

**Too Marketing-Focused**:
> "Ten Thousand Coffees is a diversity-founded talent experience platform for connectivity, mentoring, DEI, onboarding, early talent, leadership development, and more."

❌ "diversity-founded" is marketing positioning
❌ "talent experience platform" is buzzword-heavy
❌ "and more" is vague

**Better version**:
> "Ten Thousand Coffees is a platform that connects employees for mentoring, onboarding, DEI initiatives, leadership development, and professional networking within organizations."

**Too Vague**:
> "3Dplans provides innovative 3D floor plan rendering solutions, enabling users to visualize and create detailed architectural layouts. This application enhances design communication, supports real estate presentations, and facilitates better decision-making through interactive and visually appealing floor plan representations."

❌ "innovative" is marketing language
❌ "enhances", "facilitates better decision-making" are vague benefits
❌ "visually appealing" is subjective

**Better version**:
> "3Dplans is a 3D floor plan rendering application that allows users to create and visualize architectural layouts. It is used for design presentations and real estate marketing."

**Too Short / Missing Functionality**:
> "Actifio enables businesses to manage, access, and protect their data."

❌ Too generic - what kind of data?
❌ "manage, access, protect" could apply to many tools
❌ No specific capabilities mentioned

**Better version** (would need to research):
> "Actifio is a data management platform that provides backup, disaster recovery, and data protection for enterprise applications. It creates virtual copies of data for testing, development, and analytics without consuming additional storage."

## Special Cases

### 1. Applications with Long Names
If the application name is very long, use abbreviations in parentheses:

> "SAP Integration Suite, managed gateway for spend management and SAP Business Network is a no-code solution that enables businesses to connect multiple SAP procurement solutions, SAP Business Network, and other back-end systems with trading partners without using multiple adapters."

✅ Full name included
✅ Clear functional description despite long name

### 2. Technical/Enterprise Applications
Maintain technical accuracy without oversimplifying:

> "7SIGNAL's Endpoint Agent (formerly known as Mobile Eye) is a patented, AI-powered SaaS application designed to optimize the performance of IoT devices and other endpoints across wireless and wired networks. Installed onto Windows, macOS, Linux, or Android devices, the agent runs passive and active performance tests around the clock."

✅ Technical details preserved
✅ Supported platforms listed
✅ Specific functionality described

### 3. Simple Applications
For simple applications, still aim for 30+ words by explaining the use case:

> "AddEvent is a calendar management service with Add to Calendar service for websites and newsletters."

❌ Only 15 words, too brief

**Better**:
> "AddEvent is a calendar management service that provides Add to Calendar buttons and widgets for websites, emails, and newsletters. It allows event organizers to help attendees add events directly to their preferred calendar applications (Google Calendar, Outlook, Apple Calendar, etc.)."

## Quality Checklist

Before finalizing a description, verify:

- [ ] **30-150 words** (target: 30-90)
- [ ] **Functional focus** - describes what it does, not how great it is
- [ ] **No marketing language** - removed superlatives and buzzwords
- [ ] **Sourced from official website** - all information is verifiable
- [ ] **Specific to this application** - not describing a product suite or company
- [ ] **Clear capabilities** - user understands what they can do with it
- [ ] **Technical accuracy** - correct terminology and scope
- [ ] **Complete sentences** - proper grammar and structure
- [ ] **Ownership history** (if applicable) - acquisitions/rebranding noted
- [ ] **No hallucinated features** - only documented capabilities

## Anti-Patterns to Avoid

❌ **Marketing speak**: "leading solution", "innovative platform", "cutting-edge technology"
❌ **Vague benefits**: "improves productivity", "enhances collaboration", "drives growth"
❌ **Company descriptions**: Describing the provider instead of the application
❌ **Suite descriptions**: Describing multiple products when only one is relevant
❌ **Incomplete functionality**: "manages data" without specifics
❌ **Redundant phrases**: "X is a Y that does Y" (e.g., "Calendar tool that manages calendars")
❌ **Unsupported claims**: Features not found on official website
❌ **Inconsistent information**: Different facts from different pages (verify source)

## Decision Tree

```
1. Find official website → Homepage, About, Product pages
   ↓
2. Identify core functionality → What does it DO?
   ↓
3. List specific capabilities → What can users ACCOMPLISH?
   ↓
4. Remove marketing language → Delete superlatives, buzzwords
   ↓
5. Note ownership history → Any acquisitions or rebranding?
   ↓
6. Structure description:
   - Opening: What it is (1 sentence)
   - Capabilities: What users can do (1-3 sentences)
   - History: Acquisition/rebranding (1 sentence, if applicable)
   ↓
7. Quality check → Verify checklist above
```

## Common Patterns by Application Type

### **Project Management Tools**
Focus on: Task management, collaboration, resource allocation, tracking, reporting

Example: "X is a project management application that allows teams to create tasks, track project progress, manage resources, and generate status reports. It includes features for time tracking, budget management, and team collaboration."

### **Security/Monitoring Tools**
Focus on: What it monitors, what threats it detects, what it protects

Example: "X is a network security tool that monitors network traffic, detects intrusions, and blocks malicious activity. It provides real-time alerts, threat intelligence, and automated response capabilities."

### **Data/Analytics Tools**
Focus on: Data sources, analysis capabilities, outputs/visualizations

Example: "X is a business intelligence platform that connects to multiple data sources, performs data analysis, and generates interactive dashboards and reports for decision-making."

### **Communication Tools**
Focus on: Communication channels, collaboration features, integration capabilities

Example: "X is a team communication platform that provides instant messaging, video conferencing, file sharing, and project channels. It integrates with productivity tools and supports both desktop and mobile devices."

### **Document/Content Management**
Focus on: Document types, storage, collaboration, version control

Example: "X is a document management system that stores, organizes, and tracks documents throughout their lifecycle. It provides version control, access permissions, search capabilities, and workflow automation."

---

## Summary

**DO**:
- Describe functional capabilities
- Source from official website
- Be specific and technical
- Include ownership history when relevant
- Maintain 30-150 word range

**DON'T**:
- Use marketing language
- Describe the company or product suite
- Hallucinate features
- Be vague or generic
- Use superlatives or buzzwords
