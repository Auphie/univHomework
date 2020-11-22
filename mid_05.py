def checkLadder(n):
    num = str(n)
    for i in range(len(num)-1):
        if num[i]>=num[i+1]:
            continue
        else:
            return False

def get_sum(parity, n):
    digit_sum = 0
    if parity == 'odd':
        for i in range(0, len(n),2):
            digit_sum += int(n[i])
    else:
        for i in range(1, len(n),2):
            digit_sum += int(n[i])
    return digit_sum

def get_inverse_ladder(n):
    lists = []
    for i in range(11, n+1):
        if checkLadder(i) != False:
            lists.append(i)
    return lists

def main():
    num = 500
    a = 12345
    strA = str(a)
    sum_a = get_sum('even', strA)
    print('a, sumA_even =',a, sum_a)
    lists = get_inverse_ladder(num)
    for i in lists:
        if get_sum('odd', str(i)) == sum_a:
            print('ladder=', i)

main()
