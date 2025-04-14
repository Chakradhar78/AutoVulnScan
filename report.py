from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(alerts, filename="scans/vuln_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, "Vulnerability Scan Report")
    c.drawString(50, 785, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    y = 760
    for alert in alerts:
        if y < 100:
            c.showPage()
            y = 800
        c.drawString(50, y, f"[{alert['risk']}] {alert['alert']} at {alert['url']}")
        y -= 20

    c.save()
    print(f"[✓] Report generated at: {filename}")
