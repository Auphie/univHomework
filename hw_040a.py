def compute(elements, groups, group_sum, i):
#    print('elements=',elements)
#    print('groups=',groups)
#    print('group_sum=',group_sum)
#    print('i=',i)
    if len(elements)==0:
        return True
    if i >= len(elements):
        return False
    if elements[i] > total:
        return False
    if group_sum==0:
        groups -= 1
        return compute(elements, groups, total, 0)
    if elements[i] <= group_sum:
        new_sum = group_sum - elements[i]
        elements.remove(elements[i])
        return compute(elements, groups, new_sum, 0)
    else: 
        return compute(elements, groups, group_sum, i+1)

elements = [5,3,2,4,3,1,2]
elements.sort(reverse=True)
groups = 4
group_sum = total = sum(elements)/groups
if sum(elements)%groups !=0:
    print('No Way')
else:
    print('Can' if compute(elements, groups, total, i=0)
        else 'No way')