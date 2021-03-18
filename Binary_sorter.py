


def test_ascending(mystr):
    for i in range(1,len(mystr)):
        if (mystr[i-1] <= mystr[i]):
            continue
        else:
            return False
    return True



t = int(input())

for i in range(t):
    n = input()
    swap = ""
    flag = True

    while flag == True:
        
