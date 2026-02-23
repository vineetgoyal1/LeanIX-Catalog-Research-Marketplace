"""Application research logic using Perplexity MCP for field-specific research.

This module implements research logic following the application guidelines.
It's designed to be used by Claude Code agents with direct MCP access.
"""

from pathlib import Path
from typing import Any


class ApplicationResearcher:
    """Implements field-specific research logic following guidelines.

    This class is designed to work with Claude Code agents that have
    direct access to Perplexity MCP tools (mcp__perplexity__perplexity_search).
    """

    def __init__(self):
        """Initialize researcher with guidelines directory path."""
        self.guidelines_dir = Path(__file__).parent.parent / "guidelines"

    def get_url_research_query(
        self,
        application_name: str,
        initial_url: str | None = None
    ) -> str:
        """Generate Perplexity query for URL research.

        Follows Application_Webpage_URL_Guidelines.md

        Args:
            application_name: Name of the application
            initial_url: Optional URL to validate (if provided by user)

        Returns:
            Query string for Perplexity
        """
        if initial_url:
            return f"""Verify that {initial_url} is the official website for {application_name}.

Check the following:
1. Does the URL return HTTP 200 or redirect 301/302?
2. Does the page content mention {application_name}?
3. Does it have a valid SSL certificate?
4. Can you find this URL in at least 2 authoritative sources (search engines, Wikipedia, GitHub, product directories)?

Provide your assessment with confidence level (high/medium/low) and list the sources where you found this URL.

If the URL is not valid or you cannot verify it, suggest the correct official website if you can find one.

IMPORTANT: Do NOT hallucinate or guess. If you cannot verify the URL, say so clearly."""

        else:
            return f"""What is the official website homepage URL for {application_name}?

Requirements:
1. Find the URL from at least 2 authoritative sources (official website listings, Wikipedia, GitHub README, product directories, app stores)
2. Verify the URL is accessible (returns HTTP 200 or redirect 301/302)
3. Verify the page content actually mentions {application_name}
4. Confirm it has a valid SSL certificate

Provide:
- The verified URL
- Confidence level (high if 3+ sources, medium if 2 sources, low if only 1 source)
- List of sources where you found this URL
- HTTP status code if you can check it

IMPORTANT: Do NOT hallucinate or guess URLs. If you cannot find a verified URL from authoritative sources, say "URL not found" rather than guessing."""

    def get_hosting_type_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for hosting type classification.

        Follows Application_Hosting_Type_Guidelines.md with evaluation matrix

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Determine the hosting type for {application_name}. Choose ONE from: saas, paas, iaas, onPremise, hybrid, mobile.

**CRITICAL: Complete evaluation matrix for ALL 6 types before deciding.**

**Step 1: Name check (quick indicators)**
- Contains "mobile app", "iOS", "Android" → likely mobile
- Contains "Desktop", "Private Edition", "On-Premise" → likely onPremise
- Contains "Platform", "API", "SDK" → might be paas (but verify primary user)

**Step 2: Identify primary user**
- Business users (marketing, sales, HR, project management) → likely saas
- Developers (APIs, SDKs, deployment tools) → likely paas
- IT teams (infrastructure, servers, networking) → likely iaas
- Mobile device users → likely mobile
- All users can install locally → likely onPremise

**Step 3: Complete evaluation matrix**
For EACH hosting type, evaluate these criteria:

**saas** (Software as a Service):
- End-user application accessed via browser/app
- Hosted/managed by provider
- Examples: Salesforce, Slack, Zoom
- Score: [0-5]

**paas** (Platform as a Service):
- Developers build/deploy applications on it
- Provides runtime, frameworks, deployment tools
- Examples: Heroku, AWS Lambda, Google App Engine
- Score: [0-5]

**iaas** (Infrastructure as a Service):
- Provides compute, storage, networking resources
- Users manage OS, applications
- Examples: AWS EC2, Azure VMs, Google Compute
- Score: [0-5]

**onPremise**:
- Installed/runs on user's own infrastructure
- User manages hosting, updates
- Examples: On-premise databases, private servers
- Score: [0-5]

