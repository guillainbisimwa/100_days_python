#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    nbr_up, cmt, nbr_down, i = 0, 0, 0, 0
    v = ""
    while i < n:
        if s[i] == "U":
            nbr_up += 1
        else:
            nbr_down += 1
        if(nbr_down - nbr_up == 0 and v == "D") :
            cmt += 1
            nbr_down , nbr_up = 0, 0
            print()
        i += 1
        if nbr_down > nbr_up:
            v = "D"
        else:
            v = "U"
    return cmt

path2 = ["U","D","D","D","U","D","U","U"]
path = ["D","D","U","D","U","U","D","U","U","U","D","D"]
print(countingValleys(12,path))