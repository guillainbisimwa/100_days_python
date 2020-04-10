#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ret = 0
    tab = ar[:]
    for i in range(n):
        count = 0
        for j in range(len(tab)):
            if ar[i] == tab[j]:
                count += 1
            if count == 2 :
                val = tab.pop(j)
                tab.remove(val)
                ret += 1
                break
    return ret

list = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(9,list))