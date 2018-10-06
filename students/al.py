import os
os.listdir()
filename="test.txt.txt"
file=open(filename,'r')
print(file.read())
file.close()
file=open(filename,'a')
file.write("aleena k alex\n")
file.close()
file=open(filename,'r')
print(file.readline())
file.close()

