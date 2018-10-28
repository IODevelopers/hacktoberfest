#usr/bin/env python3

def quicksort(array,start=0,end=None):
    if end is None:
        end=len(array)-1
    if end-start&lt;1:
        return array
    else:
        current=start
        pivot =end
        while 1:
            if current==pivot:
                break
            elif array[current]&gt;array[pivot]:
                array[pivot],array[current],array[pivot-1]=array[current],array[pivot-1],array[pivot]
                pivot-=1
            else:
                current+=1
    quicksort(array,start,pivot-1)
    quicksort(array,pivot+1,end)
    return array

