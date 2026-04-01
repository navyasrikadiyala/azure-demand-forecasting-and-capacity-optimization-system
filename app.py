import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------- PAGE ----------------
st.set_page_config(page_title="Bakery Demand Forecast", layout="wide")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("model_ready_bakery_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Predicted"] = df["RollingMean7"]
df["Residual"] = df["Demand"] - df["Predicted"]

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #020617;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #030b1a;
    color: white;
    border-right: 1px solid #1e293b;
}

/* Header */
.header-box {
    background: linear-gradient(90deg, #0f3d91, #2563eb);
    padding: 28px;
    border-radius: 18px;
    color: white;
    margin-bottom: 18px;
    box-shadow: 0 0 18px rgba(37,99,235,0.25);
}

/* KPI cards */
.kpi-card {
    background-color: #0f172a;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #1e293b;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
}

/* Alert strip */
.alert-strip {
    background-color: #2a1f08;
    color: #facc15;
    padding: 14px;
    border-radius: 12px;
    border: 1px solid #7c5d12;
    margin-top: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
    <div style="
        background: linear-gradient(180deg,#0b1220,#111827);
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;">
        <h2 style="color:white; margin-bottom:5px;">🍞 Bakery Forecast</h2>
        <p style="color:#94a3b8; font-size:14px;">
            Demand Monitoring & Capacity
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚙️ Dashboard Controls")

    month = st.selectbox(
        "📅 Select Month",
        ["All"] + sorted(df["Month"].unique().tolist())
    )

    weekend = st.selectbox(
        "📌 Day Type",
        ["All", "Weekday", "Weekend"]
    )

    st.markdown("---")
    st.markdown("### 📊 Quick Stats")

    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:15px;
        border-radius:12px;
        border:1px solid #1e293b;
        margin-bottom:10px;">
        <p style="color:#94a3b8;">Total Records</p>
        <h3 style="color:white;">{len(df)}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:15px;
        border-radius:12px;
        border:1px solid #1e293b;">
        <p style="color:#94a3b8;">Peak Demand</p>
        <h3 style="color:white;">{df['Demand'].max()}</h3>
    </div>
    """, unsafe_allow_html=True)
    

# ---------------- FILTER ----------------
filtered_df = df.copy()

if month != "All":
    filtered_df = filtered_df[filtered_df["Month"] == month]

if weekend == "Weekend":
    filtered_df = filtered_df[filtered_df["IsWeekend"] == 1]

if weekend == "Weekday":
    filtered_df = filtered_df[filtered_df["IsWeekend"] == 0]

# ---------------- HEADER ----------------
st.markdown(f"""
<div class="header-box">
    <h1>🍞 Bakery Demand Forecast Dashboard</h1>
    <p>Forecast Integration & Capacity Planning • LIVE</p>
</div>
""", unsafe_allow_html=True)

# ---------------- TOP INFO ----------------
top1, top2, top3 = st.columns(3)

with top1:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Last Refresh</h4>
        <h2>Today</h2>
    </div>
    """, unsafe_allow_html=True)

with top2:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Records</h4>
        <h2>{len(filtered_df)}</h2>
    </div>
    """, unsafe_allow_html=True)

with top3:
    st.markdown(f"""
    <div class="kpi-card">
        <h4>Spike Count</h4>
        <h2>{filtered_df["Spike"].sum()}</h2>
    </div>
    """, unsafe_allow_html=True)

# ---------------- ALERT ----------------
if filtered_df["Demand"].max() > 250:
    st.markdown("""
    <div class="alert-strip">
        ⚠ Capacity Alert — High demand spike exceeds planning threshold.
    </div>
    """, unsafe_allow_html=True)

# ---------------- KPI ROW ----------------
# ---------------- KPI ROW ----------------
st.markdown("### 📊 KEY PERFORMANCE INDICATORS")

k1, k2, k3, k4 = st.columns(4)

mae = abs(filtered_df["Residual"]).mean()
rmse = ((filtered_df["Residual"] ** 2).mean()) ** 0.5

with k1:
    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:16px;
        text-align:center;
        border:1px solid #1e293b;
        box-shadow:0 0 12px rgba(37,99,235,0.2);">
        <h4 style="color:#cbd5e1;">Average Demand</h4>
        <h1 style="color:white;">{filtered_df['Demand'].mean():.1f}</h1>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:16px;
        text-align:center;
        border:1px solid #1e293b;
        box-shadow:0 0 12px rgba(34,197,94,0.2);">
        <h4 style="color:#cbd5e1;">Peak Demand</h4>
        <h1 style="color:white;">{filtered_df['Demand'].max()}</h1>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:16px;
        text-align:center;
        border:1px solid #1e293b;
        box-shadow:0 0 12px rgba(168,85,247,0.2);">
        <h4 style="color:#cbd5e1;">MAE</h4>
        <h1 style="color:white;">{mae:.1f}</h1>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:16px;
        text-align:center;
        border:1px solid #1e293b;
        box-shadow:0 0 12px rgba(251,191,36,0.2);">
        <h4 style="color:#cbd5e1;">RMSE</h4>
        <h1 style="color:white;">{rmse:.1f}</h1>
    </div>
    """, unsafe_allow_html=True)
# ---------------- TABS ----------------
st.markdown("### 📈 ANALYSIS PANELS")

tab1, tab2, tab3 = st.tabs([
    "Actual vs Forecast",
    "Residual Analysis",
    "Data Explorer"
])

# ---------------- CHART 1 ----------------
with tab1:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Demand"],
        mode="lines",
        name="Actual Demand"
    ))

    fig.add_trace(go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Predicted"],
        mode="lines",
        name="Predicted Demand",
        line=dict(dash="dash")
    ))

    fig.update_layout(
        paper_bgcolor="#020617",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        height=430,
        title="Actual vs Predicted Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- CHART 2 ----------------
with tab2:
    fig2 = go.Figure()

    fig2.add_trace(go.Bar(
        x=filtered_df["Date"],
        y=filtered_df["Residual"],
        name="Residual"
    ))

    fig2.update_layout(
        paper_bgcolor="#020617",
        plot_bgcolor="#0f172a",
        font=dict(color="white"),
        height=350,
        title="Residual Error"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- TABLE ----------------
with tab3:
    st.dataframe(filtered_df, use_container_width=True)