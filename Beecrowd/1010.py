sum = 0
for item in range(2):
    code, quantity, price = input().split()
    quantity = int(quantity)
    price = float(price)
    sum = sum+(quantity*price)
    
print(f"VALOR A PAGAR: R$ {sum:.2f}")