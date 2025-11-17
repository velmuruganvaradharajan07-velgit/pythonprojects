import pandas as pd
a={"name":"Vel",
   "age":"27",
   "off":"Hitachi",
   "previous org":"siemens"
   }
b=pd.Series(a,index=["name","age"])
print(b)