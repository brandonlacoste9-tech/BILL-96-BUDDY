# Zyeuté Québec - Complete Deployment Guide

## 🎯 What You've Built

A fully automated Bill 96 compliance audit system that:
1. ✅ Receives form submissions from www.zyeutequebec.com
2. ✅ Runs automated Playwright audits (HTML lang, visual predominance, legal docs, trademarks)
3. ✅ Calculates compliance scores (0-100)
4. ✅ Generates JSON reports
5. ✅ Sends personalized emails via zyeutequebec@gmail.com
6. ✅ Logs leads to CRM (outreach_log.json)

---

## 📋 Prerequisites

### 1. Python Dependencies
```bash
pip install flask playwright requests python-dotenv
python -m playwright install chromium
```

### 2. Gmail App Password
Follow `GMAIL_SETUP.md` to generate App Password for zyeutequebec@gmail.com

### 3. Set Environment Variable
```bash
# Windows PowerShell
$env:GMAIL_APP_PASSWORD="your-16-char-password"

# Linux/Mac
export GMAIL_APP_PASSWORD="your-16-char-password"
```

---

## 🚀 Local Testing (5 Minutes)

### Step 1: Start the API Server
```bash
python auto_audit_api.py
```

You should see:
```
======================================================================
ZYEUTÉ QUÉBEC - AUTOMATED AUDIT API
======================================================================
Starting Flask server on http://localhost:5000
Endpoints:
  POST /audit - Run Bill 96 audit
  GET /health - Health check
======================================================================
```

### Step 2: Test the API
Open a new terminal and run:
```bash
python test_api.py
```

This will:
- Send a test audit request for Lou's Pointe Claire
- Run the full Playwright audit
- Generate JSON report
- Send automated email (if HIGH/CRITICAL risk)
- Log to CRM

Expected output:
```
✅ SUCCESS!

Audit Result:
  Business: Lou's Pointe Claire
  Score: 0/100
  Risk Level: CRITICAL
  Violations: 4

Report saved: reports/louspointeclaire-2026-03-09.json
Lead logged: True
Email sent: True
```

### Step 3: Verify Email Sent
Check the inbox of the test email address. You should receive:
```
Subject: Alerte conformité Loi 96 - Lou's Pointe Claire | Risque critique

From: Zyeuté Québec <zyeutequebec@gmail.com>
```

---

## 🌐 Website Integration

### Option A: Direct API Integration (Recommended)

1. Copy `website_form_integration.html` code
2. Paste into your zyeutequebec.com page
3. Update `API_ENDPOINT` to your deployed URL:
   ```javascript
   const API_ENDPOINT = 'https://your-api.railway.app/audit';
   ```

### Option B: Zapier/Make.com (No Code)

1. Add Zapier webhook to your form
2. Zapier triggers HTTP POST to your API
3. Cost: $20/month (Zapier) or $9/month (Make.com)

---

## ☁️ Cloud Deployment

### Option 1: Railway (Easiest - Recommended)

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Initialize project:**
   ```bash
   railway init
   ```

4. **Set environment variable:**
   ```bash
   railway variables set GMAIL_APP_PASSWORD=your-password
   ```

5. **Deploy:**
   ```bash
   railway up
   ```

6. **Get your URL:**
   ```bash
   railway domain
   ```
   Example: `https://zyeute-quebec-production.up.railway.app`

7. **Update website form** with your Railway URL

**Cost:** $5/month (500 hours free tier)

---

### Option 2: Heroku

1. **Install Heroku CLI:**
   ```bash
   # Windows
   winget install Heroku.HerokuCLI
   
   # Mac
   brew tap heroku/brew && brew install heroku
   ```

2. **Create Procfile:**
   ```bash
   echo "web: python auto_audit_api.py" > Procfile
   ```

3. **Create requirements.txt:**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Deploy:**
   ```bash
   heroku login
   heroku create zyeute-quebec
   heroku config:set GMAIL_APP_PASSWORD=your-password
   git push heroku main
   ```

**Cost:** $7/month (Eco Dynos)

---

### Option 3: DigitalOcean App Platform

1. Connect GitHub repo
2. Set environment variable in dashboard
3. Deploy with one click

**Cost:** $5/month (Basic plan)

---

