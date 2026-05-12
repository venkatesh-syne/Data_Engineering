nums = [10, 20, 4, 45, 99]

largest = second = -1

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)