# Zyeuté Québec - Full Automation Architecture

## Overview
Transform www.zyeutequebec.com into a self-service lead generation machine that:
1. Captures business URLs from website form
2. Runs automated Bill 96 audits
3. Generates PDF reports
4. Sends personalized outreach emails
5. Tracks leads in CRM pipeline

---

## Architecture Components

### 1. FRONTEND (zyeutequebec.com)
**Current Status:** ✅ Live
**Components:**
- Landing page with value proposition
- "Obtenez votre audit technique gratuit" form
- Form fields: Business URL, Email, Business Name, Phone (optional)

### 2. FORM SUBMISSION HANDLER
**Technology:** Webhook endpoint (Zapier, Make.com, or custom Flask API)
**Flow:**
```
User submits form → Webhook receives data → Triggers audit pipeline
```

### 3. AUDIT PIPELINE (Python Backend)
**File:** `auto_audit_api.py`
**Process:**
1. Receive URL from webhook
2. Run Playwright audit (test_lous_playwright_audit.py logic)
3. Calculate compliance score
4. Generate JSON report
5. Generate PDF report (generate_pdf.py)
6. Hunt for decision maker (linkedin_hunter.py)
7. Generate personalized email (outreach template)
8. Send email via Outlook API
9. Log to CRM (outreach_log.json)

### 4. PDF REPORT GENERATOR
**File:** `generate_pdf.py` (already exists)
**Enhancements needed:**
- Add Zyeuté Québec branding
- Include screenshot evidence
- Add pricing at bottom ($2K-$5K vs $30K fine)
- Professional layout with logo

### 5. EMAIL AUTOMATION
**Current:** Manual Outlook send
**Upgrade to:** Microsoft Graph API (Outlook automation)
**Flow:**
```
Audit complete → Generate email → Send via Graph API → Log in CRM
```

### 6. CRM / LEAD TRACKING
**File:** `outreach_log.json` (already exists)
**Schema:**
```json
{
  "leads": [
    {
      "business_name": "Lou's Pointe Claire",
      "url": "https://louspointeclaire.com",
      "email": "gm@louspointeclaire.com",
      "phone": "514-xxx-xxxx",
      "compliance_score": 0,
      "risk_level": "CRITICAL",
      "audit_date": "2026-03-09",
      "email_sent": true,
      "email_sent_date": "2026-03-09 08:30",
      "status": "awaiting_reply",
      "reply_received": false,
      "consultation_booked": false,
      "deal_value": null
    }
  ]
}
```

---

## Implementation Plan

### Phase 1: Backend API (TODAY)
1. Create Flask API endpoint to receive form submissions
2. Integrate existing audit_4_targets.py logic
3. Test with manual POST requests

### Phase 2: Form Integration (TODAY)
1. Add form submission webhook to zyeutequebec.com
2. Connect to Flask API
3. Test end-to-end flow

### Phase 3: Email Automation (TOMORROW)
1. Set up Microsoft Graph API credentials
2. Automate email sending
3. Test with real leads

### Phase 4: PDF Branding (TOMORROW)
1. Add Zyeuté Québec logo and branding
2. Professional layout
3. Include pricing strategy

### Phase 5: CRM Dashboard (WEEK 2)
1. Build simple web dashboard to view leads
2. Track conversion funnel
3. Monitor reply rates

---

## Technology Stack

### Backend
- Python 3.x
- Flask (API endpoint)
- Playwright (browser automation)
- ReportLab or WeasyPrint (PDF generation)
- Microsoft Graph API (email automation)

### Frontend
- zyeutequebec.com (already built)
- Form submission via Fetch API or Zapier

### Infrastructure
- Local Python server (for testing)
- Cloud deployment: Heroku, Railway, or DigitalOcean (production)
- Database: JSON files (MVP) → PostgreSQL (scale)

---

## Webhook Integration Options

### Option A: Zapier (No Code - FASTEST)
1. Add Zapier webhook to form
2. Zapier triggers Python script via webhook
3. Cost: $20/month

### Option B: Make.com (No Code)
1. Similar to Zapier
2. More affordable: $9/month

### Option C: Custom Flask API (Full Control)
1. Deploy Flask app to Railway/Heroku
2. Form posts directly to your API
3. Cost: Free tier available

---

## Next Steps (RIGHT NOW)

1. **Create Flask API endpoint** (`auto_audit_api.py`)
2. **Test with curl/Postman** (manual POST request)
3. **Integrate with zyeutequebec.com form**
4. **Run first automated audit**

---

## Success Metrics

### Week 1 Target:
- 10 form submissions
- 10 automated audits
- 10 emails sent
- 2-3 replies

### Month 1 Target:
- 100 form submissions
- 25 replies (25% reply rate)
- 10 consultations booked
- 5 clients closed ($10K-$25K revenue)

---

## Competitive Advantage

**Traditional agencies:**
- Manual audits (2-3 days)
- $500-$1000 audit fee
- 2-week turnaround

**Zyeuté Québec (automated):**
- Instant audits (2 minutes)
- FREE audit + PDF report
- 24-hour turnaround
- Scalable to 100+ audits/day

**This is your moat.** 🚀
