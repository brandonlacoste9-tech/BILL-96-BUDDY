# 🚀 Deploy Zyeuté Québec Without CLI (Disk Full Workaround)

## Problem: Your C: drive has 0 bytes free

## Solution: Deploy via GitHub + Railway Web Interface

---

## Step 1: Push Code to GitHub (5 minutes)

### 1. Create .gitignore
Already exists, but verify it includes:
```
.env
*.pyc
__pycache__/
reports/*.png
email_log.json
outreach_log.json
```

### 2. Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Zyeuté Québec - Automated Bill 96 Audit System"
```

### 3. Create GitHub Repo
- Go to https://github.com/new
- Name: `zyeute-quebec`
- Description: "Automated Bill 96 compliance auditing system"
- Public or Private (your choice)
- Click "Create repository"

### 4. Push to GitHub
```bash
git remote add origin https://github.com/YOUR-USERNAME/zyeute-quebec.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Railway (5 minutes)

### 1. Sign Up for Railway
- Go to https://railway.app/
- Click "Login" → "Login with GitHub"
- Authorize Railway

### 2. Create New Project
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose `zyeute-quebec` repo
- Click "Deploy Now"

### 3. Configure Environment Variables
- Click on your deployed service
- Go to "Variables" tab
- Click "New Variable"
- Add:
  ```
  GMAIL_APP_PASSWORD=your-16-char-password
  ```
- Click "Add"

### 4. Wait for Deployment
- Railway will automatically:
  - Install dependencies from `requirements.txt`
  - Install Playwright
  - Start `auto_audit_api.py` (from Procfile)
- Takes 2-3 minutes

### 5. Get Your URL
- Click "Settings" tab
- Click "Generate Domain"
- You'll get: `https://zyeute-quebec-production.up.railway.app`
- Copy this URL

---

## Step 3: Test Your API (2 minutes)

### Test Health Endpoint
Open in browser:
```
https://your-railway-url.up.railway.app/health
```

Should see:
```json
{"status": "healthy", "service": "Zyeuté Québec Audit API"}
```

### Test Audit Endpoint
Use this PowerShell command:
```powershell
$body = @{
    url = "https://www.louspointeclaire.com"
    business_name = "Lou's Pointe Claire"
    email = "test@example.com"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://your-railway-url.up.railway.app/audit" -Method Post -Body $body -ContentType "application/json"
```

---

## Step 4: Update Website Form (3 minutes)

### 1. Open zyeutequebec.com editor

### 2. Find the form JavaScript section

### 3. Update API_ENDPOINT:
```javascript
const API_ENDPOINT = 'https://your-railway-url.up.railway.app/audit';
```

### 4. Save and publish

---

## Step 5: Test End-to-End (2 minutes)

### 1. Visit www.zyeutequebec.com

### 2. Fill out the form:
- Business Name: "Test Restaurant"
- URL: "https://www.louspointeclaire.com"
- Email: your-email@example.com

### 3. Submit

### 4. Check your email
You should receive an email from zyeutequebec@gmail.com with:
- Subject: "Alerte conformité Loi 96 - Test Restaurant | Risque critique"
- Compliance score
- Violations found
- Offer for free PDF report

---

## Step 6: Monitor & Scale

### View Logs in Railway
- Go to your Railway project
- Click "Deployments" tab
- Click latest deployment
- View real-time logs

### Check Metrics
- Railway dashboard shows:
  - CPU usage
  - Memory usage
  - Request count
  - Response times

### Scale if Needed
- Railway auto-scales
- Free tier: $5/month credit (500 hours)
- Upgrade if you exceed limits

---

## Alternative: Heroku (If Railway Doesn't Work)

### 1. Sign up at https://heroku.com

### 2. Create New App
- Click "New" → "Create new app"
- Name: `zyeute-quebec`
- Region: US

### 3. Connect GitHub
- Go to "Deploy" tab
- Select "GitHub" deployment method
- Connect your `zyeute-quebec` repo
- Enable "Automatic Deploys"

### 4. Add Buildpacks
- Go to "Settings" tab
- Click "Add buildpack"
- Add: `heroku/python`

### 5. Set Environment Variable
- Go to "Settings" tab
- Click "Reveal Config Vars"
- Add:
  - KEY: `GMAIL_APP_PASSWORD`
  - VALUE: `your-16-char-password`

### 6. Deploy
- Go to "Deploy" tab
- Click "Deploy Branch" (main)
- Wait 2-3 minutes

### 7. Get URL
Your app will be at: `https://zyeute-quebec.herokuapp.com`

---

## Alternative: Render.com (Free Tier)

### 1. Sign up at https://render.com

### 2. New Web Service
- Click "New +" → "Web Service"
- Connect GitHub repo
- Name: `zyeute-quebec`
- Runtime: Python 3
- Build Command: `pip install -r requirements.txt && python -m playwright install chromium`
- Start Command: `python auto_audit_api.py`

### 3. Environment Variables
- Add `GMAIL_APP_PASSWORD`

### 4. Deploy
- Click "Create Web Service"
- Free tier available

---

## Gmail App Password (Do This First!)

### 1. Go to Gmail Account
- Login to zyeutequebec@gmail.com

### 2. Enable 2FA
- https://myaccount.google.com/security
- Turn on 2-Step Verification

### 3. Generate App Password
- https://myaccount.google.com/apppasswords
- Select "Mail" → "Other"
- Name: "Railway API"
- Copy the 16-character password
- Remove spaces: `abcdefghijklmnop`

---

## 🎉 You're Live!

Once deployed, your system:
1. ✅ Receives form submissions from zyeutequebec.com
2. ✅ Runs automated Playwright audits
3. ✅ Sends personalized emails via Gmail
4. ✅ Logs leads to CRM
5. ✅ Runs 24/7 with zero maintenance

**Next Steps:**
- Share zyeutequebec.com on LinkedIn
- Email 10 restaurant owners
- Run Google Ads targeting "loi 96 conformité"
- Monitor `outreach_log.json` for leads
- Reply to "YES" responses with PDF reports
- Book consultations
- Close deals at $2K-$5K each

**Target: 5 clients in 30 days = $20K revenue** 🚀

---

## Troubleshooting

### "Module not found" errors on Railway
- Check `requirements.txt` is in root directory
- Verify Railway detected Python buildpack
- Check deployment logs for errors

### Emails not sending
- Verify GMAIL_APP_PASSWORD is set correctly
- Check 2FA is enabled on Gmail
- Try generating new App Password
- Check Railway logs for SMTP errors

### Form not submitting
- Check browser console for errors
- Verify API_ENDPOINT URL is correct
- Test API health endpoint first
- Check CORS settings if needed

---

## Need Help?

- Railway docs: https://docs.railway.app/
- Heroku docs: https://devcenter.heroku.com/
- Render docs: https://render.com/docs
- Gmail App Password: https://myaccount.google.com/apppasswords

**You've got this! 🚀**
