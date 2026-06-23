s = int(input())
e = int(input())
sum = 0
if s > e:
    a = e
    e = s
    s = a
for i in range(s+1, e):
    if i % 2 != 0:
        sum += i
        
print(sum)