**hybrid**:
- Combination of cloud + on-premise deployment
- Or multiple hosting models supported
- Examples: SAP (cloud + on-premise), Salesforce (cloud with private cloud option)
- Score: [0-5]

**mobile**:
- Native mobile app for iOS/Android
- Runs on mobile devices (not just mobile-responsive web)
- Examples: Instagram, WhatsApp, Uber
- Score: [0-5]

**Step 4: Research from these sources**
1. Security page (/security) - often mentions cloud provider (AWS, Azure, GCP)
2. Enterprise page (/enterprise) - hosting infrastructure details
3. Changelog (/changelog) - hosting announcements, migrations
4. Product page - deployment options, technical architecture

**Step 5: Apply decision logic**
- If score ties between types, use primary user test
- For cloud services (AWS Lambda, Azure Functions), check if for developers → paas not saas
- Desktop clients (Slack Desktop, Zoom client) are still saas (server-hosted with local client)

Provide:
- hostingType: ONE of (saas, paas, iaas, onPremise, hybrid, mobile)
- Evaluation matrix scores for all 6 types
- Primary user identified
- Reasoning with evidence
- Confidence level (high/medium/low)
- Sources used

IMPORTANT: Do NOT skip evaluation matrix. Do NOT pick first match. Complete all 6 evaluations."""

    def get_hosting_description_research_query(
        self,
        application_name: str,
        hosting_type: str
    ) -> str:
        """Generate Perplexity query for hosting description (technical reasoning).

        Follows Application_Hosting_Type_Guidelines.md

        Args:
            application_name: Name of the application
            hosting_type: The determined hosting type

        Returns:
            Query string for Perplexity
        """
        return f"""Provide technical reasoning for why {application_name} is classified as {hosting_type}.

**Requirements for hostingDescription:**
1. Start with: "Classified as {hosting_type}: [reasoning]"
2. Mention specific technical details:
   - For saas: primary user type, cloud provider if known
   - For paas: developer tools provided, deployment capabilities
   - For iaas: infrastructure components (compute, storage, networking)
   - For onPremise: installation model, user management
   - For hybrid: combination details
   - For mobile: platform (iOS, Android, both), native vs hybrid

3. Include evidence from official sources:
   - Cloud provider mentioned (AWS, Azure, GCP)
   - Deployment model described on website
   - Technical documentation references

4. 1-3 sentences maximum
5. Factual tone (no marketing language)
6. 90% confidence threshold - if uncertain, research more

**Anti-hallucination rules:**
- Do NOT guess cloud provider if not explicitly stated
- Do NOT infer technical details from absence of information
- Do NOT use marketing language ("seamless", "powerful", "enterprise-grade")
- If confidence < 90%, say "Classified as {hosting_type}: [basic reasoning without specific technical details]"

Example good descriptions:
- "Classified as SaaS: end-user collaboration application hosted on AWS with multi-site data redundancy"
- "Classified as PaaS: developer platform for building and deploying serverless functions with integrated CI/CD"
- "Classified as mobile: native iOS and Android application for mobile device users"

Provide: hostingDescription (1-3 sentences), confidence level, sources used"""

    def get_sso_status_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for SSO status.

        Follows Application_SSO_Status_Guidelines.md with changelog emphasis

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Determine if {application_name} supports Single Sign-On (SSO). Answer: supported or notSupported.

**Priority research locations (in order):**
1. **Changelog/Updates page** (/changelog, /updates, /whats-new, /releases) ⭐ CRITICAL
   - SSO is often announced as a major milestone
   - Look for "SSO support added", "SAML integration", "Enterprise authentication"
   - Note the date if found

2. Security page (/security, /security-features)
   - Explicit SSO mentions
   - SAML, OAuth, OIDC mentions

3. Enterprise page (/enterprise, /business)
   - Enterprise features list
   - Authentication section

4. Pricing page (/pricing)
   - SSO as paid/enterprise feature
   - Feature comparison tables

5. Integration directories
   - Okta Integration Network
   - Azure AD App Gallery
   - Google Workspace Marketplace

**Search keywords:**
- "SSO", "single sign-on"
- "SAML", "OAuth", "OIDC", "OpenID Connect"
- "Enterprise authentication"
- "Identity provider", "IdP"

**Decision criteria:**
- If found in ANY source with clear evidence → "supported"
- If explicitly states "SSO not supported" → "notSupported"
- If no clear evidence after checking all sources → Leave blank (acceptable)

**IMPORTANT:**
- Do NOT guess or infer SSO support from other features
- Do NOT mark "notSupported" unless explicitly stated
- Blank is better than wrong

Provide:
- ssoStatus: "supported", "notSupported", or "not found"
- Source where found (especially if from changelog, include date)
- Confidence level
- Evidence/quote from source

**Remember: Check changelog FIRST as primary source for SSO announcements.**"""

    def get_pricing_type_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for pricing type.

        Follows Application_Pricing_Guidelines.md

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Determine the pricing model for {application_name}. Choose ONE from: free, freemium, subscription, perpetual, transaction, enterprise.

