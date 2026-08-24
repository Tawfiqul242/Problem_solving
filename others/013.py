# Check whether two strings are anagrams

string1 = "listen"
string2 = "silent"

if sorted(string1) == sorted(string2):
    print("Anagram")

else:
    print("Not Anagram")
