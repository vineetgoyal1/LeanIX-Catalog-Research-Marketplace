"""Verification agent for cross-checking data from multiple sources.

This module implements the verification logic that compares results from
Perplexity and WebFetch to identify the most accurate data.
"""

from typing import Any, Dict, List, Tuple


class VerificationAgent:
    """Agent that verifies and cross-checks research data from multiple sources."""

    def __init__(self):
        """Initialize verification agent."""
        self.confidence_threshold = 0.7  # Minimum confidence to accept data

    def verify_and_merge(
        self,
        parallel_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cross-verify data from multiple sources and merge into final dataset.

        Args:
            parallel_results: Results from ParallelResearcher with perplexity and webfetch data

        Returns:
            Dictionary with verified data and verification metadata:
            {
                "verified_data": {
                    "homePageUrl": {...},
                    "providerCategory": {...},
                    "aliases": {...},
                    "headquartersAddress": {...},
                    "description": {...}
                },
                "verification_metadata": {
                    "conflicts": [...],
                    "confidence_scores": {...},
                    "resolution_notes": [...]
                }
            }
        """
        # This method generates verification queries for the agent to execute
        # The agent will call Perplexity to cross-check conflicting data

        return {
            "verification_strategy": self._build_verification_strategy(parallel_results),
            "field_comparisons": self._identify_field_comparisons(parallel_results)
        }

    def _build_verification_strategy(self, results: Dict[str, Any]) -> Dict[str, str]:
        """Build verification queries for cross-checking.

        Returns queries that an agent should execute to verify conflicts.
        """
        perplexity_data = results.get("perplexity", {})
        webfetch_data = results.get("webfetch", {})

        return {
            "homepage_url": self._get_url_verification_query(perplexity_data, webfetch_data),
            "category": self._get_category_verification_query(perplexity_data, webfetch_data),
            "aliases": self._get_aliases_verification_query(perplexity_data, webfetch_data),
            "headquarters": self._get_headquarters_verification_query(perplexity_data, webfetch_data),
            "description": self._get_description_verification_query(perplexity_data, webfetch_data)
        }

    def _identify_field_comparisons(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Identify which fields need comparison and conflict resolution."""
        return {
            "fields_to_compare": [
                "homePageUrl",
                "providerCategory",
                "aliases",
                "headquartersAddress",
                "description"
            ],
            "comparison_rules": {
                "homePageUrl": "prefer_source_with_http_validation",
                "providerCategory": "prefer_perplexity_with_reasoning",
                "aliases": "merge_unique_from_both_sources",
                "headquartersAddress": "prefer_most_complete_address",
                "description": "prefer_official_website_extraction"
            }
        }

    def _get_url_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify URL conflicts."""
        return """Compare these URL findings:
- Perplexity result: [will be filled by agent]
- WebFetch result: [will be filled by agent]

Verify:
1. Which URL actually returns HTTP 200?
2. Which URL is mentioned on official sources?
3. Are they the same domain or different?
4. Which is the canonical homepage?

Provide: final verified URL, confidence level, reasoning."""

    def _get_category_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify category conflicts."""
        return """Compare category classifications:
- Perplexity classification: [will be filled by agent]
- WebFetch classification: [will be filled by agent]

Apply decision tree strictly:
1. Single named person? → individual
2. Commercial company? → enterprise
3. Open-source/community? → communityBased

Which classification is correct based on evidence?

Provide: final category (lowercase), confidence level, reasoning."""

    def _get_aliases_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify aliases conflicts."""
        return """Compare alias findings:
- Perplexity aliases: [will be filled by agent]
- WebFetch aliases: [will be filled by agent]

Cross-check:
1. Which aliases can be verified from official sources?
2. Are there any fabricated/unverifiable aliases?
3. Should aliases be merged or is one source more accurate?

Provide: final verified alias list (comma-separated), confidence level."""

    def _get_headquarters_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify headquarters conflicts."""
        return """Compare headquarters findings:
- Perplexity address: [will be filled by agent]
- WebFetch address: [will be filled by agent]

Determine:
1. Which address is more complete?
2. Which came from official source (company website)?
3. Do they conflict or complement each other?
4. What's the most accurate address level (complete/city/country)?

Provide: final verified address, address level, confidence level."""

    def _get_description_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify description conflicts."""
        return """Compare descriptions:
- Perplexity description: [will be filled by agent]
- WebFetch description: [will be filled by agent]

Evaluate:
1. Which is 30-90 words?
2. Which came from official website?
3. Which is more accurate/factual?
4. Should they be merged or is one clearly better?

Provide: final description (30-90 words), confidence level."""

    def generate_verification_report(
        self,
        parallel_results: Dict[str, Any],
        verified_data: Dict[str, Any]
    ) -> str:
        """Generate human-readable verification report.

        Args:
            parallel_results: Original research results
            verified_data: Final verified data after cross-checking

        Returns:
            Formatted report string
        """
        report = "=== VERIFICATION REPORT ===\n\n"

        sources = parallel_results["metadata"]["sources_used"]
        report += f"Sources: {', '.join(sources)}\n\n"

        report += "Field-by-Field Verification:\n"

        fields = [
            ("Homepage URL", "homePageUrl"),
            ("Category", "providerCategory"),
            ("Aliases", "aliases"),
            ("Headquarters", "headquartersAddress"),
            ("Description", "description")
        ]

        for field_name, field_key in fields:
            report += f"\n{field_name}:\n"
            report += f"  - Verified: {verified_data.get(field_key, {}).get('value', 'N/A')}\n"
            report += f"  - Confidence: {verified_data.get(field_key, {}).get('confidence', 'N/A')}\n"
            report += f"  - Source: {verified_data.get(field_key, {}).get('source', 'N/A')}\n"

        return report

    def calculate_overall_confidence(self, verified_data: Dict[str, Any]) -> float:
        """Calculate overall confidence score for all verified data.

        Args:
            verified_data: Dictionary with verified field data

        Returns:
            Overall confidence score (0.0 to 1.0)
        """
        confidence_scores = []

        for field_data in verified_data.values():
            if isinstance(field_data, dict) and "confidence" in field_data:
                conf_str = field_data["confidence"]
                # Convert to numeric
                if conf_str == "high":
                    confidence_scores.append(0.9)
                elif conf_str == "medium":
                    confidence_scores.append(0.7)
                elif conf_str == "low":
                    confidence_scores.append(0.5)

        if not confidence_scores:
            return 0.0

        return sum(confidence_scores) / len(confidence_scores)

    def identify_conflicts(
        self,
        perplexity_data: Dict[str, Any],
        webfetch_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Identify conflicts between sources that need resolution.

        Args:
            perplexity_data: Data from Perplexity
            webfetch_data: Data from WebFetch

        Returns:
            List of conflict descriptions
        """
        conflicts = []

        # This will be filled in by the agent during execution
        # The agent will compare actual values and identify differences

        return conflicts

    def get_resolution_strategy(self, conflict_type: str) -> str:
        """Get strategy for resolving a specific type of conflict.

        Args:
            conflict_type: Type of conflict (url_mismatch, category_mismatch, etc.)

        Returns:
            Strategy description
        """
        strategies = {
            "url_mismatch": "Verify HTTP status for both URLs, prefer one that returns 200 and is cited in more sources",
            "category_mismatch": "Re-apply decision tree with evidence from both sources, prefer classification with stronger indicators",
            "aliases_different": "Merge unique aliases from both sources, verify each from official sources",
            "address_mismatch": "Prefer more complete address, verify from official website first",
            "description_mismatch": "Prefer description from official website (WebFetch), ensure 30-90 words"
        }

        return strategies.get(conflict_type, "Manual review required")
