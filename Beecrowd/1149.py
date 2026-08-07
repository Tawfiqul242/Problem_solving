values = list(map(int, input().split()))

a = values[0]
for n in values[1:]:
    if n > 0:
        break

sum = 0  
for i in range(n):
    sum += a + i

print(sum)