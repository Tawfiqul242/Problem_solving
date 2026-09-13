# Move all zeros to the end
sample = [0, 1, 0, 3, 12]
zero = []
non_zero = []
for num in sample:
    if num != 0:
        non_zero.append(num)
    else:
        zero.append(num)

print(non_zero+zero)