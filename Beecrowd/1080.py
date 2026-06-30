numbers = []
for i in range(100):
    numbers.append(int(input()))
random = 0
for i in range(100):
    if numbers[i] > random:
        highest = numbers[i]
        random = highest
    else:
        continue
print(highest)
print(f"{numbers.index(highest) + 1}")