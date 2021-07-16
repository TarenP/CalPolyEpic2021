import pandas as pd
import matplotlib.pyplot as plt

plotdata=pd.read_csv('Sensor Data CalPolyEpic 2021 - Data.csv')

x=plotdata['Time']
ax=plotdata['ax']
ay=plotdata['ay']
az=plotdata['az']
plt.plot(x, ax, color='red', alpha = 0.6)
plt.plot(x, ay, color='blue', alpha = 0.8)
plt.plot(x,az, color='green', alpha = 0.7)
plt.legend("xyz")
plt.ylabel("Acceleration(g)")
plt.xlabel("Time(s)")
plt.title("Nonupgraded Building")
plt.savefig('NonupgradedDataPlot.png')
plt.show()