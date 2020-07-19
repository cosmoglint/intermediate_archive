#2: for a given number print the english name of the number(as written in words)


import math

def thrdig(n):
    sat = str(n)
    val = ""
    dic = {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
    if len(sat)==3:
        if int(sat[-2:]) in dic.keys():
            val += " " + dic[int(sat[0])] + " " + "Hundred" + " " + dic[int(sat[-2:])]
        else:
            val += " " + dic[int(sat[0])] + " " + "Hundred" + " " + dic[int(sat[1])*10] + " " + dic[int(sat[2])]
        return val[1:]
    elif len(sat)==2:
        if int(sat) in dic.keys():
            val += " " + dic[int(sat)]
        else:
            val += " " + dic[int(sat[0])*10] + " " + dic[int(sat[1])]
        return val[1:]
    elif len(sat)==1:
        return dic[n]
    
def numberToWords(num):
    val = str(num)
    ans = ""
    nu = math.ceil(len(val)/3)
    thed = {1:"",2:"Thousand",3:"Million",4:"Billion",5:"Trillion"}
    for i in range(1,nu+1):
        if len(val)>3:
            ans = thrdig(int(val[(-3):])) + " " + thed[i] + " " + ans
            print(val[-3:])
            val = val[:-3]
        else:
            ans = thrdig(int(val)) + " " + thed[i] + " " + ans
    return ans
    
a = int(input())
print(numberToWords(a))