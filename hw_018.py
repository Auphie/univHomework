def myNum(n):
    for i in range(1, 2*n, 1):
        if i <= n:
            print(i, end='')
        else:
            print(2*n-i, end='')

def myMark(n, mark):
    for i in range(n, 0, -1):
        print(mark, end='')

def to_rightTri(n):
    for i in range(1, n+1, 1):
        myNum(i)
        print()

def to_equalTri(n):
    for i in range(1, n+1, 1):
        myMark(story-i, '_')
        myNum(i)
        myMark(story-i, '_')
        print()

def to_rev_equalTri(n):
    for i in range(n, 0, -1):
        myMark(story-i, '_')
        myNum(i)
        myMark(story-i, '_')
        print()

tri_type = int(input())
story = int(input())

if tri_type == 1:
    to_rightTri(story)
elif tri_type == 2:
    to_equalTri(story)
else:
    to_rev_equalTri(story)