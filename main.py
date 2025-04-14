from zap_scan import scan_with_zap
from report import generate_report
import os

os.makedirs("scans", exist_ok=True)

print("[*] Starting scan...")
alerts = scan_with_zap()
generate_report(alerts)
