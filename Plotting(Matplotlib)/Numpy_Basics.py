import matplotlib.pyplot as plt
import numpy as np

# x form [0, 10) increase by 1
x = np.arange(0,10,1)
print(x)

# y belongs to [10, 2] with twenty dots, it's a line
y = np.linspace(10,2,20)

z = np.sin(y)
''''
print(z)
plt.plot(x,x**2, label = 'sdf')
fig, ax = plt.subplots(1, 1)
ax.plot(x,x*2, label = '2df')
print(ax)
fig.show()
'''

rect = 0, 0, 0.5, 0.5
fig = plt.figure(1)
fig.add_axes(rect,label='asdasd')
fig.add_axes(rect,label='asdaddddddd')
#fig.add_axes(rect, frameon=False, facecolor='g')
#fig.add_axes(rect, polar=True)
ax=fig.add_axes(rect, projection='polar')
fig.delaxes(ax)
fig.add_axes(ax)
plt.show()
