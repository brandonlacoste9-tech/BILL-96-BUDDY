#!/usr/bin/env python3
"""
LinkedIn Hunter - Decision Maker Finder
Uses Google Dork queries to find General Managers and Owners without hitting LinkedIn's login wall
"""

import sys
import json
import re
from datetime import datetime

def build_search_query(business_name, city="Montreal"):
    """
    Build Google Dork query to find decision makers
    
    Args:
        business_name: Name of the business
        city: City location (default: Montreal)
    
    Returns:
        Formatted search query string
    """
    # Google Dork to search LinkedIn profiles indexed by Google
    query = f'site:linkedin.com/in "General Manager" OR "Owner" OR "Directeur" OR "Propriétaire" OR "GM" "{business_name}" "{city}"'
    return query

def parse_linkedin_results(search_results):
    """
    Parse Google search results to extract LinkedIn profile info
    
    Args:
        search_results: List of search result dictionaries
    
    Returns:
        List of decision maker profiles with name, title, url
    """
    decision_makers = []
    
    for result in search_results:
        profile = {}
        
        # Extract from title (usually formatted as "Name - Title - Company | LinkedIn")
        title = result.get('title', '')
        
        # Common LinkedIn title patterns
        # "John Doe - General Manager - 40 Westt | LinkedIn"
        # "Jane Smith | Directeur Général | Restaurant Lou's"
        
        if ' - ' in title or ' | ' in title:
            parts = re.split(r' - | \| ', title)
            
            if len(parts) >= 2:
                profile['name'] = parts[0].strip()
                profile['title'] = parts[1].strip()
                profile['url'] = result.get('url', '')
                profile['snippet'] = result.get('snippet', '')
                
                # Filter out irrelevant results
                relevant_titles = [
                    'general manager', 'gm', 'owner', 'propriétaire',
                    'directeur', 'director', 'gérant', 'president',
                    'co-owner', 'partner', 'associé'
                ]
                
                title_lower = profile['title'].lower()
                if any(keyword in title_lower for keyword in relevant_titles):
                    decision_makers.append(profile)
    
    return decision_makers

def find_decision_maker(business_name, city="Montreal", location="West Island"):
    """
    Main function to find decision maker for a business
    
    Args:
        business_name: Name of the business
        city: City location
        location: Specific area/neighborhood
    
    Returns:
        Dictionary with decision maker info or None
    """
    print(f"\n🔍 LinkedIn Hunter: Searching for decision maker at {business_name}...")
    
    # Build the search query
    query = build_search_query(business_name, city)
    print(f"Query: {query}")
    
    # NOTE: In actual implementation, Kiro will use web_search MCP here
    # For now, this is a placeholder that Kiro will intercept
    print("\n→ Kiro: Use web_search MCP to execute this Google Dork query")
    print("→ Kiro: Parse the results and extract LinkedIn profile information")
    
    # Placeholder return structure
    result = {
        "business_name": business_name,
        "search_query": query,
        "search_timestamp": datetime.now().isoformat(),
        "decision_maker_found": False,
        "decision_maker": {
            "name": None,
            "title": None,
            "linkedin_url": None,
            "confidence": "unknown"
        },
        "instructions_for_kiro": "Execute web_search with the query above, then call parse_linkedin_results() with the results"
    }
    
    return result

def update_pitch_email(pitch_file, decision_maker_info):
    """
    Update the pitch email with personalized decision maker info
    
    Args:
        pitch_file: Path to the pitch.txt file
        decision_maker_info: Dictionary with name, title, etc.
    """
    print(f"\n✉️ Updating pitch email: {pitch_file}")
    
    if not decision_maker_info or not decision_maker_info.get('name'):
        print("⚠️ No decision maker found - keeping generic greeting")
        return
    
    name = decision_maker_info['name']
    title = decision_maker_info.get('title', 'Manager')
    
    print(f"→ Personalizing for: {name} ({title})")
    print("→ Kiro: Replace 'Bonjour,' with 'Bonjour {name},'")
    print("→ Kiro: Add title context in the opening line")
    
    # Kiro will handle the actual file modification
    pass

def main():
    """Main execution"""
    if len(sys.argv) < 2:
        print("Usage: python linkedin_hunter.py <business_name> [city] [location]")
        print("Example: python linkedin_hunter.py '40 Westt Steakhouse' 'Montreal' 'West Island'")
        sys.exit(1)
    
    business_name = sys.argv[1]
    city = sys.argv[2] if len(sys.argv) > 2 else "Montreal"
    location = sys.argv[3] if len(sys.argv) > 3 else "West Island"
    
    # Find decision maker
    result = find_decision_maker(business_name, city, location)
    
    # Output JSON for Kiro to process
    print("\n" + "="*60)
    print("RESULT (JSON):")
    print(json.dumps(result, indent=2))
    print("="*60)
    
    return result

if __name__ == "__main__":
    main()
