num = 2357
count = 0

for i in range (10,num+1, 1):
    judge = 0
    for pair in range(len(str(i))-1):
        if str(i)[pair] > str(i)[pair+1]:
            judge += 1
    if judge > 0:
        count += 1
#    print('i, judge, count', i, judge, count)

print(num-count)