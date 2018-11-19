
import csv 
import os

cwd = os.getcwd()
cwd = cwd + '\\CSV\\'# for windows
#cwd = cwd+'/' # for macs
print(cwd)
with open(cwd+'example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    dates = []
    names = []
    nums = []

    for row in readCSV:
        name = row[3]
        date = row[0]
        num = row[1]
        
        dates.append(date)
        names.append(name)
        nums.append(num)

    print(dates)
    print(names)
    print(nums[0]+nums[1])
    
    whatname = input('Type in Name to find Date: ')
    idx = names.index(whatname)
    print('Date of ',whatname, 'is ', dates[idx])


