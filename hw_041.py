def calCount(num):
    counts = 0
    if (len(num)==0 or int(num[0])==0):
        return 0
    counts += 1
    if (len(num)>1 and int(num[0:2])<27):
        counts+=1
    else: calCount(num[1:])
    if (len(num)>2 and int(num[1:3])<27):
        counts+=1
    else: calCount(num[1:])
    return counts

def main():
    a=input()
    result = calCount(a)
    print(result)

main()