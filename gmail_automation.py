#!/usr/bin/env python3
"""
Gmail Automation for Zyeuté Québec
Sends automated outreach emails via zyeutequebec@gmail.com
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime

# Gmail credentials
GMAIL_ADDRESS = "zyeutequebec@gmail.com"
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")  # Set this in .env

def generate_outreach_email(audit_result, recipient_email, recipient_name=None):
    """
    Generate personalized outreach email based on audit results
    """
    
    business_name = audit_result["business_name"]
    score = audit_result["compliance_score"]
    risk_level = audit_result["risk_level"]
    violations = audit_result["violations"]
    
    # Personalized greeting
    if recipient_name:
        greeting = f"Bonjour {recipient_name},"
    else:
        greeting = f"Bonjour à l'équipe de {business_name},"
    
    # Risk-specific messaging
    if risk_level == "CRITICAL":
        urgency = "CRITIQUE"
        urgency_text = "Votre site présente des violations majeures qui déclenchent automatiquement les robots de l'OQLF."
    elif risk_level == "HIGH":
        urgency = "ÉLEVÉ"
        urgency_text = "Votre site présente plusieurs violations qui attirent l'attention des inspecteurs de l'OQLF."
    else:
        urgency = "MODÉRÉ"
        urgency_text = "Votre site présente des problèmes de conformité qui nécessitent une attention."
    
    # Top 2-3 violations
    violation_list = "\n".join([f"• {v}" for v in violations[:3]])
    
    # Email body
    subject = f"Alerte conformité Loi 96 - {business_name} | Risque {urgency.lower()}"
    
    body = f"""{greeting}

Je m'appelle l'équipe de Zyeuté Québec, une firme locale spécialisée en conformité numérique pour la Loi 96.

Nous avons effectué un audit technique de votre site web et identifié des violations critiques qui pourraient déclencher des amendes de l'OQLF allant jusqu'à 30 000 $.

📊 RÉSULTAT DE L'AUDIT : {score}/100 - Risque {urgency}

{urgency_text}

🚨 VIOLATIONS DÉTECTÉES :

{violation_list}

💰 EXPOSITION FINANCIÈRE

L'Office québécois de la langue française (OQLF) déploie maintenant des robots automatisés qui analysent les sites web québécois. Une seule violation de code (comme <html lang="en">) déclenche instantanément un audit formel.

Les amendes commencent à 3 000 $ et peuvent atteindre 30 000 $ par violation, avec des pénalités quotidiennes qui s'accumulent.

✅ NOTRE SOLUTION

Nous ne reconstruisons pas votre site — nous reconfigurons l'architecture en 48 heures pour forcer la conformité au niveau du code source.

• Délai : 48-72 heures
• Tarif forfaitaire : 2 000 $ - 5 000 $ (une fraction d'une seule amende)
• Zéro perturbation visuelle de votre site actuel

📄 VOULEZ-VOUS LE RAPPORT PDF COMPLET ?

Je peux vous envoyer un rapport d'audit forensique gratuit montrant exactement où votre site échoue, avec des captures d'écran et une analyse ligne par ligne du code HTML.

Répondez simplement "OUI" et je vous l'enverrai immédiatement.

Disponible pour un appel rapide cette semaine ?

Cordialement,

L'équipe Zyeuté Québec
Conformité numérique Loi 96
zyeutequebec@gmail.com
www.zyeutequebec.com

---

P.S. : L'OQLF cible activement les restaurants et commerces à haute visibilité dans l'Ouest-de-l'Île et le Grand Montréal. {business_name} est probablement déjà dans leur base de données. Agir maintenant vous protège avant qu'une inspection formelle ne soit déclenchée.
"""
    
    return subject, body

def send_email_gmail(to_email, subject, body, attachment_path=None):
    """
    Send email via Gmail SMTP
    """
    
    if not GMAIL_APP_PASSWORD:
        print("❌ ERROR: GMAIL_APP_PASSWORD not set in environment")
        print("To set up Gmail App Password:")
        print("1. Go to https://myaccount.google.com/apppasswords")
        print("2. Generate new app password for 'Mail'")
        print("3. Set environment variable: export GMAIL_APP_PASSWORD='your-password'")
        return False
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = f"Zyeuté Québec <{GMAIL_ADDRESS}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Add body
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Add attachment if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as f:
                attachment = MIMEApplication(f.read(), _subtype="pdf")
                attachment.add_header('Content-Disposition', 'attachment', 
                                    filename=os.path.basename(attachment_path))
                msg.attach(attachment)
        
        # Connect to Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Email sent to {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def send_audit_email(audit_result, recipient_email, recipient_name=None, pdf_path=None):
    """
    Complete workflow: Generate and send audit email
    """
    
    print(f"📧 Preparing email for {audit_result['business_name']}...")
    
    # Generate email content
    subject, body = generate_outreach_email(audit_result, recipient_email, recipient_name)
    
    # Send email
    success = send_email_gmail(recipient_email, subject, body, pdf_path)
    
    if success:
        # Log email sent
        log_entry = {
            "business_name": audit_result["business_name"],
            "recipient_email": recipient_email,
            "subject": subject,
            "sent_at": datetime.now().isoformat(),
            "compliance_score": audit_result["compliance_score"],
            "risk_level": audit_result["risk_level"]
        }
        
        # Append to email log
        import json
        log_file = "email_log.json"
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        else:
            log_data = {"emails": []}
        
        log_data["emails"].append(log_entry)
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Email logged to {log_file}")
    
    return success

if __name__ == "__main__":
    print("=" * 70)
    print("GMAIL AUTOMATION TEST")
    print("=" * 70)
    
    # Test with Lou's audit
    import json
    
    test_audit_path = "reports/louspointeclaire-2026-03-09.json"
    if os.path.exists(test_audit_path):
        with open(test_audit_path, 'r', encoding='utf-8') as f:
            audit_result = json.load(f)
        
        print(f"Testing email generation for {audit_result['business_name']}...")
        subject, body = generate_outreach_email(audit_result, "test@example.com")
        
        print("\n" + "=" * 70)
        print("SUBJECT:")
        print("=" * 70)
        print(subject)
        
        print("\n" + "=" * 70)
        print("BODY:")
        print("=" * 70)
        print(body)
        
        print("\n" + "=" * 70)
        print("To send this email, run:")
        print(f"  send_audit_email(audit_result, 'recipient@example.com')")
        print("=" * 70)
    else:
        print(f"❌ Test audit file not found: {test_audit_path}")
