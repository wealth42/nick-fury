import fitz
file=fitz.open('pdf1.pdf')
for page in file:
    text=page.get_text('text')
    txt=open(f'pdf1.json','a')
    txt.writelines(text)
    txt.close()
