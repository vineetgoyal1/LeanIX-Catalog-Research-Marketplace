# Application Hosting Type & Hosting Description Guidelines

## Purpose

This guideline helps AI agents correctly classify the `hostingType` and write the `hostingDescription` for Application fact sheets in LeanIX. These two fields work together to document how and where an application is deployed.

**Critical:** This requires systematic evaluation of ALL options before making a decision. Do not select the first matching keyword. Follow the structured decision process exactly.

## Fields Covered

### 1. hostingType (Enum Field)
**LeanIX field name:** `hostingType`
**Type:** Enumerated value
**Required:** Yes (recommended to set for all applications)
**Allowed values:** `saas`, `paas`, `iaas`, `onPremise`, `hybrid`, `mobile`

### 2. hostingDescription (Text Field)
**LeanIX field name:** `hostingDescription`
**Type:** Free text
**Required:** Optional
**Purpose:** Document the reasoning for the hostingType classification, including infrastructure details that support the decision
**Typical length:** 50-150 characters

---

## Quick Reference Card (Start Here)

### Fast Triage: Check Name FIRST (Eliminates 70% of cases)

| If name contains... | Likely type | Confidence | Next step |
|---------------------|-------------|------------|-----------|
| "mobile app", "for iOS", "for Android" | `mobile` | 95% | Verify it's native (not web), write reasoning |
| "on-premise", "-on premise", "Desktop" | `onPremise` | 80% | **CAUTION**: Check if desktop CLIENT (→ saas) or standalone |
| "Private Edition", "Hybrid", "Cloud Private" | `hybrid` | 70% | Verify multiple deployment options |
| AWS/Azure/GCP + (EC2, S3, VPC, VM, Storage) | `iaas` | 90% | Verify it's infrastructure layer |
| AWS/Azure/GCP + (RDS, Lambda, Functions, BigQuery) | `paas` | 90% | Verify developers use it |
| None of above | ? | 0% | Proceed to full evaluation |

**If confidence > 85% after name check:**
- Proceed directly to write hostingDescription with reasoning
- Done

**If confidence ≤ 85%:**
- Go to Full Decision Process (below)

### Common Classification Patterns

1. **Business app for end users** → `saas`
   - CRM, collaboration, project management, analytics for business users

2. **Platform for developers** → `paas`
   - Managed databases, serverless compute, container platforms, data warehouses

3. **Infrastructure resources** → `iaas`
   - Virtual machines, object storage, block storage, virtual networks

4. **Desktop standalone app** → `onPremise`
   - IDEs, design tools that run entirely on local machine

5. **Desktop CLIENT for cloud service** → `saas` (NOT onPremise!)
   - Slack Desktop, Zoom Desktop, Teams Desktop → these are saas clients

6. **Native mobile app** → `mobile`
   - App Store/Play Store downloads, not mobile-responsive websites

7. **Cloud + on-premise options** → `hybrid`
   - Same product with flexible deployment

---

# Part 1: Determining Hosting Type

## Core Principles

### 1. **Systematic Evaluation Required**
You MUST evaluate evidence for ALL 6 hosting types before deciding. Completing the evaluation matrix is mandatory for ambiguous cases.

### 2. **The Golden Question: "Who is the primary user?"**
- **Business users** accomplishing tasks → likely `saas`
- **Developers/engineers** building/deploying → likely `paas`
- **IT/Infrastructure teams** managing resources → likely `iaas`
- **End users** on mobile devices only → likely `mobile`

### 3. **Name is the Strongest Signal**
Application names often explicitly indicate hosting type:
- Contains "mobile app", "for iOS", "for Android" → `mobile`
- Contains "on-premise", "on premise", "desktop" → `onPremise` (but verify not a client)
- Contains "Private Edition", "Cloud Private" → `hybrid`

### 4. **Web Search When Uncertain**
Mandatory web search for AWS/Azure/GCP services and when confidence < 85%.

