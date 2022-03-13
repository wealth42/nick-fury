import pandas as pd

df1 = pd.read_csv("pdf1.txt")
df1.to_csv("pdf1.csv",index=None)
