"""
sales_generator.py
------------------------------------
Generate realistic sales transactions.
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from generator.lookup_data import (
    PAYMENT_STATUS,
    PAYMENT_MODES,
    SALES_PERSONS
)


def load_master_data():
    """
    Load customer and product master files.
    """

    customer_df = pd.read_excel("Customer_Master.xlsx")

    product_df = pd.read_excel("Product_Master.xlsx")

    return customer_df, product_df


def generate_invoice_number(number):

    return f"INV{number:08}"

def generate_invoice_date():

    start_date = datetime(2024, 1, 1)

    end_date = datetime(2025, 12, 31)

    days = (end_date - start_date).days

    return start_date + timedelta(
        days=random.randint(0, days)
    )


def calculate_financials(
    quantity,
    selling_price,
    cost_price
):

    gross_sales = quantity * selling_price

    discount_percent = random.choice([0, 5, 10, 15])

    discount_amount = gross_sales * discount_percent / 100

    taxable_amount = gross_sales - discount_amount

    gst_percent = 18

    tax_amount = taxable_amount * gst_percent / 100

    net_sales = taxable_amount + tax_amount

    total_cost = quantity * cost_price

    profit = taxable_amount - total_cost

    return {

        "Gross Sales": round(gross_sales, 2),

        "Discount %": discount_percent,

        "Discount Amount": round(discount_amount, 2),

        "Tax %": gst_percent,

        "Tax Amount": round(tax_amount, 2),

        "Net Sales": round(net_sales, 2),

        "Cost": round(total_cost, 2),

        "Profit": round(profit, 2)

    }


def generate_sales_record(invoice_number, customer_df, product_df):
    """
    Generate one realistic sales transaction.
    """

    customer = customer_df.sample(1).iloc[0]
    product = product_df.sample(1).iloc[0]

    quantity = random.randint(10, 500)

    financials = calculate_financials(
        quantity,
        product["Selling Price"],
        product["Cost Price"]
    )

    record = {

        "Invoice No": generate_invoice_number(invoice_number),

        "Invoice Date": generate_invoice_date(),

        "Customer Code": customer["Customer Code"],
        "Customer Name": customer["Customer Name"],
        "Customer Type": customer["Customer Type"],

        "Region": customer["Region"],
        "State": customer["State"],
        "City": customer["City"],

        "Product Code": product["Product Code"],
        "Product Name": product["Product Name"],
        "Category": product["Category"],
        "Brand": product["Brand"],

        "Quantity": quantity,

        "Unit Price": product["Selling Price"],

        "Payment Status": random.choice(PAYMENT_STATUS),

        "Payment Mode": random.choice(PAYMENT_MODES),

        "Sales Person": random.choice(SALES_PERSONS)

    }

    record.update(financials)

    return record

def generate_sales_dataframe(
    customer_df,
    product_df,
    total_records=1000
):
    """
    Generate complete sales dataset.
    """

    sales = []

    for invoice_number in range(1, total_records + 1):

        record = generate_sales_record(
            invoice_number,
            customer_df,
            product_df
        )

        sales.append(record)

    sales_df = pd.DataFrame(sales)

    return sales_df



def export_sales_data(
    sales_df,
    output_file="data/Sales_Data.xlsx"
):
    """
    Export sales data to Excel.
    """

    sales_df.to_excel(
        output_file,
        index=False
    )

    print(f"\n✅ {len(sales_df):,} records exported successfully.")

    print(f"📁 File : {output_file}")


if __name__ == "__main__":

    customer_df, product_df = load_master_data()

    sales_df = generate_sales_dataframe(
        customer_df,
        product_df,
        total_records=1000
    )

    print(sales_df.head())

    export_sales_data(sales_df)



