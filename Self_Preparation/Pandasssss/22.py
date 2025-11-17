import pandas as pd
b=pd.read_csv("products100.csv")
a=b["Date"]

pd.to_datetime(b["Date"],format="mixed")

print(b.to_string())