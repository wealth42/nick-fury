import fitz
import pandas as pd 
file=fitz.open('pdf1.pdf')
for page in file:
    word=page.get_text('words')
    #saving raw data in json file
    wd=open(f'pdf1.json','a')
    wd.writelines(str(word))
    wd.close()
