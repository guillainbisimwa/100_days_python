#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v2 > v1:
        return "NO"
    elif x2 < x1 and v1 > v2:
        return "NO"
    else:
        while True:
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2:
                #print("End at :"+str(x1))
                return "YES"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #x1V1X2V2 = input().split()
    x1V1X2V2 = [0,3,4,2]
    #x1V1X2V2 = [2,4,0,3]

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
