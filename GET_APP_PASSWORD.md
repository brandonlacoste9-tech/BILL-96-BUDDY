# Get Gmail App Password - Quick Steps

## 1. Enable 2-Step Verification (if not already enabled)
https://myaccount.google.com/security

Click "2-Step Verification" → Follow prompts

## 2. Generate App Password
https://myaccount.google.com/apppasswords

- Select app: **Mail**
- Select device: **Other (Custom name)**
- Name: **Zyeuté Québec API**
- Click **Generate**

## 3. Copy the Password
You'll see something like:
```
abcd efgh ijkl mnop
```

## 4. Remove Spaces and Set Environment Variable
```powershell
$env:GMAIL_APP_PASSWORD="abcdefghijklmnop"
```

## 5. Test It
```powershell
python -c "import os; print('Password set!' if os.getenv('GMAIL_APP_PASSWORD') else 'Not set')"
```

---

**Once you have the password set, we'll test the full system!**
