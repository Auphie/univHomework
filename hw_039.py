def C(m, count=0):
    if m == 0:
        return (0, 0)
    elif m == 1:
        return (1, count)
    else:
        if m%2 == 1:
            return C((m+1)/2, count+1)
        else:
            return C(m/2, count+1)

def transform(element):
    decimal = int(element,2)
    count = C(decimal)[1]
    print('%04d'%int(bin(count)[2:]))

def main():
    space = []
    while True:
        inp = input()
        if inp == '-1':
            break
        space.append(inp)
    target = [elm for elm in space if elm !='0']
#    print(target)
    for elm in target:
        transform(elm)

main()