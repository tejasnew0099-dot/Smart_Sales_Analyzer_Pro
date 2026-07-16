import streamlit as st
from dashboard_engine import (
    load_dashboard_data,
    calculate_dashboard_kpis
)

st.title("Dashboard Test")

df = load_dashboard_data()

st.success("Data loaded successfully!")

st.write(df.head())

kpis = calculate_dashboard_kpis(df)

st.write(kpis)