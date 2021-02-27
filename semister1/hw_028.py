def examineSingle(n, x, y):
    if y == n%x:
        return 1
    else:
        return 0

#stream = ['3', '2', '5', '3', '7', '2']
stream = input().split(' ')
num_list = [int(i) for i in stream]

n = 3
while True:
    result = 1
    for i in range(0,len(num_list)-1,2):
        x = num_list[i]
        y = num_list[i+1]
        temp_result = examineSingle(n, x, y)
        result *= temp_result
    if result ==1:
        print(n)
        break
    else:
        n+=1