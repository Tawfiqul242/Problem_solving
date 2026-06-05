s,e = map(int, input().split())
if s < e:
    print(f"O JOGO DUROU {e-s} HORA(S)")
else:
    print(f"O JOGO DUROU {24-s+e} HORA(S)")
