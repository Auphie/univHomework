def init_zeroMatrix(matrix_1, matrix_2):
    init = []
    for i in range(len(matrix_1)):
        m = []
        for j in range(len(matrix_2[0])):
            m.append(0.0)
        init.append(m)
    return init

def multiply(matrix_1, matrix_2):
    rowsA = len(matrix_1)
    colsA = len(matrix_1[0])
    rowsB = len(matrix_2)
    colsB = len(matrix_2[0])
    result = init_zeroMatrix(matrix_1, matrix_2)
    if colsA != rowsB:
        print('undefined')
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += int(matrix_1[i][k]) * int(matrix_2[k][j])
            result[i][j] = total 
    return result

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

data = [['A'], ['1', '1', '1', '2'], ['0', '1', '0', '1'], ['2', '1', '1', '2'], ['0', '2', '0', '1'], ['B'], ['124', '-200', '-24', '105'], ['-37', '108', '69', '-54'], ['119', '-219', '-11', '104'], ['-22', '-156', '68', '110']]
indices = [i for i in range(len(data)) if data[i][0].isalpha()]
#indices = [i for i, x in enumerate(data) if x[0].isalpha()]

matrixA = data[indices[0]+1:indices[1]]
matrixB =data[indices[1]+1:]
matAt = transpose(matrixA)
matBt = transpose(matrixB)
print('A=', matrixA)
print('B=', matrixB)
print('At=', matAt)
print('Bt=', matBt)

AtBt = multiply(matAt, matBt)
print(AtBt)

codes=''
for row in AtBt:
    for elem in row:
        print(chr(elem),end='')

#codes='74.117.115.116.32.100.46.111.32.105.116.33'
result = map(lambda x: chr(int(x)), codes.split('.'))
#result=[chr(int(i)) for i in codes.split('.')]
print(''.join(result))


"""

"""