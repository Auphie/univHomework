def seeking(result, num_pocket, index):
    try:
        if num_pocket[index] != result[-1]:
            result.append(num_pocket[index])
            num_pocket.pop(index)
            seeking(result, num_pocket, 0)
        else:
            seeking(result, num_pocket, index+1)
    except IndexError:
        result = 'no'
    return result

input_num = '111222223'
results = []
num_set = set([i for i in input_num])

for i in num_set:
    index_i = input_num.index(i)
    new_list = [input_num[k] for k in [j for j in range(len(input_num)) if j != index_i]]
    permutation = seeking([i], new_list, 0)
    if len(permutation)==len(input_num):
        results.append(permutation)

final_result = min(results)
print(''.join(final_result))