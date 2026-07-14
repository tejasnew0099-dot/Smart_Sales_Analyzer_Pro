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


def show_header():
    """
    Dashboard Header
    """

    st.title("📊 Smart Sales Analyzer Pro")

    st.caption("Executive Business Intelligence Dashboard")