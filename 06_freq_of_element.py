# store frequency of every element if a dictionary 

# TC - 
# SC - 

# #####################   HASHING   ###################


# Method 1

# TC - O(N)
# SC - O(N)

def freq_of_element(nums): # O(N)
    freq_map = dict()
    for i in range(0, len(nums)):
        if nums[i] in freq_map: # O(1)
            freq_map[nums[i]] +=1 # O(1)
        else:
            freq_map[nums[i]]=1 # O(1)
    return freq_map


res = freq_of_element([2,1,2,3,2,3,4,5,6,7])
print(res)



# Method 2 - using hash map

# TC - O(n)
# SC - O(n)

def freq_of_element(nums):
    hash_map = dict()
    n =len(nums)
    for i in range(0,n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0)+1


