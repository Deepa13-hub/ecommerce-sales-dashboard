import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("sales_data.csv", encoding="latin1")
st.title("Product Analysis")

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    title="Sales by Product"
)

st.plotly_chart(fig)