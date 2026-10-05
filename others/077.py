# Search for a particular word in a file

with open("others/test_file.txt", "r") as f:
    target = "second"
    found = False

    for line in f:
        words = line.split()
        for word in words:
            found = True
            break

if found:
    print("Found")
 
else:
    print("Not Found")