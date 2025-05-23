import streamlit as st
from modules.extractor import extract_financial_data

st.title("📊 Intrinsic Value Estimator from Annual Report PDF")

uploaded_file = st.file_uploader("Upload Annual Report PDF", type=["pdf"])

if uploaded_file:
    revenue, net_income, full_text = extract_financial_data(uploaded_file)

    st.subheader("🔍 Extracted Financial Data:")
    st.write(f"**Revenue (in millions):** {revenue}")
    st.write(f"**Net Income (in millions):** {net_income}")

    st.subheader("📁 Extracted PDF Text (for debugging):")
    with st.expander("Show Raw Text"):
        st.text(full_text)

    if net_income == 0:
        st.error("❌ Could not extract Net Income from the report or it is zero.")
    else:
        st.subheader("💸 Intrinsic Value Calculator")
        growth_rate = st.number_input("Expected Growth Rate (as decimal)", value=0.05, step=0.01)
        discount_rate = st.number_input("Discount Rate (as decimal)", value=0.10, step=0.01)
        years = st.slider("Years of Projection", min_value=1, max_value=10, value=5)

        future_cash_flow = net_income * ((1 + growth_rate) ** years)
        intrinsic_value = future_cash_flow / ((1 + discount_rate) ** years)

        st.success(f"📈 Estimated Intrinsic Value (in same currency, millions): {intrinsic_value:,.2f}")
