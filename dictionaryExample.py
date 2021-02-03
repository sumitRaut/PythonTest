my_dict = {1: 'apple', 2:'mango' }
print(my_dict)

my_dict = {'mango':'apple', 1: 'Banana'}
print(my_dict)

my_dict = dict({1: 'apple', 2:'mango' })
print(my_dict)

my_dict = dict([(1, 'apple'), (2,'mango')])
print(my_dict)

#Accessoing elements
print('-----------Accessoing elements-------------')
print(my_dict[1])
#print(my_dict[3])
print(my_dict.get(1))
print(my_dict.get(3))

#Changing and Adding Dictionary elements
print('--------------Changing and Adding Dictionary elements------------------')
print(my_dict)
my_dict[1] = 'Banana'
print(my_dict)

my_dict[3] = 'Guava'
print(my_dict)

#Removing elements from Dictionary
#pop(), popitem(), clear(), del
print('-----------Removing elements from Dictionary-----------------')
square = {1:1, 2:4, 3:9, 4:16, 5:25}
print(square)
square.pop(1)
print('pop: ',square )
square.popitem()
print('popitem: ', square)
square.clear()
print('clear: ', square)
del square
#print('del: ', square)

# Dictionary Methods
marks = {}.fromkeys(['English', 'Marati', 'Hindi'], 0)
print(marks)

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))

#Python Dictionary Comprehension
my_dict = {x:x*x for x in range (6)}
print('Square: ',my_dict)

my_dict = {x:x*x for x in range (13) if x%2==1}
print('Square of odd numbers: ',my_dict)

#Membership test
my_dict = {1: 'apple', 2:'mango' }
print(1 in my_dict)
print(3 in my_dict)
print('apple' in my_dict)

#dictionary methods
print('--------------dictionary methods-----------')
print(all(my_dict))
print(any(my_dict))
print(len(my_dict))
print(sorted(my_dict))