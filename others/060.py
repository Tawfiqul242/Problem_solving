# Find second largest without sorting
numbers = [0, 1, 10, 5, 8, 20, 15, 20, 3]
largest = float('-inf')
second_largest = float("-inf")

for num in numbers:
    if largest < num:
        second_largest = largest
        largest = num

    elif second_largest < num and num != largest:
        second_largest = num

print(second_largest)
