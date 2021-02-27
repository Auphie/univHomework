def cuts(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return cuts(n-1)+(n-1)+1

def main():
    num = int(input())
    print(cuts(num))

main()