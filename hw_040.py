def rm(nums, con):
    for i in con:
        nums.remove(i)

def check(nums, index, value, con):
    if index >= len(nums) or value < nums[index]:
        return False
    elif nums[index]==value:
        con.append(nums[index])
        return True
    elif check(nums, index+1, value, con)==True:
        return True
    elif check(nums, index+1, value-nums[index], con)==True:
        con.append(nums[index])
        return True
    else: return False

def compute(div, nums, value):
    if div==0:
        return True
    con = []
    if check(nums, 0, value, con)==False:
        return False
    print(con)
    rm(nums, con)
    return compute(div-1, nums, value)

def f(div, nums):
    print(compute(div, nums, sum(nums)/div), '---')

nums = [4,3,2,3,5,2,1]
div = 4
f(div, nums)