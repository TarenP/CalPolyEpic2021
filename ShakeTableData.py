import pandas as pd
import matplotlib.pyplot as plt

plotdata=pd.read_csv('Sensor Data CalPolyEpic 2021 - Data.csv')

x=plotdata['Time']
y=plotdata['ax']

plt.plot(x, y)
plt.savefig('DataPlot.png')
plt.show()