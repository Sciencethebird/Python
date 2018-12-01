
import matplotlib.pyplot as plt
import numpy as np
import math 

# arange and linespace both output np array

# arange: x1 form [0, 10) increase by 1
x1 = np.arange(0,10,0.1)
print(x1)

# linespace: x2 belongs to [10, 2] with twenty dots
x2 = np.linspace(10,2,50)
print('numpy array is converted to a python list \n', list(x2))

y1 = np.sin(x1)
y2 = np.cos(x2)

#1. math functions do not take np array
#2. math functions do not take list (one in one out)
#y3 = math.tan(list(x1))

#Visualization using matplotlib
plt.plot(x1, y1, label = 'arrange')
plt.plot(x2, y2, label = 'linspace')


plt.xlabel = 'x'
plt.ylabel = 'y'

plt.title = 'arrange vs linespace'

plt.legend()
plt.show()


