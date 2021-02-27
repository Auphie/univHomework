def printMark(n):
    for i in range(1, story+n, 1):
        print('#', end='')

def printNum(n):
    for i in range(story-n+1, 0, -1):
        print(i, end='')

story = int(input())

for i in range(1, story+1, 1):
    printMark(i)
    printNum(i)
    print()