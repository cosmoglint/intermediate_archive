t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = -1
    lst.sort()
    if sum(lst[:n]) == lst[n]:
        ans = " ".join([str(i) for i in lst[:n]])
    elif sum(lst[:n]) == lst[n+1]:
        ans = " ".join([str(i) for i in  lst[:n]])
    else:
        for i in range(n):
            if lst[n] + sum(lst[:i]) + sum(lst[i+1:n]) == lst[n+1]:
                ans = " ".join([str(i) for i in  lst[:i] + [lst[n]] + lst[i+1:n]])
    print(ans)
