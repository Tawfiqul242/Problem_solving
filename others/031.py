# Find elements present in first list but not second

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for num in list1:
    if num not in list2:
        print(num, end= " ")