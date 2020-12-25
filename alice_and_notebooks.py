# alice can produce a particular number of notebooks per day. given a range of days that each customer will wait, find out how many notebooks she needs to make per day to satisfy each customer
# eg
# 2 2 1 - customer a
# 2 3 3 - customer b
# 2 3 1 - customer c
# a needs one notebook by day 2, b needs three notebooks at either day 2 or day 3, c needs one notebook at either day 2 or day 3. so she needs to make two notebooks per day, starting from day 1
# day one she has two notes, day two she has four notes. so she sends off customer a. now in day three she makes two notes for a total of 5 notes and she gives b three and c 1


n = int(input())

for i in range(n):
    mydic = {}
    customers = int(input())
    prevnotes = 0
    prevdate = 0
    max = 1
    i = 1
    for i in range(customers):
        start,end,val = list(map(int,input().split()))

        while 1:
            if (((end-prevdate)*i)+prevnotes > val):
                prevnotes = ((end-prevdate)*i)+prevnotes
                break
            else:
                i += 1
        prevdate = end
    print(i)

# sample test case

"""
1
3
2 2 1
2 3 3
2 3 1
"""
