#!/usr/bin/env python3
"""
Test the Zyeuté Québec Audit API
"""

import requests
import json

API_URL = "http://localhost:5000/audit"

# Test data
test_submission = {
    "url": "https://www.louspointeclaire.com",
    "business_name": "Lou's Pointe Claire",
    "email": "gm@louspointeclaire.com",
    "phone": "514-123-4567"
}

print("=" * 70)
print("TESTING ZYEUTÉ QUÉBEC AUDIT API")
print("=" * 70)
print(f"Sending POST request to {API_URL}")
print(f"Test data: {json.dumps(test_submission, indent=2)}")
print()

try:
    response = requests.post(API_URL, json=test_submission, timeout=60)
    
    print(f"Status Code: {response.status_code}")
    print()
    
    if response.status_code == 200:
        result = response.json()
        print("✅ SUCCESS!")
        print()
        print("Audit Result:")
        print(f"  Business: {result['audit_result']['business_name']}")
        print(f"  Score: {result['audit_result']['compliance_score']}/100")
        print(f"  Risk Level: {result['audit_result']['risk_level']}")
        print(f"  Violations: {len(result['audit_result']['violations'])}")
        print()
        print("Violations:")
        for violation in result['audit_result']['violations']:
            print(f"  - {violation}")
        print()
        print(f"Report saved: {result['report_path']}")
        print(f"Lead logged: {result['lead_logged']}")
    else:
        print("❌ ERROR!")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("❌ CONNECTION ERROR!")
    print("Make sure the API server is running:")
    print("  python auto_audit_api.py")
except Exception as e:
    print(f"❌ ERROR: {e}")

print()
print("=" * 70)
