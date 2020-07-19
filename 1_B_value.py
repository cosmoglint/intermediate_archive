#1: given a list of 3 digit numbers find the B-value of each one
#B-value is calculate by largest digit times 11 plus smallest digit times 7, and tens,unit value of the answer
#for each B-value a pair is calculated based on following conditions
#B-values in the even position can only pair with even positions and odd values can pair only with odd positions
#a pair is created when the tens digit of the B-value is same for the two numbers. only a maximum of two pairs can be made for the same tens digit




a = int(input())
b = list(map(int,input().split()))

def bitscore(x):
	l = int(str(x)[0])
	m = int(str(x)[1])
	n = int(str(x)[2])
	v = max(l,m,n)*11 + min(l,m,n)*7
	if len(str(v))>2:
	 	return str(v)[1:]
	else:
		return str(v)

oddl = []
evenl = []
for i in range(len(b)):
	if i%2 == 0:
		evenl.append(bitscore(b[i]))
	else:
		oddl.append(bitscore(b[i]))

dic = {}
count = 0

for i in oddl:
	if i[0] in dic.keys():
		dic[i[0]].append(i[1])
	else:
		dic[i[0]] = [i[1]]


for j in dic.keys():
	if len(dic[j]) >= 3:
		count += 2
	else:
		count += 1-

dic = {}
for i in evenl:
	if i[0] in dic.keys():
		dic[i[0]].append(i[1])
	else:
		dic[i[0]] = [i[1]]


for j in dic.keys():
	if len(dic[j]) >= 3:
		count += 2
	elif len(dic[j]) == 2:
		count += 1
	else:
		continue
print(count)