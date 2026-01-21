# ********************  RIGHT ROTATE BY K  ******************************


# def rightRotate(nums,k):
#     n = len(nums)
#     rotates = k%n

#     for _ in range(0,rotates): # O(r) r-> no of rotations
#         e = nums.pop() # O(1)
#         nums.insert(0,e) # O(n)

# # TC - O(n*r)
# # SC - O(1)


# *****************  BETTER APPROACH  ************************


# def rightRotate(nums,k):
#     n = len(nums)
#     k = k%n
#     nums[:] = nums[n-k:]+nums[0:n-k]


# TC -> O(k)+O(n-k) -> O(n)
# SC -> O(1)


# nums = [1,2,3,4,5,6,7,8,9]
# print(nums)
# rightRotate(nums,13)
# print(nums)

# ************************  OPTIMAL SOLUTION  *****************************

def reverse(nums, j , k):
    while j<=k:
        nums[j], nums[k]=nums[k], nums[j]
        j+=1
        k-=1

def rotate(nums , k):
    n=len(nums)
    reverse(nums,n-k,n-1) # TC - O(k/2)
    reverse(nums,0,n-k-1) # TC - O(n-k/2)
    reverse(nums,0,n-1)   # TC - O(n/2)

# TC -> O(k/2) + O(n-k/2) + O(n/2)
# SC -> O(1)

nums = [1,2,3,4,5,6,7,8,9]
rotate(nums,3)
print(nums)





