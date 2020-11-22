def printMark2(mark, n, layers):
    m = int((1+layers)/2)
    for i in range(m-abs(m-n)):
        print(mark, end='')

def printLeft(mark, n, layers):
    m = int((1+layers)/2)
    print(mark*(abs(m-n)), end='')

def printDiamond(mark, n, layers):
    m = int((layers+1)/2)
    print(mark*(2*(m-abs(m-n))-1), end='')

def selection(n1, n2):
    types = n1
    layers = n2
    for i in range(1, n2+1):
        if n1 == 1:
            printMark('*', i, layers)
            print()
        elif n1 == 2:
            printLeft('.', i, layers)
            printMark('*', i, layers)
            print()
        else:
            printLeft('.', i, layers)
            printDiamond('*', i, layers)
            print()

def f2():
    n1 = 1
    n2 = 5
    if n1 not in range(1,4):
        print('Error')
    else:
        if n2 not in range(1,32,2):
            print('Error')
        else:
            selection(n1, n2)

f2()