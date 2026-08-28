# Find duplicate values
numbers = [1, 2, 2, 3, 4, 4]
seen = []

for i in numbers:
    if i not in seen:
        seen.append(i)
    else:
        print(i)