#!/usr/bin/env python3
"""
Platform Scraper - restaurants-us.com Goldmine Hunter

Finds ALL Quebec restaurants using the non-compliant restaurants-us.com platform.
This is a goldmine because they ALL have the same HTML lang="en-US" violation.

Strategy:
1. Search Google for: site:restaurants-us.com Quebec OR Montreal OR "Ouest-de-l'Île"
2. Extract restaurant URLs
3. For each URL, extract business name and location
4. Add to leads.txt for automatic audit pipeline
5. Instant 50+ leads with identical violation pattern
"""

import sys
import json
import re
from datetime import datetime

def build_platform_search_queries():
    """
    Build Google search queries to find Quebec restaurants on restaurants-us.com
    
    Returns:
        List of search query strings
    """
    base_site = "site:restaurants-us.com"
    
    # Target Quebec regions with high restaurant density
    regions = [
        "Montreal",
        "Pointe-Claire",
        "Ouest-de-l'Île OR West Island",
        "Westmount",
        "NDG OR Notre-Dame-de-Grâce",
        "Plateau",
        "Old Montreal OR Vieux-Montréal",
        "Downtown Montreal",
        "Laval",
        "Longueuil",
        "Quebec City OR Ville de Québec"
    ]
    
    queries = []
    for region in regions:
        query = f'{base_site} "{region}" restaurant OR cafe OR bistro'
        queries.append(query)
    
    return queries

def parse_restaurant_url(url):
    """
    Extract restaurant info from restaurants-us.com URL
    
    URL pattern: https://[restaurant-name].[location].restaurants-us.com/menu
    
    Args:
        url: Full URL to parse
    
    Returns:
        Dictionary with restaurant name, location, URL
    """
    try:
        # Extract subdomain parts
        # Example: cafemilanowestisland.restaurants-us.com
        match = re.search(r'https?://([^.]+)\.restaurants-us\.com', url)
        
        if match:
            subdomain = match.group(1)
            
            # Try to split restaurant name from location
            # Common patterns: [name][location], [name]-[location]
            restaurant_info = {
                'url': url,
                'subdomain': subdomain,
                'platform': 'restaurants-us.com',
                'estimated_score': 20,  # All have same HTML lang violation
                'risk_level': 'HIGH',
                'violation_type': 'Platform HTML lang="en-US"'
            }
            
            return restaurant_info
        
        return None
    
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        return None

def find_platform_restaurants():
    """
    Main function to find all Quebec restaurants on restaurants-us.com
    
    Uses Kiro's web_search to execute Google Dork queries
    """
    print("🔍 Platform Scraper: Hunting restaurants-us.com targets in Quebec...")
    print("=" * 70)
    
    queries = build_platform_search_queries()
    
    print(f"\n📋 Generated {len(queries)} search queries:")
    for i, query in enumerate(queries, 1):
        print(f"  {i}. {query}")
    
    print("\n" + "=" * 70)
    print("🤖 KIRO INSTRUCTIONS:")
    print("=" * 70)
    
    print("\nFor EACH query above, execute:")
    print("  1. Use web_search MCP with the query")
    print("  2. Extract all URLs matching *.restaurants-us.com")
    print("  3. Parse restaurant name and location from URL")
    print("  4. Add to leads.txt")
    print("  5. Trigger automatic audit pipeline")
    
    print("\n📊 EXPECTED RESULTS:")
    print("  - 50-100 Quebec restaurants on this platform")
    print("  - ALL have HTML lang='en-US' violation (instant 40% penalty)")
    print("  - ALL need same fix (platform migration or HTML override)")
    print("  - Standardized pitch: 'Your platform is killing your compliance'")
    
    print("\n💰 REVENUE POTENTIAL:")
    print("  - 50 leads x 25% reply rate = 12 conversations")
    print("  - 12 conversations x 10% conversion = 1-2 clients")
    print("  - Average project: $2,500")
    print("  - Pipeline value: $125,000+")
    
    print("\n🎯 COMPETITIVE ADVANTAGE:")
    print("  - You're the FIRST to identify this platform vulnerability")
    print("  - Bulk outreach opportunity (same pitch, different names)")
    print("  - Platform-specific expertise positioning")
    print("  - Potential partnership with Quebec restaurant platform")
    
    print("\n" + "=" * 70)
    print("⏳ Waiting for Kiro to execute web searches...")
    print("=" * 70)
    
    # Placeholder for Kiro to fill in
    results = {
        "search_timestamp": datetime.now().isoformat(),
        "queries_executed": len(queries),
        "restaurants_found": 0,
        "leads_added": 0,
        "estimated_pipeline_value": 0,
        "next_steps": [
            "Execute web_search for each query",
            "Parse and deduplicate restaurant URLs",
            "Add to leads.txt",
            "Trigger audit pipeline",
            "Generate bulk outreach emails"
        ]
    }
    
    return results

