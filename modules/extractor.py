import fitz  # PyMuPDF
import re

def extract_financial_data(pdf_file):
    # Load PDF and extract text from all pages
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Regex patterns to find revenue and net income with "million" unit
    revenue_match = re.search(r'Revenue[^0-9\.\,]*([\d,\.]+)\s*million', full_text, re.I)
    net_income_match = re.search(r'Net Income[^0-9\.\,]*([\d,\.]+)\s*million', full_text, re.I)

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
