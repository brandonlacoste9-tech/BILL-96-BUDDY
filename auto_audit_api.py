#!/usr/bin/env python3
"""
Zyeuté Québec - Automated Bill 96 Audit API
Receives form submissions and runs full audit pipeline
"""

from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright
import json
from datetime import date, datetime
import os
from gmail_automation import send_audit_email

app = Flask(__name__)

def audit_site(url, business_name):
    """Run complete Bill 96 audit on a site"""
    
    audit_result = {
        "url": url,
        "business_name": business_name,
        "audit_date": str(date.today()),
        "html_lang": None,
        "html_lang_compliant": False,
        "html_lang_score": 0,
        "visual_predominance": None,
        "visual_predominance_compliant": False,
        "visual_predominance_score": 0,
        "legal_docs_french": False,
        "legal_docs_violation": None,
        "legal_docs_score": 0,
        "trademark_issues": [],
        "trademark_score": 0,
        "compliance_score": 0,
        "risk_level": "UNKNOWN",
        "violations": [],
        "detailed_findings": {}
    }
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto(url, wait_until="networkidle", timeout=30000)
            
            # 1. HTML VALIDATION (40% weight)
            html_content = page.content()
            
            if '<html lang="en"' in html_content or '<html lang="en-' in html_content:
                audit_result["html_lang"] = "en"
                audit_result["html_lang_compliant"] = False
                audit_result["html_lang_score"] = 0
                audit_result["violations"].append("HTML lang attribute set to English (lang='en') - CRITICAL violation")
            elif '<html lang="fr"' in html_content:
                audit_result["html_lang"] = "fr"
                audit_result["html_lang_compliant"] = True
                audit_result["html_lang_score"] = 40
            else:
                audit_result["html_lang"] = "unknown"
                audit_result["html_lang_compliant"] = False
                audit_result["html_lang_score"] = 0
                audit_result["violations"].append("HTML lang attribute missing or unrecognized")
            
            # 2. VISUAL PREDOMINANCE (30% weight)
            all_text = page.inner_text("body").lower()
            
            # French indicators
            french_words = ["menu", "réservation", "contactez", "à propos", "accueil", "notre", "cuisine", "bienvenue"]
            english_words = ["reservation", "contact", "about", "home", "our", "kitchen", "welcome", "book"]
            
            french_count = sum(1 for word in french_words if word in all_text)
            english_count = sum(1 for word in english_words if word in all_text)
            
            if french_count > english_count:
                audit_result["visual_predominance"] = f"French predominant ({french_count} French indicators vs {english_count} English)"
                audit_result["visual_predominance_compliant"] = True
                audit_result["visual_predominance_score"] = 30
            elif french_count == english_count and french_count > 0:
                audit_result["visual_predominance"] = f"Bilingual - equal prominence ({french_count} indicators each)"
                audit_result["visual_predominance_compliant"] = True
                audit_result["visual_predominance_score"] = 25
            else:
                audit_result["visual_predominance"] = f"English predominant or French absent ({english_count} English vs {french_count} French)"
                audit_result["visual_predominance_compliant"] = False
                audit_result["visual_predominance_score"] = 0
                audit_result["violations"].append("English content more prominent than French")
            
            # Take screenshot for evidence
            screenshot_path = f"reports/{business_name.lower().replace(' ', '')}-screenshot.png"
            page.screenshot(path=screenshot_path, full_page=True)
            audit_result["detailed_findings"]["screenshot"] = screenshot_path
            
            # 3. LEGAL DOCUMENTS (20% weight)
            legal_keywords = ["privacy", "terms", "legal", "politique", "conditions", "confidentialité"]
            legal_links = []
            
            for link in page.query_selector_all("a"):
                href = link.get_attribute("href") or ""
                text = link.inner_text().lower()
                if any(keyword in text or keyword in href.lower() for keyword in legal_keywords):
                    legal_links.append({"text": text, "href": href})
            
            if not legal_links:
                audit_result["legal_docs_french"] = False
                audit_result["legal_docs_violation"] = "No Terms of Service or Privacy Policy links found"
                audit_result["legal_docs_score"] = 0
                audit_result["violations"].append("Legal documents not accessible - CRITICAL violation")
            else:
                has_french_legal = any("politique" in link["text"] or "conditions" in link["text"] for link in legal_links)
                if has_french_legal:
                    audit_result["legal_docs_french"] = True
                    audit_result["legal_docs_score"] = 20
                else:
                    audit_result["legal_docs_french"] = False
                    audit_result["legal_docs_violation"] = "Legal documents found but French availability unclear"
                    audit_result["legal_docs_score"] = 10
                    audit_result["violations"].append("Legal documents may not be available in French")
            
            # 4. TRADEMARK COMPLIANCE (10% weight)
            title = page.title()
            
            if "restaurant" in title.lower() or "resto" in title.lower() or "bistro" in title.lower() or "café" in title.lower():
                audit_result["trademark_score"] = 10
            else:
                audit_result["trademark_issues"].append(f"{business_name} - No French generic descriptor in page title")
                audit_result["trademark_score"] = 0
                audit_result["violations"].append("Business name lacks French generic descriptor")
            
            audit_result["detailed_findings"]["page_title"] = title
            audit_result["detailed_findings"]["legal_links_found"] = len(legal_links)
            
            browser.close()
            
    except Exception as e:
        audit_result["violations"].append(f"Audit error: {str(e)}")
        audit_result["detailed_findings"]["error"] = str(e)
    
    # CALCULATE FINAL SCORE
    audit_result["compliance_score"] = (
        audit_result["html_lang_score"] +
        audit_result["visual_predominance_score"] +
        audit_result["legal_docs_score"] +
        audit_result["trademark_score"]
    )
    
    # Determine risk level
    score = audit_result["compliance_score"]
    if score >= 90:
        audit_result["risk_level"] = "COMPLIANT"
    elif score >= 70:
        audit_result["risk_level"] = "MINOR"
    elif score >= 50:
        audit_result["risk_level"] = "MODERATE"
    elif score >= 30:
        audit_result["risk_level"] = "HIGH"
    else:
        audit_result["risk_level"] = "CRITICAL"
    
    return audit_result

