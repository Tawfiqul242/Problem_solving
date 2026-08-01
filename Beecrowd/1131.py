inter= germio = draw = count = 0
running = True

while(running):
    i, g = map(int, input().split())

    if i > g: inter+=1
    elif i < g: germio+=1
    else: draw+=1

    count += 1

    while (True):
        print(f"Novo grenal (1-sim 2-nao)")
        choice = int(input())
        if choice == 1: break
        else: 
            running = False
            print(f"{count} grenais")
            print(f"Inter:{inter}")
            print(f"Gremio:{germio}")
            print(f"Empates:{draw}")
            if inter == germio:
                print(f"Não houve vencedor")
            elif inter > germio:
                print(f"Inter venceu mais")
            else: print(f"Gremio venceu mais")
            
            break