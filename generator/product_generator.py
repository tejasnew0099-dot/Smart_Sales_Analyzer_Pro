"""
product_generator.py
------------------------------------
Generates Product Master Data
"""

import random
import pandas as pd

from generator.lookup_data import (
    PRODUCT_CATEGORIES,
    BRANDS
)

FABRIC_NAMES = [
    "Poplin",
    "Twill",
    "Canvas",
    "Satin",
    "Lycra",
    "Voile",
    "Cambric",
    "Oxford",
    "Drill",
    "Ribstop",
    "Denim",
    "Corduroy"
]

COLORS = [
    "White",
    "Black",
    "Blue",
    "Indigo",
    "Grey",
    "Navy",
    "Cream",
    "Red",
    "Green",
    "Brown"
]

GSM_LIST = [
    100,
    120,
    140,
    160,
    180,
    200,
    240,
    280,
    320,
    350
]

WIDTHS = [
    '44"',
    '58"',
    '60"',
    '72"'
]

UOM = [
    "Meter",
    "Kg",
    "Roll"
]


def generate_product_master(total_products=500):

    products = []

    for i in range(1, total_products + 1):

        cost_price = random.randint(80, 600)

        selling_price = round(
            cost_price * random.uniform(1.15, 1.40),
            2
        )

        products.append({

            "Product Code": f"PROD{i:06}",

            "Product Name":
                f"{random.choice(FABRIC_NAMES)} "
                f"{random.choice(GSM_LIST)} GSM",

            "Category":
                random.choice(PRODUCT_CATEGORIES),

            "Brand":
                random.choice(BRANDS),

            "Color":
                random.choice(COLORS),

            "Width":
                random.choice(WIDTHS),

            "UOM":
                random.choice(UOM),

            "Cost Price":
                cost_price,

            "Selling Price":
                selling_price

        })

    return pd.DataFrame(products)


if __name__ == "__main__":

    df = generate_product_master(50)

    print(df.head())

    df.to_excel("Product_Master.xlsx", index=False)

    print("\nProduct Master Created Successfully!")