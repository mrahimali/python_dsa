# *****************  REMOVE DUPLICATE FROM LIST [ In place]  *************************
# Unique elements ko starting me le aao baki last m jo b ho matlab nahi hai (without creating extra list)

def removeDuplicates(nums):
    i=0
    j=1
    n=len(nums)
    if n==1:
        return 1
    while j<n:
        if nums[i] != nums[j]:
            i +=1
            nums[i]=nums[j]
        j+=1
    return i+1


nums = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,8,9,9]
print(nums)
ans=removeDuplicates(nums)
print(ans)