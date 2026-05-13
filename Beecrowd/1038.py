c,q=map(int, input().split())
pricelist = [4.00, 4.50, 5.00, 2.00, 1.50]
total = 0
for index, value in enumerate(pricelist):
   if index+1 == c:
      total = value*q

print(f"Total: R$ {total:.2f}")