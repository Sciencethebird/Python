'''
- variable number of arguments
- list initialize
- for loop
- range()
- len()

'''

def count_alphabet_old(input, *alphabet):
    print(input)
    count = [] #initialize first just like temp
    for i in alphabet:
        temp = 0
        for char in input:
            if char == i:
                temp+=1
        count += [temp]

    for i in range(len(count)):
       print('Number of' , alphabet[i],' = ', count[i], ' ')
    print('')

def if_any_alphabet(input, *alphabet):
    print(input)
    count = []  # initialize first just like temp
    for i in alphabet:
        temp = False
        if i in input:
            temp = True
        count += [temp]

    for i in range(len(count)):
        print('Is there any ', alphabet[i], '? ', count[i], ' ')
    print('')

input = 'aaaaAabc'

count_alphabet_old(input, 'a', 'b','c', 'd', 'A')
if_any_alphabet(input, 'a', 'b','c', 'd', 'A')
