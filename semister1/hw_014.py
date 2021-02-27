strInput = input()
new_str = []
lower_num = 0
upper_num = 0

for i in strInput:
    if i.islower():
        new_str.append(i)
        lower_num += 1
    elif i.isupper():
        upper_num += 1
    else:
        continue

if lower_num == 0:
    print('No lowercase letters')
else:
    [print(i, end='') for i in new_str]
    print()
print(len(strInput))
print(upper_num)