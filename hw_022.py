def getNum():
    a= int(input())
    return a if a <= 15 else 0

total_sum = 1

for i in range(getNum(),0,-1):
    total_sum *= i

print(total_sum)