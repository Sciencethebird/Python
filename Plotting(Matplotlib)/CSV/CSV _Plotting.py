import matplotlib.pyplot as plt
import csv
import numpy as np
import os

cwd = os.getcwd()
cwd = cwd + '\\CSV\\'

#import data using csv
'''
x = []
y = []

with open(cwd+'plotting_data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label= 'Loaded from file!')
'''

#import data using numpy

x, y = np.loadtxt(cwd+'plotting_data.txt', delimiter=',' , unpack=True)#unpack means sends a transpose matrix
plt.plot(x, y, label= 'Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')

plt.show()

