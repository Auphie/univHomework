#chars = input().split(' ')
chars = ['One','Two','Three','Four']
#seq = input().split(' ')
seq = ['1','11','2','-111']

num_list = [int(i) for i in seq]
num_list.sort()

result=[]
for i in num_list:
    for j in range(len(chars)):
        if seq[j] == str(i):
            result.append(chars[j])

print(''.join(result))