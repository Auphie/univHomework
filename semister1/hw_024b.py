def reference_matrix(length):
    m = [[1]*9]*length
    new = [[1]*9]
    for i in range(1,length,1):
        for j in range(8,0,-1):
            m[i][j-1] = m[i-1][j-1] + m[i][j]
        k = m[0].copy()
        new.append(k)    
    return new

def whole_values(length, matrix):
    sum_whole = 0
    for i in range(length-1):
        for j in range(9):
            sum_whole += matrix[i][j]
    return sum_whole

def pivot_value(head, length, matrix):
    pivotValue = matrix[length][head]
    return pivotValue

m = reference_matrix(100000)
target = 23456
str_target = str(target)
head = str_target[0]
max_len = len(str_target)
index_num = str(head*max_len)

sum_0 = whole_values(max_len, m)

sum_1 = 0
if (int(str_target[0])>1):
    for i in range(1, int(str_target[0])):
        pivotValue = pivot_value(head=(i-1) ,length=max_len-1, matrix=m)
        sum_1 += pivotValue
else:
    sum_1 = 0

sum_2 = 0
for i in range(1, max_len-2, 1):
    if index_num[i] < str_target[i]:
        lead = 0
        for j in range(int(index_num[i]), int(str_target[i]), 1):
            pivotValue2 = pivot_value(head=(j-1), length=max_len-i-1, matrix=m)
            sum_2 += pivotValue2
#            print('pivotValue2=',pivotValue2)
            lead = j
        index_num = str(lead+1)*max_len
    else:
        continue

sum_3 = 0
for i in range(int(index_num[0]),int(str_target[-2]),1):
    pivotValue3 = pivot_value(head=i-1, length=1, matrix=m)
    sum_3 += pivotValue3
    print('i=, pivotValue3=',i, pivotValue3)

print('index_num=',index_num)

tail = int(str_target[-1])-int(index_num[0])
sum_4 = tail if tail >0 else 0

total = sum_0+sum_1+sum_2+sum_3+sum_4
print(total)
print('sum_0=',sum_0)
print('sum_1=',sum_1)
print('sum_2=',sum_2)
print('sum_3=',sum_3)
print('sum_4=',sum_4)
