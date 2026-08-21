# if a list has same value twice then return false otherwise return true

def has_duplicate(arr):
    duplicate = []
    for i in arr:
        if i in duplicate:
            return False
        duplicate.append(i)
    return True

print(has_duplicate([1,2,3,4]))
print(has_duplicate([1,2,2,4]))