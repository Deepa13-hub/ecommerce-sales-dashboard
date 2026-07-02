import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("sales_data.csv", encoding="latin1")
st.title("Region Analysis")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region_sales,
    names="Region",
    values="Sales"
)

st.plotly_chart(fig)