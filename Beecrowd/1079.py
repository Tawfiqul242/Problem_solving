n = int(input())
results = []
for i in range(n):
    a,b,c = map(float,input().split())
    results.append(((a*2)+(b*3)+(c*5))/10)

for result in results:
    print(f"{result:.1f}")
