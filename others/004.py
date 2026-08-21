# Find sum of digits

# digits = list(map(int, input().split()))
# sum = 0
# for i in digits:
#     sum += i
# print(sum)

values = input()
sum = 0

for value in values:
    sum += int(value)
print(sum)