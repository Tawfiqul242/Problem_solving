L = int(input())
T = input()

total = 0
for r in range(12):
    row = []
    for c in range(12):
        value = float(input())
        if c == L:
            total += value

if T == "S":
    print(f"{total:.1f}")
else:
    result = total/12
    print(f"{result:.1f}")