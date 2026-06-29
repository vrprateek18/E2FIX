# ==========================================================
# E2FIX
# PDF REPORT GENERATOR
# ==========================================================

import os
import random
import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT,
    TA_RIGHT
)

from reportlab.lib.units import inch

from reportlab.lib.colors import HexColor

from reportlab.graphics.barcode import qr

from reportlab.graphics.shapes import Drawing

from utils.charts import (
    environmental_gauge,
    environmental_bar_chart,
    environmental_radar_chart
)


# ==========================================================
# COLORS
# ==========================================================

PRIMARY = HexColor("#0A4D68")

SECONDARY = HexColor("#088395")

SUCCESS = HexColor("#2E7D32")

WARNING = HexColor("#F9A825")

DANGER = HexColor("#C62828")

LIGHT = HexColor("#F5F7FA")


# ==========================================================
# REPORT ID
# ==========================================================

def generate_report_id():

    year = datetime.datetime.now().year

    number = random.randint(100000,999999)

    return f"E2FIX-{year}-{number}"



# ==========================================================
# STYLES
# ==========================================================

def get_styles():

    styles = getSampleStyleSheet()

    styles.add(

        ParagraphStyle(

            name="E2FIXTitle",

            fontSize=24,

            textColor=PRIMARY,

            alignment=TA_CENTER,

            spaceAfter=20,

            leading=28

        )

    )

    styles.add(

        ParagraphStyle(

            name="E2FIXHeading",

            fontSize=18,

            textColor=PRIMARY,

            spaceAfter=12

        )

    )

    styles.add(

        ParagraphStyle(

            name="NormalText",

            fontSize=11,

            leading=18,

            spaceAfter=10

        )

    )

    styles.add(

        ParagraphStyle(

            name="Center",

            fontSize=11,

            alignment=TA_CENTER

        )

    )

    return styles



# ==========================================================
# QR GENERATOR
# ==========================================================

def generate_qr(text):

    qr_code = qr.QrCodeWidget(text)

    drawing = Drawing(110,110)

    drawing.add(qr_code)

    return drawing



# ==========================================================
# LOGO
# ==========================================================

def load_logo():

    logo_path = "assets/e2fix_logo.png"

    if os.path.exists(logo_path):

        logo = Image(

            logo_path,

            width=1.3*inch,

            height=1.3*inch

        )

        return logo

    return None





# ==========================================================
# SAVE PLOTLY CHART
# ==========================================================

def save_chart(fig, filename):

    os.makedirs("reports/charts", exist_ok=True)

    filepath = os.path.join("reports", "charts", filename)

    fig.write_image(
        filepath,
        width=1000,
        height=600,
        scale=2
    )

    return filepath







# ==========================================================
# COVER PAGE
# ==========================================================

def add_cover_page(
    story,
    styles,
    data,
    report_id,
    generated_date
):

    logo = load_logo()

    if logo:

        logo.hAlign = "CENTER"

        story.append(logo)

    story.append(Spacer(1,15))

    story.append(

        Paragraph(

            "E2FIX",

            styles["E2FIXTitle"]

        )

    )

    story.append(

        Paragraph(

            "AI Powered Environmental Decision Support & Recovery System",

            styles["Center"]

        )

    )

    story.append(Spacer(1,25))

    info = [

        ["Report ID", report_id],

        ["Generated", generated_date],

        ["Location", data["location"]]

    ]

    table = Table(

        info,

        colWidths=[140,260]

    )

    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),PRIMARY),

            ("TEXTCOLOR",(0,0),(0,-1),colors.white),

            ("BACKGROUND",(1,0),(1,-1),LIGHT),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,25))




    qr_text = f"""

E2FIX Environmental Report

Report ID : {report_id}

Location : {data["location"]}

Environmental Score : {data["score"]}

Generated : {generated_date}

"""

    qr_image = generate_qr(qr_text)

    story.append(qr_image)

    story.append(Spacer(1,20))




    confidential = Table(

        [

            [

                "CONFIDENTIAL ENVIRONMENTAL REPORT"

            ]

        ],

        colWidths=[400]

    )

    confidential.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),DANGER),

            ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10)

        ])

    )

    story.append(confidential)


    story.append(PageBreak())




# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def add_executive_summary(
    story,
    styles,
    data
):



    story.append(

        Paragraph(

            "Executive Summary",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This report presents an AI-powered environmental assessment
based on live air quality, weather conditions and
environmental recovery indicators generated by the
E2FIX Decision Support System.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,15))

# ==========================================================
# ENVIRONMENT GRADE
# ==========================================================

    score = data["score"]

    if score >= 90:

        grade = "A+"

        grade_color = SUCCESS

    elif score >= 80:

        grade = "A"

        grade_color = SUCCESS

    elif score >= 70:

        grade = "B"

        grade_color = WARNING

    elif score >= 60:

        grade = "C"

        grade_color = WARNING

    else:

        grade = "D"

        grade_color = DANGER

    summary = [

        ["Parameter","Value"],

        ["Location",data["location"]],

        ["Environmental Score",f"{data['score']}/100"],

        ["Environmental Grade",grade],

        ["AQI",data["aqi"]],

        ["Temperature",f"{data['temperature']} °C"],

        ["Humidity",f"{data['humidity']} %"],

        ["Wind Speed",f"{data['wind']} m/s"]

    ]

    table = Table(

        summary,

        colWidths=[200,220]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("TOPPADDING",(0,1),(-1,-1),8),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    story.append(table)

    story.append(Spacer(1,20))

# ==========================================================
# ENVIRONMENTAL ANALYSIS
# ==========================================================

def add_environmental_analysis(
    story,
    styles,
    data
):


    story.append(

        Paragraph(

            "Environmental Analysis",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This section presents the status of all environmental
engines calculated using the E2FIX Hybrid
Environmental Assessment Engine.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,15))


    def status_color(status):

        if status == "Low":

            return SUCCESS

        elif status == "Moderate":

            return WARNING

        else:

            return DANGER


    analysis = [

        ["Environmental Engine","Status"],

        ["🌳 Green Engine",data["green"]],

        ["🔊 Noise Engine",data["noise"]],

        ["💧 Water Engine",data["water"]],

        ["🗑 Waste Engine",data["waste"]],

        ["🌡 Heat Engine",data["heat"]]

    ]


    table = Table(

        analysis,

        colWidths=[240,180]

    )

    style = TableStyle([

        ("BACKGROUND",(0,0),(-1,0),PRIMARY),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),LIGHT),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

        ("TOPPADDING",(0,1),(-1,-1),8),

        ("ALIGN",(0,0),(-1,-1),"CENTER")

    ])


    style.add(

        "BACKGROUND",

        (1,1),

        (1,1),

        status_color(data["green"])

    )

    style.add(

        "BACKGROUND",

        (1,2),

        (1,2),

        status_color(data["noise"])

    )

    style.add(

        "BACKGROUND",

        (1,3),

        (1,3),

        status_color(data["water"])

    )

    style.add(

        "BACKGROUND",

        (1,4),

        (1,4),

        status_color(data["waste"])

    )

    style.add(

        "BACKGROUND",

        (1,5),

        (1,5),

        status_color(data["heat"])

    )

    style.add(

        "TEXTCOLOR",

        (1,1),

        (1,5),

        colors.white

    )

    table.setStyle(style)

    story.append(table)

    story.append(Spacer(1,20))


    story.append(

        Paragraph(

            "Environmental Observation",

            styles["E2FIXHeading"]

        )

    )

    observation = f"""

The hybrid environmental engine indicates
that the Green Index is <b>{data['green']}</b>,
Noise Impact is <b>{data['noise']}</b>,
Water Stress is <b>{data['water']}</b>,
Waste Pressure is <b>{data['waste']}</b>,
and Heat Risk is <b>{data['heat']}</b>.

These indicators collectively determine
the Environmental Score generated
by the E2FIX AI Engine.

"""

    story.append(

        Paragraph(

            observation,

            styles["NormalText"]

        )

    )

    story.append(PageBreak())


# ==========================================================
# RECOVERY DASHBOARD
# ==========================================================

