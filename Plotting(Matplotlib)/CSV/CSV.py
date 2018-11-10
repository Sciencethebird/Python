
import csv 
import os

cwd = os.getcwd()
cwd = cwd + '\\CSV\\'
print(cwd)
with open(cwd+'example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]
        
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)
