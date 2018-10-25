
lt = [1,2,3,4]
temp = str(lt)
print(temp)

#create a new file and delete the old one(if there's any)
#Write from begining
file = open('default.txt', 'w')
file.write('\n')
file.write('write mode')
file.close()

#'r+' read/write from beginning (keep old data)
file = open('default.txt', 'r+')
file.write('r+       ')
file.close()

#append mode
lt = [0,0,0,0]
file = open('default.txt', 'a+')
file.write('\nappend mode')
file.close()

file = open('default.txt')
text = file.read()
print(text)
file.close()
