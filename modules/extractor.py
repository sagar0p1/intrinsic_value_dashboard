import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    print("Extracted PDF Text:")
    print(full_text)  # print raw text to check what is extracted
    return full_text

# Then you can manually search in the output for revenue/net income
