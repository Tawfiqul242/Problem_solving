n = int(input())
m = 1
for i in range(n):
    print(f"{m} {m**2} {m**3}")
    print(f"{m} {m**2+1} {m**3+1}")
    m += 1