# 🚀 Deploy Zyeuté Québec - Action Plan

## ⚠️ Current Issue: Disk Space Full

Your C: drive has 0 bytes free. You have two options:

---

## Option A: Free Up Space (10 minutes)

### 1. Clean Windows Temp Files
```powershell
# Run Disk Cleanup
cleanmgr /d C:

# Or manually delete temp files
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
```

### 2. Clear Python Cache
```powershell
# Delete pip cache
pip cache purge

# Delete Python __pycache__ folders
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

### 3. Check Space
```powershell
Get-PSDrive C | Select-Object Used,Free
```

### 4. Install Dependencies
```bash
pip install flask playwright requests python-dotenv
python -m playwright install chromium
```

---

## Option B: Deploy Directly to Cloud (15 minutes - RECOMMENDED)

Skip local testing and deploy straight to Railway where disk space isn't an issue.

### 1. Install Railway CLI
```bash
npm install -g @railway/cli
```

### 2. Login to Railway
```bash
railway login
```

### 3. Initialize Project
```bash
railway init
```

### 4. Set Environment Variable
```bash
railway variables set GMAIL_APP_PASSWORD=your-16-char-password
```

### 5. Deploy
```bash
railway up
```

### 6. Get Your URL
```bash
railway domain
```

You'll get something like: `https://zyeute-quebec-production.up.railway.app`

### 7. Test Your API
```bash
curl https://your-railway-url.up.railway.app/health
```

Should return:
```json
{"status": "healthy", "service": "Zyeuté Québec Audit API"}
```

### 8. Update Website Form
Copy `website_form_integration.html` and update:
```javascript
const API_ENDPOINT = 'https://your-railway-url.up.railway.app/audit';
```

---

## Option C: Use GitHub Codespaces (Free, 60 hours/month)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/zyeute-quebec.git
git push -u origin main
```

### 2. Open in Codespaces
- Go to your GitHub repo
- Click "Code" → "Codespaces" → "Create codespace"
- You get a cloud VM with plenty of space

### 3. Install & Test
```bash
pip install -r requirements.txt
python -m playwright install chromium
python auto_audit_api.py
```

### 4. Deploy from Codespaces
```bash
railway login
railway up
```

---

## 🎯 Recommended Path: Option B (Railway Direct Deploy)

**Why?**
- No local disk space needed
- Automatic HTTPS
- Free $5/month credit
- Takes 15 minutes
- Production-ready immediately

**Steps:**
1. Get Gmail App Password (5 min)
2. Install Railway CLI (2 min)
3. Deploy (5 min)
4. Update website form (3 min)
5. Test with real submission (1 min)

---

## Gmail App Password Setup (Do This First)

### 1. Enable 2FA on zyeutequebec@gmail.com
- Go to https://myaccount.google.com/security
- Enable 2-Step Verification

### 2. Generate App Password
- Go to https://myaccount.google.com/apppasswords
- Select "Mail" → "Other (Custom name)"
- Name it: "Zyeuté Québec API"
- Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)
- Remove spaces: `abcdefghijklmnop`

### 3. Save It
You'll need this for Railway deployment.

---

## After Deployment

### Test Your API
```bash
# Health check
curl https://your-url.railway.app/health

# Test audit (replace with your URL)
curl -X POST https://your-url.railway.app/audit \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.louspointeclaire.com",
    "business_name": "Lou'\''s Pointe Claire",
    "email": "test@example.com"
  }'
```

### Monitor Logs
```bash
railway logs
```

### Check Lead Tracking
Railway will create `outreach_log.json` and `email_log.json` automatically.

---

## Website Integration

Once deployed, add this to zyeutequebec.com:

```html
<script>
const API_ENDPOINT = 'https://your-railway-url.up.railway.app/audit';

document.getElementById('audit-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = {
    business_name: document.getElementById('business-name').value,
    url: document.getElementById('url').value,
    email: document.getElementById('email').value,
    phone: document.getElementById('phone').value || null
  };
  
  const response = await fetch(API_ENDPOINT, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(formData)
  });
  
  const result = await response.json();
  
  if (result.success) {
    alert(`✅ Audit terminé! Score: ${result.audit_result.compliance_score}/100. Vérifiez votre courriel.`);
  }
});
</script>
```

---

## 🎉 You're Live!

Once deployed:
1. ✅ API running 24/7 on Railway
2. ✅ Form submissions trigger audits
3. ✅ Emails sent automatically
4. ✅ Leads logged to CRM
5. ✅ Ready to scale to 100+ audits/day

**Next:** Share zyeutequebec.com on LinkedIn, email 10 restaurant owners, and watch the leads roll in! 🚀

---

## Need Help?

- Railway docs: https://docs.railway.app/
- Gmail App Password: https://myaccount.google.com/apppasswords
- Check `DEPLOYMENT_GUIDE.md` for detailed instructions
