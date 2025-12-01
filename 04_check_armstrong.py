# Check if the number is armstrong or not

# TC - O(log(n))  ,  SC - O(1)


def check_armstrong(num):
    n = num
    pwr = len(str(abs(num))) # abs agar number negative hua to srf digit lega sign nahi
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + digit**pwr
        n = n//10
    return sum == num

res = check_armstrong(1634)
print(res)