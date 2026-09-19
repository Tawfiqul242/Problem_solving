# Find duplicate elements using a dictionary
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2]
# dictionary ={}
# for i in numbers:
#     dictionary[i]= numbers.count(i)

# print(dictionary)

count = {}
for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)