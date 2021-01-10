def rm(elms, group_list):
    for elm in group_list:
        elms.remove(elm)
    return elms

def check(elms, group_sum, group_elms, index):
    if index >= len(elms):
        return False
    elif elms[index] > group_sum:
        return False
    elif elms[index] == group_sum:
        group_elms.append(elms[index])
        return True
    elif check(elms, group_sum, group_elms, index+1)==True:
        return True
    elif check(elms, group_sum-elms[index], group_elms, index+1)==True:
        group_elms.append(elms[index])
        return True
    else: return False

def compute(elms, groups, group_sum):
    result = []
    group_list = []
    if groups == 0:
        return result
    elif check(elms, group_sum, group_list, index=0)==False:
        return False
    else:
        groups-=1
#        print(group_list)
        group_list.sort(reverse=True)
        result.append(group_list)
        elms = rm(elms, group_list)
        result += compute(elms, groups, group_sum)     
    return result

def main():
    elements = [4,3,2,3,5,2,2]
    groups = 3
    group_sum = sum(elements)/groups
    result = compute(elements, groups, group_sum)
    print('result=',result)
    sorted_result = sorted(result, key=lambda x:x[0], reverse=True)
    print('sorted=',', '.join([str(i) for i in sorted_result]), end=' ')

main()