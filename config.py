PROJECT_NAME = "Smart Sales Analyzer Pro"

INPUT_FOLDER = "data"

OUTPUT_FOLDER = "output"

LOG_FOLDER = "logs"

REPORT_FOLDER = "reports"

INPUT_FILE = "Sales_Data.xlsx"

OUTPUT_FILE = "Sales_Report_Processed.xlsx"

TOTAL_RECORDS = 100000


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"

CUSTOMER_MASTER_FILE = DATA_DIR / "Customer_Master.xlsx"
PRODUCT_MASTER_FILE = DATA_DIR / "Product_Master.xlsx"
SALES_DATA_FILE = DATA_DIR / "Sales_Data.xlsx"

SUMMARY_SHEET = "Sales Summary"

GST_RATE = 18

DEFAULT_RECORDS = 1000