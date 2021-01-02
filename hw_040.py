def rm(elements, lists):
    for i in lists:
        elements.remove(i)

def check(elements, index, group_sum, lists):
    if index >= len(elements) or group_sum < elements[index]:
        return False
    elif elements[index]==group_sum:
        lists.append(elements[index])   #append first num
        return True
    elif check(elements, index+1, group_sum, lists)==True:
        return True
    elif check(elements, index+1, group_sum-elements[index], lists)==True:
        lists.append(elements[index])   #append remaining nums
        return True
    else: return False

def compute(elements, groups, group_sum):
    index = 0
    lists = []
    if groups==0:
        return True
    if check(elements, index, group_sum, lists)==False:
        return False
    print(lists)
    rm(elements, lists)
    return compute(elements, groups-1, group_sum)

elements = [4,3,2,3,5,2,2]
groups = 3
group_sum = sum(elements)/groups
compute(elements, groups, group_sum)