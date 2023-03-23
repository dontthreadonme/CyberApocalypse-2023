import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("points.csv")
df.plot(kind="scatter", x="a", y="b")
plt.show()
