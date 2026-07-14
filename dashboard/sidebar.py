"""
sidebar.py
------------------------------------
Dashboard Sidebar
"""

import streamlit as st


def show_sidebar(df):
    """
    Display Sidebar
    """

    st.sidebar.title("📊 Smart Sales Analyzer Pro")

    st.sidebar.markdown(
        "### Executive Dashboard"
    )

    st.sidebar.divider()

    st.sidebar.info(
        """
**Version:** 4.0

**Developer:** Tejas Patel

**Status:** Production Ready
"""
    )

    st.sidebar.divider()

    st.sidebar.metric(
        "📦 Records",
        f"{len(df):,}"
    )

    st.sidebar.metric(
        "🏷 Brands",
        df["Brand"].nunique()
    )

    st.sidebar.metric(
        "🌍 Regions",
        df["Region"].nunique()
    )

    st.sidebar.divider()