**Priority research locations:**
1. Pricing page (/pricing) - PRIMARY SOURCE
2. Homepage - may mention "free", "get started", "try for free"
3. About/company page - business model description

**Pricing type definitions:**

1. **free**: Completely free with no paid options
   - No premium tiers, no paid features
   - May have donations or sponsorships

2. **freemium**: Free tier + paid premium features
   - Basic features free, advanced features paid
   - Free trial that converts to paid
   - Examples: Slack, Zoom, Dropbox

3. **subscription**: Recurring payment (monthly/annual)
   - No free tier
   - May have multiple paid tiers
   - Examples: Netflix, Office 365

4. **perpetual**: One-time purchase, lifetime access
   - Buy once, use forever
   - May have separate maintenance/support fees
   - Examples: Traditional desktop software

5. **transaction**: Pay-per-use or per-transaction
   - Charged based on usage volume
   - Examples: Payment processors, API calls

6. **enterprise**: Custom pricing, contact sales
   - No public pricing
   - Negotiated contracts
   - Examples: Enterprise software with custom deployments

**Decision logic:**
- Free tier exists + paid tiers exist → freemium
- Only paid tiers with recurring billing → subscription
- Contact sales only, no public pricing → enterprise
- Per-API-call or per-transaction → transaction
- One-time purchase → perpetual
- No pricing at all, open-source → free

Provide:
- pricingType: ONE of (free, freemium, subscription, perpetual, transaction, enterprise)
- Evidence from pricing page
- Confidence level
- Source used"""

    def get_product_category_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for product category.

        Follows Application_Product_Category_Guidelines.md

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Determine the product category for {application_name}.

**Source:** Match to predefined LeanIX categories (50+ categories available)

**Research approach:**
1. Identify application's PRIMARY functionality from:
   - Official website description
   - Product features page
   - App store categories (if mobile)

2. Common categories include:
   - Collaboration (team communication, workspaces)
   - Project Management (task tracking, project planning)
   - CRM (customer relationship management)
   - Development Tools (IDEs, version control)
   - Data Analytics (BI, reporting, dashboards)
   - Security (authentication, firewall, antivirus)
   - Infrastructure (cloud services, hosting, CDN)
   - HR/Recruiting (HRIS, ATS, talent management)
   - Marketing (email marketing, social media, advertising)
   - Finance (accounting, invoicing, payments)
   - (and many more...)

3. Use MOST SPECIFIC category:
   - "Project Management" is more specific than "Collaboration"
   - "Email Marketing" is more specific than "Marketing"
   - "Database" is more specific than "Infrastructure"

**Note:** The agent will have access to Product_Category_Reference.json with all valid categories.

Provide:
- Primary functionality description
- Suggested product category (most specific)
- Alternative categories if applicable
- Confidence level
- Source used

The agent will verify against Product_Category_Reference.json for exact category name."""

    def get_aliases_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for alias discovery.

        Follows Application_Alias_Guidelines.md

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Find all known aliases and alternative names for {application_name}.

**Alias types to look for:**
1. Abbreviations (shortened forms: "GH" for GitHub)
2. Former names (names before rebranding)
3. Product variations (different product lines with similar names)
4. Stylistic variations (spacing, capitalization, special characters)
5. Acquisitions (name changes after being acquired)

