import fitz
pdf = "pdf2.pdf"
doc = fitz.open(pdf)
for page in doc:
    text=page.get_text("text")
    print(text)
doc.close()
