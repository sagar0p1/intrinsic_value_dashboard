import fitz  # PyMuPDF
import re

def extract_financial_data(pdf_file):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    full_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        full_text += page.get_text()
    
    revenue_match = re.search(r"(Total\s)?Revenue[\s:]*\$?([\d,\.]+)?(\s?million)?", full_text, re.IGNORECASE)
    net_income_match = re.search(r"(Net\sIncome|Net\sProfit|Profit\sAfter\sTax)[\s:]*\$?([\d,\.]+)?(\s?million)?", full_text, re.IGNORECASE)

    def convert_to_number(amount_str, million_flag):
        if not amount_str or amount_str.strip() == "":
            return 0
        try:
            number = float(amount_str.replace(",", ""))
            if million_flag:
                number *= 1_000_000
            return int(number)
        except ValueError:
            return 0

    revenue = 0
    net_income = 0

    if revenue_match:
        amount_str = revenue_match.group(2)
        million_flag = revenue_match.group(3) is not None
        revenue = convert_to_number(amount_str, million_flag)
        
    if net_income_match:
        amount_str = net_income_match.group(2)
        million_flag = net_income_match.group(3) is not None
        net_income = convert_to_number(amount_str, million_flag)
    
    return {
        "full_text": full_text,
        "Revenue": revenue,
        "Net Income": net_income
    }
