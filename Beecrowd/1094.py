n = int(input())
c = r = s = 0
for i in range(n):
    quantity,name = input().split()
    quantity = int(quantity)
    
    if name == "C":
        c += quantity
    elif name == "R":
        r += quantity
    else:
        s += quantity
    
print(f"Total: {c+r+s} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
coelhos = c/(c+r+s)*100
print(f"Percentual de coelhos: {coelhos:.2f} %")
ratos = r/(c+r+s)*100
print(f"Percentual de ratos: {ratos:.2f} %")
sapos = s/(c+r+s)*100
print(f"Percentual de sapos: {sapos:.2f} %")