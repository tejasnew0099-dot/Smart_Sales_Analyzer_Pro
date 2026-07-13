"""
analyzer.py
------------------------------------
Business Analytics Engine
"""

import pandas as pd


def calculate_kpis(df: pd.DataFrame):
    """
    Calculate high-level KPIs.
    """

    total_revenue = df["Net Sales"].sum()

    total_profit = df["Profit"].sum()

    total_quantity = df["Quantity"].sum()

    total_orders = len(df)

    average_order_value = (
        total_revenue / total_orders
    )

    return {

        "Total Revenue": round(total_revenue, 2),

        "Total Profit": round(total_profit, 2),

        "Total Quantity": total_quantity,

        "Total Orders": total_orders,

        "Average Order Value":
            round(average_order_value, 2)

    }


def region_sales(df: pd.DataFrame):
    """
    Region-wise sales.
    """

    return (
        df.groupby("Region")["Net Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def product_sales(df: pd.DataFrame):
    """
    Product-wise sales.
    """

    return (
        df.groupby("Product Name")["Net Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def customer_sales(df: pd.DataFrame):
    """
    Customer-wise sales.
    """

    return (
        df.groupby("Customer Name")["Net Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def analyze_sales(df: pd.DataFrame):
    """
    Run all business analysis and return results.
    """

    return {
        "kpis": calculate_kpis(df),
        "region_sales": region_sales(df),
        "customer_sales": customer_sales(df),
        "product_sales": product_sales(df)
    }


def monthly_sales(df: pd.DataFrame):
    """
    Calculate monthly sales trend.
    """

    df = df.copy()

    df["Month"] = (
        pd.to_datetime(df["Invoice Date"])
        .dt.to_period("M")
        .astype(str)
    )

    return (
        df.groupby("Month")["Net Sales"]
        .sum()
        .sort_index()
    )


def state_sales(df: pd.DataFrame):
    """
    Calculate sales by state.
    """

    return (
        df.groupby("State")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

def city_sales(df: pd.DataFrame):
    """
    Calculate sales by city.
    """

    return (
        df.groupby("City")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


def category_sales(df: pd.DataFrame):
    """
    Calculate sales by product category.
    """

    return (
        df.groupby("Category")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

def brand_sales(df: pd.DataFrame):
    """
    Calculate sales by brand.
    """

    return (
        df.groupby("Brand")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


def product_sales(df: pd.DataFrame):
    """
    Calculate sales by product.
    """

    return (
        df.groupby("Product Name")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )


def product_profit(df: pd.DataFrame):
    """
    Calculate profit by product.
    """

    return (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

def profit_margin(df: pd.DataFrame):
    """
    Calculate profit margin percentage.
    """

    result = (
        df.groupby("Product Name")
        .agg(
            {
                "Net Sales": "sum",
                "Profit": "sum"
            }
        )
    )

    result["Profit Margin %"] = (
        result["Profit"]
        /
        result["Net Sales"]
        *
        100
    )

    return (
        result
        .sort_values(
            "Profit Margin %",
            ascending=False
        )
    )


def customer_type_sales(df: pd.DataFrame):
    """
    Calculate sales by customer type.
    """

    return (
        df.groupby("Customer Type")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

def top_customers(df: pd.DataFrame, limit=10):
    """
    Calculate top customers by sales.
    """

    return (
        df.groupby("Customer Name")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(limit)
    )

def customer_profit(df: pd.DataFrame, limit=10):
    """
    Calculate top customers by profit.
    """

    return (
        df.groupby("Customer Name")["Profit"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(limit)
    )

def customer_segmentation(df: pd.DataFrame):
    """
    Perform ABC customer segmentation.
    """

    customer_sales = (
        df.groupby("Customer Name")["Net Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    total_sales = customer_sales.sum()

    contribution = (
        customer_sales.cumsum()
        /
        total_sales
        *
        100
    )

    segment = []

    for value in contribution:

        if value <= 70:

            segment.append("A")

        elif value <= 90:

            segment.append("B")

        else:

            segment.append("C")


    result = pd.DataFrame(
        {
            "Customer Sales": customer_sales,
            "Cumulative %": contribution,
            "Segment": segment
        }
    )

    return result


if __name__ == "__main__":

    from core.excel_reader import load_sales_data

    df = load_sales_data()


    print("\n========== Monthly Sales ==========\n")

    print(monthly_sales(df))


    print("\n========== State Sales ==========\n")

    print(state_sales(df))

    print("\n========== City Sales ==========\n")

    print(city_sales(df))


    print("\n========== Category Sales ==========\n")

    print(category_sales(df))

    print("\n========== Brand Sales ==========\n")

    print(brand_sales(df))

    print("\n========== Product Sales ==========\n")

    print(product_sales(df).head(10))

    print("\n========== Product Profit ==========\n")

    print(product_profit(df).head(10))

    print("\n========== Profit Margin ==========\n")

    print(   profit_margin(df).head(10))

    print("\n========== Customer Type Sales ==========\n")

    print(customer_type_sales(df))

    print("\n========== Top Customers ==========\n")

    print(top_customers(df))

    print("\n========== Customer Profit ==========\n")

    print(customer_profit(df))

    print("\n========== Customer Segmentation ==========\n")

    print(customer_segmentation(df).head(20))
