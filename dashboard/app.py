import streamlit as st

st.title("Plotly Diagnostic")

try:
    import plotly
    st.success(f"Plotly imported successfully: {plotly.__version__}")
    st.write("Location:", plotly.__file__)
except Exception as e:
    st.error(f"Plotly import failed: {e}")
    st.stop()

try:
    import plotly.express as px
    st.success("plotly.express imported successfully")
except Exception as e:
    st.error(f"plotly.express import failed: {e}")