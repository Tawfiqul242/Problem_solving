n = float(input())
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for note in notes:
    result = int(n/note)
    print(f"{result} nota(s) de R$ {note:.2f}")
    n = round(n%note, 2)
print("MOEDAS:")
for coin in coins:
    result = int(n/coin)
    print(f"{result} moeda(s) de R$ {coin:.2f}")
    n = round(n%coin, 2)
