# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("pdf1.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("pdf1.pdf", "pdf1_csv.csv", output_format="csv", pages='all')
print(df)