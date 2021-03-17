
def meximize(lst):
    myset = sorted(list(set(lst)))
    dupe = myset[:]
    for i in myset:
        cnt = lst.count(i)
        if cnt > 1:
            dupe.extend([i]*(cnt-1))
        else:
            continue
    return dupe


t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    print(" ".join(list(map(str,meximize(lst)))))
