#  *************  MOVE ALL ZERO TO END OF ARRAY LEETCODE- 283 - DONT CHANGE ORDER OF ELEMENT ************


# def moveZero(nums):
#     temp = []
#     for ele in nums:
#         if ele != 0:
#             temp.append(ele)

#     n=len(nums)
#     m = len(temp)
#     for i in range(0,m):
#         nums[i]=temp[i]

    
#     for i in range(m, n):
#         nums[i]=0

    

# nums = [1,12,0,4,0,5,6,7,0,0]
# moveZero(nums)
# print(nums)

# TC = O(n+n)=O(2n)~O(n)
# SC = O(n)


def moveZero(nums):
    i=0
    n = len(nums)

    
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    j = i+1


    while j<n:
        if nums[j]!=0:
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
        j+=1

nums = [1,12,0,4,0,5,6,7,0,0]
moveZero(nums)
print(nums)


# TC = O(n)
# SC = O(1)

