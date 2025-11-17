import pandas as pd
a=pd.read_csv("products100.csv")
a.drop_duplicates(inplace=True)


print(a.to_string())