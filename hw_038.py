def nthElement(l,n):
    if l == 1:
        return 0
    elif l == 2:
        if n == 1:
            return 0
        else:
            return 1
    else:
        if n%2 == 1:
            return nthElement(l-1, (n+1)/2)
        else:
            if int((n/2)%2) == 1:
                return nthElement(l-1, (n/2)+1)
            else:
                return nthElement(l-1, (n/2)-1)

def main():
    inputs = input().split()
#    inputs = ['25','16777215']
    layer = int(inputs[0])
    num = int(inputs[1])
    a = nthElement(layer, num)
    print(a)

main()