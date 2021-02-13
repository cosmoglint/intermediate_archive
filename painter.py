def rectangularSquare(n: int, cost: list(), q: int, queries: list()):
  # Write your code here
    anslist = []
    for val in queries:
        tot = 0
        x,y,l,b = val
        flist =  cost[max(x-l,0):min(x+l+1,n)]
        # ylist =
        # tot += sum(sum(jj) for jj in cost[max(n-l,0):min(n+l,n)])
        tot += sum([sum(flist[j][max(y-b,0):min(y+b+1,n)]) for j in range(len(flist))])

        anslist.append(tot)
    return anslist

def main():
    n = int(input())
    matrix = [list(map(int, input().strip().split())) for _ in range(n)]
    q = int(input())
    queries = [map(int, input().split()) for _ in range(q)]
    answers = rectangularSquare(n, matrix, q, queries)
    print("\n".join(map(str, answers)))


if __name__=="__main__":
    main()
