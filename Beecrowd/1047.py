a, b, c, d = map(int, input().split())

start = (a*60)+b
end = (c*60)+d
if start < end:
    duration = end - start
else:
    duration = 1440-start+end

h = duration//60
m = duration%60

print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
