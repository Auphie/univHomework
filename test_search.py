def search(data, left, right, key):
    mid = (left+right)//2
    if data[mid] == key:
        return mid
    if left == right:
        return -1
    if data[mid] > key:
        return search(data, left, mid, key)
    else:
        return search(data, mid, right, key)

def f(x):
    print(search([2,3,7,9,21,39], 0, 5, x))

f(21)