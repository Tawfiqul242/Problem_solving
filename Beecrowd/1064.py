sum = 0
count = 0
for i in range(6):
    number = float(input())
    if number > 0:
        sum += number
        count += 1
result = sum/count
print(f"{count} valores positivos")
print(f"{result:.1f}")