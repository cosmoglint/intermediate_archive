# you are in a shop and you look at a binary string. each 0 costs c0 and each 1 costs c1. you are allowed to change the value of a string with a paricular amount of money
# your job is to find the minimum amount of money required to buy the string


n = int(input())

for i in range(n):
    x, c0, c1, h = list(map(int,input().split()))
    thes = input()
    binn = int(thes,2)
    oners = 2**x
    oc = oners & binn
    zc = ~oc
    print(min())
    print(binn)


'''
6
3 1 1 1
100
5 10 100 1
01010
5 10 1 1
11111
5 1 10 1
11111
12 2 1 10
101110110101
2 100 1 10
00
'''
