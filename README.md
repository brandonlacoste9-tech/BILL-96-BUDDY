# Zyeuté Québec - Automated Bill 96 Compliance Audits

**Website:** www.zyeutequebec.com  
**Email:** zyeutequebec@gmail.com

Automated Bill 96 compliance auditing system for Quebec businesses. Detects HTML lang violations, visual predominance issues, legal document gaps, and trademark compliance problems.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

### 2. Set Gmail App Password
```bash
export GMAIL_APP_PASSWORD="your-16-char-password"
```
See `GMAIL_SETUP.md` for detailed instructions.

### 3. Start API Server
```bash
python auto_audit_api.py
```

### 4. Test
```bash
python test_api.py
```

---

## 📁 Project Structure

```
├── auto_audit_api.py              # Main Flask API endpoint
├── gmail_automation.py            # Email sending automation
├── audit_4_targets.py             # Batch audit script
├── linkedin_hunter.py             # OSINT decision maker finder
├── generate_pdf.py                # PDF report generator
├── website_form_integration.html  # Website form code
├── reports/                       # Audit JSON reports
├── outreach/                      # Generated email drafts
├── templates/                     # Email templates
└── .kiro/                         # Kiro IDE configuration
    ├── steering/                  # Bill 96 audit methodology
    └── hooks/                     # Automation triggers
```

---

## 🎯 Features

- ✅ Automated Playwright browser audits
- ✅ 4-factor compliance scoring (HTML 40%, Visual 30%, Legal 20%, Trademark 10%)
- ✅ Personalized email generation
- ✅ Gmail automation (zyeutequebec@gmail.com)
- ✅ CRM lead tracking (outreach_log.json)
- ✅ Screenshot evidence capture
- ✅ JSON report generation

---

## 📊 Compliance Scoring

- **90-100**: Compliant
- **70-89**: Minor issues
- **50-69**: Moderate risk
- **30-49**: HIGH risk
- **0-29**: CRITICAL risk

---

## 🔧 API Endpoints

### POST /audit
Run Bill 96 compliance audit on a website.

**Request:**
```json
{
  "url": "https://example.com",
  "business_name": "Example Restaurant",
  "email": "owner@example.com",
  "phone": "514-XXX-XXXX"
}
```

**Response:**
```json
{
  "success": true,
  "audit_result": {
    "compliance_score": 35,
    "risk_level": "HIGH",
    "violations": [...]
  },
  "email_sent": true
}
```

### GET /health
Health check endpoint.

---

## 📚 Documentation

- **AUTOMATION_COMPLETE.md** - Overview and next steps
- **DEPLOYMENT_GUIDE.md** - Cloud deployment instructions
- **GMAIL_SETUP.md** - Gmail App Password setup
- **AUTOMATION_ARCHITECTURE.md** - System architecture

---

## 🚀 Deployment

### Railway (Recommended)
```bash
railway login
railway init
railway variables set GMAIL_APP_PASSWORD=your-password
railway up
```

### Heroku
```bash
heroku create zyeute-quebec
heroku config:set GMAIL_APP_PASSWORD=your-password
git push heroku main
```

---

## 📈 Target Metrics (Month 1)

- 100+ form submissions
- 80+ emails sent
- 20+ replies (25% rate)
- 10+ consultations
- 5+ clients closed
- **$20K-$40K revenue**

---

## 💰 Revenue Model

- **Free Audit** (lead magnet)
- **Compliance Fix**: $2K-$5K
- **Monitoring**: $150/month

---

## 🎯 Target Clients

- High-end restaurants (West Island, Old Montreal)
- Retail chains (5+ locations)
- Professional services
- E-commerce sites

---

## 📞 Support

Questions? Check the documentation files or review code comments.

---

**Built with Kiro IDE** 🚀
