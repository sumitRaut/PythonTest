#lamda function

double = lambda x:x*2
print(double(5))

my_list = [1, 2, 3, 4, 5, 6, 7]
new_list = list(filter(lambda x: x%2==0, my_list))
print(new_list)

new_list = list(map(lambda x: x*2, my_list))
print(new_list)