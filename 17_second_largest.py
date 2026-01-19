# ********************* SECOND LARGEST ELEMENT IN AN ARRAY WITHOUT SORTING ********************************



# ******************  FIRST METHOD  **********************

def secondLargest(nums):
    largest = float("-inf")
    sec = float("-inf")
    for ele in nums:
        largest = max ( largest , ele )

    for ele in nums:
        if ele > sec and ele < largest:
            sec = ele

    return sec

#   TC - O(n+n)= O(2n) ~ O(n)
#   SC - O(1)


# def secondLargest(nums):
#     largest = float("-inf")
#     sec = float("-inf")
#     for ele in nums:
#         if ele > largest:
#             sec = largest
#             largest = ele
#         elif ele > sec and ele != largest:
#             sec = ele

#     return sec
# #     TC - O(n)
# #     SC - O(1)



nums = [23,13,67,45,90,56,122,89, 122]
ans = secondLargest(nums)
print(ans)

