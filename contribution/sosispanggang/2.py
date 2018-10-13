'''
#2
Create a function that will take a list of integers as the input value.
The function should process the list so that:
a. All numbers divisible by 3 should print Foo
b. All numbers divisible by 5 should print Bar
c. All numbers divisible by 3 and 5 should print FooBar
d. Other numbers that does not meet a-c should print itself

Using python-3.6
'''

def myfunc(somelist):
    # Loop
    for value in somelist:
        if((value%3==0) & (value%5==0)): print("FooBar")
        elif(value%3==0): print("Foo")
        elif(value%5==0): print("Bar")
        else: print(value)

def main():
    # Getting input
    n = input()
    # Pass to myfunc as list of int
    myfunc(list(map(int, n.split())))

main()