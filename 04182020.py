import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GM.csv")
 
data["Date"] = pd.to_datetime(data["Date"])


data = data.set_index("Date")
gm_year = data.groupby(pd.Grouper(freq='Y')).agg({'Close':'mean'})

plt.plot(gm_year.index.year, gm_year["Close"], color ='red')
#barlist[0].set_color("blue")
#barlist[10].set_color("green")

plt.xlabel("Year")
plt.ylabel("close")
plt.title("Bar graph example")
plt.show()
