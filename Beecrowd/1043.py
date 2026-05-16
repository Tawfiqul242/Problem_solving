a,b,c=map(float, input().split())
if a+b>c and b+c>a and a+c>b:
    print(f"Perimetro = {a+b+c:.1f}")
else:
    trape = ((a+b)*c)/2
    print(f"Area = {trape:.1f}")