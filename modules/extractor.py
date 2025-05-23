import fitz  # PyMuPDF
import re

def extract_financial_data(file):
    text = ""

    # Extract all text from the PDF
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Attempt to extract Revenue (adjusted for EU formatting)
    revenue_match = re.search(r"Revenue\s*€\s*million\s*2024\s*([\d,]+)", text, re.IGNORECASE)
    revenue = float(revenue_match.group(1).replace(",", "")) * 1_000_000 if revenue_match else 0

    # Attempt to extract Net Income (Profit for the year)
    net_income_match = re.search(r"Profit for the year\s*€\s*million\s*2024\s*([\d,]+)", text, re.IGNORECASE)
    net_income = float(net_income_match.group(1).replace(",", "")) * 1_000_000 if net_income_match else 0

    return revenue, net_income, text
