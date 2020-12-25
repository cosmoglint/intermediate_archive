# given a binary array you can either change one to zero at a price or zero to one at a price.
# the final array must be a special array such that for any index i in the array, arr[i] xor arr[i+1] must be 1.

# in other words no two neighbours of the array must be the same


import functools

n = int(input())

for i in range(n):
    length , i1 , i2 = list(map(int,input().split()))
    binar  = list(map(int,input().split()))
    print(binar)
    val1 = 0
    val2 = 0
    for x in range(length):
        if (x%2 == 0):
            val1 +=  0 if (binar[x] == 1) else (i1)
            val2 +=  0 if (binar[x] == 0) else (i2)
        else:
            val1 += 0 if (binar[x] == 0) else (i2)
            val2 +=  0 if (binar[x] == 1) else (i1)


    print(min(val1,val2))





# sample test case
"""
2
2 1 1
1 1
2 1 1
0 1
"""
