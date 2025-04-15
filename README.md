# AutoVulnScan
Automated web vulnerability scanner using Python and OWASP ZAP
# 🔍 AutoVulnScan – Automated Web Vulnerability Scanner

AutoVulnScan is a Python-based tool that integrates with [OWASP ZAP](https://www.zaproxy.org/) to automate the detection of common web vulnerabilities, including the OWASP Top 10. It performs spidering, active scanning, and generates developer-friendly PDF reports with remediation suggestions.

---

## 🧠 Project Overview

This project was built as part of a cybersecurity learning journey. It helps developers, students, and analysts quickly assess web application security without manual testing or deep tool knowledge.

---

## 🚀 Features

- 🔎 Automated spider & active scan using OWASP ZAP API
- 📄 PDF vulnerability report generation with severity levels
- 🧩 Detects XSS, SQLi, CSRF, Missing Headers, Info Leakage
- 🕒 Scan scheduling support (via cron jobs)
- 🔧 Easily configurable via `config.ini`

---

## 🛠️ Tech Stack

| Tool/Tech     | Purpose                          |
|---------------|----------------------------------|
| Python 3      | Core scripting                   |
| OWASP ZAP API | Vulnerability scanning engine    |
| ReportLab     | PDF report generation            |
| Linux / Kali  | Execution environment            |

---

## 🗂️ Project Structure

AutoVulnScan/ 
├── main.py # Main script to run scan & generate report 
├── zap_scan.py # Handles OWASP ZAP interactions 
├── report.py # Builds PDF reports from alerts 
├── config.ini # Target URL & API config 
├── scans/ # Output folder for PDF reports 
├── README.md # This file 
└── .gitignore # Ignores venv, pycache, etc.

---

## 📷 Screenshots
![image](https://github.com/user-attachments/assets/4c25096b-bb7f-4af8-b0b9-065568172326)

You can find example output in:
- `Final_Vulnerability_Reports_Combined.pdf`
- `Chakradar_WebVulnScanner_Documentation.docx`

---

## 🧪 Sample Vulnerabilities Detected

- Reflected & Stored XSS
- SQL Injection
- Missing CSP / Anti-CSRF Tokens
- Insecure Headers (X-Frame-Options, HSTS)
- Info disclosure (Server banners, comments)

---

## 📌 How to Use

1. **Install OWASP ZAP** (CLI or GUI)
2. **Update `config.ini`** with:
   ```ini
   [SCAN]
   target_url = http://example.com
   zap_address = 127.0.0.1
   zap_port = 8080
   zap_api_key = your_api_key_here

Start ZAP in daemon mode
zap.sh -daemon -host 127.0.0.1 -port 8080 -config api.key=your_api_key_here

Run the tool
python3 main.py
