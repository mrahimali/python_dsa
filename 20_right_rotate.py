# ********************  RIGHT ROTATE BY 1  ******************************


def rightRotate(nums):
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1, -1):
        nums[i+1] = nums[i]

    nums[0]=temp



nums = [1,2,3,4,5,6,7,8,9]
print(nums)
rightRotate(nums)
print(nums)

