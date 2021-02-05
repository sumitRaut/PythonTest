#Recursive function
 
def factorial(n):
    """
    To find factorial of a function
    """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

num = 3
print("The factorial of", num, "is", factorial(num))

def recurse():
    recurse()

recurse()   #RecursionError: maximum recursion depth exceeded , max limit is 1000s