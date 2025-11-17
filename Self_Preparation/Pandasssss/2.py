import pandas as pd

a={
    "car":["volkswagon","benz","audi","bmw","honda"],
    "bike":["RE","yamaha","hero","vespa","tvs"]
}
b=pd.DataFrame(a)  # to organize data in correct format

print(b)