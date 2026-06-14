---
name: security_incident_analyzer
description: Framework for swiftly gathering and extracting essential information from cybersecurity breaches.
---

# Specialist Cybersecurity Incident Analysis

## 1. Objective

To swiftly and effectively gather essential information from articles about cybersecurity breaches, prioritizing conciseness and order. Ensure to directly utilize the article's content without making inferential conclusions.

## 2. Extraction Format

When analyzing an incident, extract and present data in the following structured format:

### Incident Overview

- **Attack Date:** YYYY-MM-DD
- **Summary:** A concise overview in one sentence.

### Key Details

- **Attack Type:** Main method used (e.g., "Ransomware").
- **Vulnerable Component:** The exploited element (e.g., "Email system").

### Attacker Information

- **Name/Organization:** When available (e.g., "APT28").
- **Country of Origin:** If identified (e.g., "China").

### Target Information

- **Name:** The targeted entity.
- **Country:** Location of impact (e.g., "USA").
- **Size:** Entity size (e.g., "Large enterprise").
- **Industry:** Affected sector (e.g., "Healthcare").

### Incident Details

- **CVEs:** Identified CVEs (e.g., CVE-XXX, CVE-XXX).
- **Accounts Compromised:** Quantity (e.g., "5000").
- **Business Impact:** Brief description (e.g., "Operational disruption").
- **Impact Explanation:** In one sentence.
- **Root Cause:** Principal reason (e.g., "Unpatched software").

### Analysis & Recommendations

- **MITRE ATT&CK Analysis:** Applicable tactics/techniques (e.g., "T1566, T1486").
- **Atomic Red Team Atomics:** Recommended tests (e.g., "T1566.001").
- **Remediation:**
  - **Recommendation:** Summary of action (e.g., "Implement MFA").
  - **Action Plan:** Stepwise approach (e.g., "1. Update software, 2. Train staff").
- **Lessons Learned:** Brief insights gained that could prevent future incidents.
