import streamlit as st
import pandas as pd

st.title("CSV Test")

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

df.to_csv("test.csv", index=False)

df2 = pd.read_csv("test.csv")

st.success("CSV works!")
st.write(df2)