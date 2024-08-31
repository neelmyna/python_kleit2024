def find_sum_of_digits(num):
    sum = 0
    while num != 0:
        remainder = num % 10
        num = num // 10
        sum += remainder
    return sum

