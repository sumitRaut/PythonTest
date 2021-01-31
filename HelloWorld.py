print('Hello World')

# empty list
list1= []
print(list1)

# list can contain items of different types, duplicate also
list2 = ['Hello',123,3.4,3.4]
print(list2)

#Indexing
print(list2[0])

print(list2[3])

#Negative Inexing
print('Backward access:')
print(list2[-1])
print(list2[-2])
print(list2[-3])
print(list2[-4])

print(list2[-1],list2[-2],list2[-3],list2[-4])
print('Last number:',list2[-1])
print('Second Last number:',list2[-1])

#slicing
# 1st index is inclusive and 2nd index is exclusive
print('Slicing:')
print('0:3 ::',list2[0:3])
print('1:4 ::',list2[1:4])
print('1:4 ::',list2[1:4])
print(':3', list2[:3] )
print('1:', list2[1:])

#chnage items of a list
#lists are mutable
# 1. 

languages = ['Java', 'Python','Ruby','Php']
print(languages)

languages[2] = 'Rust'
print(languages)

languages = ['Java', 'Python','Ruby','Php']
print(languages)
languages[1:3] = ['Rail','Rust']
print(languages)

#iterating through a list
print(languages)

print('Python' in languages)

print('Ruby' in languages)

if('Rail' in languages):
    for language in languages:
        print(language) 


#list methods
# 1. append - that will add element in list
print('----List Methods-------------------------------------------------------')
print(languages)  
languages.append('Ruby')      
print(languages)

#2. Insert - add one item in place of another element
print('-------Insert-----------------')
languages = ['Java', 'Python','Ruby','Php']
print(languages)
languages.insert(1,'Rail')
print(languages)
print('------Remove------------')
print(languages)
languages.remove('Rail')
print(languages)

print('-----Copy-----------------------')
languages1 = languages.copy()
print('Languages 1:',languages1)

#
print('-----------------------------------------------')

for x in range(10):
    print(x)

pow2 = [2 ** x for x in range(10)]    

print(pow2)

print('---------------------------------------------')
print(languages.index('Ruby'))
print(languages.count('Ruby'))
languages.sort()
print(languages)
languages.reverse()
print(languages)
