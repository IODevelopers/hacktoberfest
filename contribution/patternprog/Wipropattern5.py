n=int(input())
count=1
temp=2
first=""
print("1")
for i in range(1,n+1):
    count=count+i
    for j in range(1,count):
        first=str(temp)
        strr="*"
        first=first+strr        
        temp=temp+1
        first=str(first)+str(temp)
        print(first,end="")
        temp=temp+1
    count=1
    print('')

