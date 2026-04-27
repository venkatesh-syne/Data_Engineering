text = "hello world"

char_count = {}

for ch in text:
    if ch != " ":   # optional: ignore spaces

        #dict[key] = dict.get(key, 0) + 1 is the standard pattern for counting
        #Use dict.get(key, 0) to handle missing keys
        char_count[ch] = char_count.get(ch, 0) + 1

print(char_count)