import fitz  # PyMuPDF
import re

def extract_financial_data(pdf_file):
    # Load PDF and extract text from all pages
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Regex patterns for Revenue and Net Income (with optional 'million' unit)
    revenue_pattern = re.compile(r"revenue[^0-9\.\,]*([\d,\.]+)\s*million", re.I)
    net_income_pattern = re.compile(r"net income[^0-9\.\,]*([\d,\.]+)\s*million", re.I)

    revenue_match = revenue_pattern.search(full_text)
    net_income_match = net_income_pattern.search(full_text)

    # Function to convert extracted string to float and multiply by 1,000,000
    def convert_to_millions(amount_str):
        try:
            clean_str = amount_str.replace(',', '').strip()
            return float(clean_str) * 1_000_000
        except:
            return 0

    revenue = convert_to_millions(revenue_match.group(1)) if revenue_match else 0
    net_income = convert_to_millions(net_income_match.group(1)) if net_income_match else 0

    return revenue, net_income, full_text
