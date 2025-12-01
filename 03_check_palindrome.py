# 3. Check whether a given number is palindrome or not

# TC = O(log(num))  ,   SC = O(1)

def check_palindrome(num):
    n = num
    new_num = 0
    while n>0:
        last_digit = n % 10
        new_num = new_num * 10 +last_digit
        n = n // 10

    return new_num == num

    # if new_num == num:
    #     return True
    # else:
    #     return False 



res = check_palindrome(12231)
print(res)
