# *******************     Move Negative to end of array    ****************

def moveNeg(nums):
    n = len(nums)-1
    m = 0

    while (m<n):

        if nums[m]>0:
            m +=1
        elif nums[n]<0:
            n -=1
        else :
            nums[m], nums[n]=nums[n], nums[m]
            n -=1
            m +=1
        


nums = [-1,-4,3,2, -1,-5,8,-2]
print(nums)
moveNeg(nums)
print(nums)