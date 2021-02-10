try:
    f = open("C:/Users/pi/Desktop/Sumit/PythonTest/test.txt", 'w', encoding='utf-8')
    f.write('Hi, I am Sumit')
    f.write('I am here to leran python.')
    f.write('\nHello world')
    f.close()

    with open("C:/Users/pi/Desktop/Sumit/PythonTest/test.txt", 'r', encoding='utf-8') as file:
        print(file.read())
        print('Current position:', file.tell())
        for line in file:
            print(line, end = '')
        file.seek(5)    
        print('Current position:', file.tell ())
        for line in file:
            print(line, end = '')   
        file.seek(0)
        print('\n\nPrint by using readline')
        file.seek(0)

        #print with \n, if \n is not there then it will print whole file
        print(file.readline())
        print(file.readline())
        print(file.readline())

        #It will print all the lines, divide them by \n
        file.seek(0)
        print(file.readlines())
    
finally:
    f.close()