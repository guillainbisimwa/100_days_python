#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
