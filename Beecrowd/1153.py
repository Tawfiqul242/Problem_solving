N = int(input())
fact = N
for i in range(1, N):
    fact *= (N-i)

print(fact)