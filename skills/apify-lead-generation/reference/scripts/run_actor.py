#!/usr/bin/env python3
# /// script
# dependencies = ["python-dotenv", "requests"]
# ///
"""
Apify Actor Runner - Runs Apify actors and exports results.

Usage:
    # Quick answer (display in chat, no file saved)
    uv run scripts/run_actor.py --actor ACTOR_ID --input '{}'

    # Quick answer with essential fields filter
    uv run scripts/run_actor.py --actor ACTOR_ID --input '{}' --essential-fields 'title,url,phone'

    # Export to file
    uv run scripts/run_actor.py --actor ACTOR_ID --input '{}' --output leads.csv --format csv

    # Export basic fields only (requires --essential-fields)
    uv run scripts/run_actor.py --actor ACTOR_ID --input '{}' --output leads.csv --format csv --fields basic --essential-fields 'title,url,phone'
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
import requests

# User-Agent for tracking skill usage in Apify analytics
USER_AGENT = "apify-agent-skills/apify-lead-generation-1.1.2"



def main():
    # Load .env from current dir or any parent dir - token stays in Python process
    load_dotenv(find_dotenv(usecwd=True))
    token = os.getenv("APIFY_TOKEN")
    if not token:
        print("Error: APIFY_TOKEN not found in .env file", file=sys.stderr)
        print("", file=sys.stderr)
        print("Add your token to .env file:", file=sys.stderr)
        print("  APIFY_TOKEN=your_token_here", file=sys.stderr)
        print("", file=sys.stderr)
        print("Get your token: https://console.apify.com/account/integrations", file=sys.stderr)
        sys.exit(1)

    args = parse_args()

    # Validate essential-fields requirement early (before starting the actor run)
    if args.fields == "basic" and not args.essential_fields:
        print("Error: --essential-fields is required when using --fields basic", file=sys.stderr)
        print("", file=sys.stderr)
        print("Example: --essential-fields 'title,url,phone,address'", file=sys.stderr)
        print("", file=sys.stderr)
        print("Use mcpc fetch-actor-details to discover available output fields.", file=sys.stderr)
        sys.exit(1)

    # Parse essential fields
    essential_fields = None
    if args.essential_fields:
        essential_fields = [f.strip() for f in args.essential_fields.split(",")]

    # Start the actor run
    print(f"Starting actor: {args.actor}")
    run_id, dataset_id = start_actor(token, args.actor, args.input)
    print(f"Run ID: {run_id}")
    print(f"Dataset ID: {dataset_id}")

    # Poll for completion
    status = poll_until_complete(token, run_id, args.timeout, args.poll_interval)

    if status != "SUCCEEDED":
        print(f"Error: Actor run {status}", file=sys.stderr)
        print(f"Details: https://console.apify.com/actors/runs/{run_id}", file=sys.stderr)
        sys.exit(1)

    # Determine output mode
    if args.output:
        # File output mode
        download_results(token, dataset_id, args.output, args.format, args.fields, essential_fields)
        report_summary(args.output, args.format)
    else:
        # Quick answer mode - display in chat
        display_quick_answer(token, dataset_id, essential_fields)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Apify actor and export results",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Output Formats:
  JSON (all data)     --output file.json --format json
  CSV (all data)      --output file.csv --format csv
  CSV (basic fields)  --output file.csv --format csv --fields basic --essential-fields 'title,url,...'
  Quick answer        (no --output) - displays top 5 in chat

Examples:
  # Quick answer - display top 5 in chat
  uv run scripts/run_actor.py \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}'

  # Quick answer with essential fields filter
  uv run scripts/run_actor.py \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}' \\
    --essential-fields 'title,address,phone,website,totalScore'

  # Export all data to CSV
  uv run scripts/run_actor.py \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}' \\
    --output leads.csv --format csv

  # Export basic fields only (requires --essential-fields)
  uv run scripts/run_actor.py \\
    --actor "compass/crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}' \\
    --output leads.csv --format csv --fields basic \\
    --essential-fields 'title,address,phone,website,totalScore'
        """,
    )
    parser.add_argument(
        "--actor",
        required=True,
        help="Actor ID (e.g., compass/crawler-google-places)",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Actor input as JSON string",
    )
    parser.add_argument(
        "--output",
        help="Output file path (optional - if not provided, displays quick answer in chat)",
    )
    parser.add_argument(
        "--format",
        default="csv",
        choices=["csv", "json"],
        help="Output format (default: csv)",
    )
    parser.add_argument(
        "--fields",
        default="all",
        choices=["all", "basic"],
        help="Fields to include: all (default) or basic (essential fields only)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Max wait time in seconds (default: 600)",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=5,
        help="Seconds between status checks (default: 5)",
    )
    parser.add_argument(
        "--essential-fields",
        type=str,
        help="Comma-separated essential fields for basic output (e.g., 'title,url,phone'). Required when --fields basic is used.",
    )
    return parser.parse_args()


