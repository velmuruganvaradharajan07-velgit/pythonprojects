import pandas as pd

a=pd.read_csv("products100.csv")

b=a["Internal ID"].median()
a.fillna({"Internal ID":b},inplace=True)

print(a.to_string())