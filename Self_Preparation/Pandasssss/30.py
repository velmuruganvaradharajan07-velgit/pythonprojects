import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv("data.csv")

a.plot(kind ="scatter", x="Duration", y="Pulse")
plt.show()