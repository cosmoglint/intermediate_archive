t = int(input())


for i in range(t):
    n = int(input())
    arr = [[x for x in input()] for i in range(n)]

    v1 = 0
    v2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "*" and v1 == 0:
                v1 = (i,j)
                continue
            elif arr[i][j] == "*" and v1 != 0:
                v2 = (i,j)
                break

    arrlen = len(arr)
    subarrlen = len(arr[0])


    if (v1[0] != v2[0]) and (v1[1] != v2[1]):
        ans = [(v1[0], v2[1]), (v2[0],v1[1])]

    elif (v1[0] == v2[0]) and (v1[1] != v2[1]):
        if v1[0] + 1 < arrlen:
            ans = [(v1[0]+1,v1[1]), (v2[0]+1,v2[1])]
        else:
            ans = [(v1[0]-1,v1[1]), (v2[0]-1,v2[1])]

    elif (v1[0] != v2[0]) and (v1[1] == v2[1]):
        if v1[1] + 1 < subarrlen:
            ans = [(v1[0],v1[1]+1), (v2[0],v2[1]+1)]
        else:
            ans = [(v1[0],v1[1]-1), (v2[0],v2[1]-1)]

    newp1 = ans[0]
    newp2 = ans[1]

    arr[newp1[0]][newp1[1]] = "*"
    arr[newp2[0]][newp2[1]] = "*"

    newarr = ["".join(x) for x in arr]
    for i in newarr:
        print(i)
