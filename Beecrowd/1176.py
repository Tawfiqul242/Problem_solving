n = int(input())

for i in range(n):
    nth = int(input())
    f1 = 0
    f2 = 1
    fib_list = [f1, f2]
    for j in range(2, nth+2):
        fib = f1+f2
        fib_list.append(fib)
        f1 = f2
        f2 = fib
    print(f"Fib({nth}) = {fib_list[nth]}")
