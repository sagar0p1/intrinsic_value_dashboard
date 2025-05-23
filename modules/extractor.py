import fitz  # PyMuPDF
import re

def extract_financial_data(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Define patterns for Revenue and Net Income (case insensitive, allow some spacing)
    revenue_pattern = re.compile(r"Revenue\s*[:\-]?\s*\$?([\d,\.]+)", re.IGNORECASE)
    net_income_pattern = re.compile(r"Net Income\s*[:\-]?\s*\$?([\d,\.]+)", re.IGNORECASE)

    revenue_match = revenue_pattern.search(text)
    net_income_match = net_income_pattern.search(text)

    def parse_number(num_str):
        # Remove commas and convert to float
        try:
            return float(num_str.replace(",", ""))
        except:
            return 0

    revenue = parse_number(revenue_match.group(1)) if revenue_match else 0
    net_income = parse_number(net_income_match.group(1)) if net_income_match else 0

    return {"Revenue": revenue, "Net Income": net_income}
