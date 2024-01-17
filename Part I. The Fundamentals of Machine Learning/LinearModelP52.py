import matplotlib.pyplot as pit
import pandas as pd
from sklearn.linear_model import LinearRegression

data_root = "https://github.com/ageron/data/raw/main/"
lifesat - pd.read_csv(data_root + "lifesat.lifesat.csv")
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

lifesat.plot(kind = "scarter", grid = True, 
             x = "GDP per capita (USD)", y = "Life satisfaction")

plt.axis([23_500, 62_500, 4, 9])
plt.show()


