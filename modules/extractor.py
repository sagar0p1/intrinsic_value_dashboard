import fitz  # PyMuPDF
import re

def extract_financial_data(pdf_file):
    # Load PDF from uploaded file (BytesIO)
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    full_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        full_text += page.get_text()
    
    # Simple regex to find numbers after keywords - customize as needed
    revenue = None
    net_income = None
    
    revenue_match = re.search(r"Revenue[\s:]*\$?([\d,]+)", full_text, re.IGNORECASE)
    if revenue_match:
        revenue = revenue_match.group(1).replace(",", "")
    
    net_income_match = re.search(r"Net Income[\s:]*\$?([\d,]+)", full_text, re.IGNORECASE)
    if net_income_match:
        net_income = net_income_match.group(1).replace(",", "")
    
    # Convert to int if found
    if revenue:
        revenue = int(revenue)
    else:
        revenue = 0
    
    if net_income:
        net_income = int(net_income)
    else:
        net_income = 0

    return {
        "Revenue": revenue,
        "Net Income": net_income
    }
