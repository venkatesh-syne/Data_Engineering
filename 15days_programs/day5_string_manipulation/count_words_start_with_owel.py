def count_vowel_names(names):
    vowels = "aeiouAEIOU"
    count = 0

    for name in names:
        if name[0] in vowels:
            count += 1

    return count

names = ["Alice", "Bob", "Eve", "Uma", "John"]
print(count_vowel_names(names))