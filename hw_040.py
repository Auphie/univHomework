def isSubsetSum(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
 
    # If last element is greater than sum, then
    # ignore it
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)
 
    ''' else, check if sum can be obtained by any of 
    the following
    (a) including the last element
    (b) excluding the last element'''
 
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])
 
# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
 
 
def findPartion(arr, n, div):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % div != 0:
        return False
 
    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, sum // div)
 
string = input().split()
arr = [int(i) for i in string]
div = int(input())
# Driver code
#arr = [4,3,2,3,5,2,1]
n = len(arr)
 
# Function call
if findPartion(arr, n, div) == True:
    print("True")
else:
    print("False")
 
# This code is contributed by shreyanshi_arun.
