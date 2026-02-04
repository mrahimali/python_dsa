# *************************   LINEAR SEARCH  ***************************
# Return first occurence of element and if not found then return -1

def linearSearch(nums, target):
    n = len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1


nums = [23,1,24,26,87,90,87,123,112,54,24]
ans = linearSearch(nums, 240)
print(ans)

# TC = O(n)
# SC = O(1)