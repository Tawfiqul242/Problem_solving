a,b,c = map(int, input().split())
numbers = [a, b, c]
asend = sorted(numbers)
asend.sort()
for i in asend:
    print(i)

print("")

for i in numbers:
    print(i)