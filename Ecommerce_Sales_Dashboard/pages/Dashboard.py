import streamlit as st
import pandas as pd

df = pd.read_csv("sales_data.csv")

st.title("Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Sales",f"₹{df['Sales'].sum():,.0f}")
col2.metric("Profit",f"₹{df['Profit'].sum():,.0f}")
col3.metric("Orders",len(df))
col4.metric("Customers",df['Customer'].nunique())