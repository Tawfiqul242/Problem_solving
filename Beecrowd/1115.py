while True:
    a, b = map(int, input().split())
    if a ==0 or b ==0:
        break
    if a > 0 and b > 0:
        print(f"primeiro")
    elif a > 0 and b < 0:
        print(f"quarto")
    elif a < 0 and b < 0:
        print(f"terceiro")
    else:
        print(f"segundo")