#!/usr/bin/env python3
"""
DUAL-STRIKE EMAIL LAUNCHER
Fires compliance emails to Lou's and 40 Westt
"""

import resend

# Hardcoded for immediate execution
resend.api_key = "re_3dHPCM1S_EzfUXRaqbdATfW29RpJwEM1x"

def fire_email(target_email, subject, pitch_file):
    with open(pitch_file, 'r', encoding='utf-8') as f:
        body = f.read()
    
    try:
        r = resend.Emails.send({
            "from": "Conformité Loi 14 <audit@adgenai.ca>",
            "to": target_email,
            "subject": subject,
            "text": body
        })
        print(f"✅ FIRED to {target_email} | ID: {r['id']}")
    except Exception as e:
        print(f"❌ ERROR sending to {target_email}: {e}")

if __name__ == "__main__":
    print("🚀 LAUNCHING DUAL-STRIKE...")
    
    # Strike 1: Lou's GM
    fire_email(
        "gm@louspointeclaire.com",
        "Alerte conformité Loi 96 - Lou's Pointe Claire | Risque critique",
        "outreach/louspointeclaire-pitch-general.txt"
    )
    
    # Strike 2: 40 Westt Owner
    fire_email(
        "info@40westt.com",
        "Alerte conformité Loi 96 - 40 Westt Steakhouse | Risque élevé",
        "outreach/40westt-pitch.txt"
    )
