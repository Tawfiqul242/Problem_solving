# Check anagram without sorting
str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")

else:
    anagram = True
    for char in str1:
        if str1.count(char) != str2.count(char):
            anagram = False
            break
    if anagram:
        print("Anagram")
    else:
        print("Not Anagram")