#3: monkeys are dancing in a circle and keep moving every second. Their movement is not random and their displacements are given from the position. find the minimumm no. of seconds it takes for the monkeys to return to their original positions
a  = int(input())
b = list(map(int, input().split()))


c = [i-1 for i in b]
print(c)
def repce(i,lst,cnt):
    zz = lst.index(i)
    if zz == i:
        lst[i] = None
        return 1,lst
    elif lst[i]!= None:
        cnt += 1
        vl = lst[i]
        lst[zz] = None
        print(lst)
        return repce(vl,lst,cnt)
    else:
        cnt += 1
        lst[zz] = None
        return cnt,lst
# while lst != [1]*len(b):

ans = 1
for i in range(len(b)):
    if i in c:
        cal = repce(i,c,0)
        ans *= cal[0]
        c = cal[1]
        print(c)
    else:
        continue
print(ans)
