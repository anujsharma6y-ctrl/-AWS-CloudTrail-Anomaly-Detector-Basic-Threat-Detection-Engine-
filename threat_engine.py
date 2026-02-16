from colorama import Fore, Style

def analyze_events(events):
    findings = []

    print("Analyzing events...\n")

    for event in events:
        event_name = event.get("eventName")
        user_identity = event.get("userIdentity", {})
        user_type = user_identity.get("type")

        # CRITICAL: Root usage
        if user_type == "Root":
            print(f"{Fore.RED}[CRITICAL] Root account activity detected: {event_name}{Style.RESET_ALL}")
            findings.append({"event": event_name, "risk": "CRITICAL"})

        # HIGH: IAM policy change
        if event_name in ["AttachUserPolicy", "PutUserPolicy", "AttachRolePolicy"]:
            print(f"{Fore.RED}[HIGH] IAM policy change detected: {event_name}{Style.RESET_ALL}")
            findings.append({"event": event_name, "risk": "HIGH"})

        # MEDIUM: Security group modification
        if event_name in ["AuthorizeSecurityGroupIngress", "AuthorizeSecurityGroupEgress"]:
            print(f"{Fore.YELLOW}[MEDIUM] Security Group modified: {event_name}{Style.RESET_ALL}")
            findings.append({"event": event_name, "risk": "MEDIUM"})

        # MEDIUM: Console login failures
        if event_name == "ConsoleLogin":
            if event.get("responseElements", {}).get("ConsoleLogin") == "Failure":
                print(f"{Fore.YELLOW}[MEDIUM] Failed console login detected{Style.RESET_ALL}")
                findings.append({"event": "ConsoleLoginFailure", "risk": "MEDIUM"})

    if not findings:
        print(f"{Fore.GREEN}No suspicious activity detected in last 24 hours.{Style.RESET_ALL}")

    return findings