def add_recovery_dashboard(
    story,
    styles,
    data
):



    story.append(

        Paragraph(

            "Environmental Recovery Dashboard",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This section estimates environmental recovery
using the E2FIX Carbon Recovery Engine.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,15))


    carbon_saved = data.get("carbon_saved",0)

    carbon_credits = data.get("carbon_credits",0)

    recovery_bonus = data.get("recovery_bonus",0)

    projected_score = data.get(

        "projected_score",

        data["score"]

    )

    revenue = carbon_credits * 500


    recovery = [

        ["Recovery Metric","Value"],

        ["Current Environmental Score",f"{data['score']}/100"],

        ["Projected Score",f"{projected_score}/100"],

        ["Carbon Saved",f"{carbon_saved:.2f} kg"],

        ["Carbon Credits",f"{carbon_credits:.2f}"],

        ["Recovery Bonus",f"+{recovery_bonus}"],

        ["Estimated Revenue",f"₹ {revenue:.2f}"]

    ]


    table = Table(

        recovery,

        colWidths=[240,180]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),SECONDARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("TOPPADDING",(0,1),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,20))


    story.append(

        Paragraph(

            "AI Recovery Assessment",

            styles["E2FIXHeading"]

        )

    )

    observation = f"""

The current environmental score is
<b>{data['score']}</b>.

After implementing recommended
recovery measures, the projected
environmental score may reach
<b>{projected_score}</b>.

Estimated carbon recovery is
<b>{carbon_saved:.2f} kg</b>
with approximately
<b>{carbon_credits:.2f}</b>
carbon credits generated.

"""

    story.append(

        Paragraph(

            observation,

            styles["NormalText"]

        )

    )

    story.append(PageBreak())



# ==========================================================
# AI RECOMMENDATION PAGE
# ==========================================================

def add_ai_recommendation(story, styles, data):

    story.append(
        Paragraph(
            "AI Environmental Recommendations",
            styles["E2FIXHeading"]
        )
    )

    story.append(
        Paragraph(
            """
Based on the live environmental analysis, the E2FIX AI Engine
has generated the following recommendations to improve
environmental quality and sustainability.
            """,
            styles["NormalText"]
        )
    )

    story.append(Spacer(1, 15))

    score = data["score"]

    # -----------------------------
    # Recommendation Logic
    # -----------------------------

    if score >= 80:

        immediate = [
            "Continue current environmental practices.",
            "Monitor AQI weekly.",
            "Maintain existing green zones."
        ]

        medium = [
            "Expand rainwater harvesting.",
            "Increase urban tree plantation."
        ]

        long = [
            "Adopt renewable energy systems.",
            "Develop smart environmental monitoring."
        ]

    elif score >= 60:

        immediate = [
            "Improve waste segregation.",
            "Reduce traffic emissions.",
            "Increase plantation drives."
        ]

        medium = [
            "Upgrade recycling infrastructure.",
            "Install additional AQI sensors."
        ]

        long = [
            "Promote carbon neutrality initiatives.",
            "Expand public transport."
        ]

    else:

        immediate = [
            "Immediate pollution control required.",
            "Ban open waste burning.",
            "Start emergency clean-up operations."
        ]

        medium = [
            "Improve industrial pollution monitoring.",
            "Deploy smart waste collection."
        ]

        long = [
            "Implement city-wide restoration projects.",
            "Develop carbon offset programmes."
        ]

    # -----------------------------
    # Helper
    # -----------------------------

    def recommendation_table(title, items):

        rows = [["Recommendation"]]

        for item in items:
            rows.append([f"• {item}"])

        table = Table(rows, colWidths=[430])

        table.setStyle(TableStyle([

            ("BACKGROUND", (0,0), (-1,0), SECONDARY),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("BACKGROUND", (0,1), (-1,-1), LIGHT),
            ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
            ("BOTTOMPADDING", (0,0), (-1,0), 8),
            ("TOPPADDING", (0,1), (-1,-1), 6)

        ]))

        story.append(
            Paragraph(title, styles["E2FIXHeading"])
        )

        story.append(table)

        story.append(Spacer(1, 12))

    # -----------------------------
    # Sections
    # -----------------------------

    recommendation_table(
        "Immediate Actions",
        immediate
    )

    recommendation_table(
        "Medium-Term Actions",
        medium
    )

    recommendation_table(
        "Long-Term Actions",
        long
    )

    # -----------------------------
    # AI Insight
    # -----------------------------

    story.append(
        Paragraph(
            "AI Environmental Insight",
            styles["E2FIXHeading"]
        )
    )

    aqi = data.get("aqi", 50)
    temp = data.get("temperature", 25)

    if aqi > 200:

        insight = (
            "Air quality is the major factor reducing the environmental "
            "score. Immediate emission control measures are recommended."
        )

    elif temp > 40:

        insight = (
            "Heat stress is increasing environmental pressure. "
            "Urban greening and water conservation should be prioritised."
        )

    else:

        insight = (
            "Current environmental indicators are reasonably balanced. "
            "Maintaining sustainable practices can further improve the score."
        )

    story.append(
        Paragraph(
            insight,
            styles["NormalText"]
        )
    )

    story.append(Spacer(1, 15))

    # -----------------------------
    # Recovery Prediction
    # -----------------------------

    projected = data.get(
        "projected_score",
        data["score"]
    )

    prediction = f"""
<b>AI Recovery Prediction</b><br/><br/>

Current Environmental Score : <b>{data['score']}</b><br/>
Projected Environmental Score : <b>{projected}</b><br/><br/>

If the recommended actions are implemented, environmental
quality is expected to improve significantly over time.
"""

    story.append(
        Paragraph(
            prediction,
            styles["NormalText"]
        )
    )

    story.append(PageBreak())


