def find_kn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2*find_kn(n-1)+3*find_kn(n-2)

def main():
    num = input()
    #num = '15'
    if num.isdecimal():
        kn = find_kn(int(num))
        print(kn)
    else:
        print('Error')

main()