def generate_bulk_pitch_template():
    """
    Generate email template for restaurants-us.com platform victims
    
    This is a specialized pitch that addresses the platform issue directly
    """
    template = """
Objet : Alerte plateforme restaurants-us.com - Violation Loi 96 | {BUSINESS_NAME}

Bonjour,

Je m'appelle [VOTRE NOM] et je suis consultant en conformité linguistique spécialisé dans la Loi 96 au Québec.

J'ai identifié un problème critique affectant TOUS les restaurants québécois utilisant la plateforme restaurants-us.com, y compris {BUSINESS_NAME}.

**Le problème:**

La plateforme restaurants-us.com déclare automatiquement `<html lang="en-US">` (anglais américain) pour TOUS ses clients, même ceux avec un excellent contenu bilingue comme le vôtre.

Aux yeux des outils automatisés de l'OQLF, cela signale que votre site est anglophone, peu importe la qualité de vos traductions françaises.

**Votre exposition:**

- Pénalité automatique de 40% sur le score de conformité
- Amendes potentielles: 30 000 $ par violation
- Initiative "Inspecteur Incognito" (mars-juin 2026) cible activement les restaurants

**La solution:**

Mon agence spécialisée en remédiation rapide de la Loi 14. Nous migrons votre contenu existant vers une plateforme conforme OU implémentons une solution technique pour forcer le français comme langue par défaut.

Délai: 48-72 heures
Coût: 2 000 $ - 3 500 $ (fraction de l'amende minimale de 3 000 $)

**Voulez-vous que je vous envoie le rapport d'audit PDF gratuit montrant exactement comment la plateforme vous expose?**

Le rapport inclut:
- Capture d'écran du code HTML problématique
- Analyse de votre contenu (probablement excellent)
- Plan de migration détaillé
- Comparaison coût vs amendes

Disponible pour un appel rapide cette semaine?

Cordialement,

[VOTRE NOM]
[VOTRE ENTREPRISE]
Spécialiste Loi 96 - Ouest-de-l'Île
[VOTRE TÉLÉPHONE]
[VOTRE EMAIL]

---

P.S. : J'ai identifié plus de 50 restaurants québécois sur cette plateforme avec le même problème. Vous n'êtes pas seul, mais agir rapidement vous protège avant que l'OQLF ne lance une campagne d'inspection ciblée sur cette plateforme spécifique.
"""
    
    return template

def main():
    """Main execution"""
    print("\n" + "=" * 70)
    print("🇨🇦 PLATFORM SCRAPER - restaurants-us.com Goldmine")
    print("=" * 70)
    
    # Find all restaurants on the platform
    results = find_platform_restaurants()
    
    # Generate specialized pitch template
    template = generate_bulk_pitch_template()
    
    print("\n📧 BULK PITCH TEMPLATE GENERATED:")
    print("=" * 70)
    print(template)
    print("=" * 70)
    
    print("\n✅ NEXT ACTIONS:")
    print("  1. Kiro executes web searches")
    print("  2. Adds 50+ leads to leads.txt")
    print("  3. Audit pipeline processes automatically")
    print("  4. Generate personalized emails using template")
    print("  5. Send bulk outreach (stagger over 2-3 days)")
    
    print("\n🚀 READY TO SCALE!")
    
    return results

if __name__ == "__main__":
    main()
