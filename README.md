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
📂 Project Structure
Files are organized to ensure a clean, searchable, and professional repository hierarchy:

Plaintext
aws-cloudtrail-threat-detector/
│
├── main.py
├── log_parser.py
├── threat_engine.py
├── report_generator.py
├── requirements.txt
└── README.md
🛠️ Tech Stack & Requirements
Language: Python 3.x, Bash

Core Libraries: streamlit, boto3, psutil, fpdf, requests, pandas, hashlib

Standard Compliance: MITRE ATT&CK, NIST, CIS Benchmarks


## ⚖️ License & Legal Information

This project is primarily licensed under the **MIT License**, with specific modules covered under **Apache 2.0** and **GPL v3**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](./LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

### Key Permissions:
- ✅ **Commercial Use:** You can use this code for business purposes.
- ✅ **Modification:** You can change the code however you like.
- ✅ **Distribution:** You can share the code with others.
- ✅ **Private Use:** You can use it privately.

### Conditions:
- ⚠️ **Notice:** You must include the original copyright and license notice in any copy of the software/source code.

### Warranty:
- 🛡️ **No Warranty:** The software is provided "as is", without any warranty of any kind. The author is not liable for any claims or damages.

**For more details, view the [Full LICENSE File](./LICENSE)**


👨‍💻 Author
Anuj Sharma Cybercurity Enthusiast | Cloud Security Automation Specialist | DevSecOps Engineer
