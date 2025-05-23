import streamlit as st
from modules.extractor import extract_financial_data

st.title("Intrinsic Value Calculator")

uploaded_file = st.file_uploader("Upload Annual Report (PDF)", type=["pdf"])

if uploaded_file is not None:
    revenue, net_income, full_text = extract_financial_data(uploaded_file)

    st.subheader("Extracted Financial Data:")
    st.write(f"Revenue: {revenue}")
    st.write(f"Net Income: {net_income}")

    st.subheader("Expected Growth Rate (as decimal, e.g. 0.05 for 5%)")
    growth_rate = st.number_input("Enter expected growth rate", value=0.05, format="%.2f")

    st.subheader("Discount Rate (as decimal, e.g. 0.10 for 10%)")
    discount_rate = st.number_input("Enter discount rate", value=0.10, format="%.2f")

    if net_income > 0:
        intrinsic_value = net_income * (1 + growth_rate) / discount_rate
        st.success(f"Estimated Intrinsic Value: {intrinsic_value:,.2f}")
    else:
        st.error("Could not extract Net Income from the report or it is zero.")

    # Optional: Show raw text for debugging
    st.subheader("Extracted PDF Text (for debugging)")
    st.text_area("PDF Text", value=full_text, height=300)
