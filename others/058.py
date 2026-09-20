# Find the first non-repeating character
text = "aabbcde"
for char in text:
    if text.count(char) < 2:
        print(char)
        break
