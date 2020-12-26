import math

def eigenValue(mat):
    a = 1
    b = (mat[0][0] + mat[1][1])*(-1)
    c = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    eig1 = (-b + math.sqrt((b*b-4*a*c)))/2
    eig2 = (-b - math.sqrt((b*b-4*a*c)))/2
    return eig1, eig2

def eigenvect(mat, eigValue):
    elm_a = mat[0][0]-eigValue
    elm_b = mat[0][1]
    elm_c = mat[1][0]
    elm_d = mat[1][1]-eigValue
    if elm_a == 0:
        return '(1, 0)'
    elif elm_d == 0:
        return '(0, 1)'
    ratio = elm_b/elm_a
    return '(%s, %s)'%(-ratio, 1)

S = [[2,0],[0,-5]]
T = [[2,-12],[1,-5]]
U = [[5,2],[2,3]]
V = [[1,1],[1,1]]
W = [[2,1],[0,2]]
X = [[3,1],[-1,1]]

for mat in (S,T,U,V,W,X):
    mat_name = [ k for k,v in locals().items() if v == mat][0]
    eig1, eig2 = eigenValue(mat)
    print('Matrix %s = %s'%(mat_name,mat))
    print('eigen value lambda1 = %s, eigen vector 1 = %s'%(eig1,eigenvect(mat, eig1)))
    print('eigen value lambda2 = %s, eigen vector 2 = %s'%(eig2,eigenvect(mat, eig2)))
    print()