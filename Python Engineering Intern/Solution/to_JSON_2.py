import pandas as pd
import json
# making dataframe
df = pd.read_csv("pdf2_csv.csv")
#df.set_index("",inplace=True)

#creating a json file
jsonfile = open('json_file_2.json', 'w')
# output the dataframe
#print(df)

#converting to json data
result = df.to_json(orient="records")
parsed = json.loads(result)
out = json.dumps(parsed, indent=4)
jsonfile.write(out)

