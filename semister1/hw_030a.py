chars = input().split(' ')
#chars = ['One','Two','Three','Four']
seq = input().split(' ')
#seq = ['1','11','2','111']

seq_int = [int(i) for i in seq]

x = list(zip(seq_int, chars))
x.sort()

for k, v in x:
    print(v, end='')