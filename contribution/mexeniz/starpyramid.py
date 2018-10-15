#!/usr/bin/env python
import math

n = input("Row: ")
n = int(n)

width = 2 * (n-1) + 1
half = math.floor(width / 2)

for j in range(0, n):
    char_list = ["*"] * width
    k = half - j
    for i in range(0, half):
        if not i >= k :
            char_list[i] = " "
            char_list[width - i - 1] = " "
    string = "".join(char_list)
    print (string)
