import pandas as pd

a=pd.read_csv("products100.csv")

a.loc[0,"Price"]=100000

print(a.to_string())