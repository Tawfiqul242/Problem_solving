a,b,c,d = map(float,input().split())
media = ((a*2)+(b*3)+(c*4)+(d*1))/(2+3+4+1)
print(f"Media: {media:.1f}")
if media>=7:
    print("Aluno aprovado.")
elif media>=5:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e}")
    ave = (media+e)/2
    if ave >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {ave:.1f}")
else:
    print("Aluno reprovado.")