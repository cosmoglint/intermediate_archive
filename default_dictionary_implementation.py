# https://www.hackerrank.com/challenges/frequency-queries/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries):
    # print(queries)
    ans = []
    numbers = defaultdict(lambda: 0)
    frequency = defaultdict(lambda: 0)
    for index,value in enumerate(queries):
        # print(value,index)
        x = value[0]
        a = value[1]
        if x == 1:
            frequency[numbers[a]] -= 1
            numbers[a] += 1
            frequency[numbers[a]] += 1

        if x == 2:

            frequency[numbers[a]] -= 1
            numbers[a] -= 1
            frequency[numbers[a]] += 1

        if x == 3:
            if a in frequency.keys() and frequency[a] > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    file = open("./test_cases/dictionary_implementation","r")

    q = int(file.readline().strip())

    queries = []


    for _ in range(q):
        queries.append(list(map(int, file.readline().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    #
    # fptr.close()
