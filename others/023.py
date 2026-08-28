# Remove duplicates
numbers = [1, 2, 2, 3, 4, 4]
# for i in set(numbers):
#     print(i, end=" ")

seen = []
for i in numbers:
    if i not in seen:
        seen.append(i)
print(seen)