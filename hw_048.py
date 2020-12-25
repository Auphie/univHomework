code = input()
#code = 'do not take my money'
len_space = []

data = {}

for i in range(len(code)):
    space=[]
    for j in code[i:]:
        if j not in space:
            space.append(j)
        else:
            break
        data[i] = len(space)

max_value = max(data.values())
print(max_value)
