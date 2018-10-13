"""
#3
Create a program that takes a list of integers as the input value.
The numbers positions will be randomized but if say you have 100 numbers you
will have 100 distinct numbers from 1-100.
However, the list has an anomaly, one of it is None
The function should return the actual None number

Using Python-3.6
"""

def myfunc(listku):
    # Put None into the last element of list
    listku = sorted(listku, key=lambda x: (x is None, x))
    # Pop the None value
    listku.pop()
    # Cast into int, then sort again
    listku = sorted(list(map(int, listku)))
    # Print the result
    print(sum(range(listku[0], listku[-1] + 1)) - sum(listku))

def main():
    # Getting input as str, then split
    l = input().split()
    # Pass to myfunc
    myfunc(l)

main()