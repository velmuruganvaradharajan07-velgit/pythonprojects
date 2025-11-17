import pandas as pd

a=pd.read_csv("products100.csv")

b=a.to_string()

print(a.duplicated())