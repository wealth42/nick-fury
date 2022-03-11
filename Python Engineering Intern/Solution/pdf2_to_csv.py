# Importing the Module
import tabula
# Read a PDF File
df = tabula.read_pdf("pdf2.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("pdf2.pdf", "pdf2_csv.csv", output_format="csv", pages='all')
print(df)