# Sort a list without sort()
list = [1, 3, 2, 4]
sorted_list = []
for i in range(len(list)):
    target = list[0]
    for j in list:
        if target > j:
            target = j
    sorted_list.append(target)
    list.remove(target)
print(sorted_list)