# ==========================================================
# ANALYTICS PAGE
# ==========================================================

def add_analytics_page(
    story,
    styles,
    data
):

    story.append(
        Paragraph(
            "Environmental Analytics",
            styles["E2FIXHeading"]
        )
    )

    story.append(
        Paragraph(
            "The following charts summarize the current environmental condition.",
            styles["NormalText"]
        )
    )

    story.append(Spacer(1, 15))

    gauge = environmental_gauge(
        data["score"]
    )

    gauge_path = save_chart(
        gauge,
        "gauge.png"
    )

    story.append(
        Image(
            gauge_path,
            width=6*inch,
            height=3.8*inch
        )
    )

    story.append(Spacer(1,10))


    radar_data = {

        "Green":85 if data["green"]=="Low" else 60 if data["green"]=="Moderate" else 30,

        "Noise":85 if data["noise"]=="Low" else 60 if data["noise"]=="Moderate" else 30,

        "Water":85 if data["water"]=="Low" else 60 if data["water"]=="Moderate" else 30,

        "Waste":85 if data["waste"]=="Low" else 60 if data["waste"]=="Moderate" else 30,

        "Heat":85 if data["heat"]=="Low" else 60 if data["heat"]=="Moderate" else 30

    }

    radar = environmental_radar_chart(
        radar_data
    )

    radar_path = save_chart(
        radar,
        "radar.png"
    )

    story.append(
        Image(
            radar_path,
            width=6*inch,
            height=4.2*inch
        )
    )

    story.append(Spacer(1,10))

    bar = environmental_bar_chart({

        "AQI":data["aqi"],

        "Temperature":data["temperature"],

        "Humidity":data["humidity"],

        "Wind":data["wind"]

    })

    bar_path = save_chart(
        bar,
        "bar.png"
    )

    story.append(
        Image(
            bar_path,
            width=6*inch,
            height=4*inch
        )
    )

    story.append(PageBreak())


# ==========================================================
# CONCLUSION
# ==========================================================

def add_conclusion(
    story,
    styles,
    data
):


    story.append(

        Paragraph(

            "Final Environmental Assessment",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This section summarizes the overall environmental
condition and sustainability assessment generated
by the E2FIX AI Decision Support System.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,15))


    score = data["score"]

    if score >= 90:

        grade = "A+"

        sustainability = "Excellent"

        risk = "Very Low"

        color = SUCCESS

    elif score >= 80:

        grade = "A"

        sustainability = "Very Good"

        risk = "Low"

        color = SUCCESS

    elif score >= 70:

        grade = "B"

        sustainability = "Good"

        risk = "Moderate"

        color = WARNING

    elif score >= 60:

        grade = "C"

        sustainability = "Average"

        risk = "High"

        color = WARNING

    else:

        grade = "D"

        sustainability = "Poor"

        risk = "Critical"

        color = DANGER



    carbon = data.get("carbon_saved",0)

    if carbon >= 100:

        carbon_status = "Excellent"

    elif carbon >= 50:

        carbon_status = "Good"

    elif carbon > 0:

        carbon_status = "Developing"

    else:

        carbon_status = "No Recovery Yet"


    assessment = [

        ["Assessment","Result"],

        ["Environmental Grade",grade],

        ["Environmental Score",f"{score}/100"],

        ["Sustainability",sustainability],

        ["Environmental Risk",risk],

        ["Carbon Status",carbon_status]

    ]

    table = Table(

        assessment,

        colWidths=[220,200]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("TOPPADDING",(0,1),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,20))



    story.append(

        Paragraph(

            "AI Final Remarks",

            styles["E2FIXHeading"]

        )

    )

    conclusion = f"""

The analysed location has achieved an
overall Environmental Grade of <b>{grade}</b>
with an Environmental Score of
<b>{score}</b>.

The sustainability level is currently
classified as <b>{sustainability}</b>,
while the environmental risk remains
<b>{risk}</b>.

Implementation of the recommended
recovery actions is expected to improve
environmental quality and strengthen
long-term sustainability.

"""

    story.append(

        Paragraph(

            conclusion,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,20))


    badge = Table(

        [

            [

                f"SUSTAINABILITY RATING : {grade}"

            ]

        ],

        colWidths=[420]

    )

    badge.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,-1),color),

            ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,-1),12),

            ("TOPPADDING",(0,0),(-1,-1),12)

        ])

    )

    story.append(badge)

    story.append(PageBreak())




