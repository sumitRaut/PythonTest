#set of integer data type
my_set = {1, 2, 3}
print(my_set)

#set of different data type
my_set = {1, 2.4, 'Hello', (5, 6, 7), 4, 'World', (1, 2, 3)}
print(my_set)

#set cannot have duplicate items
my_set = {1, 2, 3, 4, 2}
print('Duplicate items: ', my_set)

#a set cn be made from a list
my_set = set([1, 2, 3, 4, 2, 4])
print('A set from a list: ',my_set)

#Empty set
print('-------------------Creating Empty set--------------------')
my_set = {}
print(type(my_set))

my_set = set()
print(type(my_set))

#add elements in list
print('---------------Add elements in set-------------------------')
my_set = {1, 2}
print('Original set: ', my_set)

my_set.add(3)
print(my_set)

my_set.update([4, 5])
print(my_set)

#Add function can add only one item, and list can be added
#my_set.add([6])
#print(my_set)

#set, tuple, list can be treated as argument 
my_set.update([7,8,1], {1, 2, 10})
print(my_set)

#removing an element from set
#discard, remove, pop, clear
print('-------------Removing an element from set----------------')
my_set = {1, 2, 3, 4}
print(my_set)

my_set.discard(2)
print('After removing 2: ',my_set)

my_set.remove(1)
print('Afer removing 1: ', my_set)

#discrad when element is not present
my_set.discard(6)
print('discrad when element is not present: ',my_set)

#remove when element is not present, it will raise exception
#my_set.remove(6)
#print(my_set)
print('---------Pop and clear examples--------')
my_set = set('HElloworld')
print(my_set)

my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print('Clear the set: ',my_set)

#set operations
print('-------Set operations--------------')
a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}
print('a: ', a)
print('b: ', b)
print('a|b: ', a|b)
print('a.union(b): ', a.union(b))
print('b.union(a): ', b.union(a))

print('-------Set Intersection------------')
print('a & b: ', a&b)
print('a.intersection(b): ',a.intersection(b))
print('b.intersection(a): ',b.intersection(a))

print('-----------Set difference-----------------')
print('a - b: ', a - b)
print('b - a: ', b - a)
print('a.difference(b): ',a.difference(b))
print('b.difference(a): ', b.difference(a))

print('-----------Set symmetric difference ------------------')
print('a^b: ', a^b)
print('a.symmetric_difference(b): ',a.symmetric_difference(b))
print('b.symmetric_difference(a): ',b.symmetric_difference(a))

print('----------------Membership test----------------')
my_set = {1, 2, 3, 4}
print(1 in my_set)
print(5 in my_set)
print(5 not in my_set)

print('------------------Iterating through a set-------')
my_set = set('HelloWorld')
for letter in my_set:
    print('\n',letter)

print('-------------Frozen set----------------')    
#frozen set is immutable
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
print(a.difference(b))
#a.add(2)#AttributeError: 'frozenset' object has no attribute 'add'