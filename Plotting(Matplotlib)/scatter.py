
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = [3,7,3,4,5,2,8,9,3,8]

#Scatter Setting
plt.scatter(x, y, label = 'dots', color='k' , marker='D', s= 100)#k is black

#Figure Setting
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend()
plt.show()