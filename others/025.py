# Reverse a list
list = [1, 2, 3]

# list.reverse()
# print(list)

reverse_list = []
for value in range(len(list)-1,-1,-1):
    reverse_list.append(list[value])
print(reverse_list)