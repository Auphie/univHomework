def sortBy(e):
    return e[0]*10+(9-e[1])

string = input().split()
#string = ['1', '1', '1', '2', '3', '2', '2', '2', '2']
str_int = [int(i) for i in string]
index = [i for i in range(10)]

count_list = []
for i in range(10):
    count = str_int.count(i)
    count_list.append(count)

pairs = list(zip(count_list, index))
pairs.sort(key=sortBy, reverse=True)

#print(pairs)

sorted_list = []
for k,v in pairs:
    sorted_list += (str(v)*k)

result = []
while len(sorted_list) > 0:
#    print('1:',sorted_list[0])
    result.append(sorted_list[0])
    if len(sorted_list)>1:
        temp_list = [i for i in sorted_list if i != sorted_list[0]]
    #    print('2:',temp_list[0])
        second_no = temp_list[0]
    #    print('2nd_no', second_no)
    #    print('2nd_index', sorted_list.index(second_no))
        result.append(temp_list[0])
        sorted_list.pop(sorted_list.index(second_no))
        sorted_list.pop(0)
    else:
        break

print(''.join(result))