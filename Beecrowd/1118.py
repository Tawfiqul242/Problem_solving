count = valid_value = 0
while(True):
    n = float(input())

    if n < 0 or n > 10:
        print(f"nota invalida")
        continue

    valid_value += n
    count += 1

    if count == 2:
        result = valid_value/count
        print(f"media = {result:.2f}")
        count = 0
        valid_value = 0
        while (True):
            print(f"novo calculo (1-sim 2-nao)")
            choice = int(input())
            if choice == 1:
                break
            elif choice == 2:
                exit()