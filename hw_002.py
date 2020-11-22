import math
def find_root(a=1, b=-2, c=1):
    x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
    print("%.1f" %x1)
    print("%.1f" %x2)

a=int(input('input a='))
b=int(input('input b='))
c=int(input('input c='))
find_root(a,b,c)