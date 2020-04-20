
import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/minimum-distances
# Complete the minimumDistances function below.
def minimumDistances(a):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()