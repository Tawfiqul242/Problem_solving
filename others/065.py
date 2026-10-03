# Check whether two lists contain the same elements
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

# count = 0
# for i in list1:
#     if i in list2:
#         count += 1
# if count == len(list2):
#     print("Contain same elements")
# else:
#     print("Not contain same elements")

if sorted(list1) == sorted(list2):
    print("Contain same elements")
else:
    print("Not contain same elements")