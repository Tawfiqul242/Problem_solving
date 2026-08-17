n = int(input())

f1 = 0
f2 = 1
fib_list = [f1, f2]

for i in range(2, n):
    fib = f1+f2
    fib_list.append(fib)
    f1 = f2
    f2 = fib
print(*fib_list)