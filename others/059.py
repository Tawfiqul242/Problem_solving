# Find the first repeating character
text = "abcdeec"
seen = {}
for char in text:
    if char in seen:
        print(char)
        break
    else:
        seen[char] = 1
        
