# Find duplicate elements without using set()
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2]
checked = []
duplicate = []
for number in numbers:
    if number not in checked:
        checked.append(number)
    else:
        if number not in duplicate:
            duplicate.append(number)

print(duplicate)