import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🤖 Sales Prediction")

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

future_day = st.number_input(
    "Enter Future Day",
    min_value=1,
    value=len(df) + 10
)

prediction = model.predict([[future_day]])

st.success(
    f"Predicted Sales: ₹{prediction[0]:,.0f}"
)