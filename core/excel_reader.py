import pandas as pd

from config import SALES_DATA_FILE


def load_sales_data():
    """
    Load Sales_Data.xlsx into a DataFrame.
    """

    df = pd.read_excel(SALES_DATA_FILE)

    return df


if __name__ == "__main__":

    df = load_sales_data()

    print(df.head())

    print(f"\nRows : {len(df):,}")

    print(f"Columns : {len(df.columns)}")