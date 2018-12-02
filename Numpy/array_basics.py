import numpy as np

'''
    np.array()
    np.reshape()
    array.size
    array.dshape
    array.dtype
    set_printoptions(precision, suppress)

    array scalor
    intialization

'''
a_list = [2, 3, 4, 4]
print('List = ', a_list)
a = np.array(a_list, dtype = np.float64)
print('Array = ', a)

#reshaping the array
#a.reshape() does not change the original value

print('\nreshaped ')
a = a.reshape(2,2)
print(a)

print('\n\nNumber of elements = ', a.size)
print('Shape of array = ', a.shape)
print('Data type of array = ', a.dtype)
print('\n\n')

#returns True/False if elements in a <4
print('Less than four?')
print(a<4)

print('\nTimes four')
a *= 4
print(a)

print('\nInitialize array with ones')
a = np.ones((2, 3))
print(a)

print('\nInitialize array with zeros')
a = np.zeros((4, 5))
print(a)

a = np.random.rand(2, 2)
print(a, '\nChange Precision')
b = np.array([0.00000000000001])
np.set_printoptions(precision = 20, suppress = True)
#if a number is really large or small, by default
#python will use the scientific notation
#suppress = 1 means no scientific notation
print(b)





