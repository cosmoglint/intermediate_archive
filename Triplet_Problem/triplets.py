#!/bin/python3

from itertools import combinations
import math
import os
import random
import re
import sys


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def recu(n,val):
    if n == val:
        return n
    else:
        return n * recu(n-1,val)

# Complete the countTriplets function below.
def countTriplets(arr, r):
    my_dic = {}
    for i in arr:
        if i in my_dic:
            my_dic[i] += 1
        else:
            my_dic[i] = 1

    count = 0
    if r == 1:
        for i in set(arr):
            val = i
            count += (recu(my_dic[val],my_dic[val]-2) / factorial(3))

    else:
        for i in arr:
            val = i
            val2 = i*r
            val3 = i * r * r
            if val2 in my_dic and val3 in my_dic:
                count += my_dic[val2] * my_dic[val3]
                if my_dic[val] == 1:
                    my_dic.pop(val)
                else:
                    my_dic[val] -= 1
            else:
                my_dic[val] -= 1

    return int(count)


if __name__ == '__main__':

    file = open("data3.txt", "r")

    nr = file.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, file.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)


def countTriplets(arr, r):
        count = 0
        dict = {}
        dictPairs = {}

        for i in reversed(arr):
                if i*r in dictPairs:
                        count += dictPairs[i*r]
                if i*r in dict:
                        dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

                dict[i] = dict.get(i, 0) + 1

        return count




# 5 2
# 4 2 1 4 2 4 4 4 4
