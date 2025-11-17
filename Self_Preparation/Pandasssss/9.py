import pandas as pd
a={
    "cars":["volkswagon","toyato","KIA","TATA","M and M"],
    "bike":["RE","TVS","Apache","Honda","hero"]
}

b=pd.DataFrame(a)
print(b)
print(b.loc[[2,1,3]])