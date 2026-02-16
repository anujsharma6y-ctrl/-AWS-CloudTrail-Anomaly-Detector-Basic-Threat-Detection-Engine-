import argparse
from log_parser import fetch_cloudtrail_events
from threat_engine import analyze_events
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="AWS CloudTrail Threat Detector")
    parser.add_argument("--export", action="store_true", help="Export report to JSON")
    args = parser.parse_args()

    print("\nFetching CloudTrail events...\n")
    events = fetch_cloudtrail_events()

    findings = analyze_events(events)

    if args.export:
        generate_report(findings)

if __name__ == "__main__":
    main()
