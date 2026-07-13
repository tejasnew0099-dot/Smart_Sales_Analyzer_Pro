"""
dashboard_engine.py
------------------------------------
Dashboard Data Engine
"""

import pandas as pd


def load_dashboard_data(
    file_path="data/Sales_Data.xlsx"
):

    df = pd.read_excel(
        file_path
    )

    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"]
    )

    return df



def calculate_dashboard_kpis(df):

    total_sales = (
        df["Net Sales"]
        .sum()
    )


    total_profit = (
        df["Profit"]
        .sum()
    )


    total_orders = (
        df["Invoice No"]
        .nunique()
    )


    profit_margin = (
        total_profit /
        total_sales *
        100
    )


    return {

        "Total Sales":
            round(total_sales,2),

        "Total Profit":
            round(total_profit,2),

        "Total Orders":
            total_orders,

        "Profit Margin %":
            round(profit_margin,2)

    }


if __name__ == "__main__":

    df = load_dashboard_data()

    print(
        calculate_dashboard_kpis(df)
    )