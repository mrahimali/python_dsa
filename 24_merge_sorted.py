# *****************************  MERGE TWO SORTED ARRAY ( EXCLUDE DUPLICATES )  ********************************

def mergeSorted(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    result = []
    i = 0
    j = 0

    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i +=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j +=1
    
    while i<n:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i +=1

    while j<m:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j +=1

    return result
            


nums1 = [1,2,3,4,4,5,6,7]
nums2 = [6,7,8,9,10,11]
ans = mergeSorted(nums1, nums2)

print(ans)

# TC = O(n+m)
# SC = result is actually a answer apart from that i did not use any space so i can say it is O(1) otherwise O(m+n)