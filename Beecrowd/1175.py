arr =[]
for i in range(20):
    value = int(input())
    arr.append(value)

arr.reverse()
for i, value in enumerate(arr):
    print(f"N[{i}] = {value}")