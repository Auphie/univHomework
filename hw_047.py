def print_result(data):
    result = ''
    for k,v in data.items():
        if k.isdecimal() == True:
            result+=str(k)*v
        elif v >= 10:
            continue
        else:
            result+=str(v)
    return result

#a = 'Business people and 123developers must work together daily 5555555555throughout the PROject'
a = input()
data = {}
for char in a:
    if char.isalnum() == True:
        data[char] = data.get(char,0)+1

result = print_result(data)
print(int(result))