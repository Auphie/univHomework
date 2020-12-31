def rm(elements, lists):
    for i in lists:
        print('i=%s,lists=%s'%(i,lists))
        elements.remove(i)

def check(elements, index, group_sum, lists):
    if index >= len(elements) or group_sum < elements[index]:
        return False
    elif elements[index]==group_sum:
        lists.append(elements[index])
        return True
    elif check(elements, index+1, group_sum, lists)==True:
        return True
    elif check(elements, index+1, group_sum-elements[index], lists)==True:
        lists.append(elements[index])
        return True
    else: return False

def compute(elements, groups, group_sum):
    index = 0
    if groups==0:
        return True
    lists = []
    if check(elements, index, group_sum, lists)==False:
        return False
    rm(elements, lists)
    print(lists)
    return compute(elements, groups-1, group_sum)

elements = [4,3,2,3,5,2,1]
groups = 2
group_sum = sum(elements)/groups
compute(elements, groups, group_sum)