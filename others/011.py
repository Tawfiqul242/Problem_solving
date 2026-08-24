#     1
#    123
#   12345
#  1234567

result = ""
for i in range(1, 5):
    print(" "*(4-i), end="")
    for j in range(1, 2*i):
        print(j, end="")
    print()
    