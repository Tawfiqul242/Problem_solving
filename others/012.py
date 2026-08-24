# Remove duplicate characters

value = "banana"
empty_string = ""
for i in value:
    if i not in empty_string:
        empty_string += i
print(empty_string)