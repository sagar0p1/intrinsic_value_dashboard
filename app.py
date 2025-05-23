import streamlit as st
from modules.extractor import extract_financial_data

st.title("Intrinsic Value Calculator")

uploaded_file = st.file_uploader("Upload your Annual Report (PDF)", type=["pdf"])
if uploaded_file:
    financial_data = extract_financial_data(uploaded_file)

    st.write("Extracted Financial Data:")
    st.write(f"Revenue: {financial_data['Revenue']}")
    st.write(f"Net Income: {financial_data['Net Income']}")

    expected_growth = st.number_input("Expected Growth Rate (decimal)", value=0.05, step=0.01)
    discount_rate = st.number_input("Discount Rate (decimal)", value=0.10, step=0.01)

    if financial_data["Net Income"] > 0:
        intrinsic_value = financial_data["Net Income"] * (1 + expected_growth) / (discount_rate - expected_growth)
        st.write(f"Estimated Intrinsic Value: {intrinsic_value:.2f}")
    else:
        st.write("Could not extract Net Income or it is zero.")
