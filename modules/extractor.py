import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    # file is the uploaded file-like object from Streamlit upload widget
    file.seek(0)  # reset file pointer to start
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def convert_to_number(s):
    try:
        return float(s.replace(',', '').replace('(', '-').replace(')', '').strip())
    except:
        return 0

def extract_financial_data(uploaded_file):
    text = extract_text_from_pdf(uploaded_file)

    # Regex patterns for Revenue and Net Income (case insensitive)
    revenue_pattern = re.compile(r"Revenue\s*[:\-]?\s*\$?([\d,\.]+)", re.IGNORECASE)
    net_income_pattern = re.compile(r"Net Income\s*[:\-]?\s*\$?([\d,\.]+)", re.IGNORECASE)

    revenue_match = revenue_pattern.search(text)
    net_income_match = net_income_pattern.search(text)

    revenue = convert_to_number(revenue_match.group(1)) if revenue_match else 0
    net_income = convert_to_number(net_income_match.group(1)) if net_income_match else 0

    return {
        "Revenue": revenue,
        "Net Income": net_income
    }
