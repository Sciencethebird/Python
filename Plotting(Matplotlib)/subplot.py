import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math 

def create_data():
    x = []
    y = []

    for i in range(10):
        x.append(i)
        y.append(rd.randrange(100))
    return x, y

#figure() is everything about a window 
#functions like .add_subplot() belongs to this window
fig = plt.figure()

#axis is everything about a single coordinate, plot, scatter...belongs to an axis
#so it make sense .add_subplot() returns a axis
ax1 = fig.add_subplot(2,1,1) #divide a window into 2x1 space, and it's the first graph
ax2 = fig.add_subplot(2,2,3) #divide a window into 2x2 space, and it's the third graph
ax3 = fig.add_subplot(2,2,4)

#how to set each subplot using axis

#subplot 1
x, y = create_data()
ax1.plot(x, y, label = 'first',  color = 'b')
ax1.set_ylim(0, 200)

#subplot 2
x, y = create_data()
ax2.scatter(x, y, label = 'second', color = 'k')

#subplot 3
x = np.linspace(0, 2*math.pi)
#y = math.sin(x) #error
y = np.sin(x)    #there are math functions in math library too, but that eat list
                 #numpy functions eats array(numpy array)
ax3.plot(x, y, label = 'sin', color = 'r')
ax3.plot(x, np.tan(x), label = 'tan', color = 'green')
plt.ylim(-10, 10)#bad method, you should use axis.set_ylim()
ax3.legend()
plt.show()