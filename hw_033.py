def find_gcd(m, n):
    if n == 0:
        return m
    else:
        return find_gcd(n, m%n)

def main():
    #inputs = ['2', '18', '6', '36']
    while True:
        inputs = input().split()
        lists = [int(i) for i in inputs]
        if lists[0] == -1:
            break
        else:
            gcd = find_gcd(lists[0], lists[1])

            for i in range(2, len(lists)):
                gcd = find_gcd(gcd, lists[i])

            print(gcd)

main()