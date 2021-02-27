def nthElement(l):
    if l == 1:
        return '0'
    elif l == 2:
        return '01'
    else:
        reverse = ''
        for i in nthElement(l-1):
            reverse += str(1-int(i))
        return str(nthElement(l-1))+reverse

inputs = input().split()

a = nthElement(int(inputs[0]))
print('a=%s, n=%s'%(a,int(inputs[1])-1))
print(a[int(inputs[1])-1])