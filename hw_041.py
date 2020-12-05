def cntTypes(str_num):
    n=len(str_num)
    if n==0: return 1
    if n==1: return 1 if int(str_num)>0 else 0
    if n>=2:
        m = int(str_num[0:2])
        if 10 <= m <= 26:
            return cntTypes(str_num[2:])+cntTypes(str_num[1:])
        elif m < 10:
            return 0
        elif str_num[1] == '0':
            return 0
        else:
            return cntTypes(str_num[1:])

s=input()
result = cntTypes(s)
print(result)