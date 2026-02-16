import boto3
import json
from datetime import datetime, timedelta

def fetch_cloudtrail_events():
    client = boto3.client("cloudtrail")

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)

    response = client.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        MaxResults=50
    )

    events = []

    for event in response["Events"]:
        event_detail = json.loads(event["CloudTrailEvent"])
        events.append(event_detail)

    return events
