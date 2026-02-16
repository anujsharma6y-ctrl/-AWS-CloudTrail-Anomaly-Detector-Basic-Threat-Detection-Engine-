# AWS CloudTrail Threat Detector

Advanced CLI-based threat detection tool that analyzes AWS CloudTrail logs for suspicious identity and infrastructure activity.

## Features
- Detect Root account usage
- Detect IAM policy changes
- Detect Security Group modifications
- Detect Console login failures
- Risk severity classification
- JSON exportable report

## Requirements
- Python 3
- boto3
- colorama
- AWS CLI configured

## Usage
pip install -r requirements.txt
python main.py
python main.py --export
