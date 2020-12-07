a='1 Geeks'
b='2 For X'
c='2 While Loop'
d='3 A Welcome'
e='3 B To'
f='3 C Geeks'
temp = []
for i in (a,b,c,d,e,f):
    z = i.split()
    temp.append(z)
#print(temp)

data = {}
for x in temp:
#    x = input().split()
    sub = {}
    if len(x)==3:
        if x[0] in data:
            sub = data[x[0]]
            print('sub=',sub)
            sub[x[1]]=x[2]
        else:
            sub[x[1]]=x[2]
        data[x[0]] = sub
    elif len(x) == 2:
        data[x[0]] = x[1]

print(data)