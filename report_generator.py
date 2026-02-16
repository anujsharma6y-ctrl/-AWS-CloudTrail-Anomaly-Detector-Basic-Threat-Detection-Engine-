import json

def generate_report(findings):
    with open("cloudtrail_threat_report.json", "w") as f:
        json.dump(findings, f, indent=4)

    print("\nReport exported as cloudtrail_threat_report.json")
