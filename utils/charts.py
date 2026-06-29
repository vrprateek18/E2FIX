import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ============================================================
# GLOBAL THEME
# ============================================================

PRIMARY = "#0A4D68"
SECONDARY = "#088395"
SUCCESS = "#4CAF50"
WARNING = "#FF9800"
DANGER = "#E53935"
BACKGROUND = "#F5F7FA"
CARD = "#FFFFFF"


def apply_layout(fig, title):

    fig.update_layout(

        title={
            "text": title,
            "x": 0.5,
            "font": {
                "size": 22,
                "color": PRIMARY
            }
        },

        paper_bgcolor=BACKGROUND,
        plot_bgcolor=BACKGROUND,

        font=dict(
            family="Segoe UI",
            size=14,
            color=PRIMARY
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        height=420,

        legend=dict(
            orientation="h",
            y=-0.20
        )

    )

    return fig


# ============================================================
# ENVIRONMENTAL SCORE GAUGE
# ============================================================

def environmental_gauge(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "Environmental Score"
            },

            number={
                "suffix": "/100"
            },

            gauge={

                "axis": {
                    "range": [0,100]
                },

                "bar": {
                    "color": PRIMARY
                },

                "steps":[

                    {
                        "range":[0,40],
                        "color":"#F8B4B4"
                    },

                    {
                        "range":[40,70],
                        "color":"#FFE599"
                    },

                    {
                        "range":[70,100],
                        "color":"#B6F2C6"
                    }

                ],

                "threshold":{

                    "line":{
                        "color":"red",
                        "width":4
                    },

                    "value":score

                }

            }

        )

    )

    fig.update_layout(

        paper_bgcolor=BACKGROUND,
        height=350,
        margin=dict(l=20,r=20,t=60,b=20)

    )

    return fig


# ============================================================
# ENVIRONMENTAL BAR CHART
# ============================================================

def environmental_bar_chart(data):

    df = pd.DataFrame({

        "Parameter": list(data.keys()),
        "Value": list(data.values())

    })

    fig = px.bar(

        df,

        x="Parameter",

        y="Value",

        color="Value",

        color_continuous_scale="Tealgrn",

        text="Value"

    )

    fig.update_traces(

        textposition="outside",

        marker_line_width=0,

        hovertemplate="<b>%{x}</b><br>Value : %{y}<extra></extra>"

    )

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(gridcolor="#DDDDDD")

    return apply_layout(
        fig,
        "Environmental Parameters"
    )


# ============================================================
# RADAR CHART
# ============================================================

def environmental_radar_chart(data):

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=list(data.values()),

            theta=list(data.keys()),

            fill="toself",

            line=dict(
                color=PRIMARY,
                width=3
            ),

            fillcolor="rgba(10,77,104,0.30)",

            name="Environment"

        )

    )

    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0,100]

            )

        ),

        paper_bgcolor=BACKGROUND,

        showlegend=False,

        height=450,

        title={

            "text":"Environmental Health Radar",

            "x":0.5

        }

    )

    return fig


    # ============================================================
# WASTE DISTRIBUTION DONUT CHART
# ============================================================

def waste_distribution_chart(waste_data):

    df = pd.DataFrame(
        waste_data.items(),
        columns=["Waste Type", "Quantity"]
    )

    fig = px.pie(
        df,
        names="Waste Type",
        values="Quantity",
        hole=0.55,
        color_discrete_sequence=px.colors.sequential.Tealgrn
    )

    fig.update_traces(
        textinfo="percent+label",
        pull=[0.02] * len(df),
        hovertemplate="<b>%{label}</b><br>%{value} kg<extra></extra>"
    )

    fig.update_layout(
        title={
            "text": "Waste Distribution",
            "x": 0.5
        },
        paper_bgcolor=BACKGROUND,
        plot_bgcolor=BACKGROUND,
        showlegend=True,
        height=420
    )

    return fig


# ============================================================
# CARBON CREDIT BAR CHART
# ============================================================

def carbon_credit_chart(carbon_saved, credits, revenue):

    df = pd.DataFrame({

        "Metric": [
            "Carbon Saved",
            "Credits",
            "Revenue"
        ],

        "Value": [
            carbon_saved,
            credits,
            revenue
        ]

    })

    fig = px.bar(

        df,

        x="Metric",

        y="Value",

        text="Value",

        color="Metric",

        color_discrete_sequence=[
            SUCCESS,
            SECONDARY,
            PRIMARY
        ]

    )

    fig.update_traces(

        textposition="outside",

        hovertemplate="<b>%{x}</b><br>%{y}<extra></extra>"

    )

    return apply_layout(
        fig,
        "Carbon Credit Summary"
    )


