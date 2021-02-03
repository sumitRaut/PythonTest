#create Strings
#Single quote
my_string = 'Hello'
print(my_string)

#double quotes
my_string = "Hello World"
print(my_string)

#triple quotes
my_string = '''Hello Sumit Raut'''
print(my_string)

#Triple quotes for multiline sentence
my_string = """Hello Sumit,
                Welcome to Python World"""
print(my_string)                

my_string = '''Welcome Python,
                    to Sumit's World'''
print(my_string)            

#Access Elements
print('-------------Access Elements------------------------')
my_string = 'Python World'
print('str[0] : ', my_string[0])
print('str[-1] : ', my_string[-1])
print('str[1:5] : ', my_string[1:5])
print('str[1:-1] : ', my_string[1:-1]) #in slicing 1st parameter is inclusive and 2nd parameter is exclusive
#print('Index out of range : ', my_string[20])#IndexError: string index out of range

#Chnage or delete or String
#Strings are immutable, so we can't change it's items, but we can reassign the string 
print('---------------Change or delete the string----------------')
my_string = 'Hello World'
#my_string[1] = 'S' #'my_string' does not support item assignmentpylint(unsupported-assignment-operation)
my_string = 'Hello Python'
print(my_string)

#del my_string[0] #'my_string' does not support item assignmentpylint(unsupported-assignment-operation)
del my_string
#print(my_string)

#Concatenation
str1 = 'Hello'
str2 = 'World'
print('str1 + str2 : ', str1 + str2)
print('str1 * 3 : ', str1 * 3)
s= ('Hello '
        'World')
print(s)

#iterating through a string
print('------------Iterating through a string--------------')
count = 0
for letter in 'Apple Apple':
    if(letter == 'p'):
        count +=1
print(count,' letters found') 


#membership Test
print('-----------------Membership test---------------------')
my_string = 'Hello World'
print('b' in my_string)
print('o' in my_string)

#Built in funtctions
print('-----------built in functions--------------')
my_string = 'Hello World'
list_enumerste = list(enumerate(my_string))
print('list_enumerste : ',list_enumerste)
print('list_enumerste : ',list(enumerate(my_string)))

#Python String Formatting
print('----------Python String Formatting---------------------')
my_string = 'He asked, "Waht\'s There?"'
print(my_string)
my_string = """He asked, What's there? """
print(my_string)
my_string = "He asked, \"What's there?\""
print(my_string)

my_string = 'C:\\Python\\Lib'
print(my_string)
my_string = 'Hello World,\n Welcome to Python'
print(my_string)

# Python string format() method
print('--------------Default order---------------------------')
default_order = '{}, {} and {}'.format('Sumit', 'Sachin', 'Shubham')
print('default_order: ', default_order)

print('--------------Positional order---------------------------')
positional_order = '{1}, {2} and {0}'.format('Sumit', 'Sachin', 'Shubham')
print('positional_order: ', positional_order)

print('---------------order using keyword argument--------------')
keyword_order = '{c}, {a} and {b}'.format(a = 'Sumit', b = 'Sachin', c = 'Shubham')
print('keyword_order: ', keyword_order)

#binary representation
print('-------------------Binary representation------------------')
binary_string ='Binary representation of {0} is {0:b}'.format(12)
print(binary_string)

print('------------------Exponential representation--------------')
exponent_string = '{0:e}'.format(1566.345)
print(exponent_string)

print('----------------Round off--------------------')
my_string = 'one third:{0:4.3f}'.format(1/3)
print(my_string)

print('--------------String alignment------------------')
my_string = '|{:<10} | {:^10} | {:>10}'.format('Sumit', 'Shubham', 'Sachin')
print(my_string)
my_string = '|{:<8} | {:^8} | {:>8}'.format('Sumit', 'Shubham', 'Sachin')
print(my_string)

my_string = 'Hello World, Welcome to python'
print('Upper: ',my_string.upper())
print('Lower: ', my_string.lower())
print('Split: ', my_string.split())
my_string = ''.join(['I','am', 'Sumit', 'Raut'])
print('Join: ', my_string)
my_string = 'Happy new year'
my_string.replace('Happy','Brilliant')
print('Replace: ', my_string)
print('Happy new year'.replace('Happy', 'Brilliant'))