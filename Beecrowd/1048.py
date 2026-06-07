number = float(input())
readjust = 0
percentage = 0
salary = 0

if number <= 400:
    readjust = (number*15)/100
    percentage = 15
    salary = number+readjust

elif number <= 800:
    readjust = (number*12)/100
    percentage = 12
    salary = number+readjust

elif number <= 1200:
    readjust = (number*10)/100
    percentage = 10
    salary = number+readjust

elif number <= 2000:
    readjust = (number*7)/100
    percentage = 7
    salary = number+readjust

else:
    readjust = (number*4)/100
    percentage = 4
    salary = number+readjust

print(f"Novo salario: {salary:.2f}") 
print(f"Reajuste ganho: {readjust:.2f}")
print(f"Em percentual: {percentage} %")