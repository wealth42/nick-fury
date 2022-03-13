import fitz
pdf = "pdf1.pdf"
doc = fitz.open(pdf)
for page in doc:
    text=page.get_text("text")
    print(text)
doc.close()
