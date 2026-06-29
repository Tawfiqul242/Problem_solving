n = int(input())
results = []
for i in range(n):
    value = int(input())
    if value == 0:
        results.append("NULL")

    elif value%2==0:
        if value > 0:
            results.append("EVEN POSITIVE")
        else:
            results.append("EVEN NEGATIVE")
    else:
        if value > 0:
            results.append("ODD POSITIVE")
        else:
            results.append("ODD NEGATIVE")  

for result in results:
    print(result)