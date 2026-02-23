#!/usr/bin/env python3
"""
Generate hosting type evaluation matrix template for an application.
This ensures agents systematically evaluate all 6 hosting types.

Usage:
    python generate_matrix.py "Application Name" > hosting_matrix.md
"""

import sys
from datetime import datetime


def generate_matrix_template(app_name):
    """Generate a complete hosting type evaluation matrix template."""

    template = f"""# Hosting Type Evaluation Matrix
## Application: {app_name}
## Date: {datetime.now().strftime('%Y-%m-%d')}

---

## ⚠️ INSTRUCTIONS - READ BEFORE STARTING

**YOU MUST COMPLETE ALL 6 SECTIONS BEFORE MAKING A DECISION**

1. Score each hosting type from 0-10
2. Provide specific reasoning for each score
3. Answer the checklist questions for each type
4. DO NOT skip any sections
5. DO NOT pick the first type that seems to match

**Scoring Guide**:
- 0-2: Definitely not this type
- 3-4: Unlikely, but some minor characteristics
- 5-6: Possible, has some characteristics
- 7-8: Likely, has most characteristics
- 9-10: Definitely this type, perfect match

---

## 1. SaaS (Software as a Service)

**Definition**: End-user application hosted in the cloud, accessed via browser or thin client, with multi-tenant infrastructure managed by the provider.

**Characteristics to Check**:
- [ ] **Primary Users**: Business users (not developers or IT teams)
- [ ] **Access Method**: Web browser or lightweight client application
- [ ] **Hosting**: Cloud-hosted infrastructure (no user installation of servers)
- [ ] **Multi-tenancy**: Single application instance serves multiple customers
- [ ] **Examples**: Salesforce, Slack, Gmail, Smartsheet

**Research Questions**:
1. Who are the primary users? (check homepage, features page)
2. How do users access it? (web app, desktop client, mobile app?)
3. Is there any mention of servers, infrastructure, or deployment? (should be NO for SaaS)
4. Does it run in the cloud or on user's device?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 8/10. Primary users are business teams (marketing page targets business users).
Accessed via web browser at app.example.com. No installation required. Cloud-hosted per security page.
Not 10/10 because also has desktop client component."]
```

---

## 2. PaaS (Platform as a Service)

**Definition**: Development platform that provides infrastructure and tools for developers to build, deploy, and manage applications without managing underlying infrastructure.

**Characteristics to Check**:
- [ ] **Primary Users**: Software developers and development teams
- [ ] **Purpose**: Build/deploy applications ON this platform
- [ ] **Provides**: APIs, runtime environments, development tools, CI/CD
- [ ] **Abstracts**: Infrastructure management (servers, OS, networking)
- [ ] **Examples**: AWS Lambda, Heroku, Google App Engine, Azure Functions

**Research Questions**:
1. Is this FOR developers to build things? (check documentation, API docs)
2. Can you deploy code/applications to this platform?
3. Does it provide runtime environments, SDKs, or build tools?
4. Does marketing target "developers" or "engineers"?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 2/10. Not a development platform. No APIs for deploying applications.
Homepage targets business users, not developers. No mention of SDKs, runtimes, or CI/CD."]
```

---

## 3. IaaS (Infrastructure as a Service)

**Definition**: Virtualized computing resources (VMs, storage, networking) where IT teams manage and configure infrastructure but don't maintain physical hardware.

**Characteristics to Check**:
- [ ] **Primary Users**: IT teams, system administrators, DevOps engineers
- [ ] **Provides**: Virtual machines, storage, networking, load balancers
- [ ] **User Manages**: OS, middleware, applications, data
- [ ] **Provider Manages**: Physical hardware, virtualization layer
- [ ] **Examples**: AWS EC2, Azure Virtual Machines, Google Compute Engine

**Research Questions**:
1. Does it provide virtual machines or compute instances?
2. Do users configure OS, networking, storage?
3. Is it infrastructure for running OTHER applications?
4. Does marketing mention "VMs", "compute", "infrastructure"?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 0/10. Not infrastructure. No VMs, no configurable compute resources.
This is an end-user application, not infrastructure for running other applications."]
```

---

## 4. On-Premise

**Definition**: Software installed and running on customer's own servers/infrastructure, fully managed by the customer's IT team.

**Characteristics to Check**:
- [ ] **Installation**: Customer installs on their servers
- [ ] **Infrastructure**: Customer provides and manages all infrastructure
- [ ] **Deployment**: Self-hosted, not cloud-based
- [ ] **Control**: Customer has full control over deployment, updates, security
- [ ] **Examples**: Traditional enterprise software, private databases, on-prem ERP

**Research Questions**:
1. Is there a self-hosted/on-premise deployment option?
2. Can customers install this on their own servers?
3. Does pricing page mention "on-premise license"?
4. Are there deployment guides for customer infrastructure?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 0/10. No on-premise option mentioned. All deployment is cloud-based.
No installation downloads or deployment guides for customer servers."]
```

---

## 5. Hybrid

**Definition**: Application offering BOTH cloud and on-premise deployment options, allowing customers to choose or combine deployment methods.

**Characteristics to Check**:
- [ ] **Options**: Both cloud-hosted AND self-hosted available
- [ ] **Customer Choice**: Customer decides deployment method
- [ ] **Flexibility**: Can deploy in cloud, on-premise, or mixed
- [ ] **Common Use**: Enterprise software with deployment flexibility
- [ ] **Examples**: Microsoft Office 365 + on-premise Exchange, SAP S/4HANA

**Research Questions**:
1. Does pricing page show both cloud and on-premise options?
2. Is there a "deployment options" or "how to deploy" page?
3. Can customers choose between cloud and self-hosted?
4. Are there separate SKUs for cloud vs on-premise?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 0/10. Only cloud deployment mentioned. No on-premise option available.
Pricing page only shows cloud subscription plans, no on-premise licenses."]
```

---

## 6. Mobile

**Definition**: Native mobile application (iOS/Android) as the primary or only interface, distributed through app stores, designed mobile-first (not just a web app accessed on mobile).

**Characteristics to Check**:
- [ ] **Native App**: iOS/Android native app (not web app in mobile browser)
- [ ] **App Store**: Distributed via Apple App Store / Google Play Store
- [ ] **Mobile-First**: Designed primarily for mobile, not desktop
- [ ] **Primary Interface**: Mobile app is main/only way to use product
- [ ] **Examples**: Instagram, TikTok, Uber, WhatsApp

**Research Questions**:
1. Is there an app in the Apple App Store or Google Play Store?
2. Is the mobile app the PRIMARY way to use the product? (or just supplementary?)
3. Is it described as a "mobile app" in marketing?
4. Does the name include "app" or specifically target mobile users?

**Score**: ___/10

**Reasoning**:
```
[REQUIRED: Explain your score. Reference specific evidence from research.
Example: "Score 1/10. Has a mobile app but it's supplementary to web application.
Primary interface is web-based. Mobile app is just convenience feature for existing users.
Not mobile-first or mobile-native product."]
```

---

## Decision Logic

### Step 1: Identify Highest Score

**Scores Summary**:
- SaaS: ___/10
- PaaS: ___/10
- IaaS: ___/10
- On-Premise: ___/10
- Hybrid: ___/10
- Mobile: ___/10

**Highest Score**: _____ (type)
**Second Highest**: _____ (type)

### Step 2: Primary User Test (if scores are close)

**Who are the PRIMARY users?**
- [ ] Business users (end users, teams, consumers) → Indicates SaaS
- [ ] Developers / Engineers → Indicates PaaS
- [ ] IT teams / System administrators → Indicates IaaS
- [ ] Mobile users (mobile-first product) → Indicates Mobile

**Primary User Identified**: _____________________

### Step 3: Name Check

**Does the application name contain indicators?**
- [ ] "mobile app", "app for iOS/Android" → Indicates Mobile
- [ ] "Desktop", "for Windows/Mac" → May indicate On-Premise or SaaS with desktop client
- [ ] "Platform", "Engine", "Framework" → Check if PaaS
- [ ] "Private Edition", "Enterprise Edition" → Check if Hybrid or On-Premise option
- [ ] "Cloud", "Online" → Indicates SaaS

**Name Indicators Found**: _____________________

### Step 4: Access Method Check

**How do users access this application?**
- [ ] Web browser (primary) → SaaS or PaaS
- [ ] Desktop client connecting to cloud → SaaS (client for cloud service)
- [ ] Mobile app (primary) → Mobile
- [ ] Installed locally (no cloud) → On-Premise
- [ ] Both cloud and local options → Hybrid

**Access Method**: _____________________

### Step 5: Tie-Breaker Rules

**If SaaS and Mobile scores are tied**:
- Desktop/web is primary → Choose SaaS
- Mobile is primary → Choose Mobile

**If SaaS and PaaS scores are tied**:
- End users are primary → Choose SaaS
- Developers are primary → Choose PaaS

**Tie-Breaker Applied?**: [ ] Yes [ ] No
**If Yes, explain**: _____________________

---

## FINAL DECISION

**Selected Hosting Type**: _____________________

**Confidence Level**: ____% (must be ≥70% to proceed)

**Decision Reasoning**:
```
[REQUIRED: Comprehensive explanation of why this type was selected.
Should reference:
1. The score from the matrix
2. Primary user analysis
3. Name/access method checks
4. Why other high-scoring types were rejected
5. Specific evidence from research

Example: "Selected SaaS with 85% confidence. Scored 8/10 on SaaS matrix (highest score).
Primary users are business teams per marketing page. Web-based access via app.example.com.
PaaS scored 2/10 (not for developers). Mobile scored 3/10 (has mobile app but web is primary).
Security page confirms cloud-hosted infrastructure. No on-premise option mentioned."]
```

**Confidence Justification**:
```
[REQUIRED: Why this confidence level?
- High (≥85%): Clear evidence, no ambiguity
- Medium (70-84%): Good evidence, some uncertainty
- Low (<70%): Insufficient evidence or highly ambiguous (should not proceed)

Example: "85% confidence because: (1) Homepage clearly targets business users,
(2) Security page confirms cloud infrastructure, (3) No developer or IT admin features found,
(4) Name and access method align with SaaS. Not 100% because company could add on-premise
option in future, but current offering is clearly SaaS."]
```

---

## Evidence & Sources

**Key Evidence Used**:
- Homepage: _____________________
- Security page: _____________________
- Pricing page: _____________________
- About page: _____________________
- Name analysis: _____________________
- Primary user: _____________________
- Perplexity search: _____________________

**Conflicting Information** (if any):
```
[If sources provided conflicting signals about hosting type, document here]
```

---

## Validation Checklist

Before proceeding, verify:
- [ ] All 6 hosting types have scores (0-10)
- [ ] All 6 reasoning sections are filled with specific evidence
- [ ] Primary user identified
- [ ] Access method documented
- [ ] Final decision has ≥70% confidence
- [ ] Decision reasoning is comprehensive (not just "it's SaaS because it's cloud")

**Matrix Complete**: [ ] Yes [ ] No

**IF NO → GO BACK AND COMPLETE ALL SECTIONS**

---

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    return template


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_matrix.py \"Application Name\"")
        print("Example: python generate_matrix.py \"TeamSmart AI\"")
        sys.exit(1)

    app_name = sys.argv[1]
    template = generate_matrix_template(app_name)
    print(template)


if __name__ == "__main__":
    main()
