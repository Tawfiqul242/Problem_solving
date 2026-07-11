n = int(input())

for j in range(n):
    x,y=map(int, input().split())
    sum = 0
    if x > y:
        r = x
        x = y
        y = r
    for i in range(x+1, y):
        if i%2!=0:
            sum += i

    print(sum)