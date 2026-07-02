import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Sales Analysis")

df = pd.read_csv("sales_data.csv")

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig1 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Region Wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# Platform Sales
platform_sales = df.groupby("Platform")["Sales"].sum().reset_index()

fig2 = px.pie(
    platform_sales,
    names="Platform",
    values="Sales",
    title="Platform Wise Sales"
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Trend
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = (
    df.groupby(df["Date"].dt.month)["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)