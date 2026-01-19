# ********************** LARGEST ELEMENT ****************************


def largestElement(arr):
    largest = arr[0]
    for ele in arr:
        largest = max(largest, ele)
    return largest

# def largestElement(arr):
#     largest = float("-inf")
#     print(largest)
#     for ele in arr:
#         largest = max(largest, ele)
#     return largest


arr = [23,12,504,-23,99,45]
ans = largestElement(arr)
print(ans)


