import fitz

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    doc = fitz.open("pdf", pdf_bytes)
    text = "\n".join([page.get_text() for page in doc])
    return text