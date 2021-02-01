# tuple with integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with different datatypes
my_tuple = (1,'Hello',3)
print(my_tuple)

#nested tuple, conataining list and tuple also
my_tuple = (1,['Hello','World'],(10,25,'Python'))
print(my_tuple)

#packin of tuple
my_tuple = 1, 2.4,'Dog'
print(my_tuple)

#unpacking of a tuple
a, b, c = my_tuple
print(a)
print(b)
print(c)

#Having one element in a tuple is a string, and a tuple with a trailing comma is a tuple
my_tuple = 'Hello'
print(type(my_tuple))

my_tuple = 'Hello',
print(type(my_tuple))

my_tuple = ('Hello')
print(type(my_tuple))

my_tuple = ('Hello',)
print(type(my_tuple))

#indexing
my_tuple = ('p','r','o','g','r','a','m')
print(my_tuple[0])
print(my_tuple[5])

print('-----N tuple-------------------------')
n_tuple = (1,2.4,[8,4,6])
print(n_tuple[2][1])
print(n_tuple[2][2])

#negative indexing
print(my_tuple[-1])
print(my_tuple[-5])

#Slicing
print(my_tuple[0:4])
print(my_tuple[:-5])
print(my_tuple[1:])
print(my_tuple[:6])
print(my_tuple[:])  #print all elements

#changing a tuple
#tuples are immutable, but if tuple contains a list which is a mutable, we can chage it's elements
print('-----------Changing a tuple-------------------')
my_tuple = (1, 2, [2, 5,7])
print(my_tuple)

my_tuple[2][0] = 9
print(my_tuple)

#We can not change elements of tuple but can reassign elements
print('-----------Reassign a tuple-------------------')
my_tuple = (10, 11, 12, 13)
print(my_tuple)

print('-----------Concatenation of a tuple-------------------')
print(my_tuple + n_tuple)

print('-----------Repeation of a tuple-------------------')
print(('Repeat',)*3)

print('----------Deleting of a tuple-------------------')
del my_tuple
#print(my_tuple)

print('----------tuple Methods-------------------')
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(type(my_tuple))
print(my_tuple.index('p')) #This will return index of 1st p
print(my_tuple.count('p'))

print('a' in my_tuple)
print('b' in my_tuple)
print('b' not in my_tuple)

#iterating through a tuple
for word in my_tuple:
    print('Letter:', word)