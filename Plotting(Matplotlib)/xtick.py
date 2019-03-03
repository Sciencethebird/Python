import matplotlib.pyplot as plt
import numpy as np



x = [1,2,3,4]
y =[2,3,4,1]

plt.scatter(x, y, c = 'r')
#locs, labels = plt.xticks()
plt.xticks(np.arange(0, 4, step=1), ('class 1', 'class 2', 'class 3'))
plt.show()