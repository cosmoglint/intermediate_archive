n= int(input())
sign=input()
arr=[i for i in range(n+1)]
lst=[]
def possibility(x,y,sign):
    return eval(f'{x}{sign}{y}')

for i in arr:
    if possibility(i,i+1,sign[i])==True:
        lst.append(i)

        
