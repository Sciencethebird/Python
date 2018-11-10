import os

cwd = os.getcwd()
cwd = cwd +'\\'+'File_IO\\'
print('Current Working Directory:\t' + cwd)

lt = [1,2,3,4]
temp = str(lt)

def what_is_in_file(filename = 'default.txt'):
    with open(cwd+filename, 'r') as file:
        return file.read()

#'w' mode
#create a new file and delete the old one(if there's any)
#discard whatever was in the file 
#Write from begining

print('\nw mode')
file = open(cwd + 'default.txt', 'w')
file.write('123456789')
file.close()
print(what_is_in_file()+'\n\n')

#'r+' mode
# read/write from beginning (keep old data)
# '+' basically means it modifies the original file, and allowing read/write
# can't run if the the file DNE 

print('r+ mode, add 000')
print('before change:' + what_is_in_file())
file = open(cwd + 'default.txt', 'r+')
file.write('000')
file.close()
print('after change: ' + what_is_in_file()+'\n\n')


#'a+' mode
#read/write from the end
# add to the end, for both read/write
print('a+ mode, add xxx')
print('before change:' + what_is_in_file())
file = open(cwd + 'default.txt', 'a+')
file.write('xxx')
file.close()
print('after change: ' + what_is_in_file()+'\n\n')

#readlines returns a list
file = open(cwd + 'default.txt','r')
text = file.readlines()
print(text[0])
file.close()

