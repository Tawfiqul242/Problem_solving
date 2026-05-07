n = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]
print(n)
for note in notes:
    result = int(n/note)
    print(f"{result} nota(s) de R$ {note},00")
    n = n%note


