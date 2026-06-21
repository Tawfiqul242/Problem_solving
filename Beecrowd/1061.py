_, day1 = input().split()
day1 = int(day1)
sh, sm, ss = map(int, input().split(':'))
_, day2 = input().split()
day2 = int(day2)
eh, em, es = map(int, input().split(':'))

starttime = day1*24*3600 + sh*3600 + sm*60 + ss
endtime = day2*24*3600 + eh*3600 + em*60 + es
duration = endtime - starttime
d = duration // (24*3600)
duration %= 24 * 3600
h = duration//3600
duration %= 3600
m = duration//60
s = duration % 60

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")
