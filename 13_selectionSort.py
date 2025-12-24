# ********************     SORTING ALGORITHM     ********************
# ********************       SELECTION SORT      ********************


def selectionSort(arr):
    n = len(arr)-1
    
    
    for i in range(0,n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx]=arr[min_idx], arr[i]




arr = [3,1,4,5,2,8,9,12]
print(arr)
selectionSort(arr)
print(arr)


# TC - O(N(N+1)/2)
# SC - O(1)

