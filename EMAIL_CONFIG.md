# Email Configuration

## Current Setup

### Sender Email (FROM):
**zyeutequebec@gmail.com**
- This is the email that appears in the "From" field
- Must be verified in SendGrid
- Professional branding

### Reply-To Email:
**northern-ventures@outlook.com** (default)
- This is where replies actually go
- You can change this anytime

---

## How to Change Reply-To Email

### Option 1: Use northern-ventures@outlook.com (Default)
No action needed - already configured!

### Option 2: Use zyeutequebec@gmail.com
```powershell
$env:REPLY_TO_EMAIL="zyeutequebec@gmail.com"
```

### Option 3: Use a different email
```powershell
$env:REPLY_TO_EMAIL="your-email@example.com"
```

---

## How It Works

When you send an email:
- **From:** zyeutequebec@gmail.com (professional branding)
- **Reply-To:** northern-ventures@outlook.com (where replies go)

When a restaurant owner clicks "Reply":
- Their email client automatically addresses it to: **northern-ventures@outlook.com**
- You receive all replies in your Outlook inbox

---

## For Deployment (Railway)

Set the environment variable:
```bash
railway variables set REPLY_TO_EMAIL=northern-ventures@outlook.com
```

Or in Railway dashboard:
- Go to Variables
- Add: `REPLY_TO_EMAIL` = `northern-ventures@outlook.com`

---

## Email Signature

All emails include:
```
Cordialement,

L'équipe Zyeuté Québec
Conformité numérique Loi 96
zyeutequebec@gmail.com
www.zyeutequebec.com
```

But replies go to: **northern-ventures@outlook.com** ✅

---

## Testing

To verify reply-to is working:
1. Send yourself a test email
2. Click "Reply" in your inbox
3. Check the "To" field - should show northern-ventures@outlook.com

---

**All replies will go to northern-ventures@outlook.com by default!** 📧
