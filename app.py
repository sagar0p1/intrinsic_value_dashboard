import streamlit as st

st.title("Test App")
st.write("If you see this, Streamlit is working!")

uploaded_file = st.file_uploader("Upload your annual report PDF")

if uploaded_file:
    st.success("PDF uploaded!")
