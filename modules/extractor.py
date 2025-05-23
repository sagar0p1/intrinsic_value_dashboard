import fitz  # PyMuPDF
import re

def extract_financial_data(file):
    text = ""

    # Extract all text from PDF
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Try to extract revenue (placeholder pattern — not found in your sample yet)
    revenue_pattern = re.search(r"Revenue.*?€\s*([\d,]+)", text, re.IGNORECASE)
    revenue = float(revenue_pattern.group(1).replace(",", "")) * 1_000_000 if revenue_pattern else 0

    # Extract Net Income / Profit for the year
    net_income_pattern = re.search(r"Profit for the year\s*\(?[€\s]*([\d,]+)", text, re.IGNORECASE)
    net_income = float(net_income_pattern.group(1).replace(",", "")) * 1_000_000 if net_income_pattern else 0

    return revenue, net_income, text
