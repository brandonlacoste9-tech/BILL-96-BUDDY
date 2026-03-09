# 🚨 IMMEDIATE ACTION REQUIRED - SEND EMAILS NOW

**Time:** Monday, March 9, 2026 - 8:20 AM
**Window:** GOLDEN HOUR (Restaurant owners clearing inbox before lunch prep)

## Email #1: Lou's Pointe Claire - Owner Email
**To:** gm@louspointeclaire.com
**Subject:** Alerte conformité Loi 96 - Lou's Pointe Claire | Risque critique
**File:** outreach/louspointeclaire-pitch-owner.txt
**Recipients:** Peter Mant, Max Ruiz Laing (co-owners)
**Priority:** URGENT - 0/100 score, zero compliance

## Email #2: Lou's Pointe Claire - General Inbox
**To:** gm@louspointeclaire.com (same, but different tone)
**Subject:** Avis de conformité Loi 96 - Lou's Pointe Claire | Action requise
**File:** outreach/louspointeclaire-pitch-general.txt
**Purpose:** Backup/escalation path

## Email #3: 40 Westt Steakhouse
**To:** info@40westt.com (or via RestaurantMontreal.ca contact form)
**Phone:** 514-428-9378
**Subject:** Alerte conformité Loi 96 - 40 Westt Steakhouse | Risque élevé
**File:** outreach/40westt-pitch.txt
**Recipient:** Stefano (owner)
**Priority:** HIGH - 35/100 score, 23K+ visitors

---

## SEND METHOD OPTIONS

### Option 1: Manual Send (FASTEST - DO THIS NOW)
1. Open your email client
2. Copy/paste from the .txt files
3. Send immediately
4. Track opens/replies manually

### Option 2: Resend API (If configured)
```bash
# Lou's Owner Email
curl -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "compliance@yourdomain.com",
    "to": "gm@louspointeclaire.com",
    "subject": "Alerte conformité Loi 96 - Lou'\''s Pointe Claire | Risque critique",
    "text": "$(cat outreach/louspointeclaire-pitch-owner.txt)"
  }'

# 40 Westt Email
curl -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "compliance@yourdomain.com",
    "to": "info@40westt.com",
    "subject": "Alerte conformité Loi 96 - 40 Westt Steakhouse | Risque élevé",
    "text": "$(cat outreach/40westt-pitch.txt)"
  }'
```

### Option 3: Gmail/Outlook (RECOMMENDED FOR NOW)
- Use your personal/business email
- Positions you as local consultant, not automated system
- Higher deliverability
- Personal touch = better response rate

---

## EXPECTED RESPONSES

### Immediate (Within 2 hours)
- "Who are you?"
- "How did you get this information?"
- "Send me the report"

### Same Day (Within 8 hours)
- "We're interested, can we schedule a call?"
- "What's your pricing?"
- "Is this legitimate?"

### No Response (48 hours)
- Follow-up phone call
- Second email with subject: "2ème avis - [Business Name]"

---

## WHILE WAITING FOR REPLIES

1. ✅ Build platform_scraper.py for restaurants-us.com goldmine
2. ✅ Create generate_pdf.py for when they reply "Yes"
3. ✅ Prepare phone script for follow-up calls
4. ✅ Scout 20 more leads in Westmount/NDG

---

## PDF GENERATION (WHEN THEY REPLY)

When Peter/Stefano replies "Yes, send the PDF":

1. Run: `python generate_pdf.py louspointeclaire-2026-03-09.json`
2. Generates: `reports/louspointeclaire-audit-report.pdf`
3. Email back within 15 minutes with PDF attached
4. Include pricing in PDF footer: $2,000-$4,000 vs $30,000 OQLF fine

---

## SUCCESS METRICS

- **Open Rate Target:** 60%+ (legal subject lines get opened)
- **Reply Rate Target:** 25%+ (fear + solution = action)
- **Call Booking Target:** 10%+ (1 in 10 books consultation)
- **Conversion Target:** 5%+ (1 in 20 becomes paying client)

**With 4 HIGH RISK leads sent = Expected 1 consultation, potential 1 client**

---

## TIMING IS EVERYTHING

**8:20 AM Monday:** ✅ PERFECT - Inbox clearing time
**9:00 AM - 11:00 AM:** Good - Still checking email
**11:00 AM - 2:00 PM:** BAD - Lunch rush, won't see it
**2:00 PM - 5:00 PM:** Medium - Afternoon lull
**After 5:00 PM:** BAD - End of day, will forget by tomorrow

**SEND NOW = MAXIMUM IMPACT**

---

## STOP READING. START SENDING. 🚀
