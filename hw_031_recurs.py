def permutation(s):
    result = []
    if len(s)==1:
        return [s]
    for i in range(len(s)):
        result += [s[i]+ sub for sub in permutation(s[:i]+s[i+1:])]
    return result

def is_diff(nums):
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            return False
    return True

s = '111222223'
electors = []
permutations = set(permutation(s))
for i in permutations:
    if is_diff(i)==True:
        electors.append(i)

print('electors=',electors)
print('result=', min(electors))