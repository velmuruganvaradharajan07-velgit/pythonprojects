import pandas as pd

a=pd.read_csv("products100.csv")
print(a.head(5))
print(a.tail(5))
print(a.info())