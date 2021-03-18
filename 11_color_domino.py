# given a number of blocks of white and black, find if w white dominoes and b black dominoes can be placed


def test_domino(first,second):
    val = 0
    rem = 0
    if (first < second):
        val = first
        rem = second - first
    elif (first == second):
        return first
    else:
        val = second
        rem = first - second

    return (val + rem // 2)



t = int(input())

for i in range(t):
    n, k1, k2 = list(map(int,input().split()))
    w, b = list(map(int,input().split()))

    maxw = test_domino(k1,k2)
    maxb = test_domino(n-k1,n-k2)

    if (maxw >= w) and (maxb >= b):
        print("YES")
    else:
        print("NO")
