# Count number of lines

with open("others/test_file.txt", "r") as f:
    print(len(f.readlines()))