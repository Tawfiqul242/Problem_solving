T = input()

total = 0
count = 0
for r in range(12):
    for c in range(12):
        value = float(input())
        if c > r:
            total += value
            count += 1

if T == "S":
    print(f"{total:.1f}")
else:
    result = total/count
    print(f"{result:.1f}")