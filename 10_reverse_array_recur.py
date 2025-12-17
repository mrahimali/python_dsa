# RECURSION
# Reverse an array using recursion

def reverseArray(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right]= arr[right], arr[left]
    reverseArray(arr, left+1, right-1)


arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
# left = 0
left = 3
right = 7
# right = len(arr)-1
ans = reverseArray(arr,left,right)

print(arr)

# TC - O(N/2) ~ O(N)
# SC - O(N/2) ~ O(N)    stack space
