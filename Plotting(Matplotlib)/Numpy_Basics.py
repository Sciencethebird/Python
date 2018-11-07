import matplotlib.pyplot as plt
import numpy as np

# arange: x form [0, 10) increase by 1
x = np.arange(0,10,1)
print(x)

# linespace: y belongs to [10, 2] with twenty dots, it's a line
y = np.linspace(10,2,20)
print(y)

z1 = x
z2 = y


#Visualization using matplotlib
plt.plot(x, z1, label = 'arrange')
plt.plot(y, z2, label = 'linspace')

plt.xlabel = 'x'
plt.ylabel = 'y'

plt.title = 'arrange vs linespace'

plt.legend()
plt.show()

