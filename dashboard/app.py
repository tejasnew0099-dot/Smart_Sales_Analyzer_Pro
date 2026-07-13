from dashboard.dashboard_charts import (
    monthly_sales_chart,
    region_sales_chart,
    category_sales_chart,
)


"""
app.py
------------------------------------
Smart Sales Analyzer Pro Web Dashboard
"""

import streamlit as st

from dashboard_engine import (
    load_dashboard_data,
    calculate_dashboard_kpis
)


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Smart Sales Analyzer Pro",
    page_icon="📊",
    layout="wide"
)


# ----------------------------
# Title
# ----------------------------

st.title(
    "📊 Smart Sales Analyzer Pro v2.0"
)

st.subheader(
    "Executive Sales Dashboard"
)


# ----------------------------
# Load Data
# ----------------------------

df = load_dashboard_data()


# ----------------------------
# KPI Calculation
# ----------------------------

kpis = calculate_dashboard_kpis(df)


# ----------------------------
# KPI Cards
# ----------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "💰 Total Sales",
        f"₹ {kpis['Total Sales']:,.2f}"
    )


with col2:

    st.metric(
        "📈 Total Profit",
        f"₹ {kpis['Total Profit']:,.2f}"
    )


with col3:

    st.metric(
        "🧾 Total Orders",
        kpis["Total Orders"]
    )


with col4:

    st.metric(
        "📊 Profit Margin",
        f"{kpis['Profit Margin %']}%"
    )


# ----------------------------
# Data Preview
# ----------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Monthly Sales Trend")

    st.plotly_chart(
        monthly_sales_chart(df),
        use_container_width=True
    )

with col2:

    st.subheader("🌍 Region-wise Sales")

    st.plotly_chart(
        region_sales_chart(df),
        use_container_width=True
    )

st.divider()

st.subheader("🥧 Category-wise Sales")

st.plotly_chart(
    category_sales_chart(df),
    use_container_width=True
)

st.divider()

st.subheader(
    "Sales Data Preview"
)

st.dataframe(
    df.head(20)
)