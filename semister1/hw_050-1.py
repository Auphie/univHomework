def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def getInput():
    data = []
    while True:
        inputs = input()
        if inputs == '0':
            break
        elms = inputs.split()
        data.append(elms)
    return data

def createCode(matAt, matBt):
    code = []
    for i in range(len(matAt)):
        for j in range(len(matBt[0])):
            total = 0
            for k in range(len(matAt[0])):
                total += int(matAt[i][k])*int(matBt[k][j])
            code.append(total)
    return code

#data = [['A'], ['1', '1', '1', '2'], ['0', '1', '0', '1'], ['2', '1', '1', '2'], ['0', '2', '0', '1'], ['B'], ['124', '-200', '-24', '105'], ['-37', '108', '69', '-54'], ['119', '-219', '-11', '104'], ['-22', '-156', '68', '110']]
data = getInput()
indices = [i for i in range(len(data)) if data[i][0].isalpha()]
#indices = [i for i, x in enumerate(data) if x[0].isalpha()]
matrixA = data[indices[0]+1:indices[1]]
matrixB =data[indices[1]+1:]
matAt = transpose(matrixA)
matBt = transpose(matrixB)
code = createCode(matAt, matBt)

print(''.join([chr(i) for i in code]))