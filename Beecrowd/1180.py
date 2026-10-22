N = int(input())

X = list(map(int, input().split()))

smallest = X[0]
place = 0

for index, value in enumerate(X):
    if smallest > value:
        smallest = value
        place = index

print(f"Menor valor: {smallest}")
print(f"Posicao: {place}")