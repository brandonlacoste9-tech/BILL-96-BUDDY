#!/usr/bin/env python3
"""
L'Ambiance - Automated Lead Generation
Scrapes Google Maps for bars, restaurants, clubs in Montreal
"""

import requests
import json
from datetime import date
import time

def scrape_google_places(query, location="Montreal, QC", radius=50000):
    """
    Scrape Google Places for venues
    Note: Requires Google Places API key
    """
    
    # For now, manual list - can integrate Google Places API later
    # API key needed: https://developers.google.com/maps/documentation/places/web-service/get-api-key
    
    print(f"🔍 Searching for: {query} in {location}")
    print("Note: Google Places API integration coming soon")
    print()
    
    # Manual seed list for testing
    seed_venues = [
        {
            "name": "Lou's Pointe Claire",
            "type": "restaurant",
            "address": "254 Lakeshore Rd, Pointe-Claire, QC",
            "phone": "514-695-2071",
            "website": "https://www.louspointeclaire.com",
            "rating": 4.5,
            "reviews": 250,
            "price_level": 3
        },
        {
            "name": "40 Westt Steakhouse",
            "type": "restaurant",
            "address": "40 Westminster Ave N, Montreal West, QC",
            "phone": "514-486-0040",
            "website": "https://www.40westt.com",
            "rating": 4.6,
            "reviews": 180,
            "price_level": 4
        },
        {
            "name": "Brasserie Le Manoir",
            "type": "restaurant",
            "address": "Multiple locations",
            "phone": "514-695-2071",
            "website": "https://www.brasseriemanoir.com",
            "rating": 4.4,
            "reviews": 320,
            "price_level": 3
        },
        {
            "name": "Cafe Milano",
            "type": "restaurant",
            "address": "West Island, QC",
            "phone": "514-505-0832",
            "website": "https://www.cafemilano.ca",
            "rating": 4.3,
            "reviews": 150,
            "price_level": 3
        }
    ]
    
    return seed_venues

def score_venue(venue):
    """
    Score venue quality for targeting
    Higher score = better lead
    """
    
    score = 0
    
    # Rating (max 40 points)
    if venue.get("rating", 0) >= 4.5:
        score += 40
    elif venue.get("rating", 0) >= 4.0:
        score += 30
    elif venue.get("rating", 0) >= 3.5:
        score += 20
    else:
        score += 10
    
    # Reviews (max 30 points)
    reviews = venue.get("reviews", 0)
    if reviews >= 200:
        score += 30
    elif reviews >= 100:
        score += 20
    elif reviews >= 50:
        score += 10
    
    # Has website (20 points)
    if venue.get("website"):
        score += 20
    
    # Price level (10 points - higher = more budget)
    price = venue.get("price_level", 0)
    score += price * 2
    
    # Determine tier
    if score >= 80:
        tier = "PREMIUM"
    elif score >= 60:
        tier = "HIGH"
    elif score >= 40:
        tier = "MEDIUM"
    else:
        tier = "LOW"
    
    return score, tier

def generate_leads(venue_types=["restaurant", "bar", "nightclub"]):
    """
    Generate leads for L'Ambiance outreach
    """
    
    all_leads = []
    
    for venue_type in venue_types:
        print(f"\n{'='*70}")
        print(f"SEARCHING: {venue_type.upper()}")
        print('='*70)
        
        venues = scrape_google_places(venue_type)
        
        for venue in venues:
            score, tier = score_venue(venue)
            
            lead = {
                "business_name": venue["name"],
                "type": venue["type"],
                "address": venue.get("address", ""),
                "phone": venue.get("phone", ""),
                "website": venue.get("website", ""),
                "rating": venue.get("rating", 0),
                "reviews": venue.get("reviews", 0),
                "price_level": venue.get("price_level", 0),
                "quality_score": score,
                "tier": tier,
                "date_added": str(date.today()),
                "status": "new",
                "email_sent": False
            }
            
            all_leads.append(lead)
            
            print(f"✅ {venue['name']}")
            print(f"   Score: {score}/100 ({tier})")
            print(f"   Rating: {venue.get('rating', 'N/A')} ({venue.get('reviews', 0)} reviews)")
            print(f"   Website: {venue.get('website', 'None')}")
    
    return all_leads

def save_leads(leads, filename="lambiance_leads.json"):
    """Save leads to JSON file"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({"leads": leads, "generated_date": str(date.today())}, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Saved {len(leads)} leads to {filename}")

if __name__ == "__main__":
    print("=" * 70)
    print("L'AMBIANCE - LEAD GENERATION")
    print("=" * 70)
    print("Website: www.lambiance.com")
    print("Target: Bars, Restaurants, Clubs in Montreal")
    print()
    
    # Generate leads
    leads = generate_leads(["restaurant", "bar", "nightclub"])
    
    # Save to file
    save_leads(leads)
    
    # Summary
    print("\n" + "=" * 70)
    print("LEAD SUMMARY")
    print("=" * 70)
    
    premium = sum(1 for l in leads if l["tier"] == "PREMIUM")
    high = sum(1 for l in leads if l["tier"] == "HIGH")
    medium = sum(1 for l in leads if l["tier"] == "MEDIUM")
    low = sum(1 for l in leads if l["tier"] == "LOW")
    
    print(f"Total Leads: {len(leads)}")
    print(f"  PREMIUM: {premium} (score 80+)")
    print(f"  HIGH: {high} (score 60-79)")
    print(f"  MEDIUM: {medium} (score 40-59)")
    print(f"  LOW: {low} (score <40)")
    print()
    print("Next: Run lambiance_outreach.py to send emails")
