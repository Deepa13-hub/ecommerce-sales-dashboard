import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

.title {
    text-align: center;
    color: #2563EB;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #475569;
    font-size: 20px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("assets/logo.png", width=180)

st.sidebar.title("📊 Navigation")

st.sidebar.success("Select a page from the sidebar")

# Main Header
st.markdown(
    '<p class="title">📊 E-Commerce Sales Analytics Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Business Intelligence & Sales Forecasting System</p>',
    unsafe_allow_html=True
)

st.write("")

# Welcome Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🚀 Project Overview

    This dashboard helps businesses analyze:

    - 📈 Sales Performance
    - 👥 Customer Insights
    - 📦 Product Performance
    - 🌎 Regional Analysis
    - 💰 Profit Analysis
    - 🤖 Sales Prediction

    Use the navigation menu on the left to explore different modules.
    """)

with col2:
    st.image("assets/amazon.png", width=120)
    st.image("assets/flipkart.png", width=120)

st.write("---")

# Features Section
st.subheader("✨ Dashboard Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
    📊 Dashboard

    View KPI metrics,
    sales trends and
    business performance.
    """)

with c2:
    st.success("""
    👥 Customer Analysis

    Analyze customer
    spending patterns
    and top buyers.
    """)

with c3:
    st.warning("""
    📦 Product Analysis

    Identify best-selling
    products and categories.
    """)

st.write("")

c4, c5, c6 = st.columns(3)

with c4:
    st.info("""
    📈 Sales Analysis

    Analyze sales by
    region, platform,
    and time period.
    """)

with c5:
    st.success("""
    🤖 Prediction

    Forecast future sales
    using Machine Learning.
    """)

with c6:
    st.warning("""
    📄 Reports

    Export reports
    and business insights.
    """)

st.write("---")

st.markdown(
    """
    <center>
    <h4 style='color:#2563EB'>
    Developed using Streamlit • Pandas • Plotly • SQLite • Scikit-Learn
    </h4>
    </center>
    """,
    unsafe_allow_html=True
)