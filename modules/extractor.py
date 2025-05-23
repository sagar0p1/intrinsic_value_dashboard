import fitz  # PyMuPDF
import re

def extract_financial_data(uploaded_file):
    # Load PDF and extract text
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Debug view (optional)
    full_text = text

    # Try to find revenue (looking for "Revenue" or similar)
    revenue_match = re.search(r'Revenue[^0-9]*([\d,]+\.?\d*)', text, re.IGNORECASE)

    # Try to find net income (may be written as "Profit for the year")
    net_income_match = re.search(r'Profit\s+for\s+the\s+year[^0-9]*([\d,]+\.?\d*)', text, re.IGNORECASE)

    try:
        revenue = float(revenue_match.group(1).replace(",", "")) if revenue_match else 0
    except:
        revenue = 0

    try:
        net_income = float(net_income_match.group(1).replace(",", "")) if net_income_match else 0
    except:
        net_income = 0

    return revenue, net_income, full_text
