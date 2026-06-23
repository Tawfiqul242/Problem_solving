n = int(input())
e = 2
count = 0
while count != 6:
    if n % 2 != 0:
        print(n)
        count += 1
        n += 1
    else:
        n += 1