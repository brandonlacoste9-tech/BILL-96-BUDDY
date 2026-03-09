#!/usr/bin/env python3
"""
Bill 96 Compliance PDF Report Generator
Converts JSON audit reports into professional, branded PDF documents
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Note: This script requires reportlab library
# Install with: pip install reportlab

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, red, green, orange, black
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("⚠️ reportlab not installed. Install with: pip install reportlab")

def load_audit_report(json_path):
    """Load JSON audit report"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_risk_color(score):
    """Get color based on compliance score"""
    if score >= 90:
        return HexColor('#28a745')  # Green
    elif score >= 70:
        return HexColor('#ffc107')  # Yellow
    elif score >= 50:
        return HexColor('#fd7e14')  # Orange
    else:
        return HexColor('#dc3545')  # Red

def get_risk_label(risk_level):
    """Get formatted risk label"""
    labels = {
        'CRITICAL': '🚨 RISQUE CRITIQUE',
        'HIGH': '⚠️ RISQUE ÉLEVÉ',
        'MODERATE': '⚡ RISQUE MODÉRÉ',
        'LOW': '✓ RISQUE FAIBLE'
    }
    return labels.get(risk_level, risk_level)

def generate_pdf_report(json_path, output_path=None):
    """Generate PDF report from JSON audit data"""
    
    if not REPORTLAB_AVAILABLE:
        print("❌ Cannot generate PDF: reportlab library not installed")
        print("Install with: pip install reportlab")
        return False
    
    # Load audit data
    data = load_audit_report(json_path)
    
    # Set output path
    if not output_path:
        json_file = Path(json_path)
        output_path = json_file.parent / f"{json_file.stem}.pdf"
    
    # Create PDF
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for PDF elements
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#34495e'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        leading=14,
        alignment=TA_JUSTIFY
    )
    
    # Title
    story.append(Paragraph("🇨🇦 RAPPORT D'AUDIT LOI 96", title_style))
    story.append(Paragraph("Analyse de Conformité Linguistique", styles['Heading3']))
    story.append(Spacer(1, 0.3*inch))
    
    # Business Info
    story.append(Paragraph(f"<b>Entreprise:</b> {data['business_name']}", body_style))
    story.append(Paragraph(f"<b>URL:</b> {data['url']}", body_style))
    story.append(Paragraph(f"<b>Date d'audit:</b> {data['audit_date']}", body_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Compliance Score - Big visual
    score = data['compliance_score']
    risk_level = data['risk_level']
    risk_color = get_risk_color(score)
    
    score_data = [[
        Paragraph(f"<font size=48 color='{risk_color.hexval()}'><b>{score}/100</b></font>", styles['Normal']),
        Paragraph(f"<font size=16>{get_risk_label(risk_level)}</font>", styles['Normal'])
    ]]
    
    score_table = Table(score_data, colWidths=[2*inch, 4*inch])
    score_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 2, risk_color),
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#f8f9fa')),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(score_table)
    story.append(Spacer(1, 0.4*inch))
    
    # Violations Section
    story.append(Paragraph("VIOLATIONS IDENTIFIÉES", heading_style))
    
    violations = data.get('violations', [])
    for i, violation in enumerate(violations, 1):
        story.append(Paragraph(f"<b>{i}.</b> {violation}", body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Detailed Breakdown
    story.append(Paragraph("ANALYSE DÉTAILLÉE", heading_style))
    
    breakdown_data = [
        ['Critère', 'Statut', 'Score'],
        ['HTML lang attribute', 
         '✓ Conforme' if data['html_lang_compliant'] else '✗ Non-conforme',
         f"{data.get('html_lang_score', 0)}/40"],
        ['Prédominance visuelle',
         '✓ Conforme' if data['visual_predominance_compliant'] else '✗ Non-conforme',
         f"{data.get('visual_predominance_score', 0)}/30"],
        ['Documents légaux',
         '✓ Conforme' if data.get('legal_docs_french', False) else '✗ Non-conforme',
         f"{data.get('legal_docs_score', 0)}/20"],
        ['Marques de commerce',
         'Voir détails',
         f"{data.get('trademark_score', 0)}/10"],
    ]
    
    breakdown_table = Table(breakdown_data, colWidths=[2.5*inch, 2*inch, 1.5*inch])
    breakdown_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#dee2e6')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor('#ffffff'), HexColor('#f8f9fa')]),
    ]))
    
    story.append(breakdown_table)
    story.append(Spacer(1, 0.4*inch))
    
    # Enforcement Context
    if 'enforcement_context_2026' in data:
        story.append(Paragraph("CONTEXTE D'APPLICATION 2026", heading_style))
        context = data['enforcement_context_2026']
        
        story.append(Paragraph(f"<b>Saison d'inspection:</b> {context.get('inspection_season', 'N/A')}", body_style))
        story.append(Paragraph(f"<b>Risque de localisation:</b> {context.get('location_risk', 'N/A')}", body_style))
        story.append(Paragraph(f"<b>Exposition aux amendes:</b> {context.get('fine_potential', 'N/A')}", body_style))
        story.append(Spacer(1, 0.3*inch))
    
    # Page break before remediation
    story.append(PageBreak())
    
    # Remediation Plan
    story.append(Paragraph("PLAN DE REMÉDIATION", heading_style))
    
    recommendations = data.get('recommendations', [])
    for i, rec in enumerate(recommendations[:5], 1):  # Top 5 recommendations
        story.append(Paragraph(f"<b>{i}.</b> {rec}", body_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.4*inch))
    
    # Pricing Section - THE CLOSER
    story.append(Paragraph("INVESTISSEMENT VS AMENDES", heading_style))
    
    pricing_data = [
        ['Service', 'Coût'],
        ['Configuration multilingue complète', '1 500 $ - 2 500 $'],
        ['Maintenance de conformité (optionnel)', '150 $/mois'],
        ['Délai de mise en œuvre', '48-72 heures'],
        ['', ''],
        ['Amende minimale OQLF', '3 000 $ par infraction'],
        ['Exposition potentielle (votre cas)', data['enforcement_context_2026'].get('fine_potential', '30 000 $+')],
    ]
    
    pricing_table = Table(pricing_data, colWidths=[3.5*inch, 2.5*inch])
    pricing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#dee2e6')),
        ('ROWBACKGROUNDS', (0, 1), (-1, 3), [HexColor('#e8f5e9')]),  # Green for our pricing
        ('ROWBACKGROUNDS', (0, 4), (-1, -1), [HexColor('#ffebee')]),  # Red for fines
        ('FONTNAME', (0, 4), (-1, -1), 'Helvetica-Bold'),
    ]))
    
    story.append(pricing_table)
    story.append(Spacer(1, 0.4*inch))
    
    # Call to Action
    cta_style = ParagraphStyle(
        'CTA',
        parent=styles['BodyText'],
        fontSize=14,
        textColor=HexColor('#2c3e50'),
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    story.append(Paragraph("<b>PROCHAINE ÉTAPE</b>", cta_style))
    story.append(Paragraph(
        "Consultation gratuite de 15 minutes pour discuter de votre plan de remédiation spécifique.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Contact Info
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['BodyText'],
        fontSize=12,
        alignment=TA_CENTER,
        textColor=HexColor('#34495e')
    )
    
    story.append(Paragraph("<b>[VOTRE NOM]</b>", contact_style))
    story.append(Paragraph("Spécialiste Loi 96 - Ouest-de-l'Île", contact_style))
    story.append(Paragraph("[VOTRE TÉLÉPHONE] | [VOTRE EMAIL]", contact_style))
    
    # Footer
    story.append(Spacer(1, 0.4*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['BodyText'],
        fontSize=9,
        textColor=HexColor('#6c757d'),
        alignment=TA_CENTER
    )
    story.append(Paragraph(
        f"Rapport généré le {datetime.now().strftime('%Y-%m-%d à %H:%M')} | Confidentiel",
        footer_style
    ))
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ PDF généré: {output_path}")
    return True

def main():
    """Main execution"""
    if len(sys.argv) < 2:
        print("Usage: python generate_pdf.py <audit_report.json> [output.pdf]")
        print("Example: python generate_pdf.py reports/louspointeclaire-2026-03-09.json")
        sys.exit(1)
    
    json_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(json_path).exists():
        print(f"❌ File not found: {json_path}")
        sys.exit(1)
    
    success = generate_pdf_report(json_path, output_path)
    
    if success:
        print("\n📄 PDF report ready to send!")
        print("Next: Email the PDF when client replies 'Yes, send the report'")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