def start_actor(token: str, actor_id: str, input_json: str) -> tuple[str, str]:
    """Start an actor run and return (run_id, dataset_id)."""
    # Convert "author/actor" format to "author~actor" for API compatibility
    actor_id = actor_id.replace("/", "~")
    url = f"https://api.apify.com/v2/acts/{actor_id}/runs"
    headers = {"Content-Type": "application/json", "User-Agent": f"{USER_AGENT}/start_actor"}
    params = {"token": token}

    try:
        data = json.loads(input_json)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    response = requests.post(url, headers=headers, params=params, json=data)

    if response.status_code == 404:
        print(f"Error: Actor '{actor_id}' not found", file=sys.stderr)
        sys.exit(1)

    response.raise_for_status()

    result = response.json()["data"]
    return result["id"], result["defaultDatasetId"]


def poll_until_complete(
    token: str, run_id: str, timeout: int, interval: int
) -> str:
    """Poll run status until complete or timeout."""
    url = f"https://api.apify.com/v2/actor-runs/{run_id}"
    params = {"token": token}

    start_time = time.time()
    last_status = None

    while True:
        response = requests.get(url, params=params)
        response.raise_for_status()

        status = response.json()["data"]["status"]

        # Only print when status changes
        if status != last_status:
            print(f"Status: {status}")
            last_status = status

        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            return status

        elapsed = time.time() - start_time
        if elapsed > timeout:
            print(f"Warning: Timeout after {timeout}s, actor still running", file=sys.stderr)
            return "TIMED-OUT"

        time.sleep(interval)


def get_nested_value(obj: dict, key: str):
    """Get value from nested dict using dot notation (e.g., 'authorMeta.name')."""
    keys = key.split('.')
    value = obj
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None
    return value


def filter_fields(items: list, fields: list) -> list:
    """Filter items to only include specified fields."""
    filtered = []
    for item in items:
        filtered_item = {}
        for field in fields:
            value = get_nested_value(item, field)
            if value is not None:
                # Flatten nested field names for output
                flat_key = field.replace('.', '_')
                filtered_item[flat_key] = value
        filtered.append(filtered_item)
    return filtered


def download_results(
    token: str, dataset_id: str, output_path: str, format: str, fields: str, essential_fields: list | None
) -> None:
    """Download dataset items in specified format."""
    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
    headers = {"User-Agent": f"{USER_AGENT}/download_{format}"}
    params = {"token": token, "format": "json"}  # Always fetch as JSON first for filtering

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    # Filter fields if basic mode
    if fields == "basic" and essential_fields:
        data = filter_fields(data, essential_fields)

    # Write output
    if format == "json":
        Path(output_path).write_text(json.dumps(data, indent=2))
    else:
        # CSV output
        if data:
            import csv
            fieldnames = list(data[0].keys()) if data else []
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    # Truncate long text fields and handle nested objects
                    clean_row = {}
                    for k, v in row.items():
                        if isinstance(v, str) and len(v) > 200:
                            clean_row[k] = v[:200] + "..."
                        elif isinstance(v, (list, dict)):
                            clean_row[k] = json.dumps(v) if v else ""
                        else:
                            clean_row[k] = v
                    writer.writerow(clean_row)
        else:
            Path(output_path).write_text("")

    print(f"Saved to: {output_path}")


def display_quick_answer(token: str, dataset_id: str, essential_fields: list | None) -> None:
    """Display top 5 results in chat format."""
    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
    headers = {"User-Agent": f"{USER_AGENT}/quick_answer"}
    params = {"token": token, "format": "json"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    total = len(data)

    if total == 0:
        print("\nNo results found.")
        return

    # Filter to essential fields if provided
    if essential_fields:
        data = filter_fields(data, essential_fields)

    # Display top 5
    print(f"\n{'='*60}")
    print(f"TOP 5 RESULTS (of {total} total)")
    print(f"{'='*60}")

    for i, item in enumerate(data[:5], 1):
        print(f"\n--- Result {i} ---")
        for key, value in item.items():
            # Truncate long values
            if isinstance(value, str) and len(value) > 100:
                value = value[:100] + "..."
            elif isinstance(value, (list, dict)):
                value = json.dumps(value)[:100] + "..." if len(json.dumps(value)) > 100 else json.dumps(value)
            print(f"  {key}: {value}")

    print(f"\n{'='*60}")
    if total > 5:
        print(f"Showing 5 of {total} results.")
    print(f"Full data available at: https://console.apify.com/storage/datasets/{dataset_id}")
    print(f"{'='*60}")


def report_summary(output_path: str, format: str) -> None:
    """Print summary of downloaded data."""
    path = Path(output_path)
    size = path.stat().st_size

    try:
        if format == "json":
            data = json.loads(path.read_text())
            count = len(data) if isinstance(data, list) else 1
        else:  # csv
            lines = path.read_text().splitlines()
            count = max(0, len(lines) - 1)  # Exclude header
    except Exception:
        count = "unknown"

    print(f"Records: {count}")
    print(f"Size: {size:,} bytes")


if __name__ == "__main__":
    main()
