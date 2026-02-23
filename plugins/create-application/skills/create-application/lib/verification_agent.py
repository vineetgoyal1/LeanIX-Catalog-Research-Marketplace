"""Verification agent for cross-checking Application data from multiple sources.

This module implements the verification logic that compares results from
Perplexity and WebFetch to identify the most accurate data.
"""

from typing import Any, Dict, List


class VerificationAgent:
    """Agent that verifies and cross-checks application research data from multiple sources."""

    def __init__(self):
        """Initialize verification agent."""
        self.confidence_threshold = 0.7  # Minimum confidence to accept data
        self.marketing_buzzwords = [
            "leading", "powerful", "innovative", "cutting-edge", "revolutionary",
            "seamless", "transform", "empower", "streamline", "enhance",
            "enterprise-grade", "best-in-class", "world-class", "industry-leading",
            "award-winning", "groundbreaking", "game-changing", "next-generation"
        ]

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
                    "webpageUrl": {...},
                    "hostingType": {...},
                    "hostingDescription": {...},
                    "ssoStatus": {...},
                    "pricingType": {...},
                    "productCategory": {...},
                    "alias": {...},
                    "type": {...},
                    "description": {...},
                    "collectionStatus": {...},
                    "deprecated": {...},
                    "asOfDate": {...}
                },
                "verification_metadata": {
                    "overall_confidence": float,
                    "conflicts_resolved": int,
                    "conflicts_unresolved": int,
                    "fields_with_high_confidence": int,
                    "fields_with_medium_confidence": int
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
        """Build verification queries for cross-checking Application fields.

        Returns queries that an agent should execute to verify conflicts.
        """
        perplexity_data = results.get("perplexity", {})
        webfetch_data = results.get("webfetch", {})

        return {
            "webpage_url": self._get_url_verification_query(perplexity_data, webfetch_data),
            "hosting_type": self._get_hosting_type_verification_query(perplexity_data, webfetch_data),
            "hosting_description": self._get_hosting_description_verification_query(perplexity_data, webfetch_data),
            "sso_status": self._get_sso_verification_query(perplexity_data, webfetch_data),
            "pricing_type": self._get_pricing_verification_query(perplexity_data, webfetch_data),
            "product_category": self._get_category_verification_query(perplexity_data, webfetch_data),
            "aliases": self._get_aliases_verification_query(perplexity_data, webfetch_data),
            "subtype": self._get_subtype_verification_query(perplexity_data, webfetch_data),
            "description": self._get_description_verification_query(perplexity_data, webfetch_data)
        }

    def _identify_field_comparisons(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Identify which fields need comparison and conflict resolution for Applications."""
        return {
            "fields_to_compare": [
                "webpageUrl",
                "hostingType",
                "hostingDescription",
                "ssoStatus",
                "pricingType",
                "productCategory",
                "alias",
                "type",
                "description"
            ],
            "fixed_fields": [
                "collectionStatus",  # Always "inReview"
                "deprecated",  # Always "no"
                "asOfDate"  # Always current date
            ],
            "comparison_rules": {
                "webpageUrl": "prefer_source_with_http_validation",
                "hostingType": "prefer_source_with_evaluation_matrix",
                "hostingDescription": "prefer_perplexity_with_90_percent_confidence",
                "ssoStatus": "prefer_changelog_source",
                "pricingType": "prefer_pricing_page_source",
                "productCategory": "prefer_most_specific_category",
                "alias": "merge_unique_from_both_sources",
                "type": "prefer_both_agree",
                "description": "prefer_factual_over_marketing"
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
1. Which URL returns HTTP 200?
2. Which is mentioned on official sources?
3. Are they the same domain or different?
4. Which is the canonical homepage?

Provide: final verified URL, confidence level, reasoning."""

    def _get_hosting_type_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify hosting type conflicts (requires evaluation matrix)."""
        return """Compare hosting type classifications:
- Perplexity classification: [will be filled by agent]
- WebFetch classification: [will be filled by agent]

Verify:
1. Did Perplexity complete evaluation matrix for all 6 types?
2. Does WebFetch evidence support the classification?
3. What is the primary user (business users, developers, IT teams)?
4. Does the name indicate hosting type?

If conflict exists:
- Complete evaluation matrix if not done
- Apply primary user test
- Check official sources (security page, enterprise page)

Provide: final hostingType, matrix scores, primary user, reasoning, confidence."""

    def _get_hosting_description_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify hosting description (technical reasoning)."""
        return """Compare hosting descriptions:
- Perplexity description: [will be filled by agent]
- WebFetch description: [will be filled by agent]

Evaluate:
1. Which has higher confidence (≥90%)?
2. Which includes specific technical details (cloud provider, deployment model)?
3. Which avoids hallucination (does NOT guess cloud provider)?
4. Format: "Classified as [type]: [technical details]"

Anti-hallucination check:
- Is cloud provider explicitly stated or guessed?
- Are technical details verified or inferred?

Provide: final hostingDescription (1-3 sentences), confidence, sources."""

    def _get_sso_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify SSO status (changelog emphasis)."""
        return """Compare SSO status findings:
- Perplexity result: [will be filled by agent]
- WebFetch result: [will be filled by agent]

Verify:
1. Did either check changelog/updates page? (critical source)
2. Is there explicit evidence of SSO support (SAML, OAuth mentions)?
3. Is SSO found in security page, enterprise page, or pricing page?
4. If conflict: which source has stronger evidence?

Decision:
- Both agree → use agreed value
- Changelog found SSO → prefer that (strongest evidence)
- Only one found evidence → use that if credible
- No clear evidence → leave blank (acceptable)

Provide: final ssoStatus (supported/notSupported/blank), source (with date if changelog), confidence."""

    def _get_pricing_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify pricing type."""
        return """Compare pricing type findings:
- Perplexity result: [will be filled by agent]
- WebFetch result: [will be filled by agent]

Verify:
1. Which came from actual pricing page?
2. Is there a free tier + paid tiers? → freemium
3. Only paid tiers with recurring? → subscription
4. Contact sales only? → enterprise
5. Per-transaction/usage? → transaction

Prefer source that scraped /pricing page directly.

Provide: final pricingType, evidence from pricing page, confidence."""

    def _get_category_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify product category (prefer most specific)."""
        return """Compare product category findings:
- Perplexity category: [will be filled by agent]
- WebFetch category: [will be filled by agent]

Evaluate:
1. Which is more specific? (e.g., "Project Management" > "Collaboration")
2. Which better describes PRIMARY functionality?
3. Do they conflict or is one a subcategory of the other?

Rule: Use most specific category that accurately describes primary function.

Verify against Product_Category_Reference.json for valid category names.

Provide: final productCategory, reasoning (why more specific), confidence."""

    def _get_aliases_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify aliases (merge unique)."""
        return """Compare alias findings:
- Perplexity aliases: [will be filled by agent]
- WebFetch aliases: [will be filled by agent]

Cross-check:
1. Which aliases can be verified from official sources?
2. Any fabricated/unverifiable aliases?
3. Any duplicates between sources?

Merge unique verified aliases from both sources.

Provide: final comma-separated alias list, sources for each, confidence."""

    def _get_subtype_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify subtype (application vs mobileApp)."""
        return """Compare subtype findings:
- Perplexity subtype: [will be filled by agent]
- WebFetch subtype: [will be filled by agent]

Verify:
1. Is it PRIMARILY a native mobile app (App Store/Google Play)?
2. Or is it web-based/desktop/platform?
3. If hybrid (web + mobile), default to "application"

Examples:
- Instagram → mobileApp (mobile-first native)
- Salesforce → application (web-based with mobile apps)

Provide: final subtype (application or mobileApp), evidence, confidence."""

    def _get_description_verification_query(
        self,
        perplexity_data: Dict,
        webfetch_data: Dict
    ) -> str:
        """Generate query to verify description (marketing language filter critical)."""
        return """Compare descriptions:
- Perplexity description: [will be filled by agent]
- WebFetch description: [will be filled by agent]

**CRITICAL: Marketing language filter**

Check BOTH descriptions for marketing buzzwords:
- "leading", "powerful", "innovative", "cutting-edge", "revolutionary"
- "seamless", "transform", "empower", "streamline", "enhance"
- "enterprise-grade", "best-in-class", "world-class"

Evaluate:
1. Which is 30-90 words?
2. Which is more factual (states WHAT it does, not how good)?
3. Which has fewer/no marketing buzzwords?
4. Which came from official website?

If BOTH have marketing language:
- Rewrite to factual alternative
- Replace buzzwords with neutral verbs: "provides", "enables", "allows", "supports"

Examples:
❌ "transforms operations through seamless integration"
✅ "integrates with business tools to automate workflows"

Provide: final description (30-90 words, factual, NO marketing buzzwords), word count, confidence."""

    def detect_marketing_language(self, text: str) -> List[str]:
        """Detect marketing buzzwords in text.

        Args:
            text: Text to check for marketing language

        Returns:
            List of detected buzzwords
        """
        detected = []
        text_lower = text.lower()
        for buzzword in self.marketing_buzzwords:
            if buzzword.lower() in text_lower:
                detected.append(buzzword)
        return detected

    def remove_marketing_language(self, text: str) -> str:
        """Remove or replace marketing language with factual alternatives.

        Args:
            text: Text to clean

        Returns:
            Text with marketing language replaced
        """
        # This is a helper that provides guidance
        # The agent will need to rewrite based on context
        marketing_replacements = {
            "transforms": "automates",
            "empowers": "enables",
            "seamless integration": "integrates with",
            "powerful": "",  # Remove, use specific capability instead
            "leading": "",  # Remove
            "innovative": "",  # Remove
            "cutting-edge": "",  # Remove
            "revolutionary": "",  # Remove
            "enterprise-grade": "",  # Remove
            "best-in-class": "",  # Remove
        }

        cleaned = text
        for marketing, replacement in marketing_replacements.items():
            cleaned = cleaned.replace(marketing, replacement)

        return cleaned

    def generate_verification_report(
        self,
        parallel_results: Dict[str, Any],
        verified_data: Dict[str, Any]
    ) -> str:
        """Generate human-readable verification report for Application.

        Args:
            parallel_results: Original research results
            verified_data: Final verified data after cross-checking

        Returns:
            Formatted report string
        """
        report = "=== APPLICATION VERIFICATION REPORT ===\n\n"

        sources = parallel_results["metadata"]["sources_used"]
        report += f"Sources: {', '.join(sources)}\n\n"

        report += "Field-by-Field Verification:\n"

        fields = [
            ("Webpage URL", "webpageUrl"),
            ("Hosting Type", "hostingType"),
            ("Hosting Description", "hostingDescription"),
            ("SSO Status", "ssoStatus"),
            ("Pricing Type", "pricingType"),
            ("Product Category", "productCategory"),
            ("Aliases", "alias"),
            ("Subtype", "type"),
            ("Description", "description"),
            ("Collection Status", "collectionStatus"),
            ("Deprecated", "deprecated"),
            ("As-of Date", "asOfDate")
        ]

        for field_name, field_key in fields:
            report += f"\n{field_name}:\n"
            field_data = verified_data.get(field_key, {})
            value = field_data.get('value', 'N/A')
            confidence = field_data.get('confidence', 'N/A')
            source = field_data.get('source', 'N/A')

            report += f"  - Value: {value}\n"
            report += f"  - Confidence: {confidence}\n"
            report += f"  - Source: {source}\n"

            # Show marketing language check for description
            if field_key == "description" and isinstance(value, str):
                buzzwords = self.detect_marketing_language(value)
                if buzzwords:
                    report += f"  - ⚠ Marketing buzzwords detected: {', '.join(buzzwords)}\n"
                else:
                    report += f"  - ✓ No marketing language detected\n"

        return report

    def calculate_overall_confidence(self, verified_data: Dict[str, Any]) -> float:
        """Calculate overall confidence score for all verified Application data.

        Args:
            verified_data: Dictionary with verified field data

        Returns:
            Overall confidence score (0.0 to 1.0)
        """
        confidence_scores = []

        for field_key, field_data in verified_data.items():
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
        """Get strategy for resolving a specific type of Application conflict.

        Args:
            conflict_type: Type of conflict

        Returns:
            Strategy description
        """
        strategies = {
            "url_mismatch": "Verify HTTP status for both URLs, prefer one that returns 200 and is cited in more sources",
            "hosting_type_mismatch": "Complete evaluation matrix if not done, apply primary user test, verify from official sources",
            "hosting_description_conflict": "Prefer description with ≥90% confidence, avoid hallucination, verify technical details",
            "sso_mismatch": "Prefer changelog source (strongest evidence), then security/enterprise pages, blank if unclear",
            "pricing_mismatch": "Prefer source that scraped /pricing page, verify from actual pricing tiers",
            "category_mismatch": "Use most specific category, verify against Product_Category_Reference.json",
            "aliases_different": "Merge unique aliases from both sources, verify each from official sources",
            "subtype_mismatch": "Check if PRIMARILY native mobile (App Store/Google Play), default to application if hybrid",
            "description_mismatch": "Apply marketing language filter to BOTH, prefer factual over marketing, ensure 30-90 words"
        }

        return strategies.get(conflict_type, "Manual review required")
