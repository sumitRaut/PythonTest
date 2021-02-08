x = 10

def foo():
    global x
    x = x + 5
    print('X inside: ', x)

foo()
print('x outside: ', x)

def foofa():
    x = 20

    def bar():
        global x
        x = 25

    print('Value of x before calling bar: ', x)
    print('Cslling bar now')
    bar()
    print('Value of x after calling bar: ', x)

foofa()  
print('Value of x in main: ', x)