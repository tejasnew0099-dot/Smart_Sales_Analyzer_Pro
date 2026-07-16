

from io import BytesIO

from sidebar import show_sidebar

from ai_assistant import answer_question

from ui import (
    show_header,
    show_kpis,
    show_summary,
    show_footer
)

import pandas as pd

import streamlit as st



from dashboard_engine import (
    load_dashboard_data,
    calculate_dashboard_kpis,
    executive_summary,
    generate_business_insights,
    business_health_score
)

from dashboard_charts import (
    monthly_sales_chart,
    region_sales_chart,
    category_sales_chart,
    brand_sales_chart,
    top_products_chart,
    top_customers_chart,
    sales_profit_trend_chart
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

show_header()

# ----------------------------
# Load Data
# ----------------------------

df = load_dashboard_data()

df = apply_filters(df)

show_sidebar(df)

kpis = calculate_dashboard_kpis(df)

##show_header()

score, health = business_health_score(kpis)

st.success(f"⭐ Overall Business Health Score: {score}/100")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Sales:** {health['Sales']}")
    st.write(f"**Profit Margin:** {health['Profit Margin']}")
    st.write(f"**Average Order Value:** {health['Average Order Value']}")

with col2:
    st.write(f"**Best Region:** {health['Best Region']}")
    st.write(f"**Best Brand:** {health['Best Brand']}")

st.divider()

##show_kpis(kpis)

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

show_kpis(kpis)

show_summary(executive_summary(kpis)
)

st.markdown(
    generate_business_insights(
        df,
        kpis
    )
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

st.divider()

st.subheader("🤖 Ask Your Sales Data")

questions = [
    "Which region generated the highest sales?",
    "Who is the top customer?",
    "Which brand performs the best?",
    "Which region performs the best?"
]

selected_question = st.selectbox(
    "Choose a business question",
    questions
)

if st.button("💬 Get Answer", use_container_width=True):
    answer = answer_question(
        selected_question,
        df,
        kpis
    )

    st.success(answer)

st.subheader("📈 Sales vs Profit Trend")

st.plotly_chart(
    sales_profit_trend_chart(df),
    use_container_width=True
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

show_footer()