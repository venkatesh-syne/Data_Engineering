def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:      # check if number is positive
            total += num # add to total
    return total

# Example list
nums = [10, -5, 3, -2, 7, -1]

result = sum_positive(nums)
print("Sum of positive numbers:", result)



