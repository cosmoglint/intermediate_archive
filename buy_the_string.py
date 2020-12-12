# you are in a shop and you look at a binary string. each 0 costs c0 and each 1 costs c1. you are allowed to change the value of a string with a paricular amount of money
# your job is to find the minimum amount of money required to buy the string


n = int(input())

for i in range(n):
    x, c0, c1, h = list(map(int,input()))
    thes = input()