## 📊 Monitoring & Analytics

### Lead Tracking
All leads are logged to `outreach_log.json`:
```json
{
  "leads": [
    {
      "business_name": "Lou's Pointe Claire",
      "compliance_score": 0,
      "risk_level": "CRITICAL",
      "email_sent": true,
      "status": "awaiting_reply"
    }
  ]
}
```

### Email Tracking
All sent emails logged to `email_log.json`:
```json
{
  "emails": [
    {
      "business_name": "Lou's Pointe Claire",
      "recipient_email": "gm@louspointeclaire.com",
      "sent_at": "2026-03-09T08:30:00",
      "compliance_score": 0
    }
  ]
}
```

### Conversion Funnel
Track these metrics:
- Form submissions (API calls)
- Audits completed (JSON reports generated)
- Emails sent (email_log.json)
- Replies received (manual tracking)
- Consultations booked (manual tracking)
- Deals closed (manual tracking)

---

## 🎯 Next Steps

### Week 1: Test & Validate
- [ ] Deploy API to Railway/Heroku
- [ ] Integrate form on zyeutequebec.com
- [ ] Test with 5-10 real restaurant URLs
- [ ] Verify emails are being received
- [ ] Monitor reply rates

### Week 2: Scale
- [ ] Add PDF report generation
- [ ] Implement LinkedIn hunter for decision makers
- [ ] Build simple CRM dashboard
- [ ] Set up email reply tracking
- [ ] Create follow-up email sequences

### Week 3: Optimize
- [ ] A/B test email subject lines
- [ ] Optimize compliance scoring algorithm
- [ ] Add more violation detection rules
- [ ] Improve email personalization
- [ ] Track conversion rates

### Month 2: Automate Everything
- [ ] Auto-reply to "YES" responses with PDF
- [ ] Auto-schedule consultation calls
- [ ] Auto-generate proposals
- [ ] Auto-send follow-up sequences
- [ ] Build client portal

---

## 🔧 Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

### "GMAIL_APP_PASSWORD not set"
```bash
# Check if set
echo $GMAIL_APP_PASSWORD  # Linux/Mac
echo $env:GMAIL_APP_PASSWORD  # Windows PowerShell

# Set it
export GMAIL_APP_PASSWORD="your-password"  # Linux/Mac
$env:GMAIL_APP_PASSWORD="your-password"  # Windows PowerShell
```

### "Connection refused" on API
- Make sure `auto_audit_api.py` is running
- Check firewall settings
- Verify port 5000 is not blocked

### Emails not sending
- Verify Gmail App Password is correct
- Check 2FA is enabled on Gmail account
- Try generating new App Password
- Check spam folder

### Playwright timeout errors
- Increase timeout in `audit_site()` function
- Check internet connection
- Some sites block headless browsers (add user agent)

---

## 📈 Success Metrics

### Target Funnel (Month 1):
```
100 form submissions
  ↓ 100% (automated)
100 audits completed
  ↓ 80% (HIGH/CRITICAL only)
80 emails sent
  ↓ 25% reply rate
20 replies received
  ↓ 50% consultation rate
10 consultations booked
  ↓ 50% close rate
5 clients closed
  ↓ $4K average deal
$20,000 revenue
```

### Key Metrics to Track:
- **Form submission rate** (website visitors → submissions)
- **Audit completion rate** (should be 100%)
- **Email delivery rate** (should be 99%+)
- **Email open rate** (target: 60%+)
- **Reply rate** (target: 25%+)
- **Consultation booking rate** (target: 50% of replies)
- **Close rate** (target: 50% of consultations)

---

## 🚀 You're Ready!

Your autonomous Bill 96 compliance firm is now operational. Every form submission on www.zyeutequebec.com will:

1. ✅ Trigger automated audit
2. ✅ Generate compliance report
3. ✅ Send personalized email
4. ✅ Log lead to CRM
5. ✅ Track in analytics

**No manual work required until they reply "YES"** 🎯

---

## 📞 Support

If you need help:
1. Check `GMAIL_SETUP.md` for email issues
2. Check `AUTOMATION_ARCHITECTURE.md` for system overview
3. Review logs in terminal output
4. Check `outreach_log.json` and `email_log.json`

**Let's close 10 clients in 30 days!** 🚀
