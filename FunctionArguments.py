# function arguments

def greet(name, msg):
    """
    To greet a person
    """
    print('Hello ' + name + ', ' + msg)


greet('sumit', 'how are you?')

# Default arguments


def greet1(name, msg='How are you?'):
    """
    To greet a person
    using default keyword
    """
    print('Hello ' + name + ', ' + msg)


# Default argument should be on right side, after there should not be any non-default argument
# SyntaxError: non-default argument follows default argument
"""
def greet2(msg = 'How are you?', name):
   # To greet a person
    # using default keyword
    print('Hello '+ name + ', '+ msg)
    """

greet1('Sachin')
greet1('Sachin', 'Very good')

# greet2('Very Good','Shubham')

# python keyword arguments


def greet3(name, msg):
    """
    To greet a person
    keyword argumets
    """
    print('Hello ' + name + ', ' + msg)

def greet4(name, msg = 'How are you'):
    """
    To greet a person
    """
    print('Hello'+ name + ', ' + msg)

greet3(name = 'Sumit', msg = 'How are you?')
greet3(msg = 'Ver Good', name = 'Rohit')
# greet3(msg = 'Very Nice', 'Sagar')#SyntaxError: positional argument follows keyword argument

greet4('Sumit', 'Very good')
greet4(msg = 'Very good', name = 'Sumit')

#Arbitrary arguments
def gret5(*name):
    """
    To grret a person
    """
    for n in name:
        print('Hello', n,  'How are you?')#while printing + sign should be avoided, concatenation is anot allowed on tuple

gret5("Sumit", "Sachin", "Rahul")