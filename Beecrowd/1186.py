O = input()

total = 0
count = 0
for r in range(12):
    for c in range(12):
        value = float(input())
        if r + c > 11:
            total += value
            count += 1

if O == "S":
    print(f"{total:.1f}")
else:
    result = total/count
    print(f"{result:.1f}")