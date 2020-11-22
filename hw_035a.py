def permutation(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        result  += [s[i]+ sub for sub in permutation(s[:i]+s[i+1:])]
    return result

inputs = input().split()
inputs = ''.join(inputs)
result = permutation(inputs)
print(result)