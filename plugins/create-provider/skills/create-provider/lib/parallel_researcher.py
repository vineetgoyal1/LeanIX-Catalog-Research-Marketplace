"""Parallel research coordinator using both Perplexity and WebFetch.

This module orchestrates parallel research from multiple sources and
prepares data for cross-verification by the verification agent.
"""

import asyncio
from typing import Any, Dict, List
from datetime import datetime


class ParallelResearcher:
    """Coordinates parallel research from multiple sources."""

    def __init__(self):
        """Initialize parallel researcher."""
        pass

    async def research_all_fields(
        self,
        provider_name: str,
        initial_url: str | None = None
    ) -> Dict[str, Any]:
        """Research all provider fields in parallel using multiple sources.

        Args:
            provider_name: Name of the provider
            initial_url: Optional homepage URL if known

        Returns:
            Dictionary with results from each source:
            {
                "perplexity": {...},
                "webfetch": {...},
                "metadata": {
                    "provider_name": str,
                    "research_timestamp": str,
                    "sources_used": list
                }
            }
        """
        # Run all research tasks in parallel
        tasks = [
            self._research_via_perplexity(provider_name, initial_url),
            self._research_via_webfetch(provider_name, initial_url),
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
                "provider_name": provider_name,
                "initial_url": initial_url,
                "research_timestamp": datetime.now().isoformat(),
                "sources_used": sources_used
            }
        }

    async def _research_via_perplexity(
        self,
        provider_name: str,
        initial_url: str | None
    ) -> Dict[str, Any]:
        """Research using Perplexity MCP.

        This will be called by Claude Code agent with direct MCP access.
        Returns structured data for each field.
        """
        # This is a placeholder - the actual implementation will be done
        # by Claude Code agent calling Perplexity MCP tools
        return {
            "method": "perplexity_mcp",
            "queries": {
                "homepage_url": self._get_url_query(provider_name, initial_url),
                "category": self._get_category_query(provider_name),
                "aliases": self._get_aliases_query(provider_name),
                "headquarters": self._get_headquarters_query(provider_name),
                "description": self._get_description_query(provider_name)
            }
        }

    async def _research_via_webfetch(
        self,
        provider_name: str,
        initial_url: str | None
    ) -> Dict[str, Any]:
        """Research using WebFetch to scrape official website.

        This will be called by Claude Code agent with WebFetch access.
        Returns structured data extracted from the website.
        """
        # This is a placeholder - the actual implementation will be done
        # by Claude Code agent calling WebFetch tool

        # Determine which URLs to fetch
        urls_to_fetch = []

        if initial_url:
            urls_to_fetch.append(initial_url)
            urls_to_fetch.append(f"{initial_url.rstrip('/')}/about")
            urls_to_fetch.append(f"{initial_url.rstrip('/')}/contact")

        return {
            "method": "webfetch",
            "urls_to_fetch": urls_to_fetch,
            "extraction_prompts": {
                "homepage": self._get_homepage_extraction_prompt(),
                "about": self._get_about_extraction_prompt(),
                "contact": self._get_contact_extraction_prompt()
            }
        }

    def _get_url_query(self, provider_name: str, initial_url: str | None) -> str:
        """Get Perplexity query for URL research."""
        if initial_url:
            return f"""Verify that {initial_url} is the official website for {provider_name}.

Check:
1. HTTP status (should be 200, 301, or 302)
2. SSL certificate validity
3. Page content mentions {provider_name}
4. Found in 2+ authoritative sources (search engines, Wikipedia, Crunchbase, GitHub)

Provide: verification status, confidence level, sources, any alternative URLs found."""
        else:
            return f"""What is the official homepage URL for {provider_name}?

Requirements:
- Find URL from 2+ authoritative sources
- Verify it's accessible (HTTP 200/301/302)
- Confirm page content mentions {provider_name}
- Check SSL certificate

Provide: URL, confidence level (high/medium/low), sources list."""

    def _get_category_query(self, provider_name: str) -> str:
        """Get Perplexity query for category classification."""
        return f"""Classify {provider_name} into ONE category:

1. **individual**: Single person project with personal attribution
2. **enterprise**: Commercial company with business operations
3. **communityBased**: Open-source/foundation/collaborative

Decision tree (apply in order):
- Single named person with personal portfolio? → individual
- Commercial company with business operations? → enterprise
- Open-source project/foundation? → communityBased

Provide: category (exact lowercase), reasoning, confidence level, key evidence."""

    def _get_aliases_query(self, provider_name: str) -> str:
        """Get Perplexity query for aliases research."""
        return f"""Find verified aliases for {provider_name}. Include:

1. Abbreviations/acronyms
2. Former names (pre-rebrand)
3. Legal name vs brand name
4. Product names
5. Acquisition-related names
6. Stylistic variations

Sources: official website, LinkedIn, Crunchbase, Wikipedia, news articles.

Only verified aliases from credible sources. Do NOT fabricate.

Provide: comma-separated alias list or "No aliases found", sources for each."""

    def _get_headquarters_query(self, provider_name: str) -> str:
        """Get Perplexity query for headquarters research."""
        return f"""What is the headquarters address for {provider_name}?

Priority sources:
1. Official website (About, Contact, Footer, Legal/Imprint)
2. Business registries (SEC, Companies House)
3. LinkedIn, Crunchbase

Acceptable levels:
- Complete: building, street, city, postal, country (preferred)
- City-level: city, state, country (acceptable)
- Country-only: country (acceptable)

For individuals: ONLY city and country (privacy).

Do NOT fabricate. Provide partial if complete unavailable.

Provide: address (most complete available), address level, confidence, source."""

    def _get_description_query(self, provider_name: str) -> str:
        """Get Perplexity query for description."""
        return f"""Provide a 30-90 word description of {provider_name} from their official website.

Focus on:
- What they do (concrete functionality, not benefits)
- Main products/services (specific offerings)
- Target audience

Requirements:
- Extract from provider's own website
- Factual, objective tone - state WHAT it is/does, not how good it is
- NO marketing language: avoid "seamless", "enhance", "transform", "streamline", "empower", "revolutionary", "cutting-edge", "enterprise-grade", "best-in-class", "leading", "innovative", "powerful"
- Use neutral verbs: "provides", "offers", "includes", "supports", "allows", "enables" (when describing capability, not benefit)
- 30-90 words exactly

Example of marketing vs factual:
❌ "transforms business operations through seamless integration"
✅ "integrates with business tools to automate tasks"

If unavailable from official website, say "Description not available"."""

    def _get_homepage_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for homepage."""
        return """Extract from homepage:
1. Official company/product name
2. What they do (description)
3. Any aliases or alternative names
4. Company type indicators (enterprise/individual/community)
5. Any contact information or location data"""

    def _get_about_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for about page."""
        return """Extract from About page:
1. Company history
2. Founders or team information
3. Headquarters address or location
4. Former names or rebrands
5. Mission/vision/description
6. Company type (enterprise/startup/individual/community)"""

    def _get_contact_extraction_prompt(self) -> str:
        """Get WebFetch extraction prompt for contact page."""
        return """Extract from Contact page:
1. Physical address (building, street, city, state, postal, country)
2. City and country at minimum
3. Office locations
4. Contact email
5. Phone number"""

    def generate_research_summary(self, results: Dict[str, Any]) -> str:
        """Generate a summary of what was researched.

        Args:
            results: Results from research_all_fields

        Returns:
            Human-readable summary string
        """
        sources = results["metadata"]["sources_used"]
        provider = results["metadata"]["provider_name"]

        summary = f"Researched {provider} using: {', '.join(sources)}\n"

        if "perplexity" in sources:
            summary += "- Perplexity: Web search with citations\n"
        if "webfetch" in sources:
            summary += "- WebFetch: Direct website scraping\n"

        return summary
