# given an array of integers, print the absolute difference between first and last occurences of elements in the list

# eg: [1,2,5,7,5,5,2,2,1]   ans: 1-8, 2-6, 5-3, 7-0

import functools

n = int(input())
mydic = {}

def index_summer(x,y):
    global mydic

    cy = max(mydic[y]) - min(mydic[y])
    return x + cy

for i in range(n):
    mydic = {}
    length = int(input())
    lst = list(map(int,input().split()))

    for j,val in enumerate(lst):
        if val not in mydic.keys():
            mydic[val] = [j]
        else:
            mydic[val].append(j)

    ans = functools.reduce(index_summer,list(mydic.keys()),0)

    print(ans)
    print(mydic)


# sample test case
"""
1
9
1 2 5 7 5 5 2 2 1
"""

"""
1
5
1 2 3 3 2
"""
