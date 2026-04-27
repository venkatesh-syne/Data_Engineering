def common_chars(strings):
    result = set(strings[0])  # take first string

    for s in strings[1:]:
        result &= set(s)  # intersection

    return result
data = ["apple", "ample", "maple"]

print(common_chars(data))