#!/usr/bin/env python3
"""LeanIX Fact Sheet Update CLI.

This tool allows you to:
1. Discover available fields for fact sheet types (one-time setup)
2. Update fact sheets with custom field values via GraphQL

Usage:
    # Discover fields (one-time setup)
    python main.py discover --type Provider

    # Update fact sheet
    python main.py update \
        --fact-sheet-id "uuid-here" \
        --type Provider \
        --fields '{"homePageUrl": "https://example.com"}'
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

# Add parent directory to path to access shared lib/
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.leanix_client import (
    LeanIXGraphQLClient,
    SchemaFetcher,
    FieldValidator,
    PatchBuilder,
)


def load_environment() -> tuple[str, str]:
    """Load required environment variables.

    Returns:
        Tuple of (api_token, subdomain)

    Raises:
        ValueError: If required environment variables are missing
    """
    api_token = os.getenv("LEANIX_API_TOKEN")
    subdomain = os.getenv("LEANIX_SUBDOMAIN")

    if not api_token:
        raise ValueError(
            "LEANIX_API_TOKEN environment variable is required.\n"
            "Set it with: export LEANIX_API_TOKEN='LXT_...'"
        )

    if not subdomain:
        raise ValueError(
            "LEANIX_SUBDOMAIN environment variable is required.\n"
            "Set it with: export LEANIX_SUBDOMAIN='demo-eu-10'"
        )

    return api_token, subdomain


async def discover_command(args: argparse.Namespace) -> int:
    """Execute the discover command to fetch available fields.

    Args:
        args: Parsed command line arguments

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        # Load environment
        api_token, subdomain = load_environment()

        print(f"Discovering fields for fact sheet type: {args.type}")
        print(f"Using subdomain: {subdomain}")
        print()

        # Initialize client and authenticate
        async with LeanIXGraphQLClient(api_token, subdomain) as client:
            if args.verbose:
                print("Authenticating...")
            await client.authenticate()
            if args.verbose:
                print("✓ Authentication successful")
                print()

            # Discover fields
            fetcher = SchemaFetcher(client)
            if args.verbose:
                print(f"Fetching schema for {args.type}...")
            fields = await fetcher.discover_fields(args.type)

            if not fields:
                print(f"Warning: No fields discovered for type {args.type}")
                return 1

            print(f"✓ Discovered {len(fields)} fields for {args.type}:")
            print()
            for field in fields:
                print(f"  - {field}")
            print()

            # Save to config file
            output_file = args.output or "field_config.json"
            fetcher.save_config(args.type, fields, output_file)
            print(f"✓ Configuration saved to: {output_file}")
            print()

            # Show current config summary
            config = SchemaFetcher.load_config(output_file)
            print(f"Current configuration includes {len(config)} fact sheet types:")
            for fs_type in sorted(config.keys()):
                field_count = len(config[fs_type]["fields"])
                print(f"  - {fs_type}: {field_count} fields")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


async def update_command(args: argparse.Namespace) -> int:
    """Execute the update command to modify a fact sheet.

    Args:
        args: Parsed command line arguments

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    try:
        # Load environment
        api_token, subdomain = load_environment()

        # Parse fields JSON
        try:
            fields = json.loads(args.fields)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in --fields argument: {e}", file=sys.stderr)
            return 1

        if not isinstance(fields, dict):
            print("Error: --fields must be a JSON object (dictionary)", file=sys.stderr)
            return 1

        if not fields:
            print("Error: --fields cannot be empty", file=sys.stderr)
            return 1

        # Load configuration
        config_file = args.config or "field_config.json"
        try:
            config = SchemaFetcher.load_config(config_file)
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

        # Validate fields
        validator = FieldValidator(config)
        validation_errors = validator.validate_fields(args.type, fields)

        if validation_errors:
            print("Validation failed:", file=sys.stderr)
            for error in validation_errors:
                print(f"  {error}", file=sys.stderr)
            return 1

        if args.verbose:
            print(f"✓ All {len(fields)} fields validated successfully")
            print()

        # Build patches
        patches = PatchBuilder.build_patches(fields)

        if args.verbose:
            print("JSON Patches to apply:")
            print(json.dumps(patches, indent=2))
            print()

        # Execute mutation
        print(f"Updating fact sheet: {args.fact_sheet_id}")
        print(f"Type: {args.type}")
        print(f"Fields: {', '.join(fields.keys())}")
        if args.validate_only:
            print("Mode: VALIDATE ONLY (no changes will be committed)")
        print()

        async with LeanIXGraphQLClient(api_token, subdomain) as client:
            if args.verbose:
                print("Authenticating...")
            await client.authenticate()
            if args.verbose:
                print("✓ Authentication successful")
                print()

            if args.verbose:
                print("Executing updateFactSheet mutation...")
            result = await client.execute_mutation(
                args.fact_sheet_id, patches, args.validate_only
            )

            print("✓ Update successful!")
            print()
            print("Result:")
            print(json.dumps(result, indent=2))

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def main() -> int:
    """Main entry point for the CLI.

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    parser = argparse.ArgumentParser(
        description="LeanIX Fact Sheet Update Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Discover fields for Provider type
  python main.py discover --type Provider

  # Update a Provider fact sheet
  python main.py update \\
    --fact-sheet-id "e7630643-c87c-4def-87f2-0ca6d53ef798" \\
    --type Provider \\
    --fields '{"homePageUrl": "https://example.com", "aliases": "Alias1, Alias2"}'

  # Validate update without committing
  python main.py update \\
    --fact-sheet-id "uuid" \\
    --type Application \\
    --fields '{"description": "New description"}' \\
    --validate-only

Environment Variables:
  LEANIX_API_TOKEN     Technical user token (required)
  LEANIX_SUBDOMAIN     LeanIX subdomain (required)
        """,
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output with debug information",
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Discover command
    discover_parser = subparsers.add_parser(
        "discover",
        help="Discover available fields for a fact sheet type",
    )
    discover_parser.add_argument(
        "--type",
        required=True,
        help="Fact sheet type (e.g., Provider, Application, ITComponent, ProductFamily)",
    )
    discover_parser.add_argument(
        "--output",
        default="field_config.json",
        help="Output configuration file (default: field_config.json)",
    )

    # Update command
    update_parser = subparsers.add_parser(
        "update",
        help="Update a fact sheet with field values",
    )
    update_parser.add_argument(
        "--fact-sheet-id",
        required=True,
        help="UUID of the fact sheet to update",
    )
    update_parser.add_argument(
        "--type",
        required=True,
        help="Fact sheet type (e.g., Provider, Application, ITComponent, ProductFamily)",
    )
    update_parser.add_argument(
        "--fields",
        required=True,
        help='JSON object with field names and values (e.g., \'{"homePageUrl": "https://example.com"}\')',
    )
    update_parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate changes without committing (dry run mode)",
    )
    update_parser.add_argument(
        "--config",
        default="field_config.json",
        help="Configuration file with allowed fields (default: field_config.json)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Run the appropriate command
    if args.command == "discover":
        return asyncio.run(discover_command(args))
    elif args.command == "update":
        return asyncio.run(update_command(args))
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
