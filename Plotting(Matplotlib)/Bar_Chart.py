
import matplotlib.pyplot as plt
import numpy as np

#Bar Charts
x = [1,2,3]
y = [3,4,5]

x1 = np.arange(1, 10, 2)
y1 = [1,2,3,6,3]

plt.bar(x, y, label = 'Bars 1', color = 'k')
plt.bar(x1, y1, label = 'Bars 2', color = 'red' )
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Bar Chart Basics')
plt.show()

#Bar Chart vs Histogram
#Bar Chart: Show ages correspoding to each person
#Histogram: Show how many people in 0-10,11-20,21-30 ........
ages = [10,12,14,62,74,23,11,34,76,45,22,64,86,45,99,35,13,35,42,22]
ids = [x for x in range (len(ages))]
bins = [x for x in range(0,111,10)]
print(bins)

#Bar Chart (Number of certain data)
plt.bar(ages, ids,color = 'orange', label = 'Bar Chart')
plt.ylabel('number of people')
plt.xlabel('age')
plt.title('Bar Chart of Age')
plt.show()

#Histogram (Number of data in certain range)
plt.hist(ages, bins, histtype='bar', rwidth = 0.8, color = 'blue')
plt.hist(ages, bins, histtype='step', color = 'orange')
plt.ylabel('number of people')
plt.xlabel('age(10 years)')
plt.title('Histogram of Age')
plt.show()
