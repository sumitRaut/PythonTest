
mylist = ['a', 0, 2]
r = 0
for mbr in mylist:
    try:
        print('The Entry is: ', mbr)
        r = 1/int(mbr)
    except Exception as e:
        print('Oops!', e.__class__, 'occurred')
        print('Next entry')
    print('Reciprocal of', mbr, ': ', r)

#raising an exception in python
try:
    a = int(input('Enter a positive integer number:'))
    if a <= 0:
        raise ValueError('That is not a positive number')
except ValueError as e:
        print(e)

#try with else clause
print('-------------------try with else clause-------------------')
try:
    num = int(input('Enter a number: '))
    assert num%2==0
except:
    print('Not an even number')
else:
    r = 1/num
    print('Reciprocal:', r)

#try ---finaly
print('-----------------Try finally----------------')
try:
    f = open("C:/Users/pi/Desktop/Sumit/PythonTest/test.txt", 'w', encoding='utf-8')
finally:
    f.close()    