n = int(input())
for i in range(n):
    value = int(input())
    prime = True
    for j in range(2, value):
        if value % j == 0:
            prime = False
            break

    if prime: 
        print(f"{value} eh primo")
    else:   
        print(f"{value} nao eh primo")