def forSum(m,n):
    sumValue = 0
    for i in range(m, n+1, 2):
        sumValue += i
    return sumValue

def forProduct(m,n):
    product = 1
    for i in range(m,n+1, 3):
        product *= i
    return product

m = int(input())
n = int(input())
if m < n:
    print(forSum(m,n))
    print(forProduct(m,n))
else:
    print(forSum(n,m))
    print(forProduct(n,m))   