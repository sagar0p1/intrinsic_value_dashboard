import streamlit as st
from modules.extractor import extract_financial_data

st.title("Intrinsic Value Dashboard")

uploaded_file = st.file_uploader("Upload Annual Report PDF", type=["pdf"])

if uploaded_file is not None:
    financial_data = extract_financial_data(uploaded_file)
    
    # Show extracted text for debugging - remove or comment out once satisfied
    st.subheader("Extracted Text from PDF (for debugging):")
    st.text_area("", financial_data.get("full_text", ""), height=400)
    
    # Show extracted financial numbers
    st.subheader("Extracted Financial Data:")
    st.write(f"Revenue: {financial_data['Revenue']:,}")
    st.write(f"Net Income: {financial_data['Net Income']:,}")
