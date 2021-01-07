def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


def check_list(list_str):
    for i in range(len(list_str) - 1):
        if list_str[i] == list_str[i + 1]:
            return False
    return True


def start(list1):
    for i in range(len(list1) - 1):
        if list1[i] != list1[i + 1]:
            continue
        else:
            for j in range(i + 2, len(list1)):
                if list1[i + 1] != list1[j]:
                    list1[i + 1], list1[j] = swap(list1[i + 1], list1[j])
                    break

    while (check_list(list1) == False):
        tmp = list1[-1]
        list1.pop()
        for i in range(len(list1) - 2, -1, -1):
            list1.insert(i, tmp)
            if check_list(list1) == True:
                break
            else:
                del list1[i]

    if check_list(list1) == True:
        for i in list1:
            print(i, end='')


num = input()
list1 = [i for i in num]
list1.sort()
start(list1)