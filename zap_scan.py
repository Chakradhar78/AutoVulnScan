from zapv2 import ZAPv2
import time
import configparser
import sys
import requests

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

target = config['SCAN']['target_url']
api_key = config['SCAN']['zap_api_key']
zap_address = config['SCAN']['zap_address']
zap_port = config['SCAN']['zap_port']

proxies = {
    'http': f"http://{zap_address}:{zap_port}",
    'https': f"http://{zap_address}:{zap_port}"
}

zap = ZAPv2(apikey=api_key, proxies=proxies)

def scan_with_zap():
    print(f"[*] Checking if ZAP is running at {zap_address}:{zap_port}...")
    try:
        requests.get(f"http://{zap_address}:{zap_port}", timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[!] Unable to connect to ZAP proxy: {e}")
        sys.exit(1)

    print(f"[*] Accessing target: {target}")
    zap.urlopen(target)
    time.sleep(2)

    # Spider Scan
    print("[*] Starting Spider scan...")
    spider_scan_id = zap.spider.scan(target)
    time.sleep(2)

    while int(zap.spider.status(spider_scan_id)) < 100:
        print(f"    [Spider] Progress: {zap.spider.status(spider_scan_id)}%")
        time.sleep(2)

    print("[✓] Spider scan completed.")

    # Active Scan
    print("[*] Starting Active scan...")
    active_scan_id = zap.ascan.scan(target)
    time.sleep(2)

    while int(zap.ascan.status(active_scan_id)) < 100:
        print(f"    [Active Scan] Progress: {zap.ascan.status(active_scan_id)}%")
        time.sleep(5)

    print("[✓] Active scan completed.\n")

    # Fetching Alerts
    print("[*] Fetching vulnerabilities...")
    alerts = zap.core.alerts(baseurl=target)

    if not alerts:
        print("[✓] No alerts found. Target might be safe or scanning failed to detect issues.")
    else:
        print(f"[+] Found {len(alerts)} alerts:\n")
        for alert in alerts:
            print(f"- Alert: {alert['alert']}")
            print(f"  Risk: {alert['risk']}")
            print(f"  URL: {alert['url']}")
            print(f"  Description: {alert['description'][:100]}...")
            print("-" * 50)

    return alerts
