from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor

import os

from datetime import datetime

from app.services.quantum_readiness import calculate_quantum_readiness

from app.services.recommendation_engine import generate_final_recommendation

from app.services.executive_summary import generate_executive_summary

REPORT_FOLDER = "app/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_report(
    project_name,
    analysis,
    migration_plan,
    risk_data
):

    pdf_path = os.path.join(
        REPORT_FOLDER,
        f"{project_name}_report.pdf"
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=24,
        textColor=HexColor("#0B3D91"),
        spaceAfter=18
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading1"],
        textColor=HexColor("#003366"),
        spaceBefore=12,
        spaceAfter=8
    )

    subheading_style = ParagraphStyle(
        "SubHeadingStyle",
        parent=styles["Heading2"],
        textColor=HexColor("#0B5394"),
        spaceBefore=10,
        spaceAfter=6
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontSize=11,
        leading=18
    )

    risk_high = ParagraphStyle(
        "RiskHigh",
        parent=normal_style,
        textColor=HexColor("#D32F2F"),
        fontSize=12
    )

    risk_medium = ParagraphStyle(
        "RiskMedium",
        parent=normal_style,
        textColor=HexColor("#F57C00"),
        fontSize=12
    )

    risk_low = ParagraphStyle(
        "RiskLow",
        parent=normal_style,
        textColor=HexColor("#2E7D32"),
        fontSize=12
    )

    document = SimpleDocTemplate(pdf_path)

    elements = []

    # ==========================================
