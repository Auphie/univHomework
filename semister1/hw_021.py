a= int(input())
b= int(input())
total_sum = 0
for i in range(a,b+1,1):
    if i%2 == 0:
        total_sum += i
    else:
        continue

print(total_sum)