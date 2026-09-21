# Find frequency of every element
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 2]
frequency = {}
for num in numbers:
    frequency[num] = numbers.count(num)

for key, value in frequency.items():
    print(f"{key}: {value}")