import sys, fitz
fname = sys.argv[0]  
doc = fitz.open('pdf2.pdf')  
out = open(fname + ".txt", "wb") 
for page in doc:  
    text = page.get_text().encode("utf8")  
    out.write(text)  
    out.write(bytes((12,))) 
out.close()

#i never used pymupdf lib but i'am trying my best
