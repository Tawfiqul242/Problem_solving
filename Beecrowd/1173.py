N = []
v = int(input())

for i in range(10):
    N.append(v)
    v += v

for i, value in enumerate(N):
    print(f"N[{i}] = {value}")