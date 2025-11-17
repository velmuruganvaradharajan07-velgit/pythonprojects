import pandas as pd
a=["vel","murugan","re","bullet 350"]
b=pd.Series(a,index=("x","y","z","v"))
print(b)
print("the assigned value can be accessed by", b["z"])