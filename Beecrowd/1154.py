total = count = 0
while (True):
    n = int(input())
    if n < 0:
        break
    count += 1
    total += n

result = total/count
print(f"{result:.2f}")