# 🚀 Quick Start Guide - Bill 96 Autonomous Firm

## System Status: ACTIVE ✅

Your autonomous compliance firm is now operational with:
- ✅ Playwright MCP configured for browser automation
- ✅ Bill 96 Auditor steering rules loaded
- ✅ Auto-audit hook on `leads.txt` changes
- ✅ High-risk alert system (score < 30)
- ✅ 6 initial leads queued for audit

## Current Leads (March 9, 2026)

### West Island Targets:
1. Lou's Pointe Claire - New American restaurant
2. 40 Westt Steakhouse - High-end steakhouse
3. Cafe Milano West Island - Italian cafe
4. Brasserie Le Manoir - French brasserie (ironic target)

### Old Montreal Targets:
5. The Farsides (via Food N Fashion guide)
6. Il Cortile - Italian courtyard restaurant

## How to Run Your First Audit

### Option 1: Automatic (Recommended)
The leads are already in `leads.txt`. The Agent Hook will trigger automatically.

### Option 2: Manual Test
Tell Kiro:
```
"Audit the first URL in leads.txt using Playwright. Follow the bill96-auditor.md rules and generate the report."
```

### Option 3: Scout More Leads
Tell Kiro:
```
"Use web search to find 10 more English-only restaurant websites in Westmount and add them to leads.txt"
```

## What Happens Next

1. **Audit Trigger**: When `leads.txt` is saved, the hook fires
2. **Browser Automation**: Playwright loads each URL
3. **Compliance Check**: 
   - HTML lang attribute
   - Visual French predominance
   - Legal documents in French
   - Trademark descriptors
4. **Report Generation**: `reports/[domain]-[date].json`
5. **Email Draft**: `outreach/[domain]-pitch.txt`
6. **High-Risk Alert**: If score < 30, you get notified immediately

## Expected High-Risk Targets

Based on 2026 enforcement patterns:
- **Lou's Pointe Claire**: English branding, likely English-only legal docs
- **40 Westt Steakhouse**: Premium English site, high fine potential
- **Il Cortile**: Italian restaurant, may lack French predominance

## The "Undercover Inspector" Pitch

Your email template is in `templates/undercover-inspector-2026.txt`

Key elements:
- References March-June 2026 inspection season
- Mentions $30,000 fine potential
- Non-threatening, helpful tone
- 15-minute free consultation offer
- Urgency without fear-mongering

## Mobile Notifications (Optional)

To get phone alerts for high-risk leads:

1. Sign up for IFTTT or Pushover
2. Get your webhook URL
3. Copy `.env.example` to `.env`
4. Add your webhook URL
5. The high-risk hook will ping your phone automatically

## Revenue Potential

With 6 leads queued:
- Expected 3-4 HIGH RISK findings (score < 50)
- Average consultation fee: $500-1,500
- Compliance package: $2,000-5,000
- Potential first-week revenue: $6,000-15,000

## Next Steps

1. ✅ System is ready - leads are queued
2. ⏳ Wait for audit hook to process (or trigger manually)
3. 📊 Review reports in `reports/` folder
4. ✉️ Customize pitch emails in `outreach/` folder
5. 📞 Start outreach to HIGH RISK targets first
6. 💰 Close your first compliance client

---

**Pro Tip**: The OQLF's "Undercover Inspector" phase runs March-June 2026. Your timing is perfect - businesses are most receptive to compliance help during active enforcement periods.

**Ready to launch?** The system is autonomous. Just monitor the `reports/` folder for new audits.
