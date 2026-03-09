#!/usr/bin/env python3
"""
VERIFICATION TEST: Lou's Pointe-Claire Playwright Audit
This script uses Playwright directly to audit and verify the scoring logic
"""

from playwright.sync_api import sync_playwright
import json
from datetime import date

def audit_lous_with_playwright():
    """
    Run a complete Bill 96 audit on Lou's using Playwright
    """
    url = "https://www.louspointeclaire.com/"
    
    print("=" * 70)
    print("PLAYWRIGHT AUDIT VERIFICATION - LOU'S POINTE-CLAIRE")
    print("=" * 70)
    print(f"Target: {url}")
    print(f"Date: {date.today()}")
    print()
    
    audit_result = {
        "url": url,
        "audit_date": str(date.today()),
        "html_lang": None,
        "html_lang_compliant": False,
        "visual_predominance": None,
        "visual_predominance_compliant": False,
        "legal_docs_french": False,
        "legal_docs_violation": None,
        "trademark_issues": [],
        "compliance_score": 0,
        "risk_level": "UNKNOWN",
        "violations": []
    }
    
    with sync_playwright() as p:
        print("🌐 Launching browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"📄 Navigating to {url}...")
        page.goto(url, wait_until="networkidle")
        
        # 1. HTML VALIDATION (40% weight)
        print("\n" + "=" * 70)
        print("1. HTML VALIDATION (40% weight)")
        print("=" * 70)
        
        html_content = page.content()
        
        # Extract lang attribute
        if '<html lang="en"' in html_content:
            audit_result["html_lang"] = "en"
            audit_result["html_lang_compliant"] = False
            audit_result["violations"].append("HTML lang attribute set to English (lang='en') instead of French")
            print("❌ VIOLATION: <html lang='en'> found")
            print("   Expected: <html lang='fr'> or <html lang='fr-CA'>")
        elif '<html lang="fr"' in html_content:
            audit_result["html_lang"] = "fr"
            audit_result["html_lang_compliant"] = True
            print("✅ COMPLIANT: <html lang='fr'> found")
        else:
            audit_result["html_lang"] = "unknown"
            audit_result["html_lang_compliant"] = False
            audit_result["violations"].append("HTML lang attribute missing or unrecognized")
            print("❌ VIOLATION: No valid lang attribute found")
        
        # 2. VISUAL PREDOMINANCE (30% weight)
        print("\n" + "=" * 70)
        print("2. VISUAL PREDOMINANCE (30% weight)")
        print("=" * 70)
        
        # Take screenshot for evidence
        screenshot_path = "reports/lous_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"📸 Screenshot saved: {screenshot_path}")
        
        # Extract all visible text
        all_text = page.inner_text("body")
        
        # Check for French content
        french_indicators = ["menu", "réservation", "contactez", "à propos", "accueil"]
        english_indicators = ["menu", "reservation", "contact", "about", "home"]
        
        has_french = any(word in all_text.lower() for word in french_indicators)
        has_english = any(word in all_text.lower() for word in english_indicators)
        
        if not has_french and has_english:
            audit_result["visual_predominance"] = "English-only content, no French visible"
            audit_result["visual_predominance_compliant"] = False
            audit_result["violations"].append("No French language content visible on page")
            print("❌ VIOLATION: English-only content detected")
        elif has_french and not has_english:
            audit_result["visual_predominance"] = "French-only content"
            audit_result["visual_predominance_compliant"] = True
            print("✅ COMPLIANT: French content present")
        else:
            audit_result["visual_predominance"] = "Bilingual content detected - needs manual review for prominence"
            audit_result["visual_predominance_compliant"] = False
            print("⚠️  NEEDS REVIEW: Bilingual content - check French prominence")
        
        # Extract navigation menu
        try:
            nav_text = page.inner_text("nav")
            print(f"\n📋 Navigation menu text:\n{nav_text[:200]}...")
        except:
            print("⚠️  Could not extract navigation menu")
        
        # 3. LEGAL DOCUMENTS (20% weight)
        print("\n" + "=" * 70)
        print("3. LEGAL DOCUMENTS CHECK (20% weight)")
        print("=" * 70)
        
        # Look for legal document links
        legal_keywords = ["privacy", "terms", "legal", "politique", "conditions", "confidentialité"]
        legal_links = []
        
        for link in page.query_selector_all("a"):
            href = link.get_attribute("href") or ""
            text = link.inner_text().lower()
            if any(keyword in text or keyword in href.lower() for keyword in legal_keywords):
                legal_links.append({"text": text, "href": href})
        
        if legal_links:
            print(f"📄 Found {len(legal_links)} potential legal document links:")
            for link in legal_links:
                print(f"   - {link['text']}: {link['href']}")
            audit_result["legal_docs_violation"] = "Legal document links found - French availability needs verification"
        else:
            print("❌ VIOLATION: No legal document links found")
            audit_result["legal_docs_french"] = False
            audit_result["legal_docs_violation"] = "No Terms of Service or Privacy Policy links visible"
            audit_result["violations"].append("Legal documents not accessible in French")
        
        # 4. TRADEMARK COMPLIANCE (10% weight)
        print("\n" + "=" * 70)
        print("4. TRADEMARK COMPLIANCE (10% weight)")
        print("=" * 70)
        
        # Check business name
        title = page.title()
        print(f"📌 Page title: {title}")
        
        if "Lou's" in title or "Lous" in title:
            # Check for French descriptor
            if "restaurant" in title.lower() or "resto" in title.lower():
                print("✅ Business name has descriptor")
            else:
                audit_result["trademark_issues"].append("Lou's - English business name without French descriptor")
                audit_result["violations"].append("Business name 'Lou's' lacks French generic descriptor")
                print("❌ VIOLATION: 'Lou's' without French descriptor (e.g., 'Restaurant Lou's')")
        
        browser.close()
    
    # CALCULATE COMPLIANCE SCORE
    print("\n" + "=" * 70)
    print("COMPLIANCE SCORE CALCULATION")
    print("=" * 70)
    
    score = 0
    
    # HTML lang (40%)
    if audit_result["html_lang_compliant"]:
        score += 40
        print("✅ HTML lang: 40/40")
    else:
        print("❌ HTML lang: 0/40")
    
    # Visual predominance (30%)
    if audit_result["visual_predominance_compliant"]:
        score += 30
        print("✅ Visual predominance: 30/30")
    else:
        print("❌ Visual predominance: 0/30")
    
    # Legal docs (20%)
    if audit_result["legal_docs_french"]:
        score += 20
        print("✅ Legal docs: 20/20")
    else:
        print("❌ Legal docs: 0/20")
    
    # Trademark (10%)
    if not audit_result["trademark_issues"]:
        score += 10
        print("✅ Trademark: 10/10")
    else:
        print("❌ Trademark: 0/10")
    
    audit_result["compliance_score"] = score
    
    # Determine risk level
    if score >= 90:
        audit_result["risk_level"] = "COMPLIANT"
    elif score >= 70:
        audit_result["risk_level"] = "MINOR"
    elif score >= 50:
        audit_result["risk_level"] = "MODERATE"
    else:
        audit_result["risk_level"] = "HIGH"
    
    print("\n" + "=" * 70)
    print(f"FINAL SCORE: {score}/100 - {audit_result['risk_level']} RISK")
    print("=" * 70)
    
    # Save JSON report
    report_path = "reports/lous-playwright-audit-2026-03-09.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(audit_result, f, indent=2, ensure_ascii=False)
    
    print(f"\n📝 Report saved: {report_path}")
    
    # Print JSON output
    print("\n" + "=" * 70)
    print("JSON OUTPUT:")
    print("=" * 70)
    print(json.dumps(audit_result, indent=2, ensure_ascii=False))
    
    return audit_result

if __name__ == "__main__":
    result = audit_lous_with_playwright()
    
    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE")
    print("=" * 70)
    print(f"✅ Playwright successfully audited Lou's")
    print(f"✅ Compliance score: {result['compliance_score']}/100")
    print(f"✅ Violations found: {len(result['violations'])}")
    print(f"✅ Screenshot captured: reports/lous_screenshot.png")
    print(f"✅ JSON report generated: reports/lous-playwright-audit-2026-03-09.json")
    print()
    print("🎯 The audit brain is calibrated and ready!")
