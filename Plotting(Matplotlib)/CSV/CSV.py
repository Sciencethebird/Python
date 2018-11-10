
import csv 
import os

cwd = os.getcwd()
cwd = cwd + '\\CSV\\'
print(cwd)
with open(cwd+'example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    dates = []
    names = []

    for row in readCSV:
        name = row[3]
        date = row[0]
        
        dates.append(date)
        names.append(name)

    print(dates)
    print(names)
    
    whatname = input('Type in Name to find Date: ')
    idx = names.index(whatname)
    print('Date of ',whatname, 'is ', dates[idx])


