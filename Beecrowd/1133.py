n = int(input())
m = int(input())
for i in range(min(n,m)+1, max(n,m)):
    if i%5 == 2 or i%5 == 3:
        print(i)