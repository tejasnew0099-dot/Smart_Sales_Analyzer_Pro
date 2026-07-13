"""
charts.py
------------------------------------
Dashboard Charts
"""

import plotly.express as px


def monthly_sales_chart(df):
    """
    Create Monthly Sales Trend Chart
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


def region_sales_chart(df):
    """
    Create Region-wise Sales Chart
    """

    import plotly.express as px

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

def category_sales_chart(df):
    """
    Create Category-wise Sales Pie Chart
    """

    import plotly.express as px

    category = (
        df.groupby("Category")["Net Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category,
        names="Category",
        values="Net Sales",
        title="Category-wise Sales",
        hole=0.4
    )

    fig.update_layout(
        height=450
    )

    return fig