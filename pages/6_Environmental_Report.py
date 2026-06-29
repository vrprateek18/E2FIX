# ==========================================================
# E2FIX
# Environmental Report
# ==========================================================

import os
import streamlit as st

from reports.pdf_generator import generate_report

from database.environment_history import (
    get_latest_record
)

from utils.ui import (
    load_css,
    page_header,
    footer
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Environmental Report",

    page_icon="📄",

    layout="wide"

)

load_css()

page_header(

    "📄 Environmental Report",

    "Generate AI Powered Environmental Assessment Report"

)



# ==========================================================
# LOAD DATA
# ==========================================================

record = get_latest_record()

if record is None:

    st.warning(

        "No Environmental Analysis Found."

    )

    st.info(

        "Please run Environmental Analysis first."

    )

    st.stop()
    
    
data = dict(record)

# PDF generator "score" key use karta hai
data["score"] = data["environmental_score"]



st.subheader("📊 Latest Environmental Analysis")

c1, c2 = st.columns(2)

with c1:

    st.metric(

        "Environmental Score",

        data["environmental_score"]

    )

    st.metric(

        "AQI",

        data["aqi"]

    )

    st.metric(

        "Temperature",

        f'{data["temperature"]} °C'

    )

    st.metric(

        "Humidity",

        f'{data["humidity"]}%'

    )

with c2:

    st.metric(

        "Location",

        data["location"]

    )

    st.metric(

        "Carbon Credits",

        data["carbon_credits"]

    )

    st.metric(

        "Carbon Saved",

        f'{data["carbon_saved"]:.2f} kg'

    )

    st.metric(

        "Projected Score",

        data["projected_score"]

    )
    
    
st.divider()

generate = st.button(

    "📄 Generate Environmental Report",

    use_container_width=True,

    type="primary"

)

if generate:

    with st.spinner("Generating Professional PDF Report..."):
        pdf_file = generate_report(data)

    if pdf_file and os.path.exists(pdf_file):

        st.success("✅ Environmental Report Generated Successfully!")

        with open(pdf_file, "rb") as file:

            st.download_button(
                "⬇ Download PDF Report",
                data=file.read(),   # <-- ye bhi important change hai
                file_name=os.path.basename(pdf_file),
                mime="application/pdf",
                use_container_width=True
            )

    else:

        st.error("❌ PDF file was not generated.")

footer()