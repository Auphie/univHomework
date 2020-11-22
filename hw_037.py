def findN(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return findN(n-3)+findN(n-2)+findN(n-1)

def main():
    inputNum = int(input())
    print(findN(inputNum))

main()