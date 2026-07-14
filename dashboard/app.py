from io import BytesIO

import pandas as pd

import streamlit as st

from dashboard_engine import (
    load_dashboard_data,
    calculate_dashboard_kpis,
    executive_summary
)

from dashboard_charts import (
    monthly_sales_chart,
    region_sales_chart,
    category_sales_chart,
    brand_sales_chart,
    top_products_chart,
    top_customers_chart
)

from filters import apply_filters


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

def format_currency(value):
    """
    Format currency for KPI cards
    """

    if value >= 1_000_000_000:
        return f"₹ {value/1_000_000_000:.2f}B"

    elif value >= 1_000_000:
        return f"₹ {value/1_000_000:.2f}M"

    elif value >= 1_000:
        return f"₹ {value/1_000:.2f}K"

    else:
        return f"₹ {value:,.2f}"


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

df = apply_filters(df)


# ----------------------------
# KPI Calculation
# ----------------------------

kpis = calculate_dashboard_kpis(df)


# ----------------------------
# KPI Cards
# ----------------------------

# ----------------------------
# KPI Cards
# ----------------------------

row1 = st.columns(4)

with row1[0]:
    st.metric(
        "💰 Total Sales",
        format_currency(
    kpis["Total Sales"]
)
    )

with row1[1]:
    st.metric(
        "📈 Total Profit",
     format_currency(
    kpis["Total Profit"]
)
   )

with row1[2]:
    st.metric(
        "🧾 Total Orders",
        f"{kpis['Total Orders']:,}"
    )

with row1[3]:
    st.metric(
        "📊 Profit Margin",
        f"{kpis['Profit Margin %']}%"
    )


row2 = st.columns(4)

with row2[0]:
    st.metric(
        "📦 Quantity Sold",
        f"{kpis['Quantity Sold']:,}"
    )

with row2[1]:
    st.metric(
        "💵 Avg Order Value",
        format_currency(
    kpis["Average Order Value"]
)
    )

with row2[2]:
    st.metric(
        "🏆 Best Region",
        kpis["Best Region"]
    )

with row2[3]:
    st.metric(
        "🥇 Best Brand",
        kpis["Best Brand"]
    )

st.divider()

st.markdown(
    executive_summary(kpis)
)

excel_buffer = BytesIO()

with pd.ExcelWriter(
    excel_buffer,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False,
        sheet_name="Sales Data"
    )

excel_data = excel_buffer.getvalue()

st.divider()

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


# ----------------------------
# Export Filtered Data
# ----------------------------

st.divider()

st.subheader("📥 Export Filtered Data")

col1, col2 = st.columns(2)

# ---------------- CSV ----------------

csv = df.to_csv(index=False).encode("utf-8")

with col1:

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name="Filtered_Sales_Data.csv",
        mime="text/csv",
        use_container_width=True
    )

# ---------------- Excel ----------------

excel_buffer = BytesIO()

with pd.ExcelWriter(
    excel_buffer,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False,
        sheet_name="Sales Data"
    )

excel_data = excel_buffer.getvalue()

with col2:

    st.download_button(
        label="📊 Download Excel",
        data=excel_data,
        file_name="Filtered_Sales_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )
st.dataframe(
    df.head(20)
)

st.subheader("🏷️ Brand-wise Sales")

st.plotly_chart(
    brand_sales_chart(df),
    use_container_width=True
)

st.divider()

st.subheader("🏆 Top 10 Products")

st.plotly_chart(
    top_products_chart(df),
    use_container_width=True
)

st.divider()

st.subheader("👥 Top 10 Customers")

st.plotly_chart(
    top_customers_chart(df),
    use_container_width=True
)