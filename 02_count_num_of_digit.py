# 2. Count the number of digits in given number

def count_digit(num):
    n = num
    count =0
    while n>0:
        n = n//10
        count +=1

    return count

an = count_digit(9876543210)
print(an)
