import streamlit as st
from modules.extractor import extract_financial_data
from modules.dcf_calculator import calculate_intrinsic_value

st.set_page_config(page_title="Intrinsic Value Analyzer", layout="centered")

st.title("📊 Intrinsic Value Calculator")

uploaded_file = st.file_uploader("Upload Annual Report (PDF)", type=["pdf"])

if uploaded_file:
    with open("temp_report.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    st.success("✅ File uploaded successfully!")

    data = extract_financial_data("temp_report.pdf")

    if data:
        st.subheader("Extracted Financials:")
        for key, value in data.items():
            st.write(f"**{key}**: {value}")

        intrinsic_value = calculate_intrinsic_value(
            earnings=data['Net Income'],
            growth_rate=data['Growth Rate'],
            discount_rate=0.10,
            years=5
        )

        st.subheader("📈 Intrinsic Value:")
        st.write(f"Estimated intrinsic value per share: **${intrinsic_value:.2f}**")
    else:
        st.warning("⚠️ Could not extract data. Please check the PDF format.")
