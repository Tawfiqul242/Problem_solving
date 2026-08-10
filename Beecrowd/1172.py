arr = []
for i in range(10):
    value = int(input())
    if value < 1:
        value = 1
    arr.append(value)

for i in range(10):
    print(f"X[{i}] = {arr[i]}")