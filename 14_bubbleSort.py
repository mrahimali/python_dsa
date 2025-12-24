# ********************     SORTING ALGORITHM     ********************
# ********************     BUBBLE SORT ( Adjacent Swap )     ********************



def bubbleSort(nums):
    n = len(nums)-1
    for i in range(0,n):
        swapped = False
        for j in range(0,n-i):
            if nums[j]>nums[j+1]:
                nums[j+1], nums[j]=nums[j], nums[j+1]
                swapped = True
                print(nums)
        if not swapped:
            break
        print(swapped)        


nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
bubbleSort(nums)
print(nums)


# TC - Best  case O(N)
# TC - O(N(N+1)/2)
# SC - O(1)