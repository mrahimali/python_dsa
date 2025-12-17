# RECURSION

# Find factorial of a given number 

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)


n=10
ans = fact(n)
print(ans)

# TC - O(N)
# SC - O(N)
