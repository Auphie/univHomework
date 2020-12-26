# Python 3
import math

def init_zeroMatrix(types, matrix_1, matrix_2):
    init = []
    if types == 'addition' or types == 'scalar_multiple':
        for i in range(len(matrix_1)):
            m = []
            for j in range(len(matrix_1[0])):
                m.append(0.0)
            init.append(m)
        return init
    elif types == 'product':
        for i in range(len(matrix_1)):
            m = []
            for j in range(len(matrix_2[0])):
                m.append(0.0)
            init.append(m)
        return init
    else:
        return 0

def addition(matrix_1, matrix_2):
    rowsA = len(matrix_1)
    colsA = len(matrix_1[0])
    rowsB = len(matrix_2)
    colsB = len(matrix_2[0])
    if rowsA != rowsB or colsA != colsB:
        print('undefined')
    else:
        result = init_zeroMatrix('addition', matrix_1, matrix_2)
        for i in range(rowsA):
            for j in range(colsB):
                result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result

def multiply(matrix_1, matrix_2):
    rowsA = len(matrix_1)
    colsA = len(matrix_1[0])
    rowsB = len(matrix_2)
    colsB = len(matrix_2[0])
    if colsA != rowsB:
        print('undefined')
    else:
        result = init_zeroMatrix('product', matrix_1, matrix_2)
    # C00 = A00*B00 + A01*B10 + A02*B20
    # C01 = A00*B01 + A01*B11 + A02*B21
    # C10 = A10*B00 + A11*B10 + A12*B20
    # C11 = A10*B10 + A11*B11 + A12*B21
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for k in range(colsA):
                    total += matrix_1[i][k] * matrix_2[k][j]
                result[i][j] = total 
    return result

def scalar_multiple(matrix, scalar):
    result = init_zeroMatrix('scalar_multiple', matrix, None)
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j] = scalar * matrix[i][j]
    return result

def transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result

def inverse(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a*d-b*c
    if det == 0:
        print('This matrix does not have inverse matrix')
    else:
        multiple = 1/det
        tmp = [[d, -b],[-c, a]]
        result = scalar_multiple(tmp, multiple)
    return result

A = [[2,-1],[3,5]]
B = [[-2,0],[4,2]]
C = [[-1,2,0],[2,0,3]]
D = [[2,0,-1],[1,-2,0]]
E = [[2,-1],[math.pi, math.log10(2)],[-2,6]]
I = [[1,0],[0,1]]
## Topic a:
print('(a)')
## 2B = scalar_multiple(B, 2)
print('Ans:\nA + 2B = ', addition(A, scalar_multiple(B, 2)))
## -C = scalar_multiple(C, -1)
print('C - D =', addition(C, scalar_multiple(D, -1)))
print('A transpose =', transpose(A))
## Topic b:
print('\n(b). Calculate F = A*B and G = B*A. Is F equal to G?')
F = multiply(A, B)
G = multiply(B, A) 
print('Ans: \nF=',F, '\nG=', G, '\nTherefore, F is not euqal to G')
## Topic c:
print('\n(c). Calculate M = C*E and N = E*C. Is M equal to N?')
M = multiply(C, E)
N = multiply(E, C)
print('Ans: \nM=',M, '\nN=', N, '\nTherefore, M is not euqal to N')
## Topic d:
print('\n(d). Calculate A-transpose dot A')
print('Ans: \n',multiply(transpose(A),A))
## Topic e:
print('\n(e). Calculate A^-1 and F^-1. Is A*A^-1 equal to I? Is F*F^-1 equal to I?')
print('Ans: \nA^-1 =', inverse(A), '\nF^-1 =', inverse(F))
print('\nA*A^-1 =',multiply(A, inverse(A)), '\nI = ', I)
print('Therefore, A*A^-1 equal to I')
print('\nF*F^-1 =',multiply(F, inverse(F)), '\nI = ', I)
print('Therefore, F*F^-1 equal to I')

"""
[[A[i][j]+B[i][j] for j in range(len(B[0]))] for i in range(len(A))]  # the matrix A+B
sum(v[i]*v[i] for i in range(len(v)))  # the dot product v.v
[sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]  # the vector A*v
[[sum(A[i][k]*B[k][j] for k in range(len(b))) for j in range(len(B[0]))] for i in range(len(A))]  # the matrix A*B
"""