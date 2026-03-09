#!/usr/bin/env python3
"""
Complete System Test - Verify Everything Works
"""

import os
import sys

print("=" * 70)
print("TESTING YOUR AUTOMATION EMPIRE")
print("=" * 70)
print()

# Test 1: Check Python packages
print("TEST 1: Python Packages")
print("-" * 70)
try:
    import flask
    print("✅ Flask installed")
except:
    print("❌ Flask missing - run: pip install flask")
    
try:
    import playwright
    print("✅ Playwright installed")
except:
    print("❌ Playwright missing - run: pip install playwright")

try:
    import sendgrid
    print("✅ SendGrid installed")
except:
    print("❌ SendGrid missing - run: pip install sendgrid")

try:
    import requests
    print("✅ Requests installed")
except:
    print("❌ Requests missing - run: pip install requests")

print()

# Test 2: Check SendGrid API Key
print("TEST 2: SendGrid API Key")
print("-" * 70)
api_key = os.getenv("SENDGRID_API_KEY")
if api_key:
    print(f"✅ SendGrid API Key set: {api_key[:10]}...")
else:
    print("❌ SendGrid API Key NOT set")
    print("   Run: $env:SENDGRID_API_KEY='WAAXPBF8S384KDAQAW647WYB'")

print()

# Test 3: Check audit files exist
print("TEST 3: Audit Reports")
print("-" * 70)
import os
if os.path.exists("reports/louspointeclaire-2026-03-09.json"):
    print("✅ Lou's audit report exists")
else:
    print("❌ Lou's audit report missing")

if os.path.exists("reports/40westt-2026-03-09.json"):
    print("✅ 40 Westt audit report exists")
else:
    print("⚠️  40 Westt audit report missing (optional)")

print()

# Test 4: Check automation scripts
print("TEST 4: Automation Scripts")
print("-" * 70)
scripts = [
    "auto_audit_api.py",
    "sendgrid_automation.py",
    "lambiance_scraper.py",
    "audit_4_targets.py"
]

for script in scripts:
    if os.path.exists(script):
        print(f"✅ {script}")
    else:
        print(f"❌ {script} missing")

print()

# Test 5: Test email generation
print("TEST 5: Email Generation")
print("-" * 70)
try:
    import json
    from sendgrid_automation import generate_outreach_email
    
    with open("reports/louspointeclaire-2026-03-09.json", 'r') as f:
        audit = json.load(f)
    
    subject, body = generate_outreach_email(audit, "test@example.com")
    print("✅ Email generation works")
    print(f"   Subject: {subject[:50]}...")
except Exception as e:
    print(f"❌ Email generation failed: {e}")

print()

# Test 6: Test audit system
print("TEST 6: Audit System")
print("-" * 70)
try:
    from audit_4_targets import audit_site
    print("✅ Audit system ready")
    print("   Can audit websites with Playwright")
except Exception as e:
    print(f"❌ Audit system error: {e}")

print()

# Final Summary
print("=" * 70)
print("SYSTEM STATUS")
print("=" * 70)

if api_key and os.path.exists("sendgrid_automation.py"):
    print("✅ READY TO SEND EMAILS")
    print()
    print("Next steps:")
    print("1. Run: python test_sendgrid.py")
    print("2. Enter your email to receive test")
    print("3. Check inbox for audit email")
else:
    print("⚠️  SETUP INCOMPLETE")
    print()
    print("To complete setup:")
    print("1. Set SendGrid API key:")
    print("   $env:SENDGRID_API_KEY='WAAXPBF8S384KDAQAW647WYB'")
    print("2. Run this test again")

print()
print("=" * 70)
