import streamlit as st

st.title("Test App")
st.write("If you see this, Streamlit is working!")

uploaded_file = st.file_uploader("Upload your annual report PDF")

if uploaded_file:
    st.success("PDF uploaded!")
if uploaded_file:
    st.write("Processing file:", uploaded_file.name)
    financial_data = extract_financial_data(uploaded_file)
    st.write("Financial Data Extracted:", financial_data)
