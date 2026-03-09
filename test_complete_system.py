#!/usr/bin/env python3
"""
Complete system test - Audit + Email
"""

import os
import json
from gmail_automation import send_audit_email

# Check if Gmail password is set
if not os.getenv("GMAIL_APP_PASSWORD"):
    print("❌ ERROR: GMAIL_APP_PASSWORD not set!")
    print("Run: $env:GMAIL_APP_PASSWORD='your-password'")
    exit(1)

print("✅ Gmail App Password is set")
print()

# Load Lou's audit result
audit_file = "reports/louspointeclaire-2026-03-09.json"
with open(audit_file, 'r', encoding='utf-8') as f:
    audit_result = json.load(f)

print("=" * 70)
print("TESTING COMPLETE SYSTEM")
print("=" * 70)
print(f"Business: {audit_result['business_name']}")
print(f"Score: {audit_result['compliance_score']}/100")
print(f"Risk: {audit_result['risk_level']}")
print()

# Ask for confirmation
test_email = input("Enter YOUR email to receive test audit: ")

if not test_email or '@' not in test_email:
    print("❌ Invalid email")
    exit(1)

print()
print(f"📧 Sending test audit email to {test_email}...")
print()

# Send email
success = send_audit_email(audit_result, test_email)

if success:
    print()
    print("=" * 70)
    print("✅ SUCCESS!")
    print("=" * 70)
    print(f"Check your inbox: {test_email}")
    print("Subject: Alerte conformité Loi 96 - Lou's Pointe Claire | Risque critique")
    print()
    print("If you received the email, the system is working!")
    print("Next step: Deploy to Railway")
else:
    print()
    print("=" * 70)
    print("❌ FAILED")
    print("=" * 70)
    print("Check:")
    print("1. GMAIL_APP_PASSWORD is correct")
    print("2. 2FA is enabled on zyeutequebec@gmail.com")
    print("3. App Password was generated correctly")
