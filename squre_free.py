
import math

def is_square(n):
    sn = math.sqrt(n)
    return (sn * sn == n)


def square_free(lst):
    if len(lst) == 1:
        return True
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            else:
                if is_square(lst[i] * lst[j]):
                    return False
                else:
                    continue


    return True




t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    if len(lst) == 1:
        print(1)
        continue

    cur = 0
    ans = 1
    for i in range(1,len(lst)):
        if square_free(lst[cur:i+1]):
            continue
        else:
            ans += 1
            cur = i
    print(ans)
