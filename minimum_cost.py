# given a binary array you can either change one to zero at a price or zero to one at a price.
# the final array must be a special array such that for any index i in the array, arr[i] xor arr[i+1] must be 1.

# in other words no two neighbours of the array must be the same


import functools

n = int(input())

for i in range(n):
    length , i1 , i0 = list(map(int,input().split()))
    binar  = list(map(int,input().split()))

    val = 1
    ls1 = ""
    ls2 = ""
    val1 = 0
    val2 = 0
    for x in range(n):
        if (x%2):
            val1 += (i1) if (binar[x] ^ 0) else 0
            val2 += (i2) if (binar[x] ^ 1) else 0
        else:
            val1 += (i1) if (binar[x] ^ 1) else 0
            val2 += (i2) if (binar[x] ^ 0) else 0


    print(val1,val2)





# sample test case
"""
2
2 1 1
1 1
2 1 1
0 1
"""
