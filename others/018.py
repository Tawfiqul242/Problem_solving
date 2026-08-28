# Check whether a string contains only digits

string = "14 5"

# if string.replace(" ", "").isdigit():
#     print("Contains only digits")

# else:
#     print("String not only contains digit")

string = string.replace(" ", "")
count = 0
for char in string:
    if "0" <= char <= "9":
        count += 1
if count == len(string):
    print("Contains only digits")
else:
    print("String not only contains digit")