"""Parallel research coordinator using both Perplexity and WebFetch for Applications.

This module orchestrates parallel research from multiple sources and
prepares data for cross-verification by the verification agent.
"""

import asyncio
from typing import Any, Dict
from datetime import datetime


class ParallelResearcher:
    """Coordinates parallel research from multiple sources for Application fact sheets."""

    def __init__(self):
        """Initialize parallel researcher."""
        pass

    async def research_all_fields(
        self,
        application_name: str,
        initial_url: str | None = None
    ) -> Dict[str, Any]:
        """Research all application fields in parallel using multiple sources.

        Args:
            application_name: Name of the application
            initial_url: Optional homepage URL if known

        Returns:
            Dictionary with results from each source:
            {
                "perplexity": {...},
                "webfetch": {...},
                "metadata": {
                    "application_name": str,
                    "research_timestamp": str,
                    "sources_used": list
                }
            }
        """
        # Run all research tasks in parallel
        tasks = [
            self._research_via_perplexity(application_name, initial_url),
            self._research_via_webfetch(application_name, initial_url),
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        perplexity_result = results[0] if not isinstance(results[0], Exception) else {"error": str(results[0])}
        webfetch_result = results[1] if not isinstance(results[1], Exception) else {"error": str(results[1])}

        sources_used = []
        if "error" not in perplexity_result:
            sources_used.append("perplexity")
        if "error" not in webfetch_result:
            sources_used.append("webfetch")

        return {
            "perplexity": perplexity_result,
            "webfetch": webfetch_result,
            "metadata": {
                "application_name": application_name,
                "initial_url": initial_url,
                "research_timestamp": datetime.now().isoformat(),
                "sources_used": sources_used
            }
        }

    async def _research_via_perplexity(
        self,
        application_name: str,
        initial_url: str | None
    ) -> Dict[str, Any]:
        """Research using Perplexity MCP for all 11 Application fields.

        This will be called by Claude Code agent with direct MCP access.
        Returns structured data for each field.

        Fields researched:
        1. webpageUrl
        2. hostingType (with evaluation matrix)
        3. hostingDescription (technical reasoning)
        4. ssoStatus (check changelog first)
        5. pricingType
        6. productCategory
        7. alias
        8. type (subtype: application/mobileApp)
        9. description (with marketing language filter)
        10. collectionStatus (fixed: "inReview")
        11. deprecated (fixed: "no")
        12. asOfDate (fixed: current date)
        """
        # This is a placeholder - the actual implementation will be done
        # by Claude Code agent calling Perplexity MCP tools
        return {
            "method": "perplexity_mcp",
            "queries": {
                "webpage_url": self._get_url_query(application_name, initial_url),
                "hosting_type": self._get_hosting_type_query(application_name),
                "hosting_description": self._get_hosting_description_query(application_name),
                "sso_status": self._get_sso_status_query(application_name),
                "pricing_type": self._get_pricing_query(application_name),
                "product_category": self._get_category_query(application_name),
                "aliases": self._get_aliases_query(application_name),
                "subtype": self._get_subtype_query(application_name),
                "description": self._get_description_query(application_name)
            },
            "fixed_fields": {
                "collectionStatus": "inReview",
                "deprecated": "no",
                "asOfDate": datetime.now().strftime("%Y-%m-%d")
            }
        }

    async def _research_via_webfetch(
        self,
        application_name: str,
        initial_url: str | None
    ) -> Dict[str, Any]:
        """Research using WebFetch to scrape official website.

        This will be called by Claude Code agent with WebFetch access.
        Returns structured data extracted from the website.

        Pages to fetch:
        1. Homepage (/) - name, description, type indicators
        2. Security/Features (/security, /features, /enterprise) - SSO, hosting
        3. Pricing (/pricing) - pricing model, SSO by plan
        4. About (/about) - history, aliases
        5. Changelog (/changelog, /updates) - SSO announcements
        """
        # This is a placeholder - the actual implementation will be done
        # by Claude Code agent calling WebFetch tool

        # Determine which URLs to fetch
        urls_to_fetch = []

        if initial_url:
            base_url = initial_url.rstrip('/')
            urls_to_fetch = [
                base_url,  # Homepage
                f"{base_url}/security",
                f"{base_url}/features",
                f"{base_url}/enterprise",
                f"{base_url}/pricing",
                f"{base_url}/about",
                f"{base_url}/changelog",
                f"{base_url}/updates",
                f"{base_url}/whats-new"
            ]

        return {
            "method": "webfetch",
            "urls_to_fetch": urls_to_fetch,
            "extraction_prompts": {
                "homepage": self._get_homepage_extraction_prompt(),
                "security": self._get_security_extraction_prompt(),
                "pricing": self._get_pricing_extraction_prompt(),
                "about": self._get_about_extraction_prompt(),
                "changelog": self._get_changelog_extraction_prompt()
            }
        }

    def _get_url_query(self, application_name: str, initial_url: str | None) -> str:
        """Get Perplexity query for URL research."""
        if initial_url:
            return f"""Verify that {initial_url} is the official website for {application_name}.
Check: HTTP status, SSL certificate, page content, 2+ authoritative sources.
Provide: verification status, confidence level, sources."""
        else:
            return f"""What is the official homepage URL for {application_name}?
Requirements: 2+ authoritative sources, accessible, SSL certificate, content verification.
Provide: URL, confidence level, sources list."""

    def _get_hosting_type_query(self, application_name: str) -> str:
        """Get Perplexity query for hosting type (with evaluation matrix)."""
        return f"""Determine hosting type for {application_name}: saas, paas, iaas, onPremise, hybrid, mobile.

CRITICAL: Complete evaluation matrix for ALL 6 types (score 0-5 each).
1. Check name for indicators
2. Identify primary user
3. Score all 6 hosting types
4. Research: security page, enterprise page, changelog
5. Apply decision logic

Provide: hostingType, matrix scores for all 6, primary user, reasoning, confidence, sources."""

    def _get_hosting_description_query(self, application_name: str) -> str:
        """Get Perplexity query for hosting description."""
        return f"""Provide technical reasoning for {application_name}'s hosting classification.

Format: "Classified as [type]: [specific technical details]"
Include: primary user, cloud provider (if known), deployment model
1-3 sentences, factual tone, 90% confidence threshold.

Anti-hallucination: Do NOT guess cloud provider or technical details.
Provide: hostingDescription, confidence, sources."""

    def _get_sso_status_query(self, application_name: str) -> str:
        """Get Perplexity query for SSO status (changelog emphasis)."""
        return f"""Does {application_name} support SSO? Answer: supported, notSupported, or not found.

Priority: CHECK CHANGELOG FIRST (/changelog, /updates, /releases) for SSO announcements.
Then check: security page, enterprise page, pricing page, integration directories.

Keywords: SSO, SAML, OAuth, OIDC, "single sign-on"

Decision: If found with evidence → supported. If explicitly states no → notSupported. If unclear → not found (blank).
Provide: ssoStatus, source (with date if from changelog), confidence, evidence."""

    def _get_pricing_query(self, application_name: str) -> str:
        """Get Perplexity query for pricing type."""
        return f"""Determine pricing model for {application_name}: free, freemium, subscription, perpetual, transaction, enterprise.

Primary source: /pricing page.
Types: free (no paid), freemium (free+paid), subscription (recurring), perpetual (one-time), transaction (per-use), enterprise (contact sales).
Provide: pricingType, evidence from pricing page, confidence, source."""

    def _get_category_query(self, application_name: str) -> str:
        """Get Perplexity query for product category."""
        return f"""Determine product category for {application_name}.

Identify PRIMARY functionality from official website.
Use most specific category (e.g., "Project Management" not "Collaboration").
Common categories: Collaboration, Project Management, CRM, Development Tools, Data Analytics, Security, etc.

Provide: primary functionality, suggested category, alternatives, confidence, source."""

    def _get_aliases_query(self, application_name: str) -> str:
        """Get Perplexity query for aliases."""
        return f"""Find verified aliases for {application_name}.

Types: abbreviations, former names, product variations, stylistic variations, acquisitions.
Sources: official website, Wikipedia, news articles, GitHub, app stores.

Only verified from official or 2+ authoritative sources. Do NOT fabricate.
Provide: comma-separated list or "No aliases found", sources."""

    def _get_subtype_query(self, application_name: str) -> str:
        """Get Perplexity query for subtype."""
        return f"""Determine subtype for {application_name}: "application" or "mobileApp".

mobileApp: Native mobile app for iOS/Android, mobile-first.
application: Web-based, desktop, APIs, platforms, or hybrid.

Examples: Instagram → mobileApp, Salesforce → application
Provide: subtype, evidence, confidence."""

    def _get_description_query(self, application_name: str) -> str:
        """Get Perplexity query for description (marketing language filter)."""
        return f"""Provide 30-90 word factual description of {application_name} from official website.

CRITICAL: Remove marketing language.
Avoid: "leading", "powerful", "innovative", "seamless", "transform", "empower", "enterprise-grade"
Use: "provides", "enables", "allows", "supports", "includes"

Focus on WHAT it does (functionality, features, users), not how good it is.
Word count: 30-90 exactly.

Provide: description (factual, no marketing buzzwords), word count, source, confidence."""

    def _get_homepage_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for homepage."""
        return """Extract from homepage:
1. Application name
2. Description (what it does)
3. Type indicators (mobile app, web app, platform, API)
4. Hosting indicators (cloud, SaaS, on-premise mentions)
5. Primary functionality
6. Target users"""

    def _get_security_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for security/features page."""
        return """Extract from security/features/enterprise page:
1. SSO support (SAML, OAuth, single sign-on mentions)
2. Hosting infrastructure (cloud provider, data centers)
3. Enterprise features
4. Authentication methods
5. Security certifications"""

    def _get_pricing_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for pricing page."""
        return """Extract from pricing page:
1. Pricing model (free, freemium, subscription, etc.)
2. Pricing tiers (plan names and prices)
3. Free tier availability
4. SSO availability by plan (which plans include SSO)
5. Feature comparison table"""

    def _get_about_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for about page."""
        return """Extract from about page:
1. Company/application history
2. Founding year
3. Former names or rebrands
4. Aliases or alternative names
5. Acquisition history
6. Mission/vision statement"""

    def _get_changelog_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for changelog/updates."""
        return """Extract from changelog/updates/releases page:
1. SSO feature announcements (SAML, OAuth support added)
2. Date of SSO announcement
3. Major feature releases
4. Hosting/infrastructure updates
5. Integration announcements"""

    def generate_research_summary(self, results: Dict[str, Any]) -> str:
        """Generate a summary of what was researched.

        Args:
            results: Results from research_all_fields

        Returns:
            Human-readable summary string
        """
        sources = results["metadata"]["sources_used"]
        application = results["metadata"]["application_name"]

        summary = f"Researched {application} using: {', '.join(sources)}\n"

        if "perplexity" in sources:
            summary += "- Perplexity: Web search with 11 field-specific queries\n"
        if "webfetch" in sources:
            summary += "- WebFetch: Direct website scraping (homepage, security, pricing, changelog)\n"

        summary += "\nFields researched:\n"
        summary += "  1. Webpage URL\n"
        summary += "  2. Hosting Type (with evaluation matrix)\n"
        summary += "  3. Hosting Description (technical reasoning)\n"
        summary += "  4. SSO Status (changelog checked)\n"
        summary += "  5. Pricing Type\n"
        summary += "  6. Product Category\n"
        summary += "  7. Aliases\n"
        summary += "  8. Subtype (application/mobileApp)\n"
        summary += "  9. Description (marketing language filtered)\n"
        summary += "  10-12. Fixed fields (collectionStatus, deprecated, asOfDate)\n"

        return summary
