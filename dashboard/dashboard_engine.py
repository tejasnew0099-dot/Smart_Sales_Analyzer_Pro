"""
dashboard_engine.py
------------------------------------
Dashboard Data Engine
"""

import pandas as pd


def load_dashboard_data(
    file_path="data/Sales_Data_New.xlsx"
):

    df = pd.read_excel(file_path)

    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"]
    )

    return df



def calculate_dashboard_kpis(df):
    """
    Calculate Dashboard KPIs
    """

    print(df.columns.tolist())    
    
    total_sales = df["Net Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Invoice No"].nunique()
    
    profit_margin = (
        total_profit / total_sales * 100
    )

    quantity_sold = df["Quantity"].sum()

    average_order_value = (
        total_sales / total_orders
    )

    best_region = (
        df.groupby("Region")["Net Sales"]
        .sum()
        .idxmax()
    )

    best_brand = (
        df.groupby("Brand")["Net Sales"]
        .sum()
        .idxmax()
    )

    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Total Orders": total_orders,
        "Profit Margin %": round(profit_margin, 2),
        "Quantity Sold": quantity_sold,
        "Average Order Value": round(average_order_value, 2),
        "Best Region": best_region,
        "Best Brand": best_brand
    }


def executive_summary(kpis):
    """
    Generate Executive Summary
    """

    summary = f"""
### 🤖 Executive Summary

**Business Snapshot**

- 💰 Total Sales: ₹ {kpis['Total Sales']:,.2f}

- 📈 Total Profit: ₹ {kpis['Total Profit']:,.2f}

- 📊 Profit Margin: {kpis['Profit Margin %']}%

- 🏆 Best Region: {kpis['Best Region']}

- 🥇 Best Brand: {kpis['Best Brand']}

- 📦 Quantity Sold: {kpis['Quantity Sold']:,}

### Recommendation

✅ Continue focusing on **{kpis['Best Region']}** region.

✅ Increase inventory of **{kpis['Best Brand']}** products.

✅ Monitor profitability while maintaining sales growth.
"""

    return summary


def generate_business_insights(df, kpis):
    """
    Generate Business Insights
    """

    # Best Customer
    top_customer = (
        df.groupby("Customer Name")["Net Sales"]
        .sum()
        .idxmax()
    )

    # Highest Profit Month
    best_month = (
        df.groupby(
            df["Invoice Date"].dt.month_name()
        )["Profit"]
        .sum()
        .idxmax()
    )

    insights = f"""
## 💡 Business Insights

🏆 **Best Region:** {kpis["Best Region"]}

🥇 **Best Brand:** {kpis["Best Brand"]}

👤 **Top Customer:** {top_customer}

📈 **Highest Profit Month:** {best_month}

### 📌 Recommendation

✅ Continue investing in **{kpis["Best Region"]}** region.

✅ Increase inventory for **{kpis["Best Brand"]}**.

✅ Strengthen relationships with **{top_customer}**.
"""

    return insights

def business_health_score(kpis):
    """
    Generate Business Health Score
    """

    score = 100
    status = {}

    # Profit Margin
    if kpis["Profit Margin %"] >= 20:
        status["Profit Margin"] = "🟢 Healthy"
    elif kpis["Profit Margin %"] >= 10:
        status["Profit Margin"] = "🟡 Moderate"
        score -= 5
    else:
        status["Profit Margin"] = "🔴 Needs Attention"
        score -= 15

    # Average Order Value
    if kpis["Average Order Value"] >= 10000:
        status["Average Order Value"] = "🟢 Excellent"
    elif kpis["Average Order Value"] >= 5000:
        status["Average Order Value"] = "🟡 Moderate"
        score -= 5
    else:
        status["Average Order Value"] = "🔴 Low"
        score -= 10

    # Sales
    if kpis["Total Sales"] >= 10_000_000:
        status["Sales"] = "🟢 Strong"
    else:
        status["Sales"] = "🟡 Growing"
        score -= 5

    status["Best Region"] = f"🟢 {kpis['Best Region']}"
    status["Best Brand"] = f"🟢 {kpis['Best Brand']}"

    return score, status