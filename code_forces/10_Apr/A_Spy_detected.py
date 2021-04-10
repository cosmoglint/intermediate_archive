t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    x = lst[0]
    y = lst[1]
    z = lst[2]
    if (x == y) and (y == z):
        ans = None
    elif (x == y) and (y != z):
        ans = 2
    elif (x != y) and (y == z):
        ans = 0
    elif (x == z) and (y != z):
        ans = 1

    if ans == None:
        for i in range(2,len(lst)):
            if lst[i] == x:
                continue
            else:
                ans = i
                break
    print(ans+1)
