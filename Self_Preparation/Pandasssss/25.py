#dropping rows
import pandas as pd

a=pd.read_csv("products100.csv")

for x in a.index:
    if a.loc[x, "Price"]>200:
        a.drop(x,inplace=True)

print(a.to_string())

