import pandas as pd
a=pd.read_csv("products100.csv")
val=a["Internal ID"].mean()
a.fillna({"Internal ID":val},inplace=True)
print(a.to_string())

