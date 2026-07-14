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
    # Year Filter
    # -------------------------
    years = sorted(df["Invoice Date"].dt.year.unique())

    selected_year = st.sidebar.selectbox(
        "Year",
        ["All"] + years
    )

    if selected_year != "All":
        df = df[
            df["Invoice Date"].dt.year == selected_year
        ]

    # -------------------------
    # Month Filter
    # -------------------------
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    available_months = sorted(
        df["Invoice Date"].dt.month.unique()
    )

    month_lookup = {
        i + 1: month
        for i, month in enumerate(months)
    }

    selected_month = st.sidebar.selectbox(
        "Month",
        ["All"] + [
            month_lookup[m]
            for m in available_months
        ]
    )

    if selected_month != "All":
        month_number = months.index(selected_month) + 1

        df = df[
            df["Invoice Date"].dt.month == month_number
        ]

    # -------------------------
    # Region Filter
    # -------------------------
    regions = ["All"] + sorted(
        df["Region"].dropna().unique().tolist()
    )

    selected_region = st.sidebar.selectbox(
        "Region",
        regions
    )

    if selected_region != "All":
        df = df[
            df["Region"] == selected_region
        ]

    # -------------------------
    # Category Filter
    # -------------------------
    categories = ["All"] + sorted(
        df["Category"].dropna().unique().tolist()
    )

    selected_category = st.sidebar.selectbox(
        "Category",
        categories
    )

    if selected_category != "All":
        df = df[
            df["Category"] == selected_category
        ]

    # -------------------------
    # Brand Filter
    # -------------------------
    brands = ["All"] + sorted(
        df["Brand"].dropna().unique().tolist()
    )

    selected_brand = st.sidebar.selectbox(
        "Brand",
        brands
    )

    if selected_brand != "All":
        df = df[
            df["Brand"] == selected_brand
        ]

    return df