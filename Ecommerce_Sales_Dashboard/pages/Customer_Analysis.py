import streamlit as st
import pandas as pd



df = pd.read_csv("sales_data.csv", encoding="latin1")
st.title("Customer Analysis")

print(df.columns.tolist())

customer_sales = (
    df.groupby("Customer")["Sales"]
    .sum()
    .reset_index()
)

st.dataframe(customer_sales)