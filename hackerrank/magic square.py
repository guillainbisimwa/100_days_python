#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
# https://www.hackerrank.com/challenges/magic-square-forming/problem
def formingMagicSquare(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
