#!/usr/bin/env python3
"""
Audit 4 new restaurant targets for Bill 96 compliance
"""

from playwright.sync_api import sync_playwright
import json
from datetime import date

TARGETS = [
    {"name": "toque", "url": "https://www.restaurant-toque.com/en"},
    {"name": "ribnreef", "url": "https://www.ribnreef.com"},
    {"name": "gibbys", "url": "https://www.gibbys.com/en"},
    {"name": "gardemanger", "url": "https://www.gardemanger.ca"}
]

def audit_site(url, business_name):
    """Run Bill 96 audit on a single site"""
    
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
        "violations": []
    }
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            
            # 1. HTML VALIDATION (40% weight)
            html_content = page.content()
            
            if '<html lang="en"' in html_content or '<html lang="en-' in html_content:
                audit_result["html_lang"] = "en"
                audit_result["html_lang_compliant"] = False
                audit_result["html_lang_score"] = 0
                audit_result["violations"].append("HTML lang attribute set to English")
            elif '<html lang="fr"' in html_content:
                audit_result["html_lang"] = "fr"
                audit_result["html_lang_compliant"] = True
                audit_result["html_lang_score"] = 40
            else:
                audit_result["html_lang"] = "unknown"
                audit_result["html_lang_compliant"] = False
                audit_result["html_lang_score"] = 0
                audit_result["violations"].append("HTML lang attribute missing")
            
            # 2. VISUAL PREDOMINANCE (30% weight)
            all_text = page.inner_text("body").lower()
            
            # Count French vs English indicators
            french_words = ["menu", "réservation", "contactez", "à propos", "accueil", "notre", "cuisine"]
            english_words = ["reservation", "contact", "about", "home", "our", "kitchen"]
            
            french_count = sum(1 for word in french_words if word in all_text)
            english_count = sum(1 for word in english_words if word in all_text)
            
            if french_count > english_count:
                audit_result["visual_predominance"] = "French predominant"
                audit_result["visual_predominance_compliant"] = True
                audit_result["visual_predominance_score"] = 30
            elif french_count == english_count and french_count > 0:
                audit_result["visual_predominance"] = "Bilingual - equal prominence"
                audit_result["visual_predominance_compliant"] = True
                audit_result["visual_predominance_score"] = 25
            else:
                audit_result["visual_predominance"] = "English predominant or French absent"
                audit_result["visual_predominance_compliant"] = False
                audit_result["visual_predominance_score"] = 0
                audit_result["violations"].append("English content more prominent than French")
            
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
                audit_result["legal_docs_violation"] = "No legal document links found"
                audit_result["legal_docs_score"] = 0
                audit_result["violations"].append("Legal documents not accessible")
            else:
                # Check if any French legal docs
                has_french_legal = any("politique" in link["text"] or "conditions" in link["text"] for link in legal_links)
                if has_french_legal:
                    audit_result["legal_docs_french"] = True
                    audit_result["legal_docs_score"] = 20
                else:
                    audit_result["legal_docs_french"] = False
                    audit_result["legal_docs_violation"] = "Legal documents found but French availability unclear"
                    audit_result["legal_docs_score"] = 10
            
            # 4. TRADEMARK COMPLIANCE (10% weight)
            title = page.title()
            
            # Check for French descriptor
            if "restaurant" in title.lower() or "resto" in title.lower() or "bistro" in title.lower():
                audit_result["trademark_score"] = 10
            else:
                audit_result["trademark_issues"].append(f"{business_name} - No French generic descriptor in title")
                audit_result["trademark_score"] = 0
            
        except Exception as e:
            print(f"ERROR auditing {url}: {e}")
            audit_result["violations"].append(f"Audit error: {str(e)}")
        
        finally:
            browser.close()
    
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
    else:
        audit_result["risk_level"] = "HIGH" if score >= 30 else "CRITICAL"
    
    return audit_result

if __name__ == "__main__":
    print("=" * 70)
    print("AUDITING 4 NEW TARGETS")
    print("=" * 70)
    
    results = []
    
    for target in TARGETS:
        print(f"\n🎯 Auditing {target['name']}...")
        result = audit_site(target["url"], target["name"])
        results.append(result)
        
        # Save individual report
        report_path = f"reports/{target['name']}-2026-03-09.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"   Score: {result['compliance_score']}/100 ({result['risk_level']})")
        print(f"   Report: {report_path}")
    
    print("\n" + "=" * 70)
    print("AUDIT SUMMARY")
    print("=" * 70)
    for result in results:
        print(f"{result['business_name']:20} {result['compliance_score']:3}/100  {result['risk_level']:10}  {len(result['violations'])} violations")
    
    print("\n✅ All audits complete!")
