L = int(input())
T = input()

matrix = []

for r in range(12):
    row = []
    for c in range(12):
        row.append(float(input()))
    matrix.append(row)

result = sum(matrix[L])

if T == "S":
    print(f"{result:.1f}")
else:
    result = result/12
    print(f"{result:.1f}")