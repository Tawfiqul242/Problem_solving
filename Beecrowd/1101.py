while True:
    a,b = map(int, input().split())
    if a<=0 or b <=0:
        break
    if a>b:
        r = a
        a = b
        b = r

    count = 0
    for i in range(a, b+1):
        count += i
        print(i, end=" ")
    print(f"Sum={count}")