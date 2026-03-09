#!/usr/bin/env python3
"""
Test SendGrid email sending
"""

import os
import json
from sendgrid_automation import send_audit_email

# Check if API key is set
if not os.getenv("SENDGRID_API_KEY"):
    print("❌ ERROR: SENDGRID_API_KEY not set!")
    print("Run: $env:SENDGRID_API_KEY='WAAXPBF8S384KDAQAW647WYB'")
    exit(1)

print("✅ SendGrid API Key is set")
print()

# Load Lou's audit result
audit_file = "reports/louspointeclaire-2026-03-09.json"
with open(audit_file, 'r', encoding='utf-8') as f:
    audit_result = json.load(f)

print("=" * 70)
print("TESTING SENDGRID EMAIL")
print("=" * 70)
print(f"Business: {audit_result['business_name']}")
print(f"Score: {audit_result['compliance_score']}/100")
print(f"Risk: {audit_result['risk_level']}")
print()

# Ask for test email
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
    print("Next: Update auto_audit_api.py to use SendGrid")
else:
    print()
    print("=" * 70)
    print("❌ FAILED")
    print("=" * 70)
    print("Check:")
    print("1. SENDGRID_API_KEY is correct")
    print("2. Sender email (zyeutequebec@gmail.com) is verified in SendGrid")
    print("3. SendGrid account is active")
