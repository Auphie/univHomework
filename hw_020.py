a= int(input())
num = 0

for i in range(2,a,1):
    if a%i == 0:
        num += 1

if num == 0:
    print('%d is prime number'%a)
else:
    print('%d is not prime number'%a)