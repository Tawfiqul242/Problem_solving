# Find intersection of two lists

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

for i in list1:
    if i in list2:
        print(i, end=" ")

# intersection = list(set(list1)&set(list2))
# print(intersection)