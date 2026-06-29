import streamlit as st


# -----------------------------
# Load Global CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -----------------------------
# Page Header
# -----------------------------
def page_header(title, subtitle):

    st.markdown(
        f"""
        <div class="main-title">{title}</div>
        <div class="sub-title">{subtitle}</div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Section Title
# -----------------------------
def section_title(title):

    st.markdown(
        f"""
        <div class="section-title">
        {title}
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Metric Card
# -----------------------------
def metric_card(title, value, status):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-status">
                {status}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Environmental Score Box
# -----------------------------
def score_box(score):

    if score >= 70:
        status = "🟢 GOOD"

    elif score >= 40:
        status = "🟠 MODERATE"

    else:
        status = "🔴 CRITICAL"

    st.markdown(
        f"""
        <div class="score-box">

            🌍 Environmental Score

            <br><br>

            {score}/100

            <br><br>

            {status}

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Recovery Score Box
# -----------------------------
def recovery_box(projected_score):

    st.markdown(
        f"""
        <div class="recovery-box">

        ♻ Projected Environmental Score

        <br><br>

        {projected_score}/100

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Action Card
# -----------------------------
def action_card(title, text):

    st.markdown(
        f"""
        <div class="action-card">

        <h4>{title}</h4>

        {text}

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# AI Recommendation Box
# -----------------------------
def ai_box(text):

    st.markdown(
        f"""
        <div class="ai-box">

        🤖 <b>AI Recommendation</b>

        <br><br>

        {text}

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# Footer
# -----------------------------
def footer():

    st.markdown(
        """
        <hr>

        <div class="footer">

        🌍 E2FIX v2.0

        <br>

        AI Powered Environmental Decision Support & Recovery System

        </div>
        """,
        unsafe_allow_html=True
    )