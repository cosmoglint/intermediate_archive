t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input()))
    lst.sort()
    if sum(lst[:n]) == lst[n-2]:
        ans = " ".join(lst[:n])
    elif sum(lst[:n]) == lst[n-1]:
        ans = " ".join(lst[:n])
    else:
        ans = -1
    print(ans)
