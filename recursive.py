def palindrome(wordPal,index):
    strlen=len(wordPal)-(index+1)
    print('wordPal[index]=%s,wordPal[strlen]=%s'%(wordPal[index],wordPal[strlen]))
    if (wordPal[index]==wordPal[strlen]):
        print('index=%s,strlen=%s'%(index,strlen))
        if (index+1==strlen or index==strlen):
            print("True")
            return
        dd(wordPal[1:-1], 0)
    else:
        print('False')

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