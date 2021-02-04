def greet(name):
    """
    This function greets to a person
    """
    print('Hello '+ name+', how are you?')

def absolute_num(num):
    """
    return absolute value of input number
    """
    if num >= 0:
        return num
    else:
        return -num

def scope_num():
    """
    To check scope of a function
    """
    x = 10
    print('Value of x inside function: ', x)

x=20
scope_num()
print('Value of x outside of a function: ', x)

greet('Sumit')
print('Docstrings: ',greet.__doc__)

print('Absolute of 2: ',absolute_num(2))
print('Absolute of -4: ', absolute_num(-4))
