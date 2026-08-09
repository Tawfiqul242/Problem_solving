s = 0
r = 1
for i in range(1, 21):
    s += r / 2**(i-1)
    r += 2

print(f"{s:.2f}")