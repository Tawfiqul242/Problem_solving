# Count number of words
with open("others/test_file.txt", "r") as file:
    count = 0
    for line in file:
        words = line.split()
        for word in words:
            count += 1

    print(count)