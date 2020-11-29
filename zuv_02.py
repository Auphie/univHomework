def QuickSort(data, left, right):
    if (left>=right): return data
    i = left
    j = right
    target = data[left]
    while i!=j:
        while (data[j]>target) and (i<j):
            j = j-1 #從右找起
        while (data[i]<=target) and (i<j):
            i+=1 #從左邊開始找比基準點大的
        if (i<j): #如果找到又沒與右邊的相遇，表示data[i]可以換到比較小的
            data[i], data[j] = data[j], data[i] #否則依定是小的最邊緣，
        print(data)                             #可以跟中間值交換
    data[left], data[i] = data[i], data[left]   #i是中間值
    data = QuickSort(data, left, i-1)           #處理左半邊
    data = QuickSort(data , i+1, right)         #處理右半邊
    return data

print(QuickSort([34,23,52],0,2))