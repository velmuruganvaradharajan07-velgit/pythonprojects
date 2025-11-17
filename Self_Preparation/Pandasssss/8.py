import pandas as pd
a={
    "numbers":[1,2,3,4,5,6,7],
    "integers":[11,22,33,44,55,66,77]
}
b=pd.DataFrame(a,index=["a","b","c","d","e","f","g"])
print(b.loc[["b","c"]])