# ============================================================
# LEADERBOARD CHART
# ============================================================

def leaderboard_chart(df):

    fig = px.bar(

        df,

        x="Credits",

        y="User",

        orientation="h",

        color="Credits",

        color_continuous_scale="Tealgrn",

        text="Credits"

    )

    fig.update_traces(

        textposition="outside",

        hovertemplate="<b>%{y}</b><br>%{x} Credits<extra></extra>"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return apply_layout(
        fig,
        "Carbon Leaderboard"
    )


# ============================================================
# KPI COMPARISON CARD CHART
# ============================================================

def kpi_comparison_chart(current, projected):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            name="Current",

            x=["Environmental Score"],

            y=[current],

            marker_color=PRIMARY

        )

    )

    fig.add_trace(

        go.Bar(

            name="Projected",

            x=["Environmental Score"],

            y=[projected],

            marker_color=SUCCESS

        )

    )

    fig.update_layout(

        barmode="group",

        paper_bgcolor=BACKGROUND,

        plot_bgcolor=BACKGROUND,

        height=400,

        title={

            "text": "Current vs Projected Score",

            "x": 0.5

        }

    )

    return fig


    # ============================================================
# ENVIRONMENTAL SCORE TIMELINE
# ============================================================

def score_timeline_chart(scores, labels):

    df = pd.DataFrame({
        "Time": labels,
        "Score": scores
    })

    fig = px.line(
        df,
        x="Time",
        y="Score",
        markers=True
    )

    fig.update_traces(
        line=dict(
            color=PRIMARY,
            width=4
        ),
        marker=dict(
            size=10,
            color=SUCCESS
        ),
        hovertemplate="<b>%{x}</b><br>Score : %{y}<extra></extra>"
    )

    fig.update_yaxes(range=[0, 100])

    return apply_layout(
        fig,
        "Environmental Score Timeline"
    )


# ============================================================
# AQI TREND CHART
# ============================================================

def aqi_trend_chart(aqi_values, labels):

    df = pd.DataFrame({
        "Time": labels,
        "AQI": aqi_values
    })

    fig = px.area(
        df,
        x="Time",
        y="AQI"
    )

    fig.update_traces(
        line=dict(
            color=DANGER,
            width=3
        ),
        fillcolor="rgba(229,57,53,0.25)"
    )

    return apply_layout(
        fig,
        "AQI Trend Analysis"
    )


# ============================================================
# RECOVERY PROGRESS CHART
# ============================================================

def recovery_progress_chart(current_score, projected_score):

    fig = go.Figure()

    fig.add_trace(

        go.Indicator(

            mode="number+delta",

            value=projected_score,

            delta={
                "reference": current_score,
                "relative": False,
                "position": "top"
            },

            title={
                "text": "Recovery Progress"
            },

            number={
                "suffix": "/100"
            }

        )

    )

    fig.update_layout(
        paper_bgcolor=BACKGROUND,
        height=300
    )

    return fig


# ============================================================
# MULTI CITY COMPARISON
# ============================================================

def comparison_chart(city_scores):

    df = pd.DataFrame({
        "City": list(city_scores.keys()),
        "Score": list(city_scores.values())
    })

    fig = px.bar(

        df,

        x="City",

        y="Score",

        color="Score",

        text="Score",

        color_continuous_scale="Viridis"

    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(range=[0,100])

    return apply_layout(
        fig,
        "Environmental Score Comparison"
    )


# ============================================================
# CARBON RECOVERY TIMELINE
# ============================================================

def carbon_history_chart(carbon_values, labels):

    df = pd.DataFrame({
        "Time": labels,
        "Carbon": carbon_values
    })

    fig = px.line(

        df,

        x="Time",

        y="Carbon",

        markers=True

    )

    fig.update_traces(

        line=dict(
            color=SUCCESS,
            width=4
        ),

        marker=dict(
            size=8
        )

    )

    return apply_layout(
        fig,
        "Carbon Recovery Timeline"
    )


# ============================================================
# IMPROVEMENT TREND
# ============================================================

def improvement_chart(before, after):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Before"],

            y=[before],

            marker_color=DANGER,

            name="Before"

        )

    )

    fig.add_trace(

        go.Bar(

            x=["After"],

            y=[after],

            marker_color=SUCCESS,

            name="After"

        )

    )

    fig.update_layout(

        barmode="group",

        paper_bgcolor=BACKGROUND,

        plot_bgcolor=BACKGROUND,

        height=400,

        title={

            "text":"Environmental Improvement",

            "x":0.5

        }

    )

    return fig


    # ============================================================
# AI PREDICTION CHART
# ============================================================

