x = int(input())
y = int(input())

while (y < x+1):
    y = int(input())

sum = count = 0
while (True):
    if sum > y:
        break
    else:
        sum += x
        x += 1
        count += 1

print(count)