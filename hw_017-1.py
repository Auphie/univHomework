def myPrint(n, mark):
    for i in range(n):
        print(mark,end='')

def to_leftTri(n):
    for i in range(1, n+1, 1):
        if i <= n//2:
            myPrint(n//2+1-i,'.')
            myPrint(i,'*')
        else:
            myPrint(i-n//2-1,'.')
            myPrint(n-i+1,'*')
        print()

def to_rightTri(n):
    for i in range(1, n+1, 1):
        if i <= n//2:
            myPrint(i,'*')
        else:
            myPrint(n-i+1,'*')
        print()

def to_dimond(n):
    for i in range(1, 2*n, 2):
        if i//2 < n//2+1:
            myPrint(abs((n-i)//2),'.')
            myPrint(i,'*')
        else:
            myPrint((i-n)//2,'.')
            myPrint(2*n-i,'*')
        print()

tri_type = int(input())
story = int(input())

if tri_type == 1:
    to_rightTri(story)
elif tri_type == 2:
    to_leftTri(story)
else:
    to_dimond(story)