import streamlit as st
import pandas as pd



df = pd.read_csv("sales_data.csv", encoding="latin1")
st.title("Reports")

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV Report",
    csv,
    "sales_report.csv",
    "text/csv"
)