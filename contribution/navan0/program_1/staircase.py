#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    o=0
    p=' '
    z=n
    for i in range(n):
        o=o+1
        z=z-1
        print(p*z+'#'*o)
        
            
            
        

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)

