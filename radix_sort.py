import math

def get_digit(num, n): # finds the nth digit of a number
    return abs(num) // 10 ** n % 10

def digit_count(num): # finds the number of base 10 places in a number
    if num == 0:
        return 1
    return int(math.log10(abs(num))) + 1

def most_digits(nums): # finds the greatest base10 number of a list of numbers
    max_digits = 0
    for i in range(len(nums)):
        max_digits = max(max_digits, digit_count(nums[i]))

    return max_digits

def radix_sort(nums):
    max_digits = most_digits(nums)
    for i in range(max_digits-1):
        digit_buckets = [list() for x in range(10)]
        for j in range(len(nums)):
            digit = get_digit(nums[j], i)
            digit_buckets[digit].append(nums[j])
        nums = [item for x in digit_buckets for item in x]

    return nums

print(radix_sort([23,345,5467,12,2345,9852]))
