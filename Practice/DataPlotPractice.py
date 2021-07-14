import numpy as np
import matplotlib.pyplot as plt
import pandas

x=np.arange(0,5,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, linestyle = '-.', color = 'mediumslateblue', linewidth = 3)
plt.plot(x,z, linestyle = '-.', color = 'coral', linewidth = 3)
plt.title('Wave')
plt.xlabel('time(seconds)')
plt.ylabel('amplitude')
plt.show()
#plt.savefig('Figure.png')