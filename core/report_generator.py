"""
report_generator.py
------------------------------------
Generate Management Report
"""

from openpyxl import Workbook
from core.formatter import format_report

from core.charts import (
    create_region_chart,
    create_product_chart,
    create_monthly_chart,
)


def create_report(analysis):
    """
    Create Excel management report.
    """

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Management Report"

    # -------------------------
    # Title
    # -------------------------
    sheet["A1"] = "SMART SALES ANALYZER REPORT"

    # -------------------------
    # KPI Section
    # -------------------------
    row = 3
    sheet[f"A{row}"] = "Executive KPIs"
    row += 1

    for key, value in analysis["kpis"].items():
        sheet[f"A{row}"] = key
        sheet[f"B{row}"] = value
        row += 1

    # -------------------------
    # Region Sales
    # -------------------------
    row += 2
    sheet[f"A{row}"] = "Region-wise Sales"
    row += 1

    for region, sales in analysis["region_sales"].items():
        sheet[f"A{row}"] = region
        sheet[f"B{row}"] = sales
        row += 1

    # -------------------------
    # Top Customers
    # -------------------------
    row += 2
    sheet[f"A{row}"] = "Top 10 Customers"
    row += 1

    for customer, sales in analysis["customer_sales"].head(10).items():
        sheet[f"A{row}"] = customer
        sheet[f"B{row}"] = sales
        row += 1

    # -------------------------
    # Top Products
    # -------------------------
    row += 2
    sheet[f"A{row}"] = "Top 10 Products"
    row += 1

    for product, sales in analysis["product_sales"].head(10).items():
        sheet[f"A{row}"] = product
        sheet[f"B{row}"] = sales
        row += 1

    return workbook


if __name__ == "__main__":

    print("🚀 Starting Report Generation...")

    from core.excel_reader import load_sales_data
    from core.analyzer import analyze_sales

    df = load_sales_data()
    analysis = analyze_sales(df)

    workbook = create_report(analysis)

    format_report(workbook)

    sheet = workbook["Management Report"]

    create_region_chart(
        sheet,
        12,
        16,
    )

    create_product_chart(
        sheet,
        34,
        43,
    )

    # Uncomment if you have monthly sales data and want the chart
    # create_monthly_chart(
    #     sheet,
    #     56,
    #     65,
    # )

    workbook.save("output/Management_Report.xlsx")

    print("✅ Management Report Created Successfully!")