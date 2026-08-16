arr = []
for i in range(100):
    value = float(input())
    arr.append(value)

for i, value in enumerate(arr):
    if value <= 10:
        print(f"A[{i}] = {value:.1f}")