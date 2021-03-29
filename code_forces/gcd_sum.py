
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def splitter(val):
    x, y = val, sum([int(i) for i in str(val)])
    return( x, y)

def solve(val):
    iter = val
    while iter >= val:
        x, y = splitter(iter)
        if gcd(x, y) > 1:
            return x
        else:
            iter += 1



a = int(input())
for i in range(a):
    x = int(input())
    print(solve(x))
