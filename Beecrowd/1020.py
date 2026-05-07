n = int(input())
y = int(n/365)
r = n%365
m = int(r/30)
d = int(r%30)
print(f"{y} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")