# Find all duplicate numbers 

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2]
seen = []
duplicate = []
for i in numbers:
    if i not in seen:
        seen.append(i)
    else:
        if i not in duplicate:
            duplicate.append(i)

print(duplicate)
