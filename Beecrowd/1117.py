count = 0
total = 0
while count < 2:
    n = float(input())
    if n>=0 and n <=10:
        total += n
        count += 1
    else: 
        print(f"nota invalida")
    if count == 2:
        result = total/count
        print(f"media = {result:.2f}")