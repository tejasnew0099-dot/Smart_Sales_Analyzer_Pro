import streamlit as st
from dashboard_engine import load_dashboard_data

st.title("Load Data Test")

df = load_dashboard_data()

st.success("Data loaded successfully!")

st.write(df.shape)
st.dataframe(df.head())