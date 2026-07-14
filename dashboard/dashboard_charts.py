"""
dashboard_charts.py
------------------------------------
Smart Sales Analyzer Pro Dashboard Charts
"""

import plotly.express as px


# --------------------------------------------------
# Monthly Sales Trend
# --------------------------------------------------

def monthly_sales_chart(df):
    """
    Monthly Sales Trend
    """

    monthly = (
        df.groupby(
            df["Invoice Date"].dt.to_period("M")
        )["Net Sales"]
        .sum()
        .reset_index()
    )

    monthly["Invoice Date"] = (
        monthly["Invoice Date"]
        .astype(str)
    )

    fig = px.line(
        monthly,
        x="Invoice Date",
        y="Net Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Net Sales",
        height=450
    )

    return fig


# --------------------------------------------------
# Region-wise Sales
# --------------------------------------------------

def region_sales_chart(df):
    """
    Region-wise Sales
    """

    region = (
        df.groupby("Region")["Net Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Net Sales",
            ascending=False
        )
    )

    fig = px.bar(
        region,
        x="Region",
        y="Net Sales",
        title="Region-wise Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Net Sales",
        height=450
    )

    return fig


# --------------------------------------------------
# Category-wise Sales
# --------------------------------------------------

def category_sales_chart(df):
    """
    Category-wise Sales
    """

    category = (
        df.groupby("Category")["Net Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        names="Category",
        values="Net Sales",
        hole=0.40,
        title="Category-wise Sales"
    )

    fig.update_layout(
        height=450
    )

    return fig

def brand_sales_chart(df):
    """
    Brand-wise Sales
    """

    brand = (
        df.groupby("Brand")["Net Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Net Sales",
            ascending=False
        )
    )

    fig = px.bar(
        brand,
        x="Brand",
        y="Net Sales",
        title="Brand-wise Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Brand",
        yaxis_title="Net Sales",
        height=450
    )

    return fig


# --------------------------------------------------
# Top 10 Products
# --------------------------------------------------

def top_products_chart(df):
    """
    Top 10 Products by Sales
    """

    products = (
        df.groupby("Product Name")["Net Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Net Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        products,
        x="Net Sales",
        y="Product Name",
        orientation="h",
        text_auto=".2s",
        title="Top 10 Products"
    )

    fig.update_layout(
        height=500,
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return fig


# --------------------------------------------------
# Top 10 Customers
# --------------------------------------------------

def top_customers_chart(df):
    """
    Top 10 Customers by Sales
    """

    customers = (
        df.groupby("Customer Name")["Net Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Net Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        customers,
        x="Net Sales",
        y="Customer Name",
        orientation="h",
        text_auto=".2s",
        title="Top 10 Customers"
    )

    fig.update_layout(
        height=500,
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return fig