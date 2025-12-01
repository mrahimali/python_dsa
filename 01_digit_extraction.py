# Extract the digits from the given number

def digit_extract(num):
    ans = []
    n = num
    while n>0:
        last_digit = n%10
        ans.append(last_digit)
        n = n//10
    return ans

an = digit_extract(9875846573)
print(an)