**Search in:**
- Official website (About, company history, press releases)
- Wikipedia (former names section, redirects)
- News articles about rebrands or acquisitions
- GitHub repository names
- App store listings

**Requirements:**
- Only verified aliases from official sources or 2+ authoritative sources
- Do NOT include: competitor names, generic terms, unrelated products
- For each alias, note the source

Provide:
- Comma-separated alias list or "No aliases found"
- Source for each alias
- Confidence level

IMPORTANT: Do NOT fabricate aliases. Only document names you can verify from credible sources."""

    def get_subtype_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for subtype (application vs mobileApp).

        Follows Application_Subtype_Guidelines.md

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Determine the subtype for {application_name}. Choose: "application" or "mobileApp".

**Definitions:**
- **application**: Web-based or desktop applications accessed via browser or desktop client
- **mobileApp**: Native mobile applications for iOS/Android that run on mobile devices

**Decision logic:**
1. Check if it's PRIMARILY a native mobile app:
   - Available on App Store / Google Play
   - Described as "mobile app for iOS/Android"
   - Native mobile-first design (not just mobile-responsive web)
   → If YES: mobileApp

2. Otherwise: application
   - Web applications (accessed via browser)
   - Desktop applications (Windows, Mac, Linux)
   - Cloud services
   - APIs/platforms
   - Hybrid apps that work on web + mobile (default to application)

**Examples:**
- Instagram, WhatsApp, Uber → mobileApp (native mobile-first)
- Salesforce, Gmail, Slack → application (web-based with mobile apps)
- AWS Lambda, GitHub → application (platform/service)
- Microsoft Word Online → application (web-based)
- Microsoft Word (desktop) → application (desktop)

Provide:
- subtype: "application" or "mobileApp"
- Evidence (platform availability, how it's described)
- Confidence level"""

    def get_description_research_query(self, application_name: str) -> str:
        """Generate Perplexity query for application description.

        Follows Application_Description_Guidelines.md with marketing language filter

        Args:
            application_name: Name of the application

        Returns:
            Query string for Perplexity
        """
        return f"""Provide a 30-90 word description of {application_name} based on their official website.

**Requirements:**
1. Extract from official website (About, homepage, product page)
2. Focus on WHAT the application does:
   - Primary functionality
   - Main features
   - Target users/use cases

3. Use factual, objective tone:
   - State WHAT it does, not how good it is
   - Use neutral verbs: "provides", "enables", "allows", "supports", "includes"
   - Focus on concrete capabilities, not benefits

4. **CRITICAL: Remove marketing language**
   Marketing buzzwords to AVOID:
   - "leading", "powerful", "innovative", "cutting-edge", "revolutionary"
   - "seamless", "transform", "empower", "streamline", "enhance"
   - "enterprise-grade", "best-in-class", "world-class"
   - "industry-leading", "award-winning"

   Replace with factual alternatives:
   - ❌ "transforms business operations" → ✅ "automates business workflows"
   - ❌ "seamless integration" → ✅ "integrates with"
   - ❌ "empowers teams" → ✅ "enables teams to"
   - ❌ "powerful analytics" → ✅ "analytics features"

5. Word count: 30-90 words exactly

**Example transformation:**
❌ Marketing: "Smartsheet is the leading platform that empowers teams to transform work through powerful collaboration and innovative project management"
✅ Factual: "Smartsheet provides an online application for collaboration and work management with features for project tracking, task assignment, and team coordination"

Provide:
- Description (30-90 words, factual, no marketing language)
- Word count
- Source (should be official website)
- Confidence level

IMPORTANT: Extract facts from official website. Remove ALL marketing buzzwords."""

    # Fixed value fields - no research queries needed
    def get_fixed_fields(self) -> dict[str, str]:
        """Return fixed field values (no research needed).

        Returns:
            Dictionary with collectionStatus, deprecated, asOfDate
        """
        from datetime import datetime
        return {
            "collectionStatus": "inReview",
            "deprecated": "no",
            "asOfDate": datetime.now().strftime("%Y-%m-%d")
        }