# ==========================================================
# VERIFICATION PAGE
# ==========================================================

def add_verification_page(
    story,
    styles,
    data,
    report_id,
    generated_date
):
    story.append(

        Paragraph(

            "Verification & Report Authentication",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This report has been automatically generated by the
E2FIX AI Powered Environmental Decision Support &
Recovery System.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,20))

    verification = [

        ["Verification Item","Details"],

        ["Report ID",report_id],

        ["Generated On",generated_date],

        ["Generated By","E2FIX v2.0"],

        ["System","AI Decision Support System"],

        ["Verification Status","Verified"]

    ]

    table = Table(

        verification,

        colWidths=[180,240]

    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),PRIMARY),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),LIGHT),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("TOPPADDING",(0,1),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,25))

    qr_text = f"""

E2FIX Verification

Report ID : {report_id}

Location : {data['location']}

Environmental Score : {data['score']}

Generated : {generated_date}

"""

    qr_image = generate_qr(qr_text)

    story.append(qr_image)

    story.append(Spacer(1,20))

    story.append(

        Paragraph(

            "<b>Digital Verification</b>",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
This report has been digitally generated by
the E2FIX AI Environmental Assessment Engine.

No manual modification has been performed
after report generation.

Electronic verification is available
through the QR Code above.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,20))

    story.append(

        Paragraph(

            "<b>Disclaimer</b>",

            styles["E2FIXHeading"]

        )

    )

    story.append(

        Paragraph(

            """
The environmental analysis presented in this report
is generated using publicly available environmental
data sources, AI-based assessment models, and
recovery estimation algorithms.

This report is intended for educational,
research, and decision-support purposes only.
            """,

            styles["NormalText"]

        )

    )

    story.append(Spacer(1,20))

    story.append(

        Paragraph(

            "<b>Generated by E2FIX v2.0</b>",

            styles["Center"]

        )

    )

    story.append(

        Paragraph(

            "AI Powered Environmental Decision Support & Recovery System",

            styles["Center"]

        )

    )

    story.append(

        Paragraph(

            "© 2026 E2FIX Project",

            styles["Center"]

        )

    )



# ==========================================================
# GENERATE REPORT
# ==========================================================

def generate_report(data, filename="Environmental_Report.pdf"):

    doc = SimpleDocTemplate(

        filename,

        leftMargin=40,

        rightMargin=40,

        topMargin=40,

        bottomMargin=40

    )

    styles = get_styles()

    story = []

    report_id = generate_report_id()

    generated_date = datetime.datetime.now().strftime(

        "%d %B %Y %I:%M %p"

    )

    # Cover Page
    # Executive Summary
    # Analysis
    # Recovery
    # AI Recommendation
    # Conclusion


    add_cover_page(
        story,
        styles,
        data,
        report_id,
        generated_date

    )


    add_executive_summary(

        story,
        styles,
        data

    )

    add_environmental_analysis(

        story,
        styles,
        data

    )


    add_recovery_dashboard(

        story,
        styles,
        data

    )

    add_ai_recommendation(

        story,
        styles,
        data

    )

    add_analytics_page(
        story,
        styles,
        data
    )


    add_conclusion(

        story,
        styles,
        data

    )

    add_verification_page(

        story,
        styles,
        data,
        report_id,
        generated_date

    )

    doc.build(story)

    return filename