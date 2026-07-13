"""
customer_generator.py
----------------------------------
Generates realistic Customer Master data.
"""

import random
import pandas as pd
from faker import Faker

from generator.lookup_data import (
    REGIONS,
    STATES,
    CITIES,
    CUSTOMER_TYPES
)

fake = Faker("en_IN")


def generate_customer_master(total_customers=10000):
    """
    Generate customer master DataFrame.
    """

    company_prefix = [
        "Shree",
        "Global",
        "Sunrise",
        "Royal",
        "Prime",
        "Modern",
        "Om",
        "Sai",
        "Mahalaxmi",
        "Krishna"
    ]

    company_suffix = [
        "Textiles",
        "Fabrics",
        "Garments",
        "Industries",
        "Exports",
        "Creation",
        "Fashion",
        "Weaving",
        "Apparels",
        "Traders"
    ]

    company_type = [
        "Pvt Ltd",
        "LLP",
        "Ltd",
        "& Co."
    ]

    customers = []

    for i in range(1, total_customers + 1):

        state = random.choice(STATES)
        city = random.choice(CITIES)
        region = random.choice(REGIONS)

        customer_name = (
            f"{random.choice(company_prefix)} "
            f"{random.choice(company_suffix)} "
            f"{random.choice(company_type)}"
        )

        customers.append({

            "Customer Code": f"CUST{i:06}",

            "Customer Name": customer_name,

            "Customer Type": random.choice(CUSTOMER_TYPES),

            "Region": region,

            "State": state,

            "City": city

        })

    df = pd.DataFrame(customers)

    return df


if __name__ == "__main__":

    df = generate_customer_master(20)

    print(df.head())

    df.to_excel("Customer_Master.xlsx", index=False)

    print("\nCustomer Master Created Successfully!")