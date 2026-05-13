def sort_by_length(strings):
    return sorted(strings, key=len)

# example
names = ["apple", "kiwi", "banana", "fig"]

result = sort_by_length(names)
print(result)