def prediction_chart(actual, predicted, labels):

    df = pd.DataFrame({
        "Time": labels,
        "Actual": actual,
        "Predicted": predicted
    })

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["Actual"],
            mode="lines+markers",
            name="Actual",
            line=dict(color=PRIMARY, width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["Predicted"],
            mode="lines+markers",
            name="Prediction",
            line=dict(color=SUCCESS, width=3, dash="dash")
        )
    )

    return apply_layout(fig, "Environmental Prediction")


# ============================================================
# COMMUNITY IMPACT CHART
# ============================================================

def community_impact_chart(metrics):

    df = pd.DataFrame({
        "Category": list(metrics.keys()),
        "Value": list(metrics.values())
    })

    fig = px.bar(
        df,
        x="Category",
        y="Value",
        color="Value",
        color_continuous_scale="Viridis",
        text="Value"
    )

    fig.update_traces(textposition="outside")

    return apply_layout(fig, "Community Environmental Impact")


# ============================================================
# GREEN INDEX GAUGE
# ============================================================

def green_index_gauge(value):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=value,

        title={"text":"Green Index"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":SUCCESS},

            "steps":[

                {"range":[0,40],"color":"#F8B4B4"},

                {"range":[40,70],"color":"#FFE599"},

                {"range":[70,100],"color":"#B6F2C6"}

            ]

        }

    ))

    fig.update_layout(
        paper_bgcolor=BACKGROUND,
        height=300
    )

    return fig


# ============================================================
# HEAT STRESS GAUGE
# ============================================================

def heat_gauge(value):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=value,

        title={"text":"Heat Stress"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":DANGER}

        }

    ))

    fig.update_layout(
        paper_bgcolor=BACKGROUND,
        height=300
    )

    return fig


# ============================================================
# WATER STRESS GAUGE
# ============================================================

def water_gauge(value):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=value,

        title={"text":"Water Stress"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"#2196F3"}

        }

    ))

    fig.update_layout(
        paper_bgcolor=BACKGROUND,
        height=300
    )

    return fig


# ============================================================
# NOISE IMPACT GAUGE
# ============================================================

def noise_gauge(value):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=value,

        title={"text":"Noise Impact"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"#9C27B0"}

        }

    ))

    fig.update_layout(
        paper_bgcolor=BACKGROUND,
        height=300
    )

    return fig


# ============================================================
# EXPORT LAYOUT
# ============================================================

def export_ready(fig):

    fig.update_layout(

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(

            family="Segoe UI",

            size=14,

            color="black"

        )

    )

    return fig


# ============================================================
# ANIMATION
# ============================================================

def add_animation(fig):

    fig.update_layout(

        transition={

            "duration":700,

            "easing":"cubic-in-out"

        }

    )

    return fig


# ==========================================================
# ENVIRONMENTAL SCORE TREND
# ==========================================================

def score_trend_chart(history):

    fig = px.line(

        history,

        x="created_at",

        y="environmental_score",

        markers=True,

        title="Environmental Score Trend"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Analysis Time",

        yaxis_title="Environmental Score",

        height=450

    )

    return fig


# ==========================================================
# AQI TREND
# ==========================================================

def aqi_trend_chart(history):

    fig = px.line(

        history,

        x="created_at",

        y="aqi",

        markers=True,

        title="AQI Trend"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Analysis Time",

        yaxis_title="AQI",

        height=450

    )

    return fig

# ==========================================================
# CARBON SAVED TREND
# ==========================================================

def carbon_trend_chart(history):

    fig = px.area(

        history,

        x="created_at",

        y="carbon_saved",

        title="Carbon Saved Trend"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Analysis Time",

        yaxis_title="Carbon Saved (kg)",

        height=450

    )

    return fig

# ==========================================================
# CARBON CREDITS TREND
# ==========================================================

def credits_trend_chart(history):

    fig = px.bar(

        history,

        x="created_at",

        y="carbon_credits",

        title="Carbon Credits Trend"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Analysis Time",

        yaxis_title="Carbon Credits",

        height=450

    )

    return fig

# ==========================================================
# RECOVERY PROGRESS CHART
# ==========================================================

def recovery_progress_chart(history):

    fig = px.line(

        history,

        x="created_at",

        y="projected_score",

        markers=True,

        title="Projected Environmental Score"

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Analysis Time",

        yaxis_title="Projected Score",

        height=450

    )

    return fig

# ==========================================================
# ENVIRONMENT STATUS
# ==========================================================

def environment_status_pie(history):

    latest = history.iloc[-1]

    values = [

        latest["environmental_score"],

        100 - latest["environmental_score"]

    ]

    fig = px.pie(

        values=values,

        names=[

            "Healthy",

            "Needs Improvement"

        ],

        title="Current Environmental Status"

    )

    fig.update_layout(

        height=450

    )

    return fig