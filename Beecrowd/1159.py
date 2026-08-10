sum = 0
while (True):
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(0, 10):
            if x % 2 == 0:
                sum += x
                x += 1
            else:
                x += 1
    print(sum)
    sum = 0

