a = [10, 9, 20, 30, 40]

if a == sorted(a):
    print("List is sorted")
else:
    print("Not sorted")

a = [10, 8,20, 30, 40]

is_sorted = True

for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("List is sorted")
else:
    print("Not sorted")