### 5. **Common Keyword Traps**
- "Platform" does NOT automatically mean PaaS
  - "Collaboration platform" → `saas` (end user tool)
  - "Deployment platform" → `paas` (developer tool)
- "Cloud" does NOT distinguish between SaaS/PaaS/IaaS
- "Managed" usually indicates PaaS (managed infrastructure)

### 6. **Desktop Client vs Standalone App** (CRITICAL)
- **Desktop CLIENT** for cloud service (Slack Desktop, Zoom Desktop) → `saas`
- **Standalone desktop app** (Adobe Photoshop, JetBrains IDEs) → `onPremise`
- Ask: "Can this function without internet/cloud?" If NO → `saas` client

---

## Full Decision Process (Use When Uncertain)

### Step 1: Gather All Available Evidence

Complete this evidence checklist:

```
Application Name: [fill in]
Description: [fill in]
Subtype: [fill in if available]
Webpage URL: [fill in if available]

Keywords found in name: [list all relevant keywords]
Keywords found in description: [list all relevant keywords]
```

### Step 2: Complete the Evaluation Matrix

For EACH hosting type, list evidence FOR and AGAINST. **Quality gate: Minimum 2 specific evidence items for your top choice.**

| Hosting Type | Evidence FOR | Evidence AGAINST | Fit Score (0-10) |
|--------------|--------------|------------------|------------------|
| saas         |              |                  |                  |
| paas         |              |                  |                  |
| iaas         |              |                  |                  |
| onPremise    |              |                  |                  |
| hybrid       |              |                  |                  |
| mobile       |              |                  |                  |

**Example of GOOD evaluation:**

| Type | Evidence FOR | Evidence AGAINST | Score |
|------|--------------|------------------|-------|
| saas | 1. End users collaborate directly<br>2. Complete business application<br>3. No code deployment | 1. Description mentions "platform" (but for end users) | 9 |
| paas | 1. Description says "platform" | 1. No mention of developers<br>2. No code deployment<br>3. End users are primary audience | 2 |

### Step 3: Apply the Primary User Test

For your top 2-3 scoring options, answer these questions:

**If saas:**
- Who are the end users? (e.g., sales teams, marketers, employees)
- What business task do they accomplish? (e.g., manage customers, track projects)
- Does this match the description? YES/NO + why

**If paas:**
- Who are the developers/engineers?
- What do they build/deploy on it? (e.g., web apps, data pipelines, containers)
- Does the description mention code deployment or developers? YES/NO

**If iaas:**
- What infrastructure resource does it provide? (e.g., VMs, storage, networking)
- Do users manage operating systems or infrastructure? YES/NO

**If onPremise:**
- Is it a standalone desktop app OR a desktop client?
- **CRITICAL**: Desktop client for cloud service = `saas`, NOT `onPremise`

**If hybrid:**
- Does it support BOTH cloud AND on-premise deployment?
- Can customers choose deployment location?

**If mobile:**
- Is it a native mobile app (App Store/Play Store)?
- Or just mobile-responsive web app? (If web → `saas`)

### Step 4: Check Anti-Patterns (MANDATORY)

Review your reasoning against these common mistakes:

- [ ] **Did I choose paas just because the description says "platform"?**
  - ❌ WRONG: "Collaboration platform" → `paas`
  - ✅ RIGHT: Is it a platform FOR DEVELOPERS? If no → `saas`

- [ ] **Did I choose onPremise for a desktop CLIENT of a cloud service?**
  - ❌ WRONG: Slack Desktop → `onPremise`
  - ✅ RIGHT: Desktop client for cloud service → `saas`

