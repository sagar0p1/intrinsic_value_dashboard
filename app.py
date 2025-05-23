import streamlit as st
from modules.extractor import extract_financial_data

def intrinsic_value(net_income, growth_rate, discount_rate):
    try:
        intrinsic_val = net_income * (1 + growth_rate) / (discount_rate - growth_rate)
        return intrinsic_val
    except ZeroDivisionError:
        return None

st.title("Intrinsic Value Calculator")

uploaded_file = st.file_uploader("Upload Annual Report (PDF)", type=["pdf"])

if uploaded_file:
    financial_data = extract_financial_data(uploaded_file)

    st.subheader("Extracted Financial Data:")
    st.write(f"Revenue: {financial_data['Revenue']:,}")
    st.write(f"Net Income: {financial_data['Net Income']:,}")

    growth_rate = st.number_input("Expected Growth Rate (as decimal, e.g. 0.05 for 5%)", value=0.05, step=0.01, format="%.2f")
    discount_rate = st.number_input("Discount Rate (as decimal, e.g. 0.10 for 10%)", value=0.10, step=0.01, format="%.2f")

    if financial_data["Net Income"] > 0:
        intrinsic_val = intrinsic_value(financial_data["Net Income"], growth_rate, discount_rate)
        if intrinsic_val:
            st.subheader("Estimated Intrinsic Value:")
            st.write(f"${intrinsic_val:,.2f}")
        else:
            st.error("Discount rate must be greater than growth rate.")
    else:
        st.error("Could not extract Net Income from the report or it is zero.")
