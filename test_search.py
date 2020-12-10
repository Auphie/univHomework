def search(data, left, right, key):
    mid = (left+right)//2
    print('left=%s,right=%s,mid=%s'%(left,right,mid))
    if data[mid] == key:
        return mid
    if left == right:
        return -1
    if data[mid] > key:
        return search(data, left, mid-1, key)
    else:
        return search(data, mid, right+1, key)

def f(x):
    print(search([2,3,7,9,21,39], 0, 5, x))

f(38)