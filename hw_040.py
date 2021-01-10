def rm(elements,  group_elms):
    for i in group_elms:
        elements.remove(i)

def check(elements, index, group_sum, group_elms):
    if index >= len(elements) or group_sum < elements[index]:
        return False
    elif elements[index]==group_sum:
        group_elms.append(elements[index])   #append first num
        return True
    elif check(elements, index+1, group_sum, group_elms)==True:
        return True
    elif check(elements, index+1, group_sum-elements[index], group_elms)==True:
        group_elms.append(elements[index])   #append remaining nums
        return True
    else: return False

def compute(elements, groups, group_sum):
    index = 0
    group_elms = []
    if groups==0:
        return True
    if check(elements, index, group_sum, group_elms)==False:
        return False
    print(group_elms)
    rm(elements, group_elms)
    return compute(elements, groups-1, group_sum)

elements = [4,3,2,3,5,2,2]
groups = 3
group_sum = sum(elements)/groups
compute(elements, groups, group_sum)