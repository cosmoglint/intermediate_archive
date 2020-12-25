# given an array of integers, print the absolute difference between first and last occurences of elements in the list

# eg: [1,2,5,7,5,5,2,2,1]   ans: 1-8, 2-6, 5-3, 7-0

n = int(input())

for i in range(n):
    mydic = {}
    length = int(input())
    lst = list(map(int,input().split()))

    for val,i in enumerate(lst):
        if i not in mydic.keys():
            mydic[i] = []
