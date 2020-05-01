#!/usr/bin/python3

def calculator(operation,var_1,var_2 ):
  
    if(operation == 'Add'):
        result = var_1 + var_2
    elif(operation == 'Subtract'):
        result = var_1 - var_2
    elif(operation == 'Multiply'):
        result = var_1 * var_2
    elif(operation == 'Divide'):
        result = var_1 / var_2
    else:
        result = 0
    return(float(result))

#print(calculator("Add", 3, 7))

def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if num == 1:
        return(int(num))
    else:
        return(int(num * factorial(num - 1)))
#print (factorial(5))