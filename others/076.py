# Count number of characters

with open("others/test_file.txt", "r") as f:

    count = 0
    for line in f:
        for char in line:
            count += 1
print(count)