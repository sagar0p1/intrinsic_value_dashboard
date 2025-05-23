import fitz  # PyMuPDF
import re
import streamlit as st

def extract_text_from_pdf(uploaded_file):
    # Open PDF file with PyMuPDF
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def convert_to_number(amount_str):
    if not amount_str:
        return 0
    # Remove commas
    amount_str = amount_str.replace(",", "").strip()
    # Handle negative numbers in parentheses
    if amount_str.startswith('(') and amount_str.endswith(')'):
        amount_str = "-" + amount_str[1:-1]
    try:
        return float(amount_str)
    except ValueError:
        return 0

def extract_financial_data(uploaded_file):
    text = extract_text_from_pdf(uploaded_file)

    # DEBUG: show extracted text in Streamlit app to help adjust regex
    st.text_area("Extracted PDF Text (for debugging)", text, height=300)

    # Regex patterns - adjust these based on your PDF text format!
    revenue_pattern = re.compile(r"Revenue[\s:]*\$?([\d,().\-]+)", re.IGNORECASE)
    net_income_pattern = re.compile(r"Net Income[\s:]*\$?([\d,().\-]+)", re.IGNORECASE)

    revenue_match = revenue_pattern.search(text)
    net_income_match = net_income_pattern.search(text)

    revenue = convert_to_number(revenue_match.group(1)) if revenue_match else 0
    net_income = convert_to_number(net_income_match.group(1)) if net_income_match else 0

    return {
        "Revenue": revenue,
        "Net Income": net_income
    }
