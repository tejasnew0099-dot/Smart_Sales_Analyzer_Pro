"""
validator.py
------------------------------------
Validate Sales Data
"""

import pandas as pd


REQUIRED_COLUMNS = [
    "Invoice No",
    "Invoice Date",
    "Customer Code",
    "Customer Name",
    "Product Code",
    "Product Name",
    "Quantity",
    "Unit Price",
    "Gross Sales",
    "Net Sales",
    "Profit"
]


def validate_required_columns(df: pd.DataFrame):
    """
    Ensure all required columns exist.
    """

    missing = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    print("✅ Required columns validated.")


def validate_missing_values(df: pd.DataFrame):
    """
    Check for missing values.
    """

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:

        print("✅ No missing values found.")

    else:

        print("\n⚠ Missing Values Found:")

        print(missing)


def validate_duplicate_invoices(df: pd.DataFrame):
    """
    Check duplicate invoice numbers.
    """

    duplicates = df["Invoice No"].duplicated().sum()

    if duplicates == 0:

        print("✅ No duplicate invoices.")

    else:

        print(f"⚠ {duplicates} duplicate invoices found.")



def validate_negative_values(df: pd.DataFrame):
    """
    Check important numeric columns.
    """

    columns = [
        "Quantity",
        "Unit Price",
        "Gross Sales",
        "Net Sales"
    ]

    for column in columns:

        negative = (df[column] < 0).sum()

        if negative:

            print(f"⚠ {column} has {negative} negative values.")

        else:

            print(f"✅ {column} validated.")


def validate_sales_data(df: pd.DataFrame):
    """
    Run all validations.
    """

    validate_required_columns(df)

    validate_missing_values(df)

    validate_duplicate_invoices(df)

    validate_negative_values(df)

    print("\n🎉 Validation Completed Successfully.")


if __name__ == "__main__":

    from core.excel_reader import load_sales_data

    df = load_sales_data()

    validate_sales_data(df)