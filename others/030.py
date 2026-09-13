# Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combine = []
for num in list1+list2:
    if num not in combine:
        combine.append(num)
print(combine)