# Find common characters between two strings

str1 = "hello"
str2 = "world"
common = ""

for char in str1:
    if char in str2 and char not in common:
        print(char)
        common += char
