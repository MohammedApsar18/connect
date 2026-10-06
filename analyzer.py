KEYWORDS = {
    "Brute Force": ["failed login", "multiple login", "brute force", "repeated password"],
    "Phishing": ["phishing", "suspicious email", "fake login", "click a link", "login link"],
    "Malware": ["malware", "virus", "trojan", "ransomware"],
    "Data Leak": ["data leak", "stolen data", "information leaked", "exposed database"],
    "Unauthorized Access": ["unauthorized access", "unknown user", "account compromised"],
}

def analyze_incident(text):
    lowered = text.lower()
    best_type = "Suspicious Activity"
    score = 20

    for threat_type, words in KEYWORDS.items():
        if any(word in lowered for word in words):
            best_type = threat_type
            score = 80
            break

    if "ransomware" in lowered or "data leak" in lowered or "account compromised" in lowered:
        score = 95
    elif "failed login" in lowered or "phishing" in lowered or "suspicious email" in lowered:
        score = 85

    if score >= 80:
        severity = "High"
    elif score >= 50:
        severity = "Medium"
    else:
        severity = "Low"

    return {
        "type": best_type,
        "severity": severity,
        "score": score,
        "recommendation": recommendation(best_type)
    }

def recommendation(threat_type):
    recommendations = {
        "Brute Force": "Lock or rate-limit the account, enable MFA, and review login logs.",
        "Phishing": "Do not open the link, report the message, and verify the sender.",
        "Malware": "Isolate the affected device and run an approved security scan.",
        "Data Leak": "Restrict access, preserve logs, and investigate exposed data.",
        "Unauthorized Access": "Disable suspicious sessions, reset credentials, and review access logs.",
        "Suspicious Activity": "Collect logs and investigate the activity before taking further action.",
    }
    return recommendations.get(threat_type, recommendations["Suspicious Activity"])
