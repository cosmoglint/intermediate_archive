a = int(input())
lst = list(map(int,input().split()))

i = 0
while (i<len(lst)):
    val = lst[i]
    if (i+1 == val):
        i += 1
        continue
    else:
        ans += 1 if abs((i+1 - val) == 1) else 0
        # ind = lst.index()
        lst[i] = lst[val-1]
        lst[val-1] = val
print(lst)
        
