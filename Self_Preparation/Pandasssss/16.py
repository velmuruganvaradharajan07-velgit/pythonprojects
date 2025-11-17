#DROPMNA()

import pandas as pd
a=pd.read_csv("products100.csv")
b=a.dropna()
print(b.to_string())