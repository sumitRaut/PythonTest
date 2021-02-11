import os
import shutil

#get current working directory
cwd = os.getcwd()
print('Current working directory: ', cwd)
print(os.getcwdb())

#Chnage working directory
os.chdir('C:/Users/pi/Desktop/Sumit')
print(os.getcwdb())

#get list of directories
print('list of directories in cwd: ',os.listdir())
print('list of directories in C: ', os.listdir('C:/'))

#create new directory
print('-----------------create a new directory------------------')
print(os.getcwd())
print('list of directories: ',os.listdir())
os.mkdir('Test')
print('list of directories: ',os.listdir())
os.mkdir('Exam')
print('list of directories: ',os.listdir())

#change name of directory
print('-----------------Change name of a directory------------------')
os.rename('Test', 'Marks')
print(os.listdir())

#remove a directory
print('----------------Remove a directory--------------------')
os.rmdir('Marks')
shutil.rmtree('Exam')
print('list of directories: ',os.listdir())

