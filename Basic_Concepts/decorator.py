import time
import math


def calculate_time(func): 
      
    def inner1(*args, **kwargs): 
  
        # storing time before function execution 
        begin = time.time() 
          
        func(*args, **kwargs) 
        # storing time after function execution 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
  
    return inner1 
  

 # with function decorator
 # decorator wraps factorial with calculate_time function
 # It basically turns old function into a new function with addtional functionalities of wrapper function
@calculate_time
def factorial(num): 
    time.sleep(2) #stop for two second
    print(math.factorial(num)) 
    print('Decorator')
  
# without function decorator
def factorial2(num): 
    time.sleep(2) 
    print(math.factorial(num)) 
    print('\nNo Decorator')



# use function decorator
factorial(10) 

# traditional equivalent method
factorial2 = calculate_time(factorial2)
factorial2(20)



