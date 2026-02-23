"""Provider research logic using Perplexity MCP for field-specific research.

This module implements research logic following the provider guidelines.
It's designed to be used by Claude Code agents with direct MCP access.
"""

from pathlib import Path
from typing import Any


class ProviderResearcher:
    """Implements field-specific research logic following guidelines.

    This class is designed to work with Claude Code agents that have
    direct access to Perplexity MCP tools (mcp__perplexity__perplexity_search).
    """

    def __init__(self):
        """Initialize researcher with guidelines directory path."""
        self.guidelines_dir = Path(__file__).parent.parent / "guidelines"

    def get_url_research_query(
        self,
        provider_name: str,
        initial_url: str | None = None
    ) -> str:
        """Generate Perplexity query for URL research.

        Follows Provider_URL_Validation_Guidelines.md

        Args:
            provider_name: Name of the provider
            initial_url: Optional URL to validate (if provided by user)

        Returns:
            Query string for Perplexity
        """
        if initial_url:
            # Validate the provided URL
            return f"""Verify that {initial_url} is the official website for {provider_name}.

Check the following:
1. Does the URL return HTTP 200 or redirect 301/302?
2. Does the page content mention {provider_name}?
3. Does it have a valid SSL certificate?
4. Can you find this URL in at least 2 authoritative sources (search engines, Wikipedia, GitHub, Crunchbase)?

Provide your assessment with confidence level (high/medium/low) and list the sources where you found this URL.

If the URL is not valid or you cannot verify it, suggest the correct official website if you can find one.

IMPORTANT: Do NOT hallucinate or guess. If you cannot verify the URL, say so clearly."""

        else:
            # Search for the official URL
            return f"""What is the official website homepage URL for {provider_name}?

Requirements:
1. Find the URL from at least 2 authoritative sources (official website listings, Wikipedia, GitHub README, Crunchbase, npm, PyPI)
2. Verify the URL is accessible (returns HTTP 200 or redirect 301/302)
3. Verify the page content actually mentions {provider_name}
4. Confirm it has a valid SSL certificate

Provide:
- The verified URL
- Confidence level (high if 3+ sources, medium if 2 sources, low if only 1 source)
- List of sources where you found this URL
- HTTP status code if you can check it

IMPORTANT: Do NOT hallucinate or guess URLs. If you cannot find a verified URL from authoritative sources, say "URL not found" rather than guessing."""

    def get_aliases_research_query(self, provider_name: str) -> str:
        """Generate Perplexity query for alias research.

        Follows Provider_Alias_Discovery_Guidelines.md (7 alias types)

        Args:
            provider_name: Name of the provider

        Returns:
            Query string for Perplexity
        """
        return f"""Find all known aliases and alternative names for {provider_name}.

Look for these 7 types of aliases:
1. Abbreviations/Acronyms (2-5 character shortened forms)
2. Former Names (names before rebranding)
3. Legal Name vs Brand Name (registered entity vs marketing name)
4. Product Names vs Company Names (if known by product not company)
5. Acquisition-Related Names (names changed after mergers/acquisitions)
6. Stylistic Variations (different formatting, spacing, capitalization)
7. Multiple Aliases (combined from different contexts)

Search in:
- Official website (About Us, company history, press releases)
- LinkedIn, Crunchbase, Wikipedia
- News articles about rebrands or acquisitions
- Business registries for legal names

Requirements:
- Only include verified aliases from official sources or 2+ authoritative sources
- Do NOT include: competitor names, partner companies, customer references, generic terms, speculation
- For each alias, note the source and type

Provide the aliases as a comma-separated list, or say "No aliases found" if none exist.

IMPORTANT: Do NOT fabricate aliases. Only document names you can verify from credible sources."""

    def get_headquarters_research_query(self, provider_name: str) -> str:
        """Generate Perplexity query for headquarters address research.

        Follows Provider_Headquarters_Address_Guidelines.md

        Args:
            provider_name: Name of the provider

        Returns:
            Query string for Perplexity
        """
        return f"""What is the headquarters address for {provider_name}?

Search priority (in order):
1. Official website (About Us, Contact Us, Footer, Legal/Imprint, Locations)
2. Business registries (SEC filings, Companies House, local registries)
3. Professional networks (LinkedIn company page, Crunchbase)
4. News articles or press releases

Acceptable address levels (provide the most complete available):
1. Complete: Building name/number, street address, city, postal code, country
2. City-level: City, state/province, country
3. State-level: State/province, country
4. Country-only: Country

Address format guidelines:
- US/Canada: [Suite], [Street Number Street], [City], [State] [Postal], [Country]
- European: [Company], [Street Number], [Postal Code] [City], [Country]
- UK: [Building], [Street Number] [Street], [City], [Postal Code], [Country]
- Asian: [Building/Floor], [Street], [District], [City] [Postal Code], [Country]

Special considerations:
- For individual developers: ONLY provide city and country (privacy)
- Accept partial information rather than guessing
- Note if company is distributed/remote-first (no physical HQ)
- Indicate confidence level and source

IMPORTANT: Do NOT fabricate addresses. If you can only find partial information (e.g., just city and country), provide that. Return "Address not found" rather than guessing."""

    def get_category_research_query(self, provider_name: str) -> str:
        """Generate Perplexity query for provider category classification.

        Follows Provider_Classification_Definitions.md
        Decision tree: Individual → Enterprise → Community Based

        Args:
            provider_name: Name of the provider

        Returns:
            Query string for Perplexity
        """
        return f"""Analyze {provider_name} and classify it into exactly ONE of these three categories:

1. **Individual**: Single person project with personal attribution
   Indicators: Personal name, personal website/blog, GitHub profile, single maintainer, personal LinkedIn, phrases like "developed by [Person Name]"

2. **Enterprise**: Commercial company with business operations
   Indicators: Company website, "About Us" with employees/founders, pricing pages, business registration, corporate structure, terms of service, customer support channels

3. **Community Based**: Open-source project, foundation, or collaborative initiative
   Indicators: Open-source licenses, GitHub with multiple contributors, foundation backing (Apache, Linux, etc.), community forums, "open-source project" language, collaborative governance

**Decision tree (apply in exact order):**
Step 1: Is it a single named person with personal portfolio? → If YES: "individual"
Step 2: Is it a commercial company with business operations? → If YES: "enterprise"
Step 3: Is it an open-source project/foundation/community? → If YES: "communityBased"

Provide:
- Classification: individual, enterprise, or communityBased (use exact lowercase values)
- Reasoning: Explain which indicators you found
- Confidence: high/medium/low
- Key evidence: List specific facts that support your classification

Research from official website, GitHub, LinkedIn, Crunchbase, Wikipedia, news articles.

IMPORTANT: Choose exactly ONE category based on the decision tree order."""

    def get_description_research_query(self, provider_name: str) -> str:
        """Generate Perplexity query for provider description.

        Requirement: 30-90 words from provider's own website

        Args:
            provider_name: Name of the provider

        Returns:
            Query string for Perplexity
        """
        return f"""Provide a 30-90 word description of {provider_name} based on their official website.

Requirements:
- Extract description from the provider's own website (About Us, homepage, main product page)
- Focus on: What the provider does, main products/services, target audience
- Use factual, objective tone
- Do NOT use marketing fluff or superlatives
- Must be 30-90 words (count the words)

Format: Just provide the description text, nothing else.

If you cannot find information on their official website, say "Description not available" rather than making something up.

IMPORTANT: Extract directly from the provider's own description. Do NOT generate marketing copy."""

    def parse_url_response(self, response: str) -> dict[str, Any]:
        """Parse Perplexity response for URL research.

        Args:
            response: Response from Perplexity

        Returns:
            Dictionary with url, confidence, sources, status_code
        """
        # This is a helper for the agent to structure the response
        # The agent will need to parse the Perplexity response
        return {
            "url": None,  # Extract from response
            "confidence": "low",  # Extract from response
            "sources": [],  # Extract from response
            "status_code": None,  # Extract from response
        }

    def parse_aliases_response(self, response: str) -> dict[str, Any]:
        """Parse Perplexity response for aliases research.

        Args:
            response: Response from Perplexity

        Returns:
            Dictionary with aliases_string, aliases_list, sources
        """
        return {
            "aliases_string": "",  # Comma-separated
            "aliases_list": [],  # List of strings
            "sources": [],  # Extract from response
        }

    def parse_headquarters_response(self, response: str) -> dict[str, Any]:
        """Parse Perplexity response for headquarters research.

        Args:
            response: Response from Perplexity

        Returns:
            Dictionary with address, address_level, confidence, source
        """
        return {
            "address": "",  # Formatted address
            "address_level": "none",  # complete|city|state|country|none
            "confidence": "low",  # high|medium|low
            "source": "",  # Source of information
        }

    def parse_category_response(self, response: str) -> dict[str, Any]:
        """Parse Perplexity response for category classification.

        Args:
            response: Response from Perplexity

        Returns:
            Dictionary with category, reasoning, confidence
        """
        return {
            "category": "enterprise",  # enterprise|individual|communityBased
            "reasoning": "",  # Extract from response
            "confidence": "low",  # high|medium|low
        }

    def parse_description_response(self, response: str) -> dict[str, Any]:
        """Parse Perplexity response for description.

        Args:
            response: Response from Perplexity

        Returns:
            Dictionary with description, word_count, source
        """
        return {
            "description": "",  # Extract from response
            "word_count": 0,  # Count words
            "source": "official_website",
        }
