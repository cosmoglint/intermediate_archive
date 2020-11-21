set_balls = list(map(int,input().split()))


x= input("enter sorting criteria")


if x == "BrandName":
    ans = sorted(set_balls,key=lambda x: x[0])
    curval = ans[0][0]
    print(curval)
    for i in ans:
        if i[0] == curval:
            print(i)
        else:
            curval = i[0]
            print(curval)
elif x == "Size":
    ans = sorted(set_balls,key=lambda x: x[1])
    curval = ans[0][1]
    print(curval)
    for i in ans:
        if i[1] == curval:
            print(i)
        else:
            curval = i[1]
            print(curval)
elif x == "Weight":
    ans = sorted(set_balls,key=lambda x: x[2])
    curval = ans[0][2]
    print(curval)
    for i in ans:
        if i[2] == curval:
            print(i)
        else:
            curval = i[2]
            print(curval)
elif x == "Color":
    ans = sorted(set_balls,key=lambda x: x[3])
    curval = ans[0][3]
    print(curval)
    for i in ans:
        if i[3] == curval:
            print(i)
        else:
            curval = i[3]
            print(curval)
else:
    print("invalid criteria")
