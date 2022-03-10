import csv
import json

csvfile = open('pdf2_csv.csv', 'r')
jsonfile = open('file2.json', 'w')

fieldnames = ("Retention code","Group code","Retention Description","Calcium, Ca","Iron, Fe","Magnesium, Mg","Phosphorus, P","Potassium, K","Sodium, Na","Zinc, Zn","Copper, Cu","Vitamin C, total ascorbic acid","Thiamin","Riboflavin","Niacin","Vitamin B-6","Folate, food","Folic acid","Folate, total","Choline, total","Vitamin B-12","Vitamin A, IU","Vitamin A, RE","Alcohol, ethyl","Carotene, beta","Carotene, alpha","Cryptoxanthin, beta","Lycopene","Lutein + zeaxanthin")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)