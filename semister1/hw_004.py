import math
def find_bmi(a=1.72, b=60):
    bmi = b/a**2
    print("%.1f" %bmi)

print('input hight= ? meter')
a=float(input())
print('input weight= ? kg')
b=float(input())
find_bmi(a,b)