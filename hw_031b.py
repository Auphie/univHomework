def check_position(counts, result):
    last_num = 0
    c=[]
    for j in range(len(counts)):
        if counts[j]>0:
            last_num = min(num[j])
    for i in range(len(result)-2, -1, -1):
        if (result[i]!=last_num and result[i+1]!=last_num):
            print('true')
            c.append(i)
            ins_position = c[0]+1
        else:
            ins_position = 0
    return last_num, ins_position

def find_min(num, counts, last):
    for i in range(len(num)):
        if counts[i]>0 and num[i]!=last:
            return str(num[i])

inputs = input().split()
#inputs = ['3', '3', '2', '2', '4', '4', '4', '4']
dist_str = sorted(set(inputs))
print(dist_str)

num = []
counts = []
result = []
last_num = 0

for i in dist_str:
    num.append(i)
    counts.append(inputs.count(i))

result = num[0] + num[1]
counts[0] -= 1
counts[1] -= 1

def progress1(num, counts, result):
    while sum(counts) > 0:
        try:
            toInsert = find_min(num, counts, result[-1])
            index = num.index(toInsert)
            print('num=%s, counts=%s'%(num, counts))
            print('toInsert=%s, index=%s'%(toInsert,index))
            result+=toInsert
            counts[index] -= 1
        except ValueError:
            break
    return result

def progress2(num, counts, result):
    while sum(counts) > 0:
        last_num, ins_pos = check_position(counts, result)
        index = num.index(last_num)
        result = result[:ins_pos] + last_num + result[ins_pos:]
        counts[index] -= 1
    return result

result = progress1(num, counts, result)
result = progress2(num, counts, result)
print(result)