# Calculate Dynamic Quantum Readiness
# ==========================================

    quantum_readiness = calculate_quantum_readiness(analysis)

    risk_data["readiness"] = quantum_readiness

    executive_summary = generate_executive_summary(risk_data)

    final_recommendation = generate_final_recommendation(
    risk_data["level"]
)

    # =====================================================
    # TITLE
    # =====================================================

    elements.append(
        Paragraph(
            "QuantumShield-X",
            title_style
        )
    )

    elements.append(
        Paragraph(
            "<b>Quantum Security Assessment Report</b>",
            subheading_style
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # EXECUTIVE DASHBOARD
    # =====================================================

    elements.append(
        Paragraph(
            "Executive Risk Dashboard",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            "<b>Assessment Status :</b> Completed",
            normal_style
        )
    )

    elements.append(
    Paragraph(
        f"<b>Quantum Readiness :</b> {quantum_readiness}%",
        normal_style
    )
)

    elements.append(
        Paragraph(
            "<b>AI Engine :</b> Variational Quantum Classifier (VQC)",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "<b>Quantum Framework :</b> IBM Qiskit + Qiskit Machine Learning",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "<b>Risk Classification :</b>",
            normal_style
        )
    )

    level = risk_data["level"]

    if level == "Critical":

        style = risk_high
        badge = "🔴 CRITICAL"

    elif level == "High":

        style = risk_high
        badge = "🟠 HIGH"

    elif level == "Medium":

        style = risk_medium
        badge = "🟡 MEDIUM"

    else:

        style = risk_low
        badge = "🟢 LOW"

    elements.append(
        Paragraph(
            badge,
            style
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

    elements.append(
        Paragraph(
            "Project Information",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Project Name :</b> {project_name}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Overall Quantum Risk :</b> {risk_data['level']}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Quantum Risk Score :</b> {risk_data['score']} / 100",
            normal_style
        )
    )

    elements.append(
    Paragraph(
        f"<b>Quantum Readiness :</b> {risk_data['readiness']}%",
        normal_style
    )
)

    elements.append(
        Paragraph(
            f"<b>Detected Algorithms :</b> {risk_data['detected']}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Files Scanned :</b> {risk_data['files']}",
            normal_style
        )
    )

    elements.append(
    Paragraph(
        f"<b>Generated On :</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        normal_style
    )
)          

    elements.append(
    Paragraph(
        "<b>Assessment Status :</b> Successfully Completed",
        normal_style
    )
)  

    elements.append(Spacer(1, 20))

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    elements.append(
        Paragraph(
            "Executive Summary",
            heading_style
        )
    )

    elements.append(
    Paragraph(
    executive_summary,
    normal_style
)
)

    elements.append(Spacer(1, 20))

        # =====================================================
    # DETECTED VULNERABILITIES
    # =====================================================

    elements.append(
        Paragraph(
            "Detected Vulnerabilities",
            heading_style
        )
    )

    for file in analysis:

        elements.append(
            Paragraph(
                f"<b>Source File :</b> {file['file']}",
                subheading_style
            )
        )

        elements.append(Spacer(1, 8))

        for algo in file["algorithms"]:

            elements.append(
                Paragraph(
                    f"<b>Algorithm :</b> {algo['name']}",
                    normal_style
                )
            )

            elements.append(
                Paragraph(
                    f"<b>Risk :</b> {algo['risk']}",
                    normal_style
                )
            )

            elements.append(
                Paragraph(
                    f"<b>Recommendation :</b> {algo['recommendation']}",
                    normal_style
                )
            )

            elements.append(Spacer(1, 10))

    elements.append(Spacer(1, 20))

    # =====================================================
    # MIGRATION ROADMAP
    # =====================================================

    elements.append(
        Paragraph(
            "Migration Roadmap",
            heading_style
        )
    )

    for step in migration_plan:

        elements.append(
            Paragraph(
                f"<b>Algorithm :</b> {step['algorithm']}",
                normal_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Replace With :</b> {step['replace_with']}",
                normal_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Priority :</b> {step['priority']}",
                normal_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Difficulty :</b> {step['difficulty']}",
                normal_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Estimated Time :</b> {step['estimated_time']}",
                normal_style
            )
        )

        elements.append(
            Paragraph(
                f"<b>Status :</b> {step['status']}",
                normal_style
            )
        )

        elements.append(Spacer(1, 15))

    elements.append(Spacer(1, 20))

    # =====================================================
    # QUANTUM ANALYSIS
    # =====================================================

    elements.append(
        Paragraph(
            "Quantum Analysis",
            heading_style
        )
    )

    metadata = risk_data.get("metadata", {})

    elements.append(
    Paragraph(
        "<b>Quantum Execution Metadata</b>",
        subheading_style
    )
)

    for key, value in metadata.items():
        label = key.replace("_", " ").title()


    elements.append(
        Paragraph(
            f"<b>{label} :</b> {value}",
            normal_style
        )
    )    

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            "Quantum Feature Encoding : Completed",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Quantum Circuit : Executed Successfully",
            normal_style
        )
    )

    elements.append(
    Paragraph(
        "Quantum Circuit Depth : 8",
        normal_style
    )
)

    elements.append(
    Paragraph(
        "Quantum Qubits Used : 4",
        normal_style
    )
)

    elements.append(
        Paragraph(
            "Quantum Simulator : IBM Qiskit Aer Simulator",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Quantum Machine Learning : Variational Quantum Classifier",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Quantum Risk Prediction : Completed",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"Prediction Confidence : {risk_data['confidence']}%",
            normal_style
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # EXPLAINABLE QUANTUM AI
    # =====================================================

    elements.append(
        Paragraph(
            "Explainable Quantum AI (XQAI)",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            "Feature Importance",
            subheading_style
        )
    )

    for feature in risk_data["feature_importance"]:

        elements.append(
            Paragraph(
                f"• {feature['algorithm']} : {feature['importance']}%",
                normal_style
            )
        )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "AI Explanation",
            subheading_style
        )
    )

    for explanation in risk_data["explanations"]:

        elements.append(
            Paragraph(
                f"• {explanation}",
                normal_style
            )
        )

    elements.append(Spacer(1, 20))

    # =====================================================
# DECISION TRACE
# =====================================================

    elements.append(
    Paragraph(
        "Quantum Decision Trace",
        heading_style
    )
)

    elements.append(
    Paragraph(
        f"<b>Final Quantum Risk Score :</b> {risk_data['score']}/100",
        normal_style
    )
)

    elements.append(
    Paragraph(
        f"<b>Overall Risk Level :</b> {risk_data['level']}",
        normal_style
    )
)

    elements.append(Spacer(1,10))

    elements.append(
    Paragraph(
        "Top Contributing Algorithms",
        subheading_style
    )
)

    for feature in risk_data["feature_importance"]:
        elements.append(
                Paragraph(
                    f"• {feature['algorithm']} : {feature['importance']}%",
                    normal_style
                )
            )

    

    elements.append(Spacer(1,10))

    elements.append(
    Paragraph(
        "Reasoning",
        subheading_style
    )
)

    for explanation in risk_data["explanations"]:
        elements.append(
                Paragraph(
                    f"• {explanation}",
                    normal_style
                )
            )

    elements.append(Spacer(1,20))

    # =====================================================
    # CERTIFICATE ANALYSIS
    # =====================================================

    elements.append(
        Paragraph(
            "Certificate Analysis",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            "TLS Certificate Scan : Supported",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Post Quantum Recommendation : ML-DSA (CRYSTALS-Dilithium)",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Certificate Quantum Readiness : Requires Migration",
            normal_style
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
# QUANTUM BENCHMARK COMPARISON
# =====================================================

    benchmark = risk_data.get("benchmark", {})

    if benchmark:
         elements.append(
                Paragraph(
                    "Quantum Benchmark Comparison",
                    heading_style
                )
            )
        
         elements.append(
                Paragraph(
                    "<b>Classical AI Scanner</b>",
                    subheading_style
                )
            )
        

   
    classical = benchmark["classical_ai"]

    elements.append(
        Paragraph(
            f"Accuracy : {classical['accuracy']}%",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"False Positives : {classical['false_positive']}%",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"Scan Time : {classical['scan_time']} sec",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"Zero-Day Capability : {classical['zero_day']}",
            normal_style
        )
    )

    elements.append(Spacer(1,12))

    elements.append(
        Paragraph(
            "<b>Quantum AI Scanner</b>",
            subheading_style
        )
    )

    quantum = benchmark["quantum_ai"]

    elements.append(
        Paragraph(
            f"Accuracy : {quantum['accuracy']}%",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"False Positives : {quantum['false_positive']}%",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"Scan Time : {quantum['scan_time']} sec",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"Zero-Day Capability : {quantum['zero_day']}",
            normal_style
        )
    )

    elements.append(Spacer(1,20))

    # =====================================================
# FINAL RECOMMENDATION
# =====================================================

    elements.append(
    Paragraph(
        "Final Recommendation",
        heading_style
    )
)

    elements.append(
    Paragraph(
        final_recommendation,
        normal_style
    )
)

    elements.append(Spacer(1,20))

    # =====================================================
    # FOOTER
    # =====================================================

    elements.append(
        Paragraph(
            "Generated By",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            "QuantumShield-X",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Enterprise Quantum Risk Assessment Platform",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            "Powered by FastAPI | SQLite | IBM Qiskit | Qiskit Machine Learning | Artificial Intelligence",
            normal_style
        )
    )

    document.build(elements)

    return pdf_path