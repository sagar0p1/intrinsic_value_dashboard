import streamlit as st
from modules.extractor import extract_financial_data

st.title("Intrinsic Value Calculator")

uploaded_file = st.file_uploader("Upload Annual Report PDF", type=["pdf"])

if uploaded_file:
    financial_data = extract_financial_data(uploaded_file)
    st.json(financial_data)

    # Example intrinsic value calculation
    revenue = financial_data.get("Revenue", 0)
    net_income = financial_data.get("Net Income", 0)
    intrinsic_value = (net_income * 10)  # Just a dummy formula

    st.success(f"Estimated Intrinsic Value: ${intrinsic_value:,.2f}")
