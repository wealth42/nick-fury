import csv
import json

csvfile = open('pdf1_csv.csv', 'r')
jsonfile = open('file1.json', 'w')

fieldnames = (" ","MTLGPUFamilyApple1","MTLGPUFamilyApple2","MTLGPUFamilyApple3","MTLGPUFamilyApple4","MTLGPUFamilyApple5","MTLGPUFamilyApple6","MTLGPUFamilyApple7","MTLGPUFamilyMac1","MTLGPUFamilyMac2","MTLGPUFamilyMacCatalyst1","MTLGPUFamilyMacCatalyst2")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)