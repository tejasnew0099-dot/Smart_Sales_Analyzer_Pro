"""
filters.py
------------------------------------
Dashboard Sidebar Filters
"""

import streamlit as st


def apply_filters(df):
    """
    Apply sidebar filters and return filtered dataframe.
    """

    st.sidebar.header("🔎 Dashboard Filters")

    # -------------------------
    # Region Filter
    # -------------------------

    regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())

    selected_region = st.sidebar.selectbox(
        "Region",
        regions
    )

    if selected_region != "All":
        df = df[df["Region"] == selected_region]

    # -------------------------
    # Category Filter
    # -------------------------

    categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())

    selected_category = st.sidebar.selectbox(
        "Category",
        categories
    )

    if selected_category != "All":
        df = df[df["Category"] == selected_category]

    # -------------------------
    # Brand Filter
    # -------------------------

    brands = ["All"] + sorted(df["Brand"].dropna().unique().tolist())

    selected_brand = st.sidebar.selectbox(
        "Brand",
        brands
    )

    if selected_brand != "All":
        df = df[df["Brand"] == selected_brand]

    return df