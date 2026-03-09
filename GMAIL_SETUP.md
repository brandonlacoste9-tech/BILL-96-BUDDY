# Gmail Automation Setup Guide

## Email Account
**Address:** zyeutequebec@gmail.com

---

## Step 1: Enable 2-Factor Authentication

1. Go to https://myaccount.google.com/security
2. Click "2-Step Verification"
3. Follow the prompts to enable 2FA (required for App Passwords)

---

## Step 2: Generate App Password

1. Go to https://myaccount.google.com/apppasswords
2. Select app: "Mail"
3. Select device: "Other (Custom name)"
4. Enter name: "Zyeuté Québec Automation"
5. Click "Generate"
6. **COPY THE 16-CHARACTER PASSWORD** (you won't see it again)

Example: `abcd efgh ijkl mnop`

---

## Step 3: Set Environment Variable

### Windows (PowerShell):
```powershell
$env:GMAIL_APP_PASSWORD="abcdefghijklmnop"
```

### Windows (CMD):
```cmd
set GMAIL_APP_PASSWORD=abcdefghijklmnop
```

### Linux/Mac:
```bash
export GMAIL_APP_PASSWORD="abcdefghijklmnop"
```

### Permanent (add to .env file):
```bash
echo "GMAIL_APP_PASSWORD=abcdefghijklmnop" >> .env
```

---

## Step 4: Test Email Sending

```bash
python gmail_automation.py
```

This will generate a test email preview.

To actually send a test email:

```python
from gmail_automation import send_email_gmail

send_email_gmail(
    to_email="your-test-email@example.com",
    subject="Test from Zyeuté Québec",
    body="This is a test email from the automation system."
)
```

---

## Step 5: Verify Automation Works

Run the full API with email automation:

```bash
python auto_audit_api.py
```

Then test with:

```bash
python test_api.py
```

If the audit finds HIGH or CRITICAL risk, it will automatically send an email to the provided address.

---

## Troubleshooting

### "GMAIL_APP_PASSWORD not set"
- Make sure you set the environment variable in the same terminal session
- Or add it to `.env` file and load with `python-dotenv`

### "Authentication failed"
- Double-check the App Password (no spaces)
- Make sure 2FA is enabled on the Gmail account
- Try generating a new App Password

### "SMTP connection error"
- Check your internet connection
- Verify Gmail SMTP is not blocked by firewall
- Try port 587 with STARTTLS instead of 465 with SSL

---

## Security Notes

⚠️ **NEVER commit the App Password to Git!**

Add to `.gitignore`:
```
.env
*.env
GMAIL_APP_PASSWORD
```

The App Password gives full access to send emails from zyeutequebec@gmail.com. Keep it secure!

---

## Email Sending Limits

Gmail free accounts have sending limits:
- **500 emails per day** (rolling 24-hour period)
- **100 recipients per email**

For higher volume, consider:
- Google Workspace (2000 emails/day)
- SendGrid, Mailgun, or AWS SES (unlimited with paid plans)

---

## Next Steps

Once Gmail automation is working:

1. ✅ Test with real audit (Lou's, 40 Westt, etc.)
2. ✅ Integrate with website form
3. ✅ Add PDF report generation
4. ✅ Deploy to cloud (Railway, Heroku, DigitalOcean)
5. ✅ Monitor email delivery rates

---

## Production Deployment

For production, use environment variables on your hosting platform:

**Railway:**
```bash
railway variables set GMAIL_APP_PASSWORD=abcdefghijklmnop
```

**Heroku:**
```bash
heroku config:set GMAIL_APP_PASSWORD=abcdefghijklmnop
```

**DigitalOcean App Platform:**
Add environment variable in dashboard under "App Settings" → "Environment Variables"

---

## Email Template Customization

Edit `gmail_automation.py` to customize:
- Email subject line
- Body content
- Signature
- Urgency messaging based on risk level

Current template automatically adjusts based on:
- Compliance score (0-100)
- Risk level (CRITICAL, HIGH, MODERATE, MINOR, COMPLIANT)
- Specific violations found

---

🚀 **You're ready to automate!**
