n = int(input())
numbers = []
new_numbers = []

for i in range(n):
    a = int(input())
    numbers.append(a)

def get_minMax(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] <= min_num:
            min_num = numbers[i]
        if numbers[i] >= max_num:
            max_num = numbers[i]
    return min_num, max_num

min_num, max_num = get_minMax(numbers)
for i in numbers:
    if i != max_num:
        new_numbers.append(i)

c, second_max = get_minMax(new_numbers)
print(second_max)
print(min_num*max_num)