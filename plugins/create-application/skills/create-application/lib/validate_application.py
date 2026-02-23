#!/usr/bin/env python3
"""
Validate Application fact sheet creation was done correctly.
Run after creating fact sheet to verify compliance with workflow.

Usage:
    python validate_application.py --checklist EXECUTION_CHECKLIST.md --fields final_fields.json
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path


# Marketing buzzwords that should not appear in descriptions
MARKETING_BUZZWORDS = [
    'leading', 'powerful', 'innovative', 'cutting-edge', 'revolutionary',
    'seamless', 'transform', 'empower', 'streamline', 'enhance',
    'enterprise-grade', 'best-in-class', 'world-class', 'industry-leading',
    'award-winning', 'groundbreaking', 'game-changing', 'next-generation'
]


def validate_field_values(fields):
    """Validate that field values meet requirements."""
    errors = []
    warnings = []

    # Required fields
    required = ['webpageUrl', 'description', 'hostingType', 'category',
                'collectionStatus', 'asOfDate', 'deprecated']
    for field in required:
        if field not in fields or not fields[field]:
            errors.append(f"❌ Missing required field: {field}")

    # Category must be "businessApplication"
    if fields.get('category') != 'businessApplication':
        errors.append(f'❌ category must be "businessApplication", got: {fields.get("category")}')

    # Deprecated must be "No" (capital N)
    if 'deprecated' in fields:
        if fields['deprecated'] == 'no':
            errors.append('❌ deprecated must be "No" (capital N), not "no"')
        elif fields['deprecated'] != 'No':
            errors.append(f'❌ deprecated must be "No", got: {fields.get("deprecated")}')

    # CollectionStatus must be "inReview"
    if fields.get('collectionStatus') != 'inReview':
        errors.append(f'❌ collectionStatus must be "inReview", got: {fields.get("collectionStatus")}')

    # Description length check
    desc = fields.get('description', '')
    word_count = len(desc.split())
    if word_count < 30:
        errors.append(f"❌ Description must be at least 30 words, got {word_count}")
    elif word_count > 90:
        errors.append(f"❌ Description must be at most 90 words, got {word_count}")
    else:
        print(f"✓ Description word count: {word_count} (within 30-90 range)")

    # Marketing buzzwords check
    desc_lower = desc.lower()
    found_buzzwords = [b for b in MARKETING_BUZZWORDS if b in desc_lower]
    if found_buzzwords:
        errors.append(f"❌ Description contains marketing buzzwords: {', '.join(found_buzzwords)}")
        errors.append("   These must be removed or rewritten to factual language")
    else:
        print(f"✓ No marketing buzzwords found in description")

    # SI ID check
    if not fields.get('siId'):
        warnings.append("⚠️  siId not set (may need manual update via LeanIX UI)")
    else:
        si_id = fields['siId']
        if ' ' in si_id:
            errors.append(f"❌ siId contains spaces: '{si_id}' (should be no spaces)")
        if len(si_id) > 60:
            errors.append(f"❌ siId too long: {len(si_id)} characters (max 60)")
        else:
            print(f"✓ SI ID: {si_id}")

    # Hosting description must start with "Classified as"
    hosting_desc = fields.get('hostingDescription', '')
    if hosting_desc:
        if not hosting_desc.startswith('Classified as'):
            warnings.append('⚠️  hostingDescription should start with "Classified as [type]:"')
        else:
            print(f"✓ Hosting description follows format")

    # Hosting type must be valid enum
    valid_hosting_types = ['saas', 'paas', 'iaas', 'onPremise', 'hybrid', 'mobile']
    if fields.get('hostingType') not in valid_hosting_types:
        errors.append(f"❌ Invalid hostingType: {fields.get('hostingType')}")
        errors.append(f"   Valid values: {', '.join(valid_hosting_types)}")
    else:
        print(f"✓ Hosting type: {fields['hostingType']}")

    # As-of date validation
    as_of_date = fields.get('asOfDate')
    if as_of_date:
        try:
            date_obj = datetime.strptime(as_of_date, '%Y-%m-%d')
            days_old = (datetime.now() - date_obj).days
            if days_old > 30:
                warnings.append(f"⚠️  asOfDate is {days_old} days old (should be recent)")
            elif days_old < 0:
                errors.append(f"❌ asOfDate is in the future: {as_of_date}")
            else:
                print(f"✓ As-of date: {as_of_date} ({days_old} days old)")
        except ValueError:
            errors.append(f"❌ asOfDate invalid format: {as_of_date} (should be YYYY-MM-DD)")

    # URL validation
    webpage_url = fields.get('webpageUrl', '')
    if webpage_url:
        if not webpage_url.startswith('http'):
            errors.append(f"❌ webpageUrl must start with http:// or https://: {webpage_url}")
        else:
            print(f"✓ Webpage URL: {webpage_url}")

    return errors, warnings


def check_matrix_completed(checklist_content):
    """Verify hosting type evaluation matrix was completed."""
    errors = []
    warnings = []

    # Check if all 6 types have scores filled in
    hosting_types = ['SaaS', 'PaaS', 'IaaS', 'On-Premise', 'Hybrid', 'Mobile']

    for hosting_type in hosting_types:
        # Look for pattern: | Type | ___/10 | which means not filled
        if f'| **{hosting_type}** | ___/10 |' in checklist_content:
            errors.append(f"❌ Hosting type '{hosting_type}' not scored in evaluation matrix")

    # Check if decision section is filled
    if 'Selected Hosting Type**: _____' in checklist_content:
        errors.append("❌ Selected hosting type not filled in checklist")

    if 'Confidence Level**: _____%' in checklist_content:
        errors.append("❌ Confidence level not filled in checklist")

    if not errors:
        print("✓ Hosting type evaluation matrix completed")

    return errors, warnings


def check_sso_research(checklist_content):
    """Verify SSO research was exhaustive."""
    warnings = []

    # Check if SSO research section was filled
    if '**URLs/Sources Attempted**:' in checklist_content:
        # Count how many SSO sources were checked
        sso_section = checklist_content.split('**URLs/Sources Attempted**:')[1].split('**SSO Status Decision**:')[0]

        checked_count = sso_section.count('[x]') + sso_section.count('[X]')

        if checked_count < 5:
            warnings.append(f"⚠️  Only {checked_count} SSO sources checked (should check 5+ sources)")
        else:
            print(f"✓ SSO research: {checked_count} sources checked")

    return warnings


def check_checklist_completion(checklist_content):
    """Check if all required sections of checklist are completed."""
    errors = []
    warnings = []

    # Check pre-flight
    if '- [ ]' in checklist_content.split('## Step 1: Parallel Research')[0]:
        warnings.append("⚠️  Some pre-flight checks not completed")

    # Check if SI ID was generated
    if 'Generated SI ID**: _____' in checklist_content:
        errors.append("❌ SI ID not generated in checklist")

    # Check if description was filled
    if '**Description**:\n```\n[PASTE FINAL DESCRIPTION HERE]' in checklist_content:
        errors.append("❌ Description not filled in checklist")

    # Check if quality check was done
    if '**Quality Check Result**: [ ] PASS [ ] FAIL' in checklist_content:
        warnings.append("⚠️  Quality check result not marked in checklist")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description='Validate Application fact sheet creation compliance'
    )
    parser.add_argument('--checklist', required=True, help='Path to EXECUTION_CHECKLIST.md')
    parser.add_argument('--fields', help='Path to final_fields.json (optional)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed output')

    args = parser.parse_args()

    # Read checklist
    checklist_path = Path(args.checklist)
    if not checklist_path.exists():
        print(f"❌ ERROR: Checklist file not found: {args.checklist}")
        print("   Agent must complete EXECUTION_CHECKLIST.md before validation")
        sys.exit(1)

    checklist_content = checklist_path.read_text()

    print("=" * 70)
    print("APPLICATION CREATION VALIDATION")
    print("=" * 70)
    print()

    all_errors = []
    all_warnings = []

    # 1. Check matrix completion
    print("1. Checking Hosting Type Evaluation Matrix...")
    errors, warnings = check_matrix_completed(checklist_content)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    print()

    # 2. Check SSO research
    print("2. Checking SSO Research Thoroughness...")
    warnings = check_sso_research(checklist_content)
    all_warnings.extend(warnings)
    print()

    # 3. Check checklist completion
    print("3. Checking Checklist Completion...")
    errors, warnings = check_checklist_completion(checklist_content)
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    print()

    # 4. Validate field values if provided
    if args.fields:
        fields_path = Path(args.fields)
        if not fields_path.exists():
            print(f"⚠️  Warning: Fields file not found: {args.fields}")
        else:
            print("4. Validating Field Values...")
            with open(fields_path, 'r') as f:
                fields = json.load(f)

            errors, warnings = validate_field_values(fields)
            all_errors.extend(errors)
            all_warnings.extend(warnings)
            print()

    # Summary
    print("=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)

    if all_errors:
        print(f"\n❌ {len(all_errors)} ERRORS FOUND:\n")
        for error in all_errors:
            print(f"  {error}")
        print()

    if all_warnings:
        print(f"⚠️  {len(all_warnings)} WARNINGS:\n")
        for warning in all_warnings:
            print(f"  {warning}")
        print()

    if not all_errors and not all_warnings:
        print("\n✅ ALL VALIDATIONS PASSED")
        print("   Application creation followed workflow correctly")
        print()
        return 0
    elif not all_errors:
        print("\n✓ Validation passed with warnings")
        print("  Warnings should be addressed but do not block completion")
        print()
        return 0
    else:
        print("\n❌ VALIDATION FAILED")
        print("   Fix errors above before proceeding")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
