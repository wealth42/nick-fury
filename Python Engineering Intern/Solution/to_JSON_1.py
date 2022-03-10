import pandas as pd
import json
# making dataframe
df = pd.read_csv("pdf1_csv.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.set_index("index",inplace=True)

#creating a json file
jsonfile = open('json_file_1.json', 'w')
# output the dataframe
#print(df)

#converting to json data
result = df.to_json(orient="index")
parsed = json.loads(result)
out = json.dumps(parsed, indent=4)
jsonfile.write(out)

