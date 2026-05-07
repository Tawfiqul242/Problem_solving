n = int(input())
h = int(n/ 3600)
r = n % 3600
m = int(r / 60)
s = int(r % 60)
print(f"{h}:{m}:{s}")