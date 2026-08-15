n = int(input())
for i in range(n):
    value = int(input())
    sum = 0
    for j in range(1, value):
        if value%j == 0:
            sum += j

    if sum == value:
        print(f"{value} eh perfeito")

    else:
        print(f"{value} nao eh perfeito")