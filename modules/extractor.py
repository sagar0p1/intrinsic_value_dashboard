import fitz  # PyMuPDF
import re

def extract_financial_data(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Extract Revenue
    revenue_match = re.search(r"Revenue[s]?\s*[:\-]?\s*\$?\s*([\d,\.]+)", text, re.IGNORECASE)
    revenue = float(revenue_match.group(1).replace(",", "")) if revenue_match else 0

    # Extract Net Income
    net_income_match = re.search(r"Net Income\s*[:\-]?\s*\$?\s*([\d,\.]+)", text, re.IGNORECASE)
    net_income = float(net_income_match.group(1).replace(",", "")) if net_income_match else 0

    return revenue, net_income, text
