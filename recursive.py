def palindrome(wordPal):
    if len(wordPal) <2:
        return 'True'
    if (wordPal[0]==wordPal[-1]):
        result = palindrome(wordPal[1:-1])
    else: return 'False'
    return result

a='amma'
result = palindrome(a)
print(result)

def permutation(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        print('i=%s, string=%s'%(i, s))
        result += [s[i]+ sub for sub in permutation(s[:i]+s[i+1:])]
        print('i=%s, result=%s'%(i, result))
    return result

def fibonacci(data, n):
    print('1. data=%s, n=%s'%(data,n))
    if data[n]!=0:
        return data[n]
    else:
        data[n-1] = fibonacci(data,n-1)
        data[n-2] = fibonacci(data, n-2)
        data[n] = data[n-1] + data[n-2]
        return data[n]

#print(palindrome('amoema',0))
#print(permutation('123'))

data = [0,1,1,0,0,0,0,0]
n = fibonacci(data,6)