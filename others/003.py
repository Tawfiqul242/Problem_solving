# Check whether a character is alphabet, digit or special character
char = input()

if ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
    print("Alphabet")
elif ord(char) >= 48 and ord(char) <= 57:
    print("Digits")
else:
    print("Special Character")