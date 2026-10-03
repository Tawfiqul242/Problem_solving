# Find union of two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# union = list(set(list1) | set(list2))
# print(union)

union = []
for i in list1+list2:
    if i not in union:
        union.append(i)
print(union)