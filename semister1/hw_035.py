def permutation(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        temp = []
        temp.append(s[i])
        result  += [temp + sub for sub in permutation(s[:i]+s[i+1:])]
    return result

def main():
    inputs = input().split()
    a = [int(i) for i in inputs]
    a.sort()
#    a = [1,2,3]
    result = permutation(a)
    
#    temp = str(result)[1:-1]
    for elem in result:
        if elem != result[-1]:
            print(str(elem)+',')
        else:
            print(elem)

main()