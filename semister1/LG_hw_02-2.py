import math
import sympy as sp
sp.init_printing(use_unicode=True)

def bySymPy(mat):
    data = sp.Matrix(mat)
    data.eigenvects()

S = [[2,0],[0,-5]]
T = [[2,-12],[1,-5]]
U = [[5,2],[2,3]]
V = [[1,1],[1,1]]
W = [[2,1],[0,2]]
X = [[3,1],[-1,1]]

data = sp.Matrix(V)
data.eigenvects()