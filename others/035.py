# Find maximum/minimum in tuple

sample = (4, 2, 3, 5,8,1)
max_value = sample[0]
for i in sample:
    if i > max_value:
        max_value = i
print(max_value)