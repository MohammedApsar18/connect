# CyberThreat Detector

A small beginner-friendly cybersecurity mini project built with Python Flask.

## Features
- Analyze a security incident description
- Rule-based threat classification
- Risk score from 0-100
- Severity level
- Basic security recommendation
- Simple web interface

## Requirements
- Python 3.10+
- Flask

## Windows setup

Open Command Prompt inside this project folder:

```text
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Example
Input:
Multiple failed login attempts detected

Output:
Threat Type: Brute Force
Severity: High
Risk Score: 85/100

## Project structure

CyberThreatDetector/
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css

This is an educational rule-based detector, not a production security system.
