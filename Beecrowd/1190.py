O = input()
total = 0
count = 0

for i in range(12):
    for j in range(12):
        value = float(input())
        if i < j and i+j > 11:
            total += value
            count += 1
if O == "S":
    print(f"{total:.1f}")
else:
    result = total/count
    print(f"{result:.1f}")