word = "hellow python"
count = word.count("l")
print(count)

text = "apple"

result = {}

for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)
