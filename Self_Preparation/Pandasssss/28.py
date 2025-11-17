import pandas as pd

a=pd.read_csv("data.csv")

print(a.corr())


# import pandas as pd
#
# data = {
#     'temperature': [20, 25, 30, 35, 40],
#     'ice_cream_sales': [100, 150, 200, 250, 300],
#     'rainfall': [50, 40, 30, 20, 10]
# }
# df = pd.DataFrame(data)
#
# # Get correlation matrix
# print(df.corr())