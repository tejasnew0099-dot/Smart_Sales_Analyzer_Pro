import streamlit as st

st.set_page_config(page_title="Test")

st.title("Deployment Test")

import plotly.express as px

st.success("✅ Plotly imported successfully")

from dashboard_charts import monthly_sales_chart

st.success("✅ dashboard_charts imported successfully")