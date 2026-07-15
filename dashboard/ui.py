"""
ui.py
------------------------------------
Dashboard UI Components
"""

import streamlit as st


def format_currency(value):
    """
    Format currency values for KPI cards
    """

    if value >= 1_000_000_000:
        return f"₹ {value/1_000_000_000:.2f}B"

    elif value >= 1_000_000:
        return f"₹ {value/1_000_000:.2f}M"

    elif value >= 1_000:
        return f"₹ {value/1_000:.2f}K"

    else:
        return f"₹ {value:,.2f}"


from datetime import datetime

def show_header():
    """
    Professional Dashboard Header
    """

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title("📊 Smart Sales Analyzer Pro")

        st.caption(
            "Executive Business Intelligence Platform"
        )

    with col2:

        st.metric(
            "Version",
            "4.5"
        )

    st.caption(
        f"🕒 Last Refreshed: {datetime.now().strftime('%d %b %Y | %I:%M %p')}"
    )

    st.divider()


def show_kpis(kpis):
    """
    Display KPI Cards
    """

    row1 = st.columns(4)

    with row1[0]:
        st.metric(
            "💰 Total Sales",
            format_currency(kpis["Total Sales"])
        )

    with row1[1]:
        st.metric(
            "📈 Total Profit",
            format_currency(kpis["Total Profit"])
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


def show_summary(summary):
    """
    Display Executive Summary
    """

    st.divider()

    st.markdown(summary)

def show_footer():
    """
    Professional Dashboard Footer
    """

    st.divider()

    st.caption(
        "📊 Smart Sales Intelligence Platform | Version 4.5"
    )

    st.caption(
        "Developed by Tejas Patel"
    )

    st.caption(
        "Powered by Python • Streamlit • Pandas • Plotly"
    )