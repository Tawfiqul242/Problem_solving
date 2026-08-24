# Find the longest word
sentence = "Python is very powerful"

longest = ""
for word in sentence.split():
    if len(word) > len(longest):
        longest = word
print(longest)

# print(max(sentence.split(), key=len))