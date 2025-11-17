import pandas as pd

a=pd.read_csv("products100.csv")

a.fillna(100, inplace=True)
print(a.to_string())