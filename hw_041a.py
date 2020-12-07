def cntTypes(str_num):
    n=len(str_num)
    if n==0: return 0
    if n==1 and int(str_num)>0: return 1
    elif int(str_num) ==0:return 0
    if n==2: 
        if (int(str_num) == 0 or int(str_num)>26):
            return 0
        elif (10<int(str_num)<=26 and int(str_num[1])!=0):
            return 2
        else: return 1
    if n>2:
        m = int(str_num[0:2])
        if 10 <= m <= 26:
            if int(str_num[1:3])==0:
                return 0
            if int(str_num[2:]) == int(str_num[1:]):
                return cntTypes(str_num[2:])
            return cntTypes(str_num[2:])+cntTypes(str_num[1:])
        elif str_num[1]=='0':
            return 0
        else:
            return cntTypes(str_num[1:])


s=input()
if int(s) == 0:
    result = 0
else:
    result = cntTypes(s)
print(result)