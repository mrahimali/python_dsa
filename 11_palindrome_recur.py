# RECURSION 
# Check if string is palindrome or not 


# def checkPalindrome(st):
#     left =0
#     right = len(st)-1
#     while left<right:
#         if st[left]==st[right]:
#             left +=1
#             right -=1
#         else :
#             return False
#     return True


# st = "aabbccdrddccbbaa"
# ans = checkPalindrome(st)
# print(ans)

# TC O(n/2)- O(n)
# SC O(1)

#               Using recursion 


def checkPalin(st, left, right):
    if left>=right:
        return True
    if st[left]!=st[right]:
        return False
    return checkPalin(st, left+1, right-1)


st = "aaccssddssccaa"
right = len(st)-1
ans = checkPalin(st,0, right)
print(ans)

