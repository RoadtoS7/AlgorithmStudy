#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonSubstring' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def commonSubstring(a, b):
    for i in range(len(a)):
        aLetter = list(set(a[i]))
        bLetter = list(set(b[i]))

        longOne = str()
        shortOne = str()

        if len(aLetter) < len(bLetter):
            longOne, shortOne = aLetter, bLetter
        else:
            longOne, shortOne = bLetter, aLetter

        idx = 0
        while idx < len(shortOne):
            if shortOne[idx] in longOne:
                print('YES')
                break
            else:
                idx += 1
        if idx >= len(shortOne):
            print('NO')


if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    commonSubstring(a, b)