def log_lead(audit_result, email, phone=None):
    """Log lead to CRM"""
    
    lead_entry = {
        "business_name": audit_result["business_name"],
        "url": audit_result["url"],
        "email": email,
        "phone": phone,
        "compliance_score": audit_result["compliance_score"],
        "risk_level": audit_result["risk_level"],
        "audit_date": audit_result["audit_date"],
        "timestamp": datetime.now().isoformat(),
        "email_sent": False,
        "status": "audit_complete",
        "violations": audit_result["violations"]
    }
    
    # Load existing log
    log_file = "outreach_log.json"
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
    else:
        log_data = {"leads": []}
    
    # Append new lead
    log_data["leads"].append(lead_entry)
    
    # Save updated log
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)
    
    return lead_entry

@app.route('/audit', methods=['POST'])
def run_audit():
    """API endpoint to receive form submissions and run audit"""
    
    try:
        data = request.json
        
        # Extract form data
        url = data.get('url')
        business_name = data.get('business_name')
        email = data.get('email')
        phone = data.get('phone', None)
        
        # Validate required fields
        if not url or not business_name or not email:
            return jsonify({
                "success": False,
                "error": "Missing required fields: url, business_name, email"
            }), 400
        
        # Normalize URL
        if not url.startswith('http'):
            url = 'https://' + url
        
        print(f"🎯 Running audit for {business_name} ({url})...")
        
        # Run audit
        audit_result = audit_site(url, business_name)
        
        # Save report
        report_filename = f"{business_name.lower().replace(' ', '')}-{date.today()}.json"
        report_path = f"reports/{report_filename}"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(audit_result, f, indent=2, ensure_ascii=False)
        
        # Log to CRM
        lead_entry = log_lead(audit_result, email, phone)
        
        print(f"✅ Audit complete: {audit_result['compliance_score']}/100 ({audit_result['risk_level']})")
        
        # Send automated email if HIGH or CRITICAL risk
        email_sent = False
        if audit_result['risk_level'] in ['HIGH', 'CRITICAL']:
            print(f"🚨 {audit_result['risk_level']} risk detected - sending automated email...")
            email_sent = send_audit_email(audit_result, email)
        else:
            print(f"ℹ️  {audit_result['risk_level']} risk - email not sent automatically")
        
        return jsonify({
            "success": True,
            "audit_result": audit_result,
            "report_path": report_path,
            "lead_logged": True,
            "email_sent": email_sent,
            "message": f"Audit complete: {audit_result['compliance_score']}/100 - {audit_result['risk_level']} risk"
        }), 200
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "Zyeuté Québec Audit API"}), 200

if __name__ == "__main__":
    print("=" * 70)
    print("ZYEUTÉ QUÉBEC - AUTOMATED AUDIT API")
    print("=" * 70)
    print("Starting Flask server on http://localhost:5000")
    print("Endpoints:")
    print("  POST /audit - Run Bill 96 audit")
    print("  GET /health - Health check")
    print("=" * 70)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
