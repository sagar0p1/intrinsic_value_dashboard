import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def clean_number(text):
    try:
        text = text.replace(",", "").replace("(", "-").replace(")", "").strip()
        return float(re.findall(r"-?\d+(?:\.\d+)?", text)[0])
    except:
        return 0.0

def find_financial_value(text, keywords):
    lines = text.split("\n")
    for line in lines:
        for kw in keywords:
            if kw.lower() in line.lower():
                match = re.search(r"(-?\(?\d[\d,.\(\)]{3,})", line)
                if match:
                    return clean_number(match.group(1))
    return 0.0

def extract_financial_data(file):
    text = extract_text_from_pdf(file)

    revenue_keywords = ["total revenue", "revenue", "sales", "turnover"]
    net_income_keywords = ["net income", "net profit", "profit after tax", "earnings"]

    revenue = find_financial_value(text, revenue_keywords)
    net_income = find_financial_value(text, net_income_keywords)

    return revenue, net_income, text  # Return full text for debugging
