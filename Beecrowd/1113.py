while True:
    a,b = map(int, input().split())
    if a == b:
        break
    if a < b:
        print(f"Crescente")
    else:
        print(f"Decrescente")