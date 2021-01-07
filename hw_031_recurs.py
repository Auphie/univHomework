def permutation(n):
    result = []
    if len(n)==1:
        return [n]
    for i in range(len(n)):
        result += [n[i]+ sub for sub in permutation(n[:i]+n[i+1:])]
    return result

def is_diff(nums):
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            return False
    return True

input_num = '111222223'
electors = []
permutations = set(permutation(input_num))
for case in permutations:
    if is_diff(case)==True:
        electors.append(case)

print('electors=',electors)
print('result=', min(electors))