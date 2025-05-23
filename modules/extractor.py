import fitz  # PyMuPDF
import re

def extract_number(text):
    try:
        return float(text.replace(",", "").replace(" ", ""))
    except (ValueError, AttributeError):
        return 0

def extract_financial_data(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Use regular expressions to extract financials
    revenue_match = re.search(r"Revenue[s]?\s*[:\-]?\s*\$?\s*([\d,\.]+)", text, re.IGNORECASE)
    net_income_match = re.search(r"Net Income\s*[:\-]?\s*\$?\s*([\d,\.]+)", text, re.IGNORECASE)

    revenue = extract_number(revenue_match.group(1)) if revenue_match else 0
    net_income = extract_number(net_income_match.group(1)) if net_income_match else 0

    return revenue, net_income, text
