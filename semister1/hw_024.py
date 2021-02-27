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
target = int(input())
str_target = str(target)
head = str_target[0]
max_len = len(str_target)
index_num = str(head*max_len)

if target <10:
    total = target
else:
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
                lead = j
            index_num = str(lead+1)*max_len
        else:
            continue

    sum_3 = 0
    sw = True
    for i in range(len(str_target)-2):
        if str_target[i] > str_target[i+1]:
            sw = False
    
    if sw == True:
        for i in range(int(index_num[0]),int(str_target[-2]),1):
            pivotValue3 = pivot_value(head=i-1, length=1, matrix=m)
 #           print('i={}, index_num{}, pivotValue3={}'.format(i, index_num, pivotValue3))
            sum_3 += pivotValue3
    else:
        sum_3 = 0

    sum_4 = 0
    switch = True
    for i in range(len(str_target)-1):
        if str_target[i] > str_target[i+1]:
            switch = False
    
    if switch == True:
        sum_4 = int(str_target[-1])-int(str_target[-2])+1
    else:
        sum_4 = 0

    total = sum_0+sum_1+sum_2+sum_3+sum_4
print(total)