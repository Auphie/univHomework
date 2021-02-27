def permutation(s):
    p = []
    if len(s)==1:
        return [s]
    for i in range(len(s)):
         p += [s[i] + sub for sub in permutation(s[:i]+s[i+1:])]
    return p

def is_diff(case):
    for i in range(len(case)-1):
        if case[i]==case[i+1]:
            return False
    return True

def main():
    result = []
    input_num = '111222223'
    cases = (set(permutation(input_num)))
    for case in cases:
        if is_diff(case) == True:
            result.append(case)
    print(min(result))

main()