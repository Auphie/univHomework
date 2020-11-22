def printMark(mark, n, num):
    for i in range(0, num+n):
        print(mark, end='')

def printNum(n, num):
    for i in range(num-n, 0, -1):
        print(i, end='')

def f1():
    num = 10
    if num in range(1,10):
        for i in range(num):
            printMark('#', i, num)
            printNum(i, num)
            print()
    else:
        print('Error')

f1()