
import csv 
import os

cwd = os.getcwd()
cwd = cwd + '\\CSV\\'
print(cwd)
with open('example.csv','w') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    print(readCSV[0])