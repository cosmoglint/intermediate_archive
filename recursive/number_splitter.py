# given m and n output the number of ways m items can be grouped with a max group size of n

def partition(m,n):
    if (m==0):
        return 1
    elif (n==0 or m<0):
        return 0
    else:
        return partition(m-n,n) + partition(m,n-1)


m,n = list(map(int,input().split()))
print(partition(m,n))

# the first base case is if m(number of items) is 0. here max size of group does not matter because there is only one possible arrangement. (selecting nothing)
# the second base case is , n(if max group size) is 0, here it doesnt matter what the number of items is there is no way it can be arranged , so answer is 0

# the pattern that follows is that every partition, is a sum of (m-n) items with n max group size and (m) items with (n-1) max group size.
