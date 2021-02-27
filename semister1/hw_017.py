def to_rightTri(n):
    for i in range(1, n+1, 1):
        m = n//2+1
        print('*'*(m - abs(m-i)), end='')
        print()

def to_leftTri(n):
    for i in range(1, n+1, 1):
        m = n//2+1
        print('.'*abs(m-i), end='')
        print('*'*(m - abs(m-i)), end='')
        print()

def to_dimond(n):
    for i in range(1, n+1, 1):
        m = n//2+1
        print('.'*abs((m-i)), end='')
        print('*'*(2*(m-abs(m-i))-1), end='')
        print()

tri_type = int(input())
story = int(input())

if tri_type == 1:
    to_rightTri(story)
elif tri_type == 2:
    to_leftTri(story)
else:
    to_dimond(story)