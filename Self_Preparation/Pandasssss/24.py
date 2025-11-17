import pandas as pd
a=pd.read_csv("products100.csv")
for x in a.index:
    if a.loc[x,"Price"]>100:
        a.loc[x,"Price"]=100000
print(a.to_string())