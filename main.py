"""
main.py
------------------------------------
Smart Sales Analyzer Pro v2.0
Main Application Controller
"""


from generator.customer_generator import (
    generate_customer_master
)

from generator.product_generator import (
    generate_product_master
)

from generator.sales_generator import (
    generate_sales_dataframe,
    export_sales_data,
    load_master_data
)

from core.excel_reader import (
    load_sales_data
)

from core.validator import (
    validate_sales_data
)

from core.analyzer import (
    calculate_kpis,
    monthly_sales,
    state_sales,
    city_sales,
    category_sales,
    brand_sales,
    product_sales,
    product_profit,
    profit_margin,
    customer_type_sales,
    top_customers,
    customer_profit,
    customer_segmentation
)

from core.report_generator import (
    create_report
)


def main():

    print("\n================================")
    print(" SMART SALES ANALYZER PRO v2.0 ")
    print("================================\n")


    # --------------------------------
    # Step 1: Generate Master Data
    # --------------------------------

    print("🚀 Generating Master Data...")


    generate_customer_master()

    generate_product_master()


    # --------------------------------
    # Step 2: Generate Sales Data
    # --------------------------------

    print("\n🚀 Generating Sales Data...")


    customer_df, product_df = load_master_data()


    sales_df = generate_sales_dataframe(
        customer_df,
        product_df,
        total_records=1000
    )


    export_sales_data(
        sales_df
    )


    # --------------------------------
    # Step 3: Validation
    # --------------------------------

    print("\n🚀 Validating Sales Data...")


    df = load_sales_data()


    validate_sales_data(df)



    # --------------------------------
    # Step 4: Analytics
    # --------------------------------

    print("\n🚀 Running Analytics...")


    analysis = {}


    analysis["kpis"] = calculate_kpis(df)

    analysis["monthly_sales"] = monthly_sales(df)

    analysis["region_sales"] = (
    df.groupby("Region")["Net Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    )

    analysis["state_sales"] = state_sales(df)

    analysis["city_sales"] = city_sales(df)

    analysis["category_sales"] = category_sales(df)

    analysis["brand_sales"] = brand_sales(df)

    analysis["product_sales"] = product_sales(df)

    analysis["product_profit"] = product_profit(df)

    analysis["profit_margin"] = profit_margin(df)

    analysis["customer_type_sales"] = customer_type_sales(df)

    analysis["customer_sales"] = top_customers(df)

    analysis["customer_profit"] = customer_profit(df)

    analysis["customer_segment"] = customer_segmentation(df)



    print("✅ Analytics Completed")



    # --------------------------------
    # Step 5: Report
    # --------------------------------

    print("\n🚀 Creating Management Report...")


    workbook = create_report(
        analysis
    )


    workbook.save(
        "reports/Management_Report.xlsx"
    )


    print(
        "✅ Management Report Created Successfully!"
    )



if __name__ == "__main__":

    main()