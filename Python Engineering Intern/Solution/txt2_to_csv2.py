import pandas as pd

df1 = pd.read_csv("pdf2.txt")
df1.to_csv("pdf2.csv",index=None)
