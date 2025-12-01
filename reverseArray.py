def rev(arr):
    i=0
    n = len(arr)-1
    while i <= n:
        arr[i], arr[n] = arr[n], arr[i]
        i +=1
        n -=1

    return arr


arr = [1,2,3,4,5,6,7,8,9,10]
ans = rev(arr)
print(ans)