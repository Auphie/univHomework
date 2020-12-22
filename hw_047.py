def print_result(data):
    result = ''
    for k,v in data.items():
        if k.isdecimal() == True:
            result+=str(k)
        elif v > 10:
            continue
        else:
            result+=str(v)
    return result

#a = 'Be9tter to light one candle than to curse the darkness xxxxxxxxxxx'
a = input()
data = {}
for char in a:
    if char.isalnum() == True:
        data[char] = data.get(char,0)+1

result = print_result(data)
print(int(result))