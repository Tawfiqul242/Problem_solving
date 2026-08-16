n = int(input())

for i in range(n):
    ap, bp, ar, br = input().split()
    ap = int(ap)
    bp = int(bp)
    ar = float(ar)
    br = float(br)

    year = 0
    while ap <= bp and year <= 100:
        ap += int(ap*ar/100)
        bp += int(bp*br/100)
        year += 1
        
    if year > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{year} anos.")
