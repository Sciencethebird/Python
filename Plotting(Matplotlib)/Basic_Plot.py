import matplotlib.pyplot as plt

x = [1,2,3]
y = [3,4,5]

x1 = [4,5,6]
y1 = [4,5,6]

plt.plot(x, y, label = 'jjj')
plt.plot(x1,y1, label = 'kkkkk')

plt.legend()
plt.show()