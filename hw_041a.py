def numDecod(string):
    res = 0
    if string == '' or string[0] == '0':
        return res
    if len(string) <= 2 and int(string)<=26:
        res += 1    
    if 1 <= int(string[0]) <=26:
        res += numDecod(string[1:])
    if 1 <= int(string[0:2]) <=26:
        res += numDecod(string[2:])
    return res

a ='121'
result = numDecod(a)
print(result)