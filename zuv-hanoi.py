def move(i, x, y):
    print(i, x, y)

def hanoi(i,A,C,B):
    if i==1: move(i,A,C)
    else:
        hanoi(i-1,A,B,C)
        move(i,A,C)
        hanoi(i-1,B,C,A)

hanoi(3,'A','C','B')