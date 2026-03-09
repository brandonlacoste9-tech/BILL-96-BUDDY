#!/usr/bin/env python3
"""
URGENT: Send Lou's Pointe-Claire compliance emails
Execution time: Monday 8:20 AM - Golden window for restaurant B2B
"""

import os
import json
from datetime import datetime

# Email configuration
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", "compliance@yourdomain.com")

# Target contacts
LOUS_OWNER_EMAIL = "peter@louspointeclaire.com"  # Placeholder - needs real email
LOUS_GM_EMAIL = "gm@louspointeclaire.com"
LOUS_PHONE = "438-596-5517"

# Email subjects
OWNER_SUBJECT = "Alerte conformité Loi 96 - Lou's Pointe Claire | Risque critique"
GM_SUBJECT = "Avis de conformité Loi 96 - Lou's Pointe Claire | Action requise"

print("=" * 70)
print("BILL 96 COMPLIANCE OUTREACH - LOU'S POINTE-CLAIRE")
print("=" * 70)
print(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Target: Lou's Pointe-Claire")
print(f"Compliance Score: 0/100 (CRITICAL)")
print(f"Primary Violation: <html lang='en'> (smoking gun)")
print()
print("DUAL-STRIKE STRATEGY:")
print("1. Owner email (Peter & Max) - Technical + Business impact")
print("2. GM email - Operational urgency + Escalation path")
print()
print("=" * 70)
print()

# Check if Resend API is configured
if not RESEND_API_KEY or RESEND_API_KEY == "re_your_api_key_here":
    print("⚠️  WARNING: RESEND_API_KEY not configured in .env")
    print()
    print("MANUAL EXECUTION REQUIRED:")
    print()
    print("Option 1: Configure Resend API")
    print("  1. Sign up at https://resend.com/")
    print("  2. Get API key")
    print("  3. Add to .env: RESEND_API_KEY=re_xxxxx")
    print("  4. Add to .env: FROM_EMAIL=compliance@yourdomain.com")
    print()
    print("Option 2: Manual email send (RECOMMENDED FOR NOW)")
    print("  1. Open your email client")
    print("  2. Copy content from outreach/louspointeclaire-pitch-owner.txt")
    print("  3. Send to: [FIND OWNER EMAIL]")
    print("  4. Copy content from outreach/louspointeclaire-pitch-general.txt")
    print("  5. Send to: gm@louspointeclaire.com")
    print()
    print("Option 3: Use curl with Resend API")
    print()
    print('curl -X POST "https://api.resend.com/emails" \\')
    print('  -H "Authorization: Bearer YOUR_API_KEY" \\')
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"from": "compliance@yourdomain.com",')
    print('       "to": "gm@louspointeclaire.com",')
    print(f'       "subject": "{GM_SUBJECT}",')
    print('       "text": "[PASTE EMAIL CONTENT]"}\'')
    print()
    print("=" * 70)
    print()
    print("NEXT STEPS WHILE WAITING FOR REPLY:")
    print("1. Restart Playwright MCP server for screenshot capability")
    print("2. Build platform_scraper.py for restaurants-us.com goldmine")
    print("3. Prepare PDF generator for when Lou's replies 'Yes'")
    print()
else:
    print("✅ Resend API configured")
    print(f"   From: {FROM_EMAIL}")
    print()
    print("🚀 READY TO SEND")
    print()
    print("Execute with:")
    print("  python send_lous_emails.py --execute")
    print()

# Log the outreach attempt
outreach_log = {
    "timestamp": datetime.now().isoformat(),
    "target": "Lou's Pointe-Claire",
    "url": "https://www.louspointeclaire.com/",
    "compliance_score": 0,
    "risk_level": "CRITICAL",
    "primary_violation": "HTML lang='en'",
    "emails_prepared": [
        {"type": "owner", "subject": OWNER_SUBJECT, "file": "louspointeclaire-pitch-owner.txt"},
        {"type": "gm", "subject": GM_SUBJECT, "file": "louspointeclaire-pitch-general.txt"}
    ],
    "contact_info": {
        "gm_email": LOUS_GM_EMAIL,
        "phone": LOUS_PHONE
    },
    "status": "READY_TO_SEND",
    "window": "Monday 8:20 AM - Golden B2B window"
}

# Save log
with open("outreach_log.json", "w") as f:
    json.dump([outreach_log], f, indent=2)

print("📝 Outreach logged to outreach_log.json")
