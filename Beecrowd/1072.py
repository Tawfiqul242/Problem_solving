n = int(input())
incount = outcount = 0
for i in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        incount += 1
    else:
        outcount += 1
print(f"{incount} in")
print(f"{outcount} out")