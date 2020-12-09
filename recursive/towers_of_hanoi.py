# given number of disks find the minimum number of moves to solve the towers of hanoi problem

# in the function n is number of disks, start is the starting rod number and end is the ending rod number

def hanoi(n,start,end):
    other = 6-(start+end)
    if (n == 1):
        return 1
    # elif (n == 2):
    #     return 2
    # elif (n==3):
    #     return 7
    else:
        return 1 + hanoi(n-1,start,other) + hanoi(n-1,other,end)

print(hanoi(4,1,3))
