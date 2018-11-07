import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [3,4,5]

x1 = np.arange(0,2*np.pi, 0.01)
y1 = np.sin(x1)

plt.plot(x, y, label = 'line')
plt.plot(x1,y1, label = 'sin')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Graph') 

plt.legend()#圖例
plt.show()