#using dictionaries
numbers = [1, 2, 2, 3, 4, 2, 5, 3]
freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

most_frequent = max(freq, key=freq.get)
print("Most frequent element:", most_frequent)

#using count
most_frequent = max(numbers, key=numbers.count)
print("Most frequent element:", most_frequent)

