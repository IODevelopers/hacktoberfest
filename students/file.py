import os
filename="test.txt"
file=open(filename,'a')
file.write("\nhello world !!!")
file.close()
file=open(filename,'r')
print(file.read())
file.close()
