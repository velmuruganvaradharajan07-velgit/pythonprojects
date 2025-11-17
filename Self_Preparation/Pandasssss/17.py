import pandas as pf

a=pf.read_csv("products100.csv")
a.dropna(inplace=True)

print(a.to_string())