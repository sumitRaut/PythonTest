x = 10

def foo():
    global x
    x = 5
    print('X inside: ', x)

foo()
print('x outside: ', x)