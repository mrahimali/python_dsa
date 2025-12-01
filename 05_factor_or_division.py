# Print all the factor or divisor of a given number 

# TC -O(n)  ,   SC - O(k) - k would be total no of factors

# def all_factor(num):
#     n = num
#     factor = []

#     for i in range(1,num//2):
#         if num % i == 0:
#             factor.append(i)
#     factor.append(num)
#     return factor

# res = all_factor(36)
# print(res)


###############   OPTIMISED SOLUTION   ########################

# TC - O(sqrt(n))  if sorting is done the TC - O(sqrt(n))+O(nlog(n))   
# SC - O(k) - k would be total no of factors
import math
def all_factor(num):
    n = num
    factor = []
    m = int(math.sqrt(num))
    for i in range(1,m+1):
        if num % i == 0:
            quot = num//i
            factor.append(i)
            if i != m:
                factor.append(quot)
    return factor

res = all_factor(36)
print(res)