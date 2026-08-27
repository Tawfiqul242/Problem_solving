# Check if list contains duplicates

def has_duplicate(list):
    return len(list) != len(set(list))

print(has_duplicate([1, 2, 3, 4]))
print(has_duplicate([1, 2, 4, 4]))