- [ ] **Did I choose saas for AWS/Azure/GCP developer services?**
  - ❌ WRONG: AWS Lambda → `saas` (it's `paas`)
  - ✅ RIGHT: Services for developers = `paas`, for IT = `iaas`, for end users = `saas`

- [ ] **Did I ignore the name entirely?**
  - ❌ WRONG: "SAP X mobile app" → `saas` (ignored "mobile app")
  - ✅ RIGHT: Name is the strongest signal

- [ ] **Did I choose the first matching keyword without completing the matrix?**
  - ❌ WRONG: Saw "platform" → selected `paas` immediately
  - ✅ RIGHT: Complete evaluation for all 6 types

**If you checked ANY box above, RESTART your analysis from Step 1.**

### Step 5: Web Search Requirements

**MANDATORY web search for:**
1. ✅ ALL AWS/Azure/GCP/Oracle Cloud services (no exceptions)
2. ✅ Any application with "platform" in description but unclear target user
3. ✅ Top 2 candidates within 2 points
4. ✅ Applications where name and description conflict (e.g., "Desktop" but mentions cloud)
5. ✅ Confidence < 85%

**No web search needed:**
- Confidence > 90% after name check
- Clear indicators (e.g., "SAP Field Service mobile app" → obviously `mobile`)
- Self-evident cases (e.g., Adobe Photoshop → `onPremise` desktop)

**What to search for:**
- Official product homepage
- "What is [Product Name]?" page
- Look for: "IaaS", "PaaS", "SaaS", "on-premise", "mobile app"
- Target audience: developers vs business users vs IT teams

### Step 6: Final Decision

Only after completing Steps 1-5:

```
Selected hostingType: [choose one: saas, paas, iaas, onPremise, hybrid, mobile]
Confidence level: [0-100%]
Key deciding factors: [what made you choose this over others]
```

---

## Hosting Type Definitions

### 1. saas (Software as a Service)

**Definition:** Complete, ready-to-use application for end users. Users consume it as a service without managing infrastructure.

**Primary users:** Business users, employees, customers
**What they do:** Accomplish business tasks (collaborate, manage, track, analyze, communicate)
**Who manages infrastructure:** Provider handles everything

**Key indicators:**
- Complete business application
- End users consume directly
- No coding/development required
- Keywords: "collaboration", "CRM", "project management", "analytics", "communication"

**Examples:**
- ✅ **Smartsheet** - Project management (business users track projects)
- ✅ **Salesforce** - CRM (sales teams manage customers)
- ✅ **Microsoft Teams** - Collaboration (employees communicate)
- ✅ **Slack Desktop** - Desktop client for cloud messaging service (NOT onPremise!)

**Common traps:**
- ❌ "Collaboration platform" sounds like PaaS, but if END USERS collaborate → `saas`
- ❌ Desktop client (Zoom Desktop, Slack Desktop) → `saas`, NOT `onPremise`

---

### 2. paas (Platform as a Service)

**Definition:** Platform that enables developers to build, deploy, and run applications without managing underlying infrastructure.

**Primary users:** Software developers, data engineers, DevOps engineers
**What they do:** Build apps, deploy code, manage data pipelines, run containers
**Who manages infrastructure:** Provider manages servers, OS, runtime; users manage applications

**Key indicators:**
- Platform FOR DEVELOPERS
- Users write/deploy code
- Keywords: "deploy applications", "managed database", "serverless", "container platform", "data warehouse"

**Examples:**
- ✅ **Heroku** - Deploy applications
- ✅ **AWS RDS** - Managed database (developers use it, AWS manages infrastructure)
- ✅ **AWS Lambda** - Serverless compute (developers deploy functions)
- ✅ **Google Cloud BigQuery** - Data warehouse (data engineers query/analyze)
- ✅ **Red Hat OpenShift** - Container orchestration

**Decision framework:**
Ask: "Would a developer write code that runs on this?" If YES → likely `paas`

**Cloud provider services commonly PaaS:**
- Managed databases (RDS, Cloud SQL, Azure SQL Database)
- Serverless compute (Lambda, Cloud Functions, Azure Functions)
- Container platforms (ECS, EKS, AKS, GKE)
- Data warehouses (BigQuery, Redshift)
- Message queues (SQS, Cloud Pub/Sub)

---

### 3. iaas (Infrastructure as a Service)

**Definition:** Fundamental computing resources (compute, storage, networking) that users provision and manage.

**Primary users:** IT infrastructure teams, system administrators, DevOps engineers
**What they do:** Provision VMs, manage storage, configure networks
**Who manages infrastructure:** Provider manages hardware; users manage VMs, OS, applications, data

**Key indicators:**
- Raw building blocks (compute, storage, network)
- Users manage operating systems
- Keywords: "virtual machine", "compute instance", "object storage", "block storage"

**Examples:**
- ✅ **Amazon EC2** - Virtual machines
- ✅ **Amazon S3** - Object storage
- ✅ **AWS Elastic Block Store** - Block storage
- ✅ **Azure Virtual Machines** - Compute infrastructure

**Decision framework:**
Ask: "Does it provide raw compute/storage/network that users build on?" If YES → likely `iaas`

**Key distinction: IaaS vs PaaS**
- IaaS = "Here's a VM, you install everything"
- PaaS = "Here's a managed database, you use it"

---

### 4. onPremise

**Definition:** Software installed and run on customer's own infrastructure, not hosted by the provider.

**Primary users:** Varies by application type
**Deployment location:** Customer data center or local machine
**Who manages infrastructure:** Customer manages everything

**CRITICAL DISTINCTION: Desktop Client vs Standalone App**

**Standalone Desktop Application (TRUE onPremise):**
- Runs independently on user's machine
- No cloud backend required for core functionality
- Examples: Adobe Photoshop (perpetual license), JetBrains CLion, Microsoft Office (non-365)

**Desktop Client for Cloud Service (NOT onPremise - should be saas!):**
- Desktop app that connects to cloud backend
- Cannot function without cloud service
- Examples: Slack Desktop, Zoom Desktop, Microsoft Teams Desktop
- **These should be classified as `saas`, NOT `onPremise`**

**How to identify:**
- Name includes "Desktop Client" for a known cloud service → `saas`
- Product has both web and desktop versions → `saas` (desktop is a client)
- Can the app function offline indefinitely? If NO → `saas`

**Examples of TRUE onPremise:**
- ✅ **Adobe Captivate** - Desktop authoring tool
- ✅ **JetBrains CLion** - Desktop IDE (standalone)
- ✅ **Atlassian Confluence - on premise** - Self-hosted version

**Common traps:**
- ❌ Desktop client (Slack Desktop) → NOT onPremise, it's `saas`
- ❌ Don't confuse "private cloud" with "on-premise"

---

### 5. hybrid

**Definition:** Application that supports BOTH cloud and on-premise deployment, giving customers flexibility in where to host it.

**Primary users:** Varies by application type
**Deployment location:** Customer chooses (cloud OR on-premise OR both)

**Key indicators:**
- Supports multiple deployment models
- Customer can choose where to host
- Keywords: "hybrid", "cloud and on-premise", "flexible deployment", "private edition"

**Examples:**
- ✅ **SAP S/4HANA Cloud Private Edition** - Cloud or on-premise deployment
- ✅ **Red Hat OpenShift** - Can run on cloud, on-premise, or edge

**Decision framework:**
Ask: "Can customers choose between cloud AND on-premise deployment?" If YES → `hybrid`

**Common traps:**
- ❌ Separate products ("Jira Cloud" vs "Jira Server") = 2 separate apps, not hybrid
- ❌ SaaS with mobile client ≠ hybrid

---

### 6. mobile

**Definition:** Application designed exclusively or primarily as a native mobile app for iOS and/or Android devices.

**Primary users:** Mobile device users
**Platform:** iOS, Android, or both

**Key indicators:**
- Native mobile application
- NOT mobile-responsive web app
- Keywords: "mobile app", "for iOS", "for Android"

**Examples:**
- ✅ **SAP Field Service Management mobile app**
- ✅ **SAP SuccessFactors Mobile for iOS**

**Decision framework:**
Ask: "Is this a native mobile app, not a web app accessed via mobile browser?" If YES → `mobile`

**Critical distinction:**
- **mobile** = Native app (App Store/Play Store)
- **saas** = Mobile-responsive web app

**Common traps:**
- ❌ Mobile-responsive web app ≠ `mobile` (it's `saas`)
- ❌ SaaS with mobile client ≠ `mobile` (main product is `saas`)

---

## Decision Trees

### Cloud Services Classification

For AWS, Azure, GCP, Oracle Cloud services:

```
What does it provide?
  ├─ Virtual Machines / Compute Instances → iaas
  ├─ Storage (Object, Block, File) → iaas
  ├─ Networking (VPC, Load Balancers) → iaas
  ├─ Managed Database → paas
  ├─ Serverless Compute → paas
  ├─ Container Orchestration → paas
  ├─ Data Warehouse / Analytics → paas
  ├─ Message Queue / Event Bus → paas
  └─ Complete End-User Application → saas
```

### "Platform" Disambiguation

```
"Platform" mentioned
  ├─ Platform FOR DEVELOPERS?
  │   ├─ Deploy code? → paas
  │   ├─ Build applications? → paas
  │   └─ Manage data pipelines? → paas
  │
  └─ Platform FOR END USERS?
      ├─ Collaboration → saas
      ├─ Analytics (business users) → saas
      └─ CRM → saas
```

---

# Part 2: Writing Hosting Description

## Purpose of hostingDescription

**Primary purpose:** Document the reasoning and evidence for the hostingType classification.

The `hostingDescription` field should explain:
1. **WHY** this hosting type was selected
2. **Infrastructure details** that support the classification
3. **Cloud provider or deployment model** (when applicable)

**This is NOT just "where it's hosted" - it's the REASONING for your classification decision.**

## Format: Technical Reasoning

**Required format:**
```
Classified as [hostingType] because [reasoning]. Hosted on [Provider] [optional: additional details].
```

**Alternative concise format (when obvious):**
```
[Application Name] is [description that implies hostingType] hosted on [Provider]
```

### Length Guidelines

- **Target:** 50-150 characters
- **Minimum:** 30 characters
- **Maximum:** 200 characters

## When to Include hostingDescription

**Always include for:**
- All applications you are classifying (document your reasoning)
- Cloud-hosted applications - specify provider

**Leave blank only if:**
- Hosting/infrastructure information is genuinely unavailable
- For some `onPremise` standalone apps where there's no provider

**Current data:** Only 32% have this field. Your goal is to SET it for applications you classify.

---

## Writing Guidelines by Hosting Type

### For saas Applications

**Format: Classification reasoning + provider**

**Pattern 1 - With reasoning (preferred):**
```
Classified as SaaS: end-user [application type] hosted on [Cloud Provider]
```

**Examples:**
- ✅ "Classified as SaaS: end-user collaboration application hosted on AWS"
- ✅ "Classified as SaaS: CRM for business users, hosted on Salesforce infrastructure"
- ✅ "End-user project management application hosted on AWS and Azure"

**Pattern 2 - Concise (when hostingType is obvious):**
```
[Application Name] is hosted on [Cloud Provider]
```

**Examples:**
- ✅ "10Duke is hosted by Amazon Web Service"
- ✅ "Ten Thousand Coffees is hosted on Google Cloud Platform"
- ✅ "Smartsheet hosted on AWS with multi-site data redundancy"

**Pattern 3 - For desktop clients (important):**
```
Desktop client for cloud-based [service type] hosted on [Provider]
```

**Examples:**
- ✅ "Desktop client for cloud-based messaging service hosted on AWS"
- ✅ "Slack Desktop connects to Slack's cloud infrastructure hosted on AWS"

---

### For paas Applications

**Format: Emphasize developer use + provider**

**Pattern 1 - With reasoning (preferred):**
```
Classified as PaaS: [service type] for developers to [action] on [Provider]
```

**Examples:**
- ✅ "Classified as PaaS: serverless compute platform for developers to deploy functions on AWS"
- ✅ "Classified as PaaS: managed database service where developers deploy applications, AWS manages infrastructure"
- ✅ "Container orchestration platform for deploying containerized applications on Google Cloud"

**Pattern 2 - Concise (when obvious):**
```
[Service type] hosted on [Provider]
```

**Examples:**
- ✅ "Managed database service hosted on AWS"
- ✅ "Heroku's infrastructure hosted on AWS, providing deployment platform for developers"
- ✅ "Google Cloud BigQuery data warehouse hosted on Google Cloud Platform"

**For first-party cloud services:**
- ✅ "AWS Lambda provides serverless compute on AWS infrastructure"
- ✅ "Amazon RDS is a managed database service on AWS"

---

### For iaas Applications

**Format: Emphasize infrastructure layer + provider**

**Pattern 1 - With reasoning:**
```
Classified as IaaS: provides [infrastructure type] where users manage [what they manage]
```

**Examples:**
- ✅ "Classified as IaaS: provides virtual machines where users manage OS and applications on AWS"
- ✅ "Classified as IaaS: object storage infrastructure on AWS where users manage data"
- ✅ "Virtual network infrastructure hosted on Azure where users manage network configuration"

**Pattern 2 - Concise (self-referential for cloud services):**
```
[Infrastructure service] hosted on [Provider]
```

**Examples:**
- ✅ "Amazon EC2 virtual machines hosted on AWS"
- ✅ "Amazon S3 object storage hosted on AWS"
- ✅ "Azure Virtual Machines hosted on Microsoft Azure"

---

### For onPremise Applications

**Special considerations:**

**For standalone desktop applications:**
- Often best to leave blank (no provider hosting)
- OR: "Standalone desktop application running on user's local machine"

**For self-hosted server software:**
```
Self-hosted on customer infrastructure [optional: vendor support details]
```

**Examples:**
- ✅ "Self-hosted on customer infrastructure"
- ✅ "On-premise deployment on customer's own servers"
- Leave blank (acceptable)

**DO NOT include if it's a desktop CLIENT for a cloud service** - those should be `saas`, not `onPremise`!

---

### For hybrid Applications

**Format: Emphasize deployment flexibility**

**Pattern:**
```
Classified as hybrid: supports [deployment options]
```

**Examples:**
- ✅ "Classified as hybrid: supports both cloud and on-premise deployment options"
- ✅ "Flexible deployment model: customers can choose cloud (AWS/Azure) or on-premise"
- ✅ "SAP S/4HANA can be deployed in cloud or on customer's infrastructure"

---

### For mobile Applications

**Format: Emphasize native mobile platform**

**Pattern:**
```
Native mobile application for [iOS/Android] [optional: backend infrastructure]
```

**Examples:**
- ✅ "Native mobile application for iOS and Android"
- ✅ "Mobile app for field service technicians on iOS and Android platforms"
- Often acceptable to leave blank (mobile apps rarely disclose backend infrastructure)

**If backend is known:**
- ✅ "Native iOS/Android app with backend infrastructure hosted on AWS"

---

## Information Sources

### Where to Find Hosting Information

**Priority order:**

1. **Official website - Infrastructure/Security pages**
   - "Security", "Trust Center", "Infrastructure", "Compliance" pages
   - Often lists cloud providers

2. **Application description field**
   - May already mention hosting provider

3. **Official documentation**
   - Architecture documentation
   - API documentation

4. **For cloud provider services:**
   - Self-evident (AWS services on AWS, Azure on Azure)

### What to Extract

**Key information:**
- Cloud provider (AWS, Azure, GCP, IBM Cloud, Oracle Cloud)
- Service type that supports classification reasoning
- Data center locations (if notable: "US and EU")

**Critical: NEVER HALLUCINATE**
- If hosting information not found, leave blank OR use generic reasoning
- Don't assume cloud provider
- Only include if confidence ≥ 90%

---

## Anti-Hallucination Rules (CRITICAL)

**NEVER:**
- ❌ Assume cloud provider based on company size
- ❌ Guess "probably AWS since most use it"
- ❌ Infer from industry or geography
- ❌ Copy from similar products
- ❌ Use phrases like "likely hosted on" or "appears to use"

**ONLY include hostingDescription if:**
1. Explicitly stated on official website
2. Self-evident for cloud provider services (AWS Lambda → AWS)
3. Found in official documentation
4. Confidence ≥ 90%

**If uncertain:**
- Focus on classification reasoning without provider: "Classified as PaaS: managed database service for developers"
- Or leave blank (acceptable)

---

## Examples Analysis

### Excellent Descriptions (Technical Reasoning)

**Pattern: Classification reasoning**
```
"Classified as PaaS: serverless compute platform for developers on AWS infrastructure"
```
✅ Clear reasoning, technical, explains classification

**Pattern: Concise with implied reasoning**
```
"Managed database service hosted on AWS"
```
✅ "Managed database" implies PaaS, specific provider

**Pattern: Simple for obvious cases**
```
"10Duke is hosted by Amazon Web Service"
```
✅ Factual, concise (appropriate when hostingType is obvious from other context)

### Good Descriptions

**With infrastructure details:**
```
"10,000ft is hosted by Microsoft Azure and Amazon Web Services"
```
✅ Specific providers, shows multi-cloud

**With classification context:**
```
"End-user collaboration application hosted on AWS with multi-site data redundancy"
```
✅ "End-user" signals SaaS classification

### Descriptions to Avoid

**Too vague:**
```
❌ "Hosted in the cloud"
```
No specific provider, doesn't help classification

**Marketing language:**
```
❌ "Hosted on world-class infrastructure"
```
Not factual or useful

**Missing reasoning:**
```
❌ "AWS"
```
Too terse, doesn't explain classification (though "AWS" alone is acceptable if space is limited)

---

## Complete Workflow Example

### Example: AWS Lambda

**Step 1: Determine hostingType**
- Quick check: AWS + "Lambda" → likely `paas` (serverless)
- Evaluation: Developers deploy functions, AWS manages servers
- Decision: `hostingType` = `paas`
- Confidence: 95%

**Step 2: Write hostingDescription**
```
"Classified as PaaS: serverless compute platform where developers deploy functions, AWS manages infrastructure"
```

**Or concise version:**
```
"Serverless compute service for developers hosted on AWS"
```

---

### Example: Smartsheet

**Step 1: Determine hostingType**
- Quick check: Business users, project management → `saas`
- Evaluation: Complete business application for end users
- Decision: `hostingType` = `saas`
- Confidence: 100%

**Step 2: Write hostingDescription**
```
"Classified as SaaS: project management application for business users, hosted on AWS"
```

**Or concise version:**
```
"Smartsheet hosted on AWS with multi-site data redundancy"
```

---

### Example: Slack Desktop

**Step 1: Determine hostingType**
- Name check: "Desktop" → might think `onPremise`
- **CRITICAL CHECK**: Is this a desktop CLIENT for cloud service? YES
- Evaluation: Desktop client requires Slack cloud backend
- Decision: `hostingType` = `saas` (NOT onPremise!)
- Confidence: 100%

**Step 2: Write hostingDescription**
```
"Desktop client for Slack's cloud-based messaging service hosted on AWS"
```

---

### Example: JetBrains CLion

**Step 1: Determine hostingType**
- Name check: IDE, desktop tool
- Evaluation: Standalone desktop IDE, no cloud backend required
- Decision: `hostingType` = `onPremise`
- Confidence: 100%

**Step 2: Write hostingDescription**
```
"Standalone desktop IDE running on user's local machine"
```

**Or leave blank** (acceptable for on-premise)

---

## Quality Checklist

Before finalizing, verify:

### For hostingType:
- [ ] I completed evidence gathering
- [ ] I checked the name FIRST for obvious indicators
- [ ] I completed the evaluation matrix (if needed)
- [ ] I checked the desktop client vs standalone distinction
- [ ] I verified my confidence level ≥ 85%
- [ ] I can explain WHY I rejected the second-most-likely option

### For hostingDescription:
- [ ] Information is from official sources (not hallucinated)
- [ ] Includes reasoning for the classification OR clearly implies it
- [ ] Cloud provider is specifically named (when applicable)
- [ ] Length is 50-150 characters (acceptable range: 30-200)
- [ ] No marketing language or superlatives
- [ ] Factual and technical tone
- [ ] Consistent with hostingType classification
- [ ] Only included if confidence ≥ 90%

---

## Common Mistakes and How to Avoid Them

### Mistake 1: Desktop Client Misclassification

**Wrong:**
- hostingType: `onPremise`
- Application: "Slack Desktop"

**Why wrong:**
- Slack Desktop is a client for cloud service, not standalone
- Should be `saas`

**Correct:**
- hostingType: `saas`
- hostingDescription: "Desktop client for cloud-based messaging service hosted on AWS"

---

### Mistake 2: "Platform" = PaaS Assumption

**Wrong:**
- Description: "Collaboration platform for teams"
- Chosen: `paas`

**Why wrong:**
- Platform FOR END USERS (collaboration), not developers
- Should be `saas`

**Correct:**
- hostingType: `saas`
- hostingDescription: "Classified as SaaS: collaboration application for business users"

---

### Mistake 3: Hallucinating Cloud Provider

**Wrong:**
- hostingDescription: "Probably hosted on AWS based on company size"

**Why wrong:**
- No evidence, just assumption
- Hallucination

**Correct:**
- Leave blank OR
- "Classified as SaaS: end-user application (hosting provider not publicly disclosed)"

---

### Mistake 4: Generic Description

**Wrong:**
- hostingDescription: "Hosted in the cloud with enterprise security"

**Why wrong:**
- No specific provider
- Marketing language
- Doesn't help explain classification

**Correct:**
- "Classified as SaaS: business application hosted on AWS"

---

## Summary

### hostingType Decision Process:
1. **Quick triage**: Check name for obvious indicators (70% of cases)
2. **Full evaluation**: Complete matrix for ambiguous cases
3. **Primary user test**: Developers (PaaS), Business users (SaaS), IT (IaaS)
4. **Anti-patterns check**: Desktop clients, "platform" keyword, cloud services
5. **Web search**: Mandatory for cloud provider services
6. **Final decision**: With confidence ≥ 85%

### hostingDescription Writing:
1. **Purpose**: Document reasoning for classification
2. **Format**: Technical reasoning + provider (when known)
3. **Length**: 50-150 characters target
4. **Tone**: Technical, factual, no marketing
5. **Rule**: Only include if confidence ≥ 90%
6. **Never hallucinate**: Evidence-based only

### Key Principles:
- **Name is strongest signal** (check first)
- **Desktop client ≠ onPremise** (it's usually saas)
- **"Platform" needs context** (developers → paas, users → saas)
- **hostingDescription = reasoning** (not just provider)
- **Blank is acceptable** (better than hallucination)

---

## Revision History

- **Version 1.1** (2026-02-22): Added Quick Reference Card, enhanced desktop client distinction, reframed hostingDescription as reasoning documentation

