# Find the next fibonacci number

def fib(num):
    if num == 0 or num == 1:
        return num
    
    return fib(num-1) + fib(num-2)


ans = fib(8)
print(ans)

# TC - 2^^n
# SC - 2^^n