import streamlit as st

# ==========================================================
# HERO SECTION
# ==========================================================

def hero_section():

    st.markdown("""
    <div style="
        padding:40px;
        border-radius:20px;
        background:linear-gradient(135deg,#0A4D68,#088395);
        color:white;
        text-align:center;
        margin-bottom:30px;
    ">

    <h1 style="font-size:48px;">
        🌍 E2FIX
    </h1>

    <h3>
        AI Powered Environmental Decision
        Support & Recovery Platform
    </h3>

    <br>

    <h4>
        Monitor • Analyze • Recover • Improve
    </h4>

    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

def overview_section():

    st.header("📖 About E2FIX")

    st.write("""

E2FIX is an AI-powered Environmental Decision Support System
that combines live AQI, weather monitoring, environmental
analysis, carbon recovery, and AI recommendations.

The platform helps users monitor environmental conditions,
understand pollution impacts, estimate environmental recovery,
and improve sustainability through Carbon Credits.

""")

# ==========================================================
# FEATURES
# ==========================================================

def feature_section():

    st.header("🚀 Core Features")

    c1,c2,c3 = st.columns(3)

    with c1:

        st.info("""

🌍 Environmental Analysis

Real-time AQI

Weather Monitoring

Environmental Score

""")

    with c2:

        st.info("""

♻ Carbon Recovery

Carbon Credits

Recovery Bonus

Projected Score

""")

    with c3:

        st.info("""

🤖 AI Recommendation

Smart Suggestions

Recovery Planning

Environmental Insights

""")

    c4,c5,c6 = st.columns(3)

    with c4:

        st.success("""

📊 Analytics

Radar Charts

Bar Charts

Trend Analysis

""")

    with c5:

        st.success("""

🗺 Smart Map

Interactive Map

Location Analysis

Future Heatmaps

""")

    with c6:

        st.success("""

📄 Reports

Environmental Reports

Future PDF Export

""")

# ==========================================================
# WORKFLOW
# ==========================================================

def workflow_section():

    st.header("⚙ How E2FIX Works")

    st.markdown
    
    
("""

```text

Location

↓

AQI + Weather

↓

Hybrid Engine

↓

Environmental Score

↓

Carbon Credits

↓

Recovery Bonus

↓

AI Recommendation

""")




# Technology Stack

# ==========================================================
# TECH STACK
# ==========================================================

def tech_stack_section():

    st.header("💻 Technology Stack")

    col1,col2,col3 = st.columns(3)

    with col1:

        st.markdown("""

- Python

- Streamlit

- SQLite

""")

    with col2:

        st.markdown("""

- Folium

- Plotly

- Pandas

""")

    with col3:

        st.markdown("""

- AQICN API

- OpenWeather API

- AI Engine

""")


# ==========================================================
# PROJECT STATS
# ==========================================================

def statistics_section():

    st.header("📈 Project Statistics")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(

        "Pages",

        "5"

    )

    c2.metric(

        "Components",

        "6"

    )

    c3.metric(

        "Charts",

        "10+"

    )

    c4.metric(

        "Live APIs",

        "2"

    )


# ==========================================================
# ROADMAP
# ==========================================================

def roadmap_section():

    st.header("🛣 Future Roadmap")

    st.markdown("""

✅ Community Leaderboard

✅ Environmental Simulator

✅ Machine Learning Prediction

✅ PDF Reports

✅ Smart Environmental Map

✅ Admin Dashboard

""")



# ==========================================================
# HOME PAGE
# ==========================================================

def show_home():

    hero_section()

    overview_section()

    feature_section()

    workflow_section()

    tech_stack_section()

    statistics_section()